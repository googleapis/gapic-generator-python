# Copyright (C) 2019  Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import dataclasses
import itertools
import jinja2
import keyword
import re
import time

from gapic.samplegen import utils, yaml
from gapic.schema import (api, wrappers)

from collections import (defaultdict, namedtuple, ChainMap as chainmap)
from textwrap import dedent
from typing import (ChainMap, Dict, List, Mapping, Optional, Set, Tuple, Union)

# Outstanding issues:
# * In real sample configs, many variables are
#   defined with an _implicit_ $resp variable.

MIN_SCHEMA_VERSION = (1, 2, 0)

VALID_CONFIG_TYPE = "com.google.api.codegen.SampleConfigProto"

# TODO: read in copyright and license from files.
FILE_HEADER: Dict[str, str] = {
    "copyright": "TODO: add a copyright",
    "license": "TODO: add a license",
}

RESERVED_WORDS = frozenset(
    itertools.chain(
        keyword.kwlist,
        dir(__builtins__),
        {
            "client",
            "f",  # parameter used in file I/O statements
            "operation",  # temporary used in LROs
            "page",  # used in paginated responses
            "page_result",  # used in paginated responses
            "response",  # basic 'response'
            "stream",  # used in server and bidi streaming
        },
    )
)

TEMPLATE_NAME = "sample.py.j2"


@dataclasses.dataclass(frozen=True)
class AttributeRequestSetup:
    value: str
    field: Optional[str] = None
    value_is_file: bool = False
    input_parameter: Optional[str] = None
    comment: Optional[str] = None


@dataclasses.dataclass(frozen=True)
class TransformedRequest:
    """Class representing a single field in a method call.

    The Optional[single]/Optional[body] is workaround for not having tagged unions;
    each transformed request either describes an attribute with multiple fields
    ('base' is the top level field name, 'body' contains a list of AttributeRequestSetups,
     where each one describes how to set up a subfield) or a top level field,
    where 'single' refers to the value of the singleton top level attribute.
    """
    base: str
    single: Optional[AttributeRequestSetup]
    body: Optional[List[AttributeRequestSetup]]


class SampleError(Exception):
    pass


class ReservedVariableName(SampleError):
    pass


class RpcMethodNotFound(SampleError):
    pass


class UnknownService(SampleError):
    pass


class InvalidConfig(SampleError):
    pass


class InvalidStatement(SampleError):
    pass


class BadLoop(SampleError):
    pass


class MismatchedFormatSpecifier(SampleError):
    pass


class UndefinedVariableReference(SampleError):
    pass


class BadAttributeLookup(SampleError):
    pass


class RedefinedVariable(SampleError):
    pass


class BadAssignment(SampleError):
    pass


class InconsistentRequestName(SampleError):
    pass


class InvalidRequestSetup(SampleError):
    pass


class InvalidEnumVariant(SampleError):
    pass


def coerce_response_name(s: str) -> str:
    # In the sample config, the "$resp" keyword is used to refer to the
    # item of interest as received by the corresponding calling form.
    # For a 'regular', i.e. unary, synchronous, non-long-running method,
    # it's the return value; for a server-streaming method, it's the iteration
    # variable in the for loop that iterates over the return value, and for
    # a long running promise, the user calls result on the method return value to
    # resolve the future.
    #
    # The sample schema uses '$resp' as the special variable,
    # but in the samples the 'response' variable is used instead.
    return s.replace("$resp", "response")


class Validator:
    """Class that validates a sample.

    Contains methods that validate different segments of a sample and maintains
    state that's relevant to validation across different segments.
    """

    COLL_KWORD = "collection"
    VAR_KWORD = "variable"
    MAP_KWORD = "map"
    KEY_KWORD = "key"
    VAL_KWORD = "value"
    BODY_KWORD = "body"

    def __init__(self, method: wrappers.Method):
        # The response ($resp) variable is special and guaranteed to exist.
        # TODO: name lookup also involes type checking
        self.request_type_ = method.input
        response_type = method.output
        if method.paged_result_field:
            response_type = method.paged_result_field
        elif method.lro:
            response_type = method.lro.response_type

        # This is a shameless hack to work around the design of wrappers.Field
        MockField = namedtuple("MockField", ["message", "repeated"])

        # TODO: pass var_defs_ around during response verification
        #       instead of assigning/restoring.
        self.var_defs_: ChainMap[str, wrappers.Field] = chainmap(
            # When validating expressions we need to store the Field,
            # not just the message type, because there are additional data we need:
            # whether a name refers to a repeated value (or a map),
            # and whether it's an enum or a message or a primitive type.
            # The method call response isn't a field, so construct an artificial
            # field that wraps the response.
            {  # type: ignore
                "$resp": MockField(response_type, False)
            }
        )

    def var_field(self, var_name: str) -> Optional[wrappers.Field]:
        return self.var_defs_.get(var_name)

    def validate_and_transform_request(self,
                                       calling_form: utils.CallingForm,
                                       request: List[Mapping[str, str]]) -> List[TransformedRequest]:
        """Validates and transforms the "request" block from a sample config.

           In the initial request, each dict has a "field" key that maps to a dotted
           variable name, e.g. clam.shell.

           The only required keys in each dict are "field" and value".
           Optional keys are "input_parameter", "value_is_file". and "comment".
           All values in the initial request are strings except for the value
           for "value_is_file", which is a bool.

           The TransformedRequest structure of the return value has three fields:
           "base", "body", and "single", where "base" maps to the top level attribute name,
           "body" maps to a list of subfield assignment definitions, and "single"
           maps to a singleton attribute assignment structure with no "field" value.
           The "field" attribute in the requests in a "body" list have their prefix stripped;
           the request in a "single" attribute has no "field" attribute.

           Note: gRPC API methods only take one parameter (ignoring client-side streaming).
                 The reason that GAPIC client library API methods may take multiple parameters
                 is a workaround to provide idiomatic protobuf support within python.
                 The different 'bases' are really attributes for the singular request parameter.

           TODO: properly handle subfields, indexing, and so forth.
           TODO: Add/transform to list repeated element fields.
                 Requires proto/method/message descriptors.

           E.g. [{"field": "clam.shell", "value": "10 kg", "input_parameter": "shell"},
                 {"field": "clam.pearls", "value": "3"},
                 {"field": "squid.mantle", "value": "100 kg"},
                 {"field": "whelk", "value": "speckled"}]
                  ->
                [TransformedRequest(
                     base="clam",
                     body=[AttributeRequestSetup(field="shell",
                                                 value="10 kg",
                                                 input_parameter="shell"),
                           AttributeRequestSetup(field="pearls", value="3")],
                     single=None),
                 TransformedRequest(base="squid",
                                    body=[AttributeRequestSetup(field="mantle",
                                                                value="100 kg")],
                                    single=None),
                 TransformedRequest(base="whelk",
                                    body=None,
                                    single=AttributeRequestSetup(value="speckled))]

           The transformation makes it easier to set up request parameters in jinja
           because it doesn't have to engage in prefix detection, validation,
           or aggregation logic.


        Args:
            request (list[dict{str:str}]): The request body from the sample config

        Returns:
            List[TransformedRequest]: The transformed request block.

        Raises:
            InvalidRequestSetup: If a dict in the request lacks a "field" key,
                                 a "value" key, if there is an unexpected keyword,
                                 or if more than one base parameter is given for
                                 a client-side streaming calling form.
            BadAttributeLookup: If a request field refers to a non-existent field
                                in the request message type.

        """
        base_param_to_attrs: Dict[str,
                                  List[AttributeRequestSetup]] = defaultdict(list)

        for r in request:
            duplicate = dict(r)
            val = duplicate.get("value")
            if not val:
                raise InvalidRequestSetup(
                    "Missing keyword in request entry: 'value'")

            field = duplicate.get("field")
            if not field:
                raise InvalidRequestSetup(
                    "Missing keyword in request entry: 'field'")

            spurious_keywords = set(duplicate.keys()) - {"value",
                                                         "field",
                                                         "value_is_file",
                                                         "input_parameter",
                                                         "comment"}
            if spurious_keywords:
                raise InvalidRequestSetup(
                    "Spurious keyword(s) in request entry: {}".format(
                        ", ".join(f"'{kword}'" for kword in spurious_keywords)))

            input_parameter = duplicate.get("input_parameter")
            if input_parameter:
                self._handle_lvalue(input_parameter, str)

            attr_chain = field.split(".")
            base = self.request_type_
            for attr_name in attr_chain:
                attr = base.fields.get(attr_name)
                if not attr:
                    raise BadAttributeLookup(
                        "Method request type {} has no attribute: '{}'".format(
                            self.request_type_.type, attr_name))

                if attr.message:
                    base = attr.message

                else:
                    raise TypeError

                # TODO: uncomment this when handling enums
                # if attr.enum:
                #     # A little bit hacky, but 'values' is a list, and this is the easiest
                #     # way to verify that the value is a valid enum variant.
                #     witness = next((e.name for e in attr.enum.values if e.name == val), None)
                #     if not witness:
                #         raise InvalidEnumVariant
                #     # Python code can set protobuf enums from strings.
                #     # This is preferable to adding the necessary import statement
                #     # and requires less munging of the assigned value
                #     duplicate["value"] = f"'{witness}'"

            # TODO: what if there's more stuff in the chain?
            if len(attr_chain) > 1:
                duplicate["field"] = ".".join(attr_chain[1:])
            else:
                # Because of the way top level attrs get rendered,
                # there can't be duplicates.
                # This is admittedly a bit of a hack.
                if attr_chain[0] in base_param_to_attrs:
                    raise InvalidRequestSetup(
                        "Duplicated top level field in request block: '{}'".format(
                            attr_chain[0]))
                del duplicate["field"]

            # Mypy isn't smart enough to handle dictionary unpacking,
            # so disable it for the AttributeRequestSetup ctor call.
            base_param_to_attrs[attr_chain[0]].append(
                AttributeRequestSetup(**duplicate))  # type: ignore

        client_streaming_forms = {
            utils.CallingForm.RequestStreamingClient,
            utils.CallingForm.RequestStreamingBidi,
        }

        if len(base_param_to_attrs) > 1 and calling_form in client_streaming_forms:
            raise InvalidRequestSetup(
                "Too many base parameters for client side streaming form")

        return [
            (TransformedRequest(base=key, body=val, single=None) if val[0].field
             else TransformedRequest(base=key, body=None, single=val[0]))
            for key, val in base_param_to_attrs.items()
        ]

    def validate_response(self, response):
        """Validates a "response" block from a sample config.

        A full description of the response block is outside the scope of this code;
        refer to the samplegen documentation.

        Dispatches statements to sub-validators.

        Args:
            response: list[dict{str:Any}]: The structured data representing
                                           the sample's response.

        Raises:
            InvalidStatement: If an unexpected key is found in a statement dict
                              or a statement dict has more than or less than one key.
        """

        for statement in response:
            if len(statement) != 1:
                raise InvalidStatement(
                    "Invalid statement: {}".format(statement))

            keyword, body = next(iter(statement.items()))
            validater = self.STATEMENT_DISPATCH_TABLE.get(keyword)
            if not validater:
                raise InvalidStatement(
                    "Invalid statement keyword: {}".format(keyword))

            validater(self, body)

    def validate_expression(self, exp: str) -> wrappers.Field:
        """Validate an attribute chain expression.

        Given a lookup expression, e.g. squid.clam.whelk,
        recursively validate that each base has an attr with the name of the
        next lookup lower down and repeated attributes are indexed.

        Args:
            expr: str: The attribute expression.

        Raises:
            UndefinedVariableReference: If the root of the expression is not
                                        a previously defined lvalue.
            BadAttributeLookup: If an attribute other than the final is repeated OR
                                if an attribute in the chain is not a field of its parent.

        Returns:
            wrappers.Field: The final field in the chain.
        """
        # TODO: handle mapping attributes, i.e. {}
        # TODO: Add resource name handling, i.e. %
        indexed_exp_re = re.compile(
            r"^(?P<attr_name>\$?\w+)(?:\[(?P<index>\d+)\])?$")

        toks = exp.split(".")
        match = indexed_exp_re.match(toks[0])
        if not match:
            raise BadAttributeLookup(
                f"Badly formatted attribute expression: {exp}")

        base_tok, previous_was_indexed = (match.groupdict()["attr_name"],
                                          bool(match.groupdict()["index"]))
        base = self.var_field(base_tok)
        if not base:
            raise UndefinedVariableReference(
                "Reference to undefined variable: {}".format(base_tok))
        if previous_was_indexed and not base.repeated:
            raise BadAttributeLookup(
                "Cannot index non-repeated attribute: {}".format(base_tok))

        for tok in toks[1:]:
            match = indexed_exp_re.match(tok)
            if not match:
                raise BadAttributeLookup(
                    f"Badly formatted attribute expression: {tok}")

            attr_name, lookup_token = match.groups()
            if base.repeated and not previous_was_indexed:
                raise BadAttributeLookup(
                    "Cannot access attributes through repeated field: {}".format(attr_name))
            if previous_was_indexed and not base.repeated:
                raise BadAttributeLookup(
                    "Cannot index non-repeated attribute: {}".format(attr_name))

            # TODO: handle enums, primitives, and so forth.
            attr = base.message.fields.get(attr_name)  # type: ignore
            if not attr:
                raise BadAttributeLookup(
                    "No such attribute in type '{}': {}".format(base, attr_name))

            base, previous_was_indexed = attr, bool(lookup_token)

        return base

    def _handle_lvalue(self, lval: str, type_=None):
        """Conducts safety checks on an lvalue and adds it to the lexical scope.

        Raises:
            ReservedVariableName: If an attempted lvalue is a reserved keyword.
        """
        if lval in RESERVED_WORDS:
            raise ReservedVariableName(
                "Tried to define a variable with reserved name: {}".format(
                    lval)
            )

        # Even though it's valid python to reassign variables to any rvalue,
        # the samplegen spec prohibits this.
        if lval in self.var_defs_:
            raise RedefinedVariable(
                "Tried to redefine variable: {}".format(lval))

        self.var_defs_[lval] = type_

    def _validate_format(self, body: List[str]):
        """Validates a format string and corresponding arguments.

         The number of format tokens in the string must equal the
         number of arguments, and each argument must be a defined variable.

         TODO: the attributes of the variable must correspond to attributes
               of the variable's type.

         Raises:
             MismatchedFormatSpecifier: If the number of format string segments ("%s") in
                                        a "print" or "comment" block does not equal the
                                        size number of strings in the block minus 1.
             UndefinedVariableReference: If the base lvalue in an expression chain
                                         is not a previously defined lvalue.
        """
        fmt_str = body[0]
        num_prints = fmt_str.count("%s")
        if num_prints != len(body) - 1:
            raise MismatchedFormatSpecifier(
                "Expected {} expresssions in format string but received {}".format(
                    num_prints, len(body) - 1
                )
            )

        for expression in body[1:]:
            var = expression.split(".")[0]
            if var not in self.var_defs_:
                raise UndefinedVariableReference(
                    "Reference to undefined variable: {}".format(var)
                )

    def _validate_define(self, body: str):
        """"Validates 'define' statements.

        Adds the defined lvalue to the lexical scope.
        Other statements can reference it.

         Raises:
             BadAssignment: If a "define" statement is badly formed lexically.
             UndefinedVariableReference: If an attempted rvalue base is a previously
                                         undeclared variable.
        """
        # TODO: Need to check the defined variables
        #       if the rhs references a non-response variable.
        # TODO: Need to rework the regex to allow for subfields,
        #       indexing, and so forth.
        #
        # Note: really checking for safety would be equivalent to
        #       re-implementing the python interpreter.
        m = re.match(r"^([a-zA-Z]\w*)=([^=]+)$", body)
        if not m:
            raise BadAssignment("Bad assignment statement: {}".format(body))

        lval, rval = m.groups()

        rval_type = self.validate_expression(rval)
        self._handle_lvalue(lval, rval_type)

    def _validate_write_file(self, body):
        """Validate 'write_file' statements.

        The body of a 'write_file' statement is a two-element dict
        with known keys: 'filename' and 'contents'.
        'filename' maps to a list of strings which constitute a format string
        and variable-based rvalues defining the fields.
        'contents' maps to a single variable-based rvalue.

        Raises:
            MismatchedFormatSpecifier: If the filename formatstring is badly formed.
            UndefinedVariableReference: If any of the formatstring variables
                                        or the file contents variable are undefined.
            InvalidStatement: If either 'filename' or 'contents' are absent keys.
        """

        fname_fmt = body.get("filename")
        if not fname_fmt:
            raise InvalidStatement(
                "Missing key in 'write_file' statement: 'filename'")

        self._validate_format(fname_fmt)

        contents_var = body.get("contents")
        if not contents_var:
            raise InvalidStatement(
                "Missing key in 'write_file' statement: 'contents'")

        # TODO: check the rest of the elements for valid subfield attribute
        base = contents_var.split(".")[0]
        if base not in self.var_defs_:
            raise UndefinedVariableReference(
                "Reference to undefined variable: {}".format(base)
            )

    def _validate_loop(self, body):
        """Validates loop headers and statement bodies.

        Checks for correctly defined loop constructs,
        either 'collection' loops with a collection and iteration variable,
        or 'map' loops with a map and at least one of 'key' or 'value'.
        Loops also have a 'body', which contains statments that may
        use the variables from the header.

        The body statements are validated recursively.
        The iteration variable(s) is/are added to the lexical scope
        before validating the statements in the loop body.

        Raises:
            UndefinedVariableReference: If an attempted rvalue base is a previously
                                        undeclared variable.
            BadLoop: If a "loop" segments has unexpected keywords
                     or keyword combinatations.

        """
        segments = set(body.keys())
        map_args = {self.MAP_KWORD, self.BODY_KWORD}

        # Even though it's valid python to use a variable outside of the lexical
        # scope it was defined in,
        #
        # i.e.
        #   for m in molluscs:
        #     handle(m)
        #   print("Last mollusc: {}".format(m))
        #
        # is allowed, the samplegen spec requires that errors are raised
        # if strict lexical scoping is violated.
        self.var_defs_ = self.var_defs_.new_child()

        if {self.COLL_KWORD, self.VAR_KWORD, self.BODY_KWORD} == segments:
            tokens = body[self.COLL_KWORD].split(".")

            # TODO: resolve the implicit $resp dilemma
            # if collection_name.startswith("."):
            #     collection_name = "$resp" + collection_name
            collection_field = self.validate_expression(
                body[self.COLL_KWORD])

            if not collection_field.repeated:
                raise BadLoop(
                    "Tried to use a non-repeated field as a collection: {}".format(tokens[-1]))

            var = body[self.VAR_KWORD]
            self._handle_lvalue(var)

        elif map_args <= segments:
            segments -= map_args
            segments -= {self.KEY_KWORD, self.VAL_KWORD}
            if segments:
                raise BadLoop(
                    "Unexpected keywords in loop statement: {}".format(
                        segments)
                )

            map_name_base = body[self.MAP_KWORD].split(".")[0]
            if map_name_base not in self.var_defs_:
                raise UndefinedVariableReference(
                    "Reference to undefined variable: {}".format(map_name_base)
                )

            key = body.get(self.KEY_KWORD)
            if key:
                self._handle_lvalue(key)

            val = body.get(self.VAL_KWORD)
            if val:
                self._handle_lvalue(val)

            if not (key or val):
                raise BadLoop(
                    "Need at least one of 'key' or 'value' in a map loop")

        else:
            raise BadLoop("Unexpected loop form: {}".format(segments))

        self.validate_response(body[self.BODY_KWORD])
        # Restore the previous lexical scope.
        # This is stricter than python scope rules
        # because the samplegen spec mandates it.
        self.var_defs_ = self.var_defs_.parents

    # Add new statement keywords to this table.
    STATEMENT_DISPATCH_TABLE = {
        "define": _validate_define,
        "print": _validate_format,
        "comment": _validate_format,
        "write_file": _validate_write_file,
        "loop": _validate_loop,
    }


def generate_sample(sample,
                    id_is_unique: bool,
                    env: jinja2.environment.Environment,
                    api_schema: api.API) -> Tuple[str, jinja2.environment.TemplateStream]:

    sample_template = env.get_template(TEMPLATE_NAME)

    service_name = sample["service"]
    service = api_schema.services.get(service_name)
    if not service:
        raise UnknownService("Unknown service: {}", service_name)

    rpc_name = sample["rpc"]
    rpc = service.methods.get(rpc_name)
    if not rpc:
        raise RpcMethodNotFound(
            "Could not find rpc in service {}: {}".format(
                service_name, rpc_name)
        )

    calling_form = utils.CallingForm.method_default(rpc)

    v = Validator(rpc)
    sample["request"] = v.validate_and_transform_request(calling_form,
                                                         sample["request"])
    v.validate_response(sample["response"])

    sample_fpath = (
        sample["id"] + (str(calling_form)
                        if not id_is_unique else "") + ".py"
    )

    sample["package_name"] = api_schema.naming.warehouse_package_name

    return (
        sample_fpath,
        sample_template.stream(
            file_header=FILE_HEADER,
            sample=sample,
            imports=[],
            calling_form=calling_form,
            calling_form_enum=utils.CallingForm,
        ),
    )


def generate_manifest(fpaths_and_samples, api_schema, *, manifest_time: int = None):
    """Generate a samplegen manifest for use by sampletest

    Args:
        fpaths_and_samples (Iterable[Tuple[str, Mapping[str, Any]]]):
                         The file paths and samples to be listed in the manifest

        api_schema (~.api.API): An API schema object.
        manifest_time (int): Optional. An override for the timestamp in the name of the manifest filename.
                             Primarily used for testing.

    Returns:
        Tuple[str, Dict[str,Any]]: The filename of the manifest and the manifest data as a dictionary.

    """
    all_info = [
        yaml.KeyVal("type", "manifest/samples"),
        yaml.KeyVal("schema_version", "3"),
        yaml.Map(
            name="python",
            anchor_name="python",
            elements=[
                yaml.KeyVal("environment", "python"),
                yaml.KeyVal("bin", "python3"),
                # TODO: make this the real sample base directory
                yaml.KeyVal("base_path", "sample/base/directory"),
                yaml.KeyVal("invocation", "'{bin} {path} @args'"),
            ],
        ),
        yaml.Collection(
            name="samples",
            elements=[
                [
                    yaml.Alias("python"),
                    yaml.KeyVal("sample", sample["id"]),
                    yaml.KeyVal("path", "'{base_path}/%s'" % fpath),
                    yaml.KeyVal("region_tag", sample.get("region_tag", "")),
                ]
                for fpath, sample in fpaths_and_samples
            ],
        ),
    ]

    dt = time.gmtime(manifest_time)
    manifest_fname_template = (
        "{api}.{version}.python."
        "{year:04d}{month:02d}{day:02d}."
        "{hour:02d}{minute:02d}{second:02d}."
        "manifest.yaml"
    )

    manifest_fname = manifest_fname_template.format(
        api=api_schema.naming.name,
        version=api_schema.naming.version,
        year=dt.tm_year,
        month=dt.tm_mon,
        day=dt.tm_mday,
        hour=dt.tm_hour,
        minute=dt.tm_min,
        second=dt.tm_sec,
    )

    return manifest_fname, all_info
