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
from gapic.schema import naming


def test_address_str():
    addr = metadata.Address(package=('foo', 'bar'), module='baz', name='Bacon')
    assert str(addr) == 'baz.Bacon'


def test_address_str_with_context():
    addr = metadata.Address(
        package=('foo', 'bar'),
        module='baz',
        name='Bacon',
    ).with_context(collisions={'baz'})
    assert str(addr) == 'fb_baz.Bacon'


def test_address_str_parent():
    addr = metadata.Address(package=('foo', 'bar'), module='baz', name='Bacon',
                            parent=('spam', 'eggs'))
    assert str(addr) == 'baz.spam.eggs.Bacon'


def test_address_proto():
    addr = metadata.Address(package=('foo', 'bar'), module='baz', name='Bacon')
    assert addr.proto == 'foo.bar.Bacon'
    assert addr.proto_package == 'foo.bar'


def test_address_child_no_parent():
    addr = metadata.Address(package=('foo', 'bar'), module='baz')
    child = addr.child('Bacon', path=(4, 0))
    assert child.name == 'Bacon'
    assert child.parent == ()
    assert child.module_path == (4, 0)


def test_address_child_with_parent():
    addr = metadata.Address(package=('foo', 'bar'), module='baz')
    child = addr.child('Bacon', path=(4, 0))
    grandchild = child.child('Ham', path=(2, 0))
    assert grandchild.parent == ('Bacon',)
    assert grandchild.name == 'Ham'
    assert grandchild.module_path == (4, 0, 2, 0)


def test_address_rel():
    addr = metadata.Address(package=('foo', 'bar'), module='baz', name='Bacon')
    assert addr.rel(
        metadata.Address(package=('foo', 'bar'), module='baz'),
    ) == 'Bacon'


def test_address_rel_other():
    addr = metadata.Address(package=('foo', 'bar'), module='baz', name='Bacon')
    assert addr.rel(
        metadata.Address(package=('foo', 'not_bar'), module='baz'),
    ) == 'baz.Bacon'
    assert addr.rel(
        metadata.Address(package=('foo', 'bar'), module='not_baz'),
    ) == 'baz.Bacon'


def test_address_rel_later():
    addr = metadata.Address(
        module='baz', module_path=(4, 1),
        name='Bacon', package=('foo', 'bar'),
    )
    other = metadata.Address(
        module='baz', module_path=(4, 0),
        name='Ham', package=('foo', 'bar'),
    )
    assert addr.rel(other) == "'Bacon'"


def test_address_rel_nested_sibling():
    addr = metadata.Address(
        module='baz', name='Bacon',
        package=('foo', 'bar'), parent=('Spam',)
    )
    other = metadata.Address(
        module='baz', name='Ham',
        package=('foo', 'bar'), parent=('Spam',)
    )
    assert addr.rel(other) == "'Spam.Bacon'"


def test_address_rel_nested_parent():
    parent = metadata.Address(module='baz', name='Ham', package=('foo', 'bar'))
    child = metadata.Address(
        module='baz', name='Bacon',
        package=('foo', 'bar'), parent=('Ham',)
    )
    assert child.rel(parent) == 'Bacon'


def test_address_resolve():
    addr = metadata.Address(package=('foo', 'bar'), module='baz', name='Qux')
    assert addr.resolve('Bacon') == 'foo.bar.Bacon'
    assert addr.resolve('foo.bar.Bacon') == 'foo.bar.Bacon'
    assert addr.resolve('google.example.Bacon') == 'google.example.Bacon'


def test_address_subpackage():
    addr = metadata.Address(
        package=('foo', 'bar', 'baz', 'v1', 'spam', 'eggs'),
        api_naming=naming.Naming(proto_package='foo.bar.baz.v1'),
    )
    assert addr.subpackage == ('spam', 'eggs')


def test_address_subpackage_no_version():
    addr = metadata.Address(
        package=('foo', 'bar', 'baz', 'spam', 'eggs'),
        api_naming=naming.Naming(proto_package='foo.bar.baz'),
    )
    assert addr.subpackage == ('spam', 'eggs')


def test_address_subpackage_empty():
    addr = metadata.Address(
        package=('foo', 'bar', 'baz', 'v1'),
        api_naming=naming.Naming(proto_package='foo.bar.baz.v1'),
    )
    assert addr.subpackage == ()


def test_metadata_with_context():
    meta = metadata.Metadata()
    assert meta.with_context(
        collisions={'foo', 'bar'},
    ).address.collisions == {'foo', 'bar'}


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
