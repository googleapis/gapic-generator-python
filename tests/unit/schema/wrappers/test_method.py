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

import collections
from typing import Sequence

from google.api import annotations_pb2
from google.api import client_pb2
from google.api import http_pb2
from google.protobuf import descriptor_pb2

from gapic.schema import metadata
from gapic.schema import wrappers


def test_method_types():
    input_msg = make_message(name='Input', module='baz')
    output_msg = make_message(name='Output', module='baz')
    method = make_method('DoSomething', input_msg, output_msg,
                         package='foo.bar', module='bacon')
    assert method.name == 'DoSomething'
    assert method.input.name == 'Input'
    assert method.output.name == 'Output'


def test_method_void():
    empty = make_message(name='Empty', package='google.protobuf')
    method = make_method('Meh', output_message=empty)
    assert method.void


def test_method_not_void():
    not_empty = make_message(name='OutputMessage', package='foo.bar.v1')
    method = make_method('Meh', output_message=not_empty)
    assert not method.void


def test_method_client_output():
    output = make_message(name='Input', module='baz')
    method = make_method('DoStuff', output_message=output)
    assert method.client_output is method.output


def test_method_client_output_empty():
    empty = make_message(name='Empty', package='google.protobuf')
    method = make_method('Meh', output_message=empty)
    assert method.client_output == wrappers.PrimitiveType.build(None)


def test_method_client_output_paged():
    paged = make_field(name='foos', message=make_message('Foo'), repeated=True)
    input_msg = make_message(name='ListFoosRequest', fields=(
        make_field(name='parent', type=9),      # str
        make_field(name='page_size', type=5),   # int
        make_field(name='page_token', type=9),  # str
    ))
    output_msg = make_message(name='ListFoosResponse', fields=(
        paged,
        make_field(name='next_page_token', type=9),  # str
    ))
    method = make_method('ListFoos',
        input_message=input_msg,
        output_message=output_msg,
    )
    assert method.paged_result_field == paged
    assert method.client_output.ident.name == 'ListFoosPager'


def test_method_paged_result_field_not_first():
    paged = make_field(name='foos', message=make_message('Foo'), repeated=True)
    input_msg = make_message(name='ListFoosRequest', fields=(
        make_field(name='parent', type=9),      # str
        make_field(name='page_size', type=5),   # int
        make_field(name='page_token', type=9),  # str
    ))
    output_msg = make_message(name='ListFoosResponse', fields=(
        make_field(name='next_page_token', type=9),  # str
        paged,
    ))
    method = make_method('ListFoos',
        input_message=input_msg,
        output_message=output_msg,
    )
    assert method.paged_result_field == paged


def test_method_paged_result_field_no_page_field():
    input_msg = make_message(name='ListFoosRequest', fields=(
        make_field(name='parent', type=9),      # str
        make_field(name='page_size', type=5),   # int
        make_field(name='page_token', type=9),  # str
    ))
    output_msg = make_message(name='ListFoosResponse', fields=(
        make_field(name='foos', message=make_message('Foo'), repeated=False),
        make_field(name='next_page_token', type=9),  # str
    ))
    method = make_method('ListFoos',
        input_message=input_msg,
        output_message=output_msg,
    )
    assert method.paged_result_field is None


def test_method_field_headers_none():
    method = make_method('DoSomething')
    assert isinstance(method.field_headers, collections.Sequence)


def test_method_field_headers_present():
    http_rule = http_pb2.HttpRule(get='/v1/{parent=projects/*}/topics')
    method = make_method('DoSomething', http_rule=http_rule)
    assert method.field_headers == ('parent',)


def test_method_idempotent_yes():
    http_rule = http_pb2.HttpRule(get='/v1/{parent=projects/*}/topics')
    method = make_method('DoSomething', http_rule=http_rule)
    assert method.idempotent is True


def test_method_idempotent_no():
    http_rule = http_pb2.HttpRule(post='/v1/{parent=projects/*}/topics')
    method = make_method('DoSomething', http_rule=http_rule)
    assert method.idempotent is False


def test_method_idempotent_no_http_rule():
    method = make_method('DoSomething')
    assert method.idempotent is False


def test_method_unary_unary():
    method = make_method('F', client_streaming=False, server_streaming=False)
    assert method.grpc_stub_type == 'unary_unary'


def test_method_unary_stream():
    method = make_method('F', client_streaming=False, server_streaming=True)
    assert method.grpc_stub_type == 'unary_stream'


def test_method_stream_unary():
    method = make_method('F', client_streaming=True, server_streaming=False)
    assert method.grpc_stub_type == 'stream_unary'


def test_method_stream_stream():
    method = make_method('F', client_streaming=True, server_streaming=True)
    assert method.grpc_stub_type == 'stream_stream'


def test_method_flattened_fields():
    a = make_field('a', type=5)  # int
    b = make_field('b', type=5)
    input_msg = make_message('Z', fields=(a, b))
    method = make_method('F', input_message=input_msg, signatures=('a,b',))
    assert len(method.flattened_fields) == 2
    assert 'a' in method.flattened_fields
    assert 'b' in method.flattened_fields


def test_method_ignored_flattened_fields():
    a = make_field('a', type=5)
    b = make_field('b', type=11, message=make_message('Eggs'))
    input_msg = make_message('Z', fields=(a, b))
    method = make_method('F', input_message=input_msg, signatures=('a,b',))
    assert len(method.flattened_fields) == 0


def make_method(
        name: str, input_message: wrappers.MessageType = None,
        output_message: wrappers.MessageType = None,
        package: str = 'foo.bar.v1', module: str = 'baz',
        http_rule: http_pb2.HttpRule = None,
        signatures: Sequence[str] = (),
        **kwargs) -> wrappers.Method:
    # Use default input and output messages if they are not provided.
    input_message = input_message or make_message('MethodInput')
    output_message = output_message or make_message('MethodOutput')

    # Create the method pb2.
    method_pb = descriptor_pb2.MethodDescriptorProto(
        name=name,
        input_type=str(input_message.meta.address),
        output_type=str(output_message.meta.address),
        **kwargs
    )

    # If there is an HTTP rule, process it.
    if http_rule:
        ext_key = annotations_pb2.http
        method_pb.options.Extensions[ext_key].MergeFrom(http_rule)

    # If there are signatures, include them.
    for sig in signatures:
        ext_key = client_pb2.method_signature
        method_pb.options.Extensions[ext_key].append(sig)

    # Instantiate the wrapper class.
    return wrappers.Method(
        method_pb=method_pb,
        input=input_message,
        output=output_message,
        meta=metadata.Metadata(address=metadata.Address(
            name=name,
            package=package,
            module=module,
            parent=(f'{name}Service',),
        )),
    )


def make_message(name: str, package: str = 'foo.bar.v1', module: str = 'baz',
        fields: Sequence[wrappers.Field] = (),
        ) -> wrappers.MessageType:
    message_pb = descriptor_pb2.DescriptorProto(
        name=name,
        field=[i.field_pb for i in fields],
    )
    return wrappers.MessageType(
        message_pb=message_pb,
        nested_messages={},
        nested_enums={},
        fields=collections.OrderedDict((i.name, i) for i in fields),
        meta=metadata.Metadata(address=metadata.Address(
            name=name,
            package=tuple(package.split('.')),
            module=module,
        )),
    )


def make_field(name: str, repeated: bool = False,
               meta: metadata.Metadata = None,
               message: wrappers.MessageType = None,
               **kwargs) -> wrappers.Method:
    field_pb = descriptor_pb2.FieldDescriptorProto(
        name=name,
        label=3 if repeated else 1,
        **kwargs
    )
    return wrappers.Field(
        field_pb=field_pb,
        message=message,
        meta=meta or metadata.Metadata(),
    )
