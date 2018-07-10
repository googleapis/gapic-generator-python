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

from api_factory.schema import naming


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


def make_naming(**kwargs) -> naming.Naming:
    kwargs.setdefault('name', 'Hatstand')
    kwargs.setdefault('namespace', ('Google', 'Cloud'))
    kwargs.setdefault('version', 'v1')
    kwargs.setdefault('product_name', 'Hatstand')
    kwargs.setdefault('product_url', 'https://cloud.google.com/hatstand/')
    return naming.Naming(**kwargs)
