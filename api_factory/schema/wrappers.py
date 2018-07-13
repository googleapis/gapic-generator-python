# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module containing wrapper classes around meta-descriptors.

This module contains dataclasses which wrap the descriptor protos
defined in google/protobuf/descriptor.proto (which are descriptors that
describe descriptors).

These wrappers exist in order to provide useful helper methods and
generally ease access to things in templates (in particular, documentation,
certain aggregate views of things, etc.)

Reading of underlying descriptor properties in templates *is* okay, a
``__getattr__`` method which consistently routes in this way is provided.
Documentation is consistently at ``{thing}.meta.doc``.
"""

import collections
import dataclasses
import re
from typing import List, Mapping, Sequence, Tuple, Union

from google.api import annotations_pb2
from google.api import signature_pb2
from google.protobuf import descriptor_pb2

from api_factory import utils
from api_factory.schema.metadata import Metadata



@dataclasses.dataclass(frozen=True)
class Field:
    """Description of a field."""
    field_pb: descriptor_pb2.FieldDescriptorProto
    message: 'MessageType' = None
    enum: 'EnumType' = None
    meta: Metadata = dataclasses.field(default_factory=Metadata)

    def __getattr__(self, name):
        return getattr(self.field_pb, name)

    @property
    def repeated(self) -> bool:
        """Return True if this is a repeated field, False otherwise.

        Returns:
            bool: Whether this field is repeated.
        """
        return self.label == \
            descriptor_pb2.FieldDescriptorProto.Label.Value('LABEL_REPEATED')

    @utils.cached_property
    def type(self) -> Union['MessageType', 'EnumType', 'PythonType']:
        """Return the type of this field."""
        # If this is a message or enum, return the appropriate thing.
        if self.type_name and self.message:
            return self.message
        if self.type_name and self.enum:
            return self.enum

        # This is a primitive. Return the corresponding Python type.
        # The enum values used here are defined in:
        #   Repository: https://github.com/google/protobuf/
        #   Path: src/google/protobuf/descriptor.proto
        #
        # The values are used here because the code would be excessively
        # verbose otherwise, and this is guaranteed never to change.
        #
        # 10, 11, and 14 are intentionally missing. They correspond to
        # group (unused), message (covered above), and enum (covered above).
        if self.field_pb.type in (1, 2):
            return PythonType(python_type=float)
        if self.field_pb.type in (3, 4, 5, 6, 7, 13, 15, 16, 17, 18):
            return PythonType(python_type=int)
        if self.field_pb.type == 8:
            return PythonType(python_type=bool)
        if self.field_pb.type == 9:
            return PythonType(python_type=str)
        if self.field_pb.type == 12:
            return PythonType(python_type=bytes)

        # This should never happen.
        raise TypeError('Unrecognized protobuf type. This code should '
                        'not be reachable; please file a bug.')


@dataclasses.dataclass(frozen=True)
class MessageType:
    """Description of a message (defined with the ``message`` keyword)."""
    message_pb: descriptor_pb2.DescriptorProto
    fields: Mapping[str, Field]
    meta: Metadata = dataclasses.field(default_factory=Metadata)

    def __getattr__(self, name):
        return getattr(self.message_pb, name)

    def get_field(self, *field_path: Sequence[str]) -> Field:
        """Return a field arbitrarily deep in this message's structure.

        This method recursively traverses the message tree to return the
        requested inner-field.

        Traversing through repeated fields is not supported; a repeated field
        may be specified if and only if it is the last field in the path.

        Args:
            field_path (Sequence[str]): The field path.

        Returns:
            ~.Field: A field object.

        Raises:
            KeyError: If a repeated field is used in the non-terminal position
                in the path.
        """
        # Get the first field in the path.
        cursor = self.fields[field_path[0]]

        # Base case: If this is the last field in the path, return it outright.
        if len(field_path) == 1:
            return cursor

        # Sanity check: If cursor is a repeated field, then raise an exception.
        # Repeated fields are only permitted in the terminal position.
        if cursor.repeated:
            raise KeyError(
                f'The {cursor.name} field is repeated; unable to use '
                '`get_field` to retrieve its children.\n'
                'This exception usually indicates that a '
                'google.api.method_signature annotation uses a repeated field '
                'in the fields list in a position other than the end.',
            )

        # Recursion case: Pass the remainder of the path to the sub-field's
        # message.
        return cursor.message.get_field(*field_path[1:])

    @property
    def pb2_module(self) -> str:
        """Return the name of the Python pb2 module."""
        return f'{self.meta.address.module}_pb2'

    @property
    def proto_path(self) -> str:
        """Return the fully qualfied proto path as a string."""
        return f'{str(self.meta.address)}.{self.name}'


@dataclasses.dataclass(frozen=True)
class EnumValueType:
    """Description of an enum value."""
    enum_value_pb: descriptor_pb2.EnumValueDescriptorProto
    meta: Metadata = dataclasses.field(default_factory=Metadata)

    def __getattr__(self, name):
        return getattr(self.enum_value_pb, name)


@dataclasses.dataclass(frozen=True)
class EnumType:
    """Description of an enum (defined with the ``enum`` keyword.)"""
    enum_pb: descriptor_pb2.EnumDescriptorProto
    values: List[EnumValueType]
    meta: Metadata = dataclasses.field(default_factory=Metadata)

    def __getattr__(self, name):
        return getattr(self.enum_pb, name)


@dataclasses.dataclass(frozen=True)
class PythonType:
    """Wrapper class for Python types.

    This exists for interface consistency, so that methods like
    :meth:`Field.type` can return an object and the caller can be confident
    that a ``name`` property will be present.
    """
    python_type: type

    @property
    def name(self) -> str:
        return self.python_type.__name__


@dataclasses.dataclass(frozen=True)
class Method:
    """Description of a method (defined with the ``rpc`` keyword)."""
    method_pb: descriptor_pb2.MethodDescriptorProto
    input: MessageType
    output: MessageType
    lro_payload: MessageType = None
    lro_metadata: MessageType = None
    meta: Metadata = dataclasses.field(default_factory=Metadata)

    def __getattr__(self, name):
        return getattr(self.method_pb, name)

    @property
    def field_headers(self) -> Sequence[str]:
        """Return the field headers defined for this method."""
        http = self.options.Extensions[annotations_pb2.http]
        if http.get:
            return tuple(re.findall(r'\{([a-z][\w\d_.]+)=', http.get))
        return ()

    @utils.cached_property
    def signatures(self) -> Tuple[signature_pb2.MethodSignature]:
        """Return the signature defined for this method."""
        sig_pb2 = self.options.Extensions[annotations_pb2.method_signature]

        # Sanity check: If there are no signatures (which should be by far
        # the common case), just abort now.
        if len(sig_pb2.fields) == 0:
            return ()

        # Signatures are annotated with an `additional_signatures` key that
        # allows for specifying additional signatures. This is an uncommon
        # case but we still want to deal with it.
        answer = []
        for sig in (sig_pb2,) + tuple(sig_pb2.additional_signatures):
            # Build a MethodSignature object with the appropriate name
            # and fields. The fields are field objects, retrieved from
            # the method's `input` message.
            answer.append(MethodSignature(
                name=sig.function_name if sig.function_name else self.name,
                fields=collections.OrderedDict([
                    (f.split('.')[-1], self.input.get_field(f))
                    for f in sig.fields
                ]),
            ))

        # Done; return a tuple of signatures.
        return tuple(answer)


@dataclasses.dataclass(frozen=True)
class MethodSignature:
    name: str
    fields: Mapping[str, Field]

    @property
    def dispatch_type(self) -> Union[MessageType, EnumType, PythonType]:
        """Return the type object for the first field."""
        return iter(self.fields.values()).next()


@dataclasses.dataclass(frozen=True)
class Service:
    """Description of a service (defined with the ``service`` keyword)."""
    service_pb: descriptor_pb2.ServiceDescriptorProto
    methods: Mapping[str, Method]
    meta: Metadata = dataclasses.field(default_factory=Metadata)

    def __getattr__(self, name):
        return getattr(self.service_pb, name)

    @property
    def host(self) -> str:
        """Return the hostname for this service, if specified.

        Returns:
            str: The hostname, with no protocol and no trailing ``/``.
        """
        if self.options.Extensions[annotations_pb2.default_host]:
            return self.options.Extensions[annotations_pb2.default_host]
        return utils.Placeholder('<<< HOSTNAME >>>')

    @property
    def oauth_scopes(self) -> Sequence[str]:
        """Return a sequence of oauth scopes, if applicable.

        Returns:
            Sequence[str]: A sequence of OAuth scopes.
        """
        oauth = self.options.Extensions[annotations_pb2.oauth]
        return tuple(oauth.scopes)

    @property
    def module_name(self) -> str:
        """Return the appropriate module name for this service.

        Returns:
            str: The service name, in snake case.
        """
        return utils.to_snake_case(self.name)

    @property
    def pb2_modules(self) -> Sequence[Tuple[str, str]]:
        """Return a sequence of pb2 modules, for import.

        The results of this method are in alphabetical order (by package,
        then module), and do not contain duplicates.

        Returns:
            Sequence[str, str]: The package and pb2_module pair, intended
            for use in a ``from package import pb2_module`` type
            of statement.
        """
        answer = set()
        for method in self.methods.values():
            # Add the module containing both the request and response
            # messages. (These are usually the same, but not necessarily.)
            answer.add((
                '.'.join(method.input.meta.address.package),
                method.input.pb2_module,
            ))
            answer.add((
                '.'.join(method.output.meta.address.package),
                method.output.pb2_module,
            ))

            # If this method has LRO, it is possible (albeit unlikely) that
            # the LRO messages reside in a different module.
            if method.lro_payload:
                answer.add((
                    '.'.join(method.lro_payload.meta.address.package),
                    method.lro_payload.pb2_module,
                ))
            if method.lro_metadata:
                answer.add((
                    '.'.join(method.lro_metadata.meta.address.package),
                    method.lro_metadata.pb2_module,
                ))
        return tuple(sorted(answer))

    @property
    def has_lro(self) -> bool:
        """Return whether the service has a long-running method."""
        return any([m.lro_payload for m in self.methods.values()])

    @property
    def has_field_headers(self) -> bool:
        """Return whether the service has a method containing field headers."""
        return any([m.field_headers for m in self.methods.values()])
