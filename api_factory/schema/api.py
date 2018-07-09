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

"""This module contains the "roll-up" class, :class:`~.API`.
Everything else in the :mod:`~.schema` module is usually accessed
through an :class:`~.API` object.
"""

import collections
import dataclasses
import sys
from typing import Callable, List, Mapping, Sequence, Tuple

from google.api import annotations_pb2
from google.longrunning import operations_pb2
from google.protobuf import descriptor_pb2

from api_factory import utils
from api_factory.schema import metadata
from api_factory.schema import naming
from api_factory.schema import wrappers


@dataclasses.dataclass(frozen=True, init=False)
class API:
    """A representation of a full API.

    This represents a top-down view of a complete API, as loaded from a
    set of protocol buffer files. Once the descriptors are loaded
    (see :meth:`load`), this object contains every message, method, service,
    and everything else needed to write a client library.

    An instance of this object is made available to every template
    (as ``api``).
    """
    naming: naming.Naming
    protos: Tuple[Proto]

    def __init__(self,
            file_descriptors: Sequence[descriptor_pb2.FileDescriptorProto],
            package: str = ''):
        """Build the internal API schema based on the request.

        Args:
            file_descriptors (Sequence[~.FileDescriptorProto]): A list of
                :class:`~.FileDescriptorProto` objects describing the
                API.
            package (str): A protocol buffer package, as a string, for which
                code should be explicitly generated (including subpackages).
                Protos with packages outside this list are considered imports
                rather than explicit targets.
        """
        # Save information about the overall naming for this API.
        object.__setattr__('naming', naming.Naming(file_descriptors=filter(
            lambda fd: fd.startswith(package),
            file_descriptors,
        )))

        # Iterate over each FileDescriptorProto and fill out a Proto
        # object describing it, and save these to the instance.
        protos = []
        for fd in file_descriptors:
            protos.append(Proto(
                file_descriptor=fd,
                file_to_generate=fd.startswith(package),
            ))
        object.__setattr__('protos', tuple(protos))


@dataclasses.dataclass(init=False)
class Proto:
    """A representation of a particular proto file within an API."""

    services: Mapping[str, wrappers.Service]
    messages: Mapping[str, wrappers.MessageType]
    enums: Mapping[str, wrappers.EnumType]
    file_to_generate: bool

    def __init__(self, file_descriptor: descriptor_pb2.FileDescriptorProto,
            file_to_generate: bool):
        """Build and return a Proto instance.

        Args:
            file_descriptor (~.FileDescriptorProto): The protocol buffer
                object describing the proto file.
            file_to_generate (bool): Whether this is a file which is
                to be directly generated, or a dependency.
        """
        attrs = {'enums': {}, 'messages': {}, 'services': {}}

        # Iterate over the documentation and place it into a dictionary.
        #
        # The comments in protocol buffers are sorted by a concept called
        # the "path", which is a sequence of integers described in more
        # detail below; this code simply shifts from a list to a dict,
        # with tuples of paths as the dictionary keys.
        source_info = {}
        for location in file_descriptor.source_code_info.location:
            source_info[tuple(location.path)] = location

        # Everything has an "address", which is the proto where the thing
        # was declared.
        #
        # We put this together by a baton pass of sorts: everything in
        # this file *starts with* this address, which is appended to
        # for each item as it is loaded.
        address = metadata.Address(
            module=file_descriptor.name.split('/')[-1][:-len('.proto')],
            package=file_descriptor.package.split('.'),
        )

        # Now iterate over the FileDescriptorProto and pull out each of
        # the messages, enums, and services.
        #
        # The hard-coded path keys sent here are based on how descriptor.proto
        # works; it uses the proto message number of the pieces of each
        # message (e.g. the hard-code `4` for `message_type` immediately
        # below is because `repeated DescriptorProto message_type = 4;` in
        # descriptor.proto itself).
        self._load_children(file_descriptor.message_type, _load_message,
                base_address=address, path=(4,), source_info=source_info)
        self._load_children(file_descriptor.enum_type, _load_enum,
                base_address=address, path=(5,), source_info=source_info)
        self._load_children(file_descriptor.service_type, _load_service,
                base_address=address, path=(6,), source_info=source_info)
        # TODO(lukesneeringer): oneofs are on path 7.

    def _load_children(children: Sequence, loader: Callable, *,
                       base_address: metadata.Address, path: Tuple[int],
                       source_info: SourceInfo) -> None:
        """Return wrapped versions of arbitrary children from a Descriptor.

        Args:
            children (list): A sequence of children of the given field to
                be loaded. For example, a FileDescriptorProto contains the
                lists ``message_type``, ``enum_type``, etc.; these are valid
                inputs for this argument.
            loader (Callable[Message, Address, dict]): The function able
                to load the kind of message in ``children``. This should
                be one of the ``_load_{noun}`` methods on this class
                (e.g. ``_load_descriptor``).
            base_address (~.metadata.Address): The address up to this point.
                This will include the package and may include outer messages.
            path (Tuple[int]): The location path up to this point. This is
                used to correspond to documentation in ``SourceCodeInfo.Location``
                in ``descriptor.proto``.
            source_info (Mapping[Tuple[int], ~.SourceCodeInfo.Location]): A
                dictionary with all of the comments retrieved from the proto.
        """
        # Iterate over the list of children provided and call the
        # applicable loader function on each.
        for child, i in zip(children, range(0, sys.maxsize)):
            loader(child, base_address=base_address, path=path + (i,), source_info=source_info)

    def _get_fields(self, field_pbs: List[descriptor_pb2.FieldDescriptorProto],
                    address: metadata.Address, info: dict,
                    ) -> Mapping[str, wrappers.Field]:
        """Return a dictionary of wrapped fields for the given message.

        Args:
            fields (Sequence[~.descriptor_pb2.FieldDescriptorProto]): A
                sequence of protobuf field objects.
            address (~.metadata.Address): An address object denoting the
                location of these fields.
            info (dict): The appropriate slice of proto comments
                corresponding to these fields.

        Returns:
            Mapping[str, ~.wrappers.Field]: A ordered mapping of
                :class:`~.wrappers.Field` objects.
        """
        # Iterate over the fields and collect them into a dictionary.
        answer = collections.OrderedDict()
        for field_pb, i in zip(field_pbs, range(0, sys.maxsize)):
            answer[field_pb.name] = wrappers.Field(
                field_pb=field_pb,
                meta=metadata.Metadata(
                    address=address,
                    documentation=info.get(i, {}).get(
                        'TERMINAL',
                        descriptor_pb2.SourceCodeInfo.Location(),
                    ),
                ),
            )

        # Done; return the answer.
        return answer

    def _get_methods(self, methods: List[descriptor_pb2.MethodDescriptorProto],
                     address: metadata.Address, info: dict,
                     ) -> Mapping[str, wrappers.Method]:
        """Return a dictionary of wrapped methods for the given service.

        Args:
            methods (Sequence[~.descriptor_pb2.MethodDescriptorProto]): A
                sequence of protobuf method objects.
            address (~.metadata.Address): An address object denoting the
                location of these methods.
            info (dict): The appropriate slice of proto comments
                corresponding to these methods.

        Returns:
            Mapping[str, ~.wrappers.Method]: A ordered mapping of
                :class:`~.wrappers.Method` objects.
        """
        # Iterate over the methods and collect them into a dictionary.
        answer = collections.OrderedDict()
        for method_pb, i in zip(methods, range(0, sys.maxsize)):
            types = method_pb.options.Extensions[operations_pb2.operation_types]
            answer[method_pb.name] = wrappers.Method(
                input=self.messages[method_pb.input_type.lstrip('.')],
                lro_metadata=self.messages.get(types.metadata, None),
                lro_payload=self.messages.get(types.response, None),
                method_pb=method_pb,
                meta=metadata.Metadata(
                    address=address,
                    documentation=info.get(i, {}).get(
                        'TERMINAL',
                        descriptor_pb2.SourceCodeInfo.Location(),
                    ),
                ),
                output=self.messages[method_pb.output_type.lstrip('.')],
            )

        # Done; return the answer.
        return answer

    def _load_descriptor(self, message_pb: descriptor_pb2.DescriptorProto,
                         address: metadata.Address, info: dict) -> None:
        """Load message descriptions from DescriptorProtos."""
        ident = f'{str(address)}.{message_pb.name}'
        nested_addr = address.child(message_pb.name)

        # Create a dictionary of all the fields for this message.
        fields = self._get_fields(
            message_pb.field,
            address=nested_addr,
            info=info.get(2, {}),
        )
        fields.update(self._get_fields(
            message_pb.extension,
            address=nested_addr,
            info=info.get(6, {}),
        ))

        # Create a message correspoding to this descriptor.
        self.messages[ident] = wrappers.MessageType(
            fields=fields,
            message_pb=message_pb,
            meta=metadata.Metadata(address=address, documentation=info.get(
                'TERMINAL',
                descriptor_pb2.SourceCodeInfo.Location(),
            )),
        )

        # Load all nested items.
        self._load_children(message_pb.nested_type, address=nested_addr,
                            loader=self._load_descriptor, info=info.get(3, {}))
        self._load_children(message_pb.enum_type, address=nested_addr,
                            loader=self._load_enum, info=info.get(4, {}))
        # self._load_children(message.oneof_decl, loader=self._load_field,
        #                     address=nested_addr, info=info.get(8, {}))

    def _load_enum(self, enum: descriptor_pb2.EnumDescriptorProto,
                   address: metadata.Address, info: dict) -> None:
        """Load enum descriptions from EnumDescriptorProtos."""
        # Put together wrapped objects for the enum values.
        values = []
        for enum_value, i in zip(enum.value, range(0, sys.maxsize)):
            values.append(wrappers.EnumValueType(
                enum_value_pb=enum_value,
                meta=metadata.Metadata(
                    address=address,
                    documentation=info.get(2, {}).get(
                        'TERMINAL',
                        descriptor_pb2.SourceCodeInfo.Location(),
                    ),
                ),
            ))

        # Load the enum itself.
        ident = f'{str(address)}.{enum.name}'
        self.enums[ident] = wrappers.EnumType(
            enum_pb=enum,
            meta=metadata.Metadata(address=address, documentation=info.get(
                'TERMINAL',
                descriptor_pb2.SourceCodeInfo.Location(),
            )),
            values=values,
        )

    def _load_service(self, service: descriptor_pb2.ServiceDescriptorProto,
                      address: metadata.Address, info: dict) -> None:
        """Load comments for a service and its methods."""
        service_addr = address.child(service.name)

        # Put together a dictionary of the service's methods.
        methods = self._get_methods(
            service.method,
            address=service_addr,
            info=info.get(2, {}),
        )

        # Load the comments for the service itself.
        self.services[f'{str(address)}.{service.name}'] = wrappers.Service(
            meta=metadata.Metadata(address=address, documentation=info.get(
                'TERMINAL',
                descriptor_pb2.SourceCodeInfo.Location(),
            )),
            methods=methods,
            service_pb=service,
        )
