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

import pytest

from google.protobuf import descriptor_pb2

from gapic.schema import naming


def test_long_name():
    n = make_naming(name='Genie', namespace=['Agrabah', 'Lamp'])
    assert n.long_name == 'Agrabah Lamp Genie'


def test_module_name():
    n = make_naming(
        name='Genie',
        namespace=['Agrabah', 'Lamp'],
        version='v2',
    )
    assert n.module_name == 'genie'


def test_versioned_module_name_no_version():
    n = make_naming(
        name='Genie',
        namespace=['Agrabah', 'Lamp'],
        version='',
    )
    assert n.versioned_module_name == 'genie'


def test_versioned_module_name():
    n = make_naming(
        name='Genie',
        namespace=['Agrabah', 'Lamp'],
        version='v2',
    )
    assert n.versioned_module_name == 'genie_v2'


def test_namespace_packages():
    n = make_naming(name='BigQuery', namespace=('Google', 'Cloud'))
    assert n.namespace_packages == ('google', 'google.cloud')


def test_warehouse_package_name_no_namespace():
    n = make_naming(name='BigQuery', namespace=[])
    assert n.warehouse_package_name == 'bigquery'


def test_warehouse_package_name_with_namespace():
    n = make_naming(
        name='BigQuery',
        namespace=('Google', 'Cloud'),
    )
    assert n.warehouse_package_name == 'google-cloud-bigquery'


def test_warehouse_package_name_multiple_words():
    n = make_naming(name='Big Query', namespace=[])
    assert n.warehouse_package_name == 'big-query'


def test_build_no_annotations():
    protos = (
        descriptor_pb2.FileDescriptorProto(
            name='baz_service.proto',
            package='foo.bar.baz.v1',
        ),
        descriptor_pb2.FileDescriptorProto(
            name='baz_common.proto',
            package='foo.bar.baz.v1',
        ),
    )
    n = naming.Naming.build(*protos)
    assert n.name == 'Baz'
    assert n.namespace == ('Foo', 'Bar')
    assert n.version == 'v1'
    assert n.product_name == 'Baz'


def test_build_no_annotations_no_version():
    protos = (
        descriptor_pb2.FileDescriptorProto(
            name='baz_service.proto',
            package='foo.bar',
        ),
        descriptor_pb2.FileDescriptorProto(
            name='baz_common.proto',
            package='foo.bar',
        ),
    )
    n = naming.Naming.build(*protos)
    assert n.name == 'Bar'
    assert n.namespace == ('Foo',)
    assert n.version == ''


def test_build_no_namespace():
    protos = (
        descriptor_pb2.FileDescriptorProto(
            name='foo_service.proto',
            package='foo',
        ),
    )
    n = naming.Naming.build(*protos)
    assert n.name == 'Foo'
    assert n.namespace == ()
    assert n.version == ''
    assert n.product_name == 'Foo'


def test_inconsistent_package_error():
    proto1 = descriptor_pb2.FileDescriptorProto(package='google.spanner.v1')
    proto2 = descriptor_pb2.FileDescriptorProto(package='spanner.v1')
    proto3 = descriptor_pb2.FileDescriptorProto(package='google.spanner.v2')

    # These should all error against one another.
    with pytest.raises(ValueError):
        naming.Naming.build(proto1, proto2)
    with pytest.raises(ValueError):
        naming.Naming.build(proto1, proto3)


def test_subpackages():
    proto1 = descriptor_pb2.FileDescriptorProto(package='google.ads.v0.foo')
    proto2 = descriptor_pb2.FileDescriptorProto(package='google.ads.v0.bar')
    n = naming.Naming.build(proto1, proto2)
    assert n.name == 'Ads'
    assert n.namespace == ('Google',)
    assert n.version == 'v0'


def make_naming(**kwargs) -> naming.Naming:
    kwargs.setdefault('name', 'Hatstand')
    kwargs.setdefault('namespace', ('Google', 'Cloud'))
    kwargs.setdefault('version', 'v1')
    kwargs.setdefault('product_name', 'Hatstand')
    return naming.Naming(**kwargs)
