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

import typing

from google.protobuf import descriptor_pb2

from gapic.schema import metadata


def test_address_str_no_parent():
    addr = metadata.Address(package=('foo', 'bar'), module='baz', name='Bacon')
    assert str(addr) == 'baz_pb2.Bacon'


def test_address_str_parent():
    addr = metadata.Address(package=('foo', 'bar'), module='baz', name='Bacon',
                            parent=('spam', 'eggs'))
    assert str(addr) == 'baz_pb2.Bacon'


def test_address_proto():
    addr = metadata.Address(package=('foo', 'bar'), module='baz', name='Bacon')
    assert addr.proto == 'foo.bar.Bacon'
    assert addr.proto_package == 'foo.bar'


def test_address_child_no_parent():
    addr = metadata.Address(package=('foo', 'bar'), module='baz')
    child = addr.child('Bacon')
    assert child.name == 'Bacon'
    assert child.parent == ()


def test_address_child_with_parent():
    addr = metadata.Address(package=('foo', 'bar'), module='baz')
    child = addr.child('Bacon')
    grandchild = child.child('Ham')
    assert grandchild.parent == ('Bacon',)
    assert grandchild.name == 'Ham'


def test_address_rel():
    addr = metadata.Address(package=('foo', 'bar'), module='baz', name='Bacon')
    assert addr.rel(
        metadata.Address(package=('foo', 'bar'), module='baz'),
    ) == 'Bacon'
    assert addr.rel(
        metadata.Address(package=('foo', 'not_bar'), module='baz'),
    ) == 'baz_pb2.Bacon'
    assert addr.rel(
        metadata.Address(package=('foo', 'bar'), module='not_baz'),
    ) == 'baz_pb2.Bacon'


def test_address_resolve():
    addr = metadata.Address(package=('foo', 'bar'), module='baz', name='Qux')
    assert addr.resolve('Bacon') == 'foo.bar.Bacon'
    assert addr.resolve('foo.bar.Bacon') == 'foo.bar.Bacon'
    assert addr.resolve('google.example.Bacon') == 'google.example.Bacon'


def test_doc_nothing():
    meta = metadata.Metadata()
    assert meta.doc == ''


def test_doc_leading_trumps_all():
    meta = make_doc_meta(leading='foo', trailing='bar', detached=['baz'])
    assert meta.doc == 'foo'


def test_doc_trailing_trumps_detached():
    meta = make_doc_meta(trailing='spam', detached=['eggs'])
    assert meta.doc == 'spam'


def test_doc_detached_joined():
    meta = make_doc_meta(detached=['foo', 'bar'])
    assert meta.doc == 'foo\n\nbar'


def make_doc_meta(
        *,
        leading: str = '',
        trailing: str = '',
        detached: typing.List[str] = [],
        ) -> descriptor_pb2.SourceCodeInfo.Location:
    return metadata.Metadata(
        documentation=descriptor_pb2.SourceCodeInfo.Location(
            leading_comments=leading,
            trailing_comments=trailing,
            leading_detached_comments=detached,
        ),
    )
