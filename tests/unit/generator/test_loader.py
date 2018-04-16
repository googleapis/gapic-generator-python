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

from unittest import mock

import jinja2

from api_factory.generator.loader import TemplateLoader


def test_get_source():
    # This test is ensuring that the _loaded property is added to
    # whenever get_source is called.
    #
    # This is effectively a pure subset of the remanining_templates test,
    # but `get_source` is a public method.
    loader = TemplateLoader(searchpath='<<< IRRELEVANT >>>')
    env = jinja2.Environment()
    with mock.patch.object(jinja2.FileSystemLoader, 'get_source') as super_gs:
        super_gs.return_value = ('', '', 0)  # Throwaway return value.
        loader.get_source(env, 'foo')
        super_gs.assert_called_once_with(env, 'foo')
        assert 'foo' in loader._loaded


def test_remaining_templates():
    # This test is ensuring that the remaining_templates property returns
    # back unrendered templates only.
    loader = TemplateLoader(searchpath='<<< IRRELEVANT >>>')
    with mock.patch.object(loader, 'list_templates') as list_templates:
        list_templates.return_value = ['a', 'b', 'c']
        with mock.patch.object(jinja2.FileSystemLoader, 'get_source') as sgs:
            sgs.return_value = ('', '', 0)  # Throwaway return value.
            assert loader.remaining_templates == {'a', 'b', 'c'}
            loader.get_source(jinja2.Environment(), 'b')
            assert loader.remaining_templates == {'a', 'c'}
            loader.get_source(jinja2.Environment(), 'b')
            assert loader.remaining_templates == {'a', 'c'}
