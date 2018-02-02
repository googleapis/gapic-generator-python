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

import jinja2


class TemplateLoader(jinja2.FileSystemLoader):
    """A jinja2 template loader that tracks what is left to be loaded.

    This class behaves identically to :class:`jinja2.FileSystemLoader`
    except that it adds an additional method for remaining templates
    which are in the directory or directories and have not yet been loaded
    with :meth:`get_source`.
    """
    def get_source(self,
            environment: jinja2.Environment,
            template: str,
        ) -> typing.Tuple[str, str, bool]:
        """Return information about the template.

        This method is generally called from the jinja2 environment, rather
        than directly.

        Args:
            environment (jinja2.Environment): The jinja2 environment.
            template (str): The template being loaded. This is generally
                what was provided to :meth:`get_template` on the
                ``environment``.

        Returns:
            Tuple[str, str, bool]: The template contents, filename, and
                whether the template is up to date, respectively.
        """
        contents, filename, current = super().get_source(environment, template)

        # Track that this filename has been loaded.
        # This removes that filename from `remaining_templates`.
        self.__dict__.setdefault('_loaded', set()).add(template)

        # Just return the answer from the superclass invocation above.
        return contents, filename, current

    @property
    def remaining_templates(self) -> typing.Set[str]:
        """Return the (public) templates not yet loaded.

        Templates already loaded are not included, nor are those beginning
        with underscore.

        This explicitly returns a metastatized set, not a generator,
        because the use case for this method is "go load all the remaining
        templates".

        Returns:
            set[str]: A list of templates not yet loaded.
        """
        # Start with the full list of templates, excluding private ones.
        available = set(filter(
            lambda t: not t.startswith('_'),
            self.list_templates(),
        ))

        # Remove all templates already loaded, and return the rest.
        loaded = self.__dict__.setdefault('_loaded', set())
        return available.difference(loaded)
