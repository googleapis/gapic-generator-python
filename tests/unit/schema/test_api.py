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

from typing import Sequence
from unittest import mock

import pytest

from google.protobuf import descriptor_pb2

from api_factory.schema import api
from api_factory.schema import metadata
from api_factory.schema import naming
from api_factory.schema import wrappers


def test_proto_build():
    fdp = descriptor_pb2.FileDescriptorProto(
        name='my_proto_file.proto',
        package='google.example.v1',
    )
    proto = api.Proto.build(fdp, file_to_generate=True)
    assert isinstance(proto, api.Proto)


def test_proto_builder_constructor():
    sentinel_message = descriptor_pb2.DescriptorProto()
    sentinel_enum = descriptor_pb2.EnumDescriptorProto()
    sentinel_service = descriptor_pb2.ServiceDescriptorProto()

    # Create a file descriptor proto. It does not matter that none
    # of the sentinels have actual data because this test just ensures
    # they are sent off to the correct methods unmodified.
    fdp = make_file_pb2(
        messages=(sentinel_message,),
        enums=(sentinel_enum,),
        services=(sentinel_service,),
    )

    # Test the load function.
    with mock.patch.object(api._ProtoBuilder, '_load_children') as lc:
        pb = api._ProtoBuilder(fdp, file_to_generate=True)

        # There should be three total calls to load the different types
        # of children.
        assert lc.call_count == 3

        # The message type should come first.
        _, args, _ = lc.mock_calls[0]
        assert args[0][0] == sentinel_message
        assert args[1] == pb._load_message

        # The enum type should come second.
        _, args, _ = lc.mock_calls[1]
        assert args[0][0] == sentinel_enum
        assert args[1] == pb._load_enum

        # The services should come third.
        _, args, _ = lc.mock_calls[2]
        assert args[0][0] == sentinel_service
        assert args[1] == pb._load_service


def test_not_taget_file():
    """Establish that services are not ignored for untargeted protos."""
    message_pb = make_message_pb2(name='Foo',
        fields=(make_field_pb2(name='bar', type=3, number=1),)
    )
    service_pb = descriptor_pb2.ServiceDescriptorProto()
    fdp = make_file_pb2(messages=(message_pb,), services=(service_pb,))

    # Actually make the proto object.
    proto = api.Proto.build(fdp, file_to_generate=False)

    # The proto object should have the message, but no service.
    assert len(proto.messages) == 1
    assert len(proto.services) == 0


def test_messages():
    L = descriptor_pb2.SourceCodeInfo.Location

    message_pb = make_message_pb2(name='Foo',
        fields=(make_field_pb2(name='bar', type=3, number=1),)
    )
    locations = (
        L(path=(4, 0), leading_comments='This is the Foo message.'),
        L(path=(4, 0, 2, 0), leading_comments='This is the bar field.'),
    )
    fdp = make_file_pb2(
        messages=(message_pb,),
        locations=locations,
        package='google.example.v2',
    )

    # Make the proto object.
    proto = api.Proto.build(fdp, file_to_generate=True)

    # Get the message.
    message = proto.messages['google.example.v2.Foo']
    assert message.meta.doc == 'This is the Foo message.'
    assert message.fields['bar'].meta.doc == 'This is the bar field.'


# def test_load_children():
#     # Set up the data to be sent to the method.
#     children = (mock.sentinel.child_zero, mock.sentinel.child_one)
#     address = metadata.Address()
#     info = {0: mock.sentinel.info_zero, 1: mock.sentinel.info_one}
#     loader = mock.Mock(create_autospec=lambda child, address, info: None)
#
#     # Run the `_load_children` method.
#     make_api()._load_children(children, loader, address, info)
#
#     # Assert that the loader ran in the expected way (twice, once per child).
#     assert loader.call_count == 2
#     _, args, kwargs = loader.mock_calls[0]
#     assert args[0] == mock.sentinel.child_zero
#     assert kwargs['info'] == mock.sentinel.info_zero
#     _, args, kwargs = loader.mock_calls[1]
#     assert args[0] == mock.sentinel.child_one
#     assert kwargs['info'] == mock.sentinel.info_one
#
#
# def test_get_fields():
#     L = descriptor_pb2.SourceCodeInfo.Location
#
#     # Set up data to test with.
#     field_pbs = [
#         descriptor_pb2.FieldDescriptorProto(name='spam'),
#         descriptor_pb2.FieldDescriptorProto(name='eggs'),
#     ]
#     address = metadata.Address(package=['foo', 'bar'], module='baz')
#     info = {1: {'TERMINAL': L(leading_comments='Eggs.')}}
#
#     # Run the method under test.
#     fields = make_api()._get_fields(field_pbs, address=address, info=info)
#
#     # Test that we get two field objects back.
#     assert len(fields) == 2
#     for field in fields.values():
#         assert isinstance(field, wrappers.Field)
#     items = iter(fields.items())
#
#     # Test that the first field is spam, and it has no documentation
#     # (since `info` has no `0` key).
#     field_name, field = next(items)
#     assert field_name == 'spam'
#     assert field.meta.doc == ''
#
#     # Test that the second field is eggs, and it does have documentation
#     # (since `info` has a `1` key).
#     field_name, field = next(items)
#     assert field_name == 'eggs'
#     assert field.meta.doc == 'Eggs.'
#
#     # Done.
#     with pytest.raises(StopIteration):
#         next(items)
#
#
# def test_get_methods():
#     # Start with an empty API object.
#     api = make_api()
#
#     # Load the input and output type for a method into the API object.
#     address = metadata.Address(package=['foo', 'bar'], module='baz')
#     api._load_descriptor(descriptor_pb2.DescriptorProto(name='In'),
#                          address=address, info={})
#     api._load_descriptor(descriptor_pb2.DescriptorProto(name='Out'),
#                          address=address, info={})
#
#     # Run the method under test.
#     method_pb = descriptor_pb2.MethodDescriptorProto(
#         name='DoThings',
#         input_type='foo.bar.In',
#         output_type='foo.bar.Out',
#     )
#     methods = api._get_methods([method_pb], address=address, info={})
#
#     # Test that we get a method object back.
#     assert len(methods) == 1
#     for method in methods.values():
#         assert isinstance(method, wrappers.Method)
#     items = iter(methods.items())
#
#     # Test that the method has what we expect, an input and output type
#     # and appropriate name.
#     method_key, method = next(items)
#     assert method_key == 'DoThings'
#     assert isinstance(method.input, wrappers.MessageType)
#     assert method.input.name == 'In'
#     assert isinstance(method.output, wrappers.MessageType)
#     assert method.output.name == 'Out'
#
#     # Done.
#     with pytest.raises(StopIteration):
#         next(items)
#
#
# def test_get_methods_lro():
#     # Start with an empty API object.
#     api = make_api()
#
#     # Load the message types for a method into the API object, including LRO
#     # payload and metadata.
#     address = metadata.Address(package=['foo', 'bar'], module='baz')
#     api._load_descriptor(descriptor_pb2.DescriptorProto(name='In'),
#                          address=address, info={})
#     api._load_descriptor(descriptor_pb2.DescriptorProto(name='Out'),
#                          address=address, info={})
#     api._load_descriptor(descriptor_pb2.DescriptorProto(name='Progress'),
#                          address=address, info={})
#     operations_address = metadata.Address(
#         package=['google', 'longrunning'],
#         module='operations',
#     )
#     api._load_descriptor(descriptor_pb2.DescriptorProto(name='Operation'),
#                          address=operations_address, info={})
#     method_pb = descriptor_pb2.MethodDescriptorProto(
#         name='DoBigThings',
#         input_type='foo.bar.In',
#         output_type='google.longrunning.Operation',
#     )
#     method_pb.options.Extensions[lro_pb2.types].MergeFrom(lro_pb2.MethodTypes(
#         lro_return_type='foo.bar.Out',
#         lro_metadata_type='foo.bar.Progress',
#     ))
#
#     # Run the method under test.
#     methods = api._get_methods([method_pb], address=address, info={})
#
#     # Test that the method has the expected lro output, payload, and metadata.
#     method = next(iter(methods.values()))
#     assert method.output.name == 'Operation'
#     assert isinstance(method.lro_payload, wrappers.MessageType)
#     assert method.lro_payload.name == 'Out'
#     assert isinstance(method.lro_metadata, wrappers.MessageType)
#     assert method.lro_metadata.name == 'Progress'
#
#
# def test_load_descriptor():
#     message_pb = descriptor_pb2.DescriptorProto(name='Riddle')
#     address = metadata.Address(package=['foo', 'bar', 'v1'], module='baz')
#     api = make_api()
#     api._load_descriptor(message_pb=message_pb, address=address, info={})
#     assert 'foo.bar.v1.Riddle' in api.messages
#     assert isinstance(api.messages['foo.bar.v1.Riddle'], wrappers.MessageType)
#     assert api.messages['foo.bar.v1.Riddle'].message_pb == message_pb
#
#
# def test_load_enum():
#     # Set up the appropriate protos.
#     enum_value_pb = descriptor_pb2.EnumValueDescriptorProto(name='A', number=0)
#     enum_pb = descriptor_pb2.EnumDescriptorProto(
#         name='Enum',
#         value=[enum_value_pb],
#     )
#
#     # Load it into the API.
#     address = metadata.Address(package=['foo', 'bar', 'v1'], module='baz')
#     api = make_api()
#     api._load_enum(enum_pb, address=address, info={})
#
#     # Assert we got back the right stuff.
#     assert 'foo.bar.v1.Enum' in api.enums
#     assert isinstance(api.enums['foo.bar.v1.Enum'], wrappers.EnumType)
#     assert api.enums['foo.bar.v1.Enum'].enum_pb == enum_pb
#     assert len(api.enums['foo.bar.v1.Enum'].values) == 1
#
#
# def test_load_service():
#     service_pb = descriptor_pb2.ServiceDescriptorProto(name='RiddleService')
#     address = metadata.Address(package=['foo', 'bar', 'v1'], module='baz')
#     api = make_api()
#     api._load_service(service_pb, address=address, info={})
#     assert 'foo.bar.v1.RiddleService' in api.services
#     assert isinstance(api.services['foo.bar.v1.RiddleService'],
#                       wrappers.Service)
#     assert api.services['foo.bar.v1.RiddleService'].service_pb == service_pb


def make_file_pb2(name: str = '', package: str = '', *,
        messages: Sequence[descriptor_pb2.DescriptorProto] = (),
        enums: Sequence[descriptor_pb2.EnumDescriptorProto] = (),
        services: Sequence[descriptor_pb2.ServiceDescriptorProto] = (),
        locations: Sequence[descriptor_pb2.SourceCodeInfo.Location] = (),
        ) -> descriptor_pb2.FileDescriptorProto:
    return descriptor_pb2.FileDescriptorProto(
        name=name or 'my_proto_file.proto',
        package=package or 'google.example.v1',
        message_type=messages,
        enum_type=enums,
        service=services,
        source_code_info=descriptor_pb2.SourceCodeInfo(location=locations),
    )


def make_message_pb2(name: str, fields=()) -> descriptor_pb2.DescriptorProto:
    return descriptor_pb2.DescriptorProto(name=name, field=fields)


def make_field_pb2(name: str, number: int,
        type: int = 11,  # 11 == message
        type_name: str = None,
        ) -> descriptor_pb2.FieldDescriptorProto:
    return descriptor_pb2.FieldDescriptorProto(
        name=name,
        number=number,
        type=type,
        type_name=type_name,
    )


def make_api(naming: naming.Naming = None, protos=()) -> api.API:
    return API(naming=naming or make_naming(), protos=protos)


def make_naming(**kwargs) -> naming.Naming:
    kwargs.setdefault('name', 'Hatstand')
    kwargs.setdefault('namespace', ('Google', 'Cloud'))
    kwargs.setdefault('version', 'v1')
    kwargs.setdefault('product_name', 'Hatstand')
    kwargs.setdefault('product_url', 'https://cloud.google.com/hatstand/')
    return naming.Naming(**kwargs)
