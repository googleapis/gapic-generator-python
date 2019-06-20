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

import itertools
import keyword
import re
import gapic.samplegen.utils

from collections import defaultdict

# Outstanding issues:
# * Neither license nor copyright are defined
# * In real sample configs, many variables are
#   defined with an _implicit_ $resp variable.

MIN_SCHEMA_VERSION = (1, 2, 0)

VALID_CONFIG_TYPE = 'com.google.api.codegen.SampleConfigProto'

# There are a couple of other names that should be reserved
# for sample variable assignments, e.g. 'client', but there are diminishing returns:
# the sample config author isn't a pathological adversary, they're a normal person
# who may make mistakes occasionally.
RESERVED_WORDS = frozenset(itertools.chain(keyword.kwlist, dir(__builtins__)))

TEMPLATE_NAME = 'samplegen_template.j2'


class ReservedVariableName(Exception):
    pass


class SchemaVersion(Exception):
    pass


class RpcMethodNotFound(Exception):
    pass


class InvalidConfigType(Exception):
    pass


class InvalidStatement(Exception):
    pass


class BadLoop(Exception):
    pass


class MismatchedPrintStatement(Exception):
    pass


class UndefinedVariableReference(Exception):
    pass


class BadAssignment(Exception):
    pass


class InconsistentRequestName(Exception):
    pass


class InvalidRequestSetup(Exception):
    pass


class DuplicateInputParameter(Exception):
    pass


def validate_response(response):
    coll_kword = "collection"
    var_kword = "variable"
    map_kword = "map"
    key_kword = "key"
    val_kword = "value"
    body_kword = "body"
    # Do NOT need checks for valid lexical scoping
    # because of python variable definition rules.
    # E.g. the following is valid python:
    #
    # for i in range(10):
    #   squid = "Squid {}".format(i)
    #
    # print("Last squid is {}".format(squid))

    def handle_define(body):
        m = re.match(r"^([^=]+)=([^=]+)$", body)
        if not m:
            raise BadAssignment("Bad assignment statement: {}", body)

        var, rval = m.groups()
        if var in RESERVED_WORDS:
            raise ReservedVariableName(
                "Tried to define a variable with reserved name: {}".format(var))

        rval_base = rval.split(".")[0]
        if not rval_base in var_defs:
            raise UndefinedVariableReference("Reference to undefined variable: {}"
                                             .format(rval_base))
        # TODO: Need to validate the attributes of the response
        #       based on the method return type.
        # TODO: Need to check the defined variables
        #       if the rhs references a non-response variable.
        #
        # Note: really checking for safety would be equivalent to
        #       re-implementing the python interpreter.
        var_defs.add(var)

    def handle_print(body):
        fmtStr = body[0]
        numPrints = fmtStr.count("%s")
        if numPrints != len(body) - 1:
            raise MismatchedPrintStatement(
                "Expected {} expresssions in print statement but received {}"
                .format(numPrints, len(body) - 1))

        for expression in body[1:]:
            var = expression.split(".")[0]
            if var not in var_defs:
                raise UndefinedVariableReference("Reference to undefined variable: {}"
                                                 .format(var))

    def handle_comment(body):
        fmtStr = body[0]
        numVars = fmtStr.count("%s")
        if numVars != len(body) - 1:
            raise MismatchedPrintStatement(
                "Expected {} var names in comment but received {}"
                .format(numVars, len(body) - 1))

        for var_name in body[1:]:
            var_base = var_name.split(".")[0]
            if var_base not in var_defs:
                raise UndefinedVariableReference("Reference to undefined variable: {}"
                                                 .format(var_base))

    def handle_loop(body):
        segments = set(body.keys())
        map_args = {map_kword, body_kword}
        if {coll_kword, var_kword, body_kword} == segments:
            collection_name = body[coll_kword].split(".")[0]
            # TODO: resolve the implicit $resp dilemma
            # if collection_name.startswith("."):
            #     collection_name = "$resp" + collection_name
            if collection_name not in var_defs:
                raise UndefinedVariableReference("Reference to undefined variable: {}"
                                                 .format(collection_name))

            var = body[var_kword]
            if var in RESERVED_WORDS:
                raise ReservedVariableName(
                    "Tried to define a variable with reserved name: {}".format(var))

            var_defs.add(var)

            inner_validate(body[body_kword])

        elif map_args <= segments:
            segments -= {map_kword, body_kword}
            map_name_base = body[map_kword].split(".")[0]
            if map_name_base not in var_defs:
                raise UndefinedVariableReference("Reference to undefined variable: {}"
                                                 .format(map_name_base))

            key = body.get(key_kword)
            if key:
                if key in RESERVED_WORDS:
                    raise ReservedVariableName(
                        "Tried to define a variable with reserved name: {}".format(key))

                var_defs.add(key)
                segments.remove(key_kword)

            val = body.get(val_kword)
            if val:
                if val in RESERVED_WORDS:
                    raise ReservedVariableName(
                        "Tried to define a variable with reserved name: {}".format(val))

                var_defs.add(val)
                segments.remove(val_kword)

            if not (key or val):
                raise BadLoop(
                    "Need at least one of 'key' or 'value' in a map loop")

            if segments:
                raise BadLoop("Unexpected keywords in loop statement: {}"
                              .format(segments))

            inner_validate(body[body_kword])

        else:
            raise BadLoop("Unexpected loop form: {}".format(segments))

    # The response variable is special and guaranteed to exist.
    var_defs = {"$resp"}
    statement_dispatcher = {
        "define": handle_define,
        "print": handle_print,
        "loop": handle_loop,
        "comment": handle_comment
    }

    def inner_validate(sample_segment):
        for statement in sample_segment:
            if len(statement) != 1:
                raise InvalidStatement(
                    "Invalid statement: {}".format(statement))

            keyword, body = next(iter(statement.items()))
            handler = statement_dispatcher.get(keyword)
            if not handler:
                raise InvalidStatement("Invalid statement keyword: {}"
                                       .format(keyword))

            handler(body)

        return True

    return inner_validate(response)


# TODO: this will eventually need the method name and the proto file
# so that it can do the correct value transformation for enums.
def validate_and_transform_request(request):
    base_param_to_attrs = defaultdict(list)
    input_params = set()
    # request looks like
    # [{"field": base.attr, "value": value, "input_parameter": varname},
    # {"field": base.attr, "value": value, "comment": helpful_comment},
    # {"field": base.attr, "value": value, value_is_file: True }]
    #
    # The base does not need to be the same for all arguments;
    # input_parameter, comment, and value_is_file are all optional.
    for field_assignment in request:
        field_assignment_copy = dict(field_assignment)
        input_param = field_assignment_copy.get("input_parameter")
        if input_param:
            if input_param in input_params:
                raise DuplicateInputParameter(
                    "Already declared input parameter: {}", input_param)

            if input_param in RESERVED_WORDS:
                raise ReservedVariableName(
                    "Invalid input_parameter name: {}", input_param)

            input_params.add(input_param)

        field = field_assignment_copy.get("field")
        if not field:
            raise InvalidRequestSetup(
                "No field attribute found in request setup assignment: {}",
                field_assignment_copy)

        m = re.match("^([^.]+)\.([^.]+)$", field)
        if not m:
            raise InvalidRequestSetup(
                "Malformed request attribute description: {}", field)

        base, attr = m.groups()
        if base in RESERVED_WORDS:
            raise ReservedVariableName(
                "Tried to define '{}', which is a reserved name".format(base))

        field_assignment_copy["field"] = attr
        base_param_to_attrs[base].append(field_assignment_copy)

    return [{"base": base, "body": body}
            for base, body in base_param_to_attrs.items()]
