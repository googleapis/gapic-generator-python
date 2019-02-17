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

import dataclasses
import os
import re
from typing import Iterable, Sequence, Tuple

from google.api import client_pb2
from google.protobuf import descriptor_pb2

from gapic import utils


@dataclasses.dataclass(frozen=True)
class Naming:
    """Naming data for an API.

    This class contains the naming nomenclature used for this API
    within templates.

    An instance of this object is made available to every template
    (as ``api.naming``).
    """
    name: str = ''
    namespace: Tuple[str] = dataclasses.field(default_factory=tuple)
    version: str = ''
    product_name: str = ''
    proto_package: str = ''

    def __post_init__(self):
        if not self.product_name:
            self.__dict__['product_name'] = self.name

    @classmethod
    def build(cls,
            *file_descriptors: Iterable[descriptor_pb2.FileDescriptorProto]
            ) -> 'Naming':
        """Return a full Naming instance based on these file descriptors.

        This is pieced together from the proto package names as well as the
        ``google.api.metadata`` file annotation. This information may be
        present in one or many files; this method is tolerant as long as
        the data does not conflict.

        Args:
            file_descriptors (Iterable[~.FileDescriptorProto]): A list of
                file descriptor protos. This list should only include the
                files actually targeted for output (not their imports).

        Returns:
            ~.Naming: A :class:`~.Naming` instance which is provided to
                templates as part of the :class:`~.API`.

        Raises:
            ValueError: If the provided file descriptors contain contradictory
                information.
        """
        # Determine the set of proto packages.
        proto_packages = {fd.package for fd in file_descriptors}
        root_package = os.path.commonprefix(tuple(proto_packages)).rstrip('.')

        # Sanity check: If there is no common ground in the package,
        # we are obviously in trouble.
        if not root_package:
            raise ValueError(
                'The protos provided do not share a common root package. '
                'Ensure that all explicitly-specified protos are for a '
                'single API. '
                f'The packages we got are: {", ".join(proto_packages)}'
            )

        # Define the valid regex to split the package.
        #
        # It is not necessary for the regex to be as particular about package
        # name validity (e.g. avoiding .. or segments starting with numbers)
        # because protoc is guaranteed to give us valid package names.
        pattern = r'^((?P<namespace>[a-z0-9_.]+)\.)?(?P<name>[a-z0-9_]+)'

        # Only require the version portion of the regex if the version is
        # present.
        #
        # This code may look counter-intuitive (why not use ? to make it
        # optional), but the engine's greediness routine will decide that
        # the version is the name, which is not what we want.
        version = r'\.(?P<version>v[0-9]+(p[0-9]+)?((alpha|beta)[0-9]+)?)'
        if re.search(version, root_package):
            pattern += version

        # Okay, do the match
        match = re.search(pattern=pattern, string=root_package).groupdict()
        match['namespace'] = match['namespace'] or ''
        package_info = cls(
            name=match['name'].capitalize(),
            namespace=tuple([i.capitalize()
                             for i in match['namespace'].split('.') if i]),
            product_name=match['name'].capitalize(),
            proto_package=root_package,
            version=match.get('version', ''),
        )

        # Sanity check: Ensure that the package directives all inferred
        # the same information.
        if not package_info.version and len(proto_packages) > 1:
            raise ValueError('All protos must have the same proto package '
                             'up to and including the version.')

        # Iterate over the metadata annotations and collect the package
        # information from there.
        #
        # This creates a naming class non-empty metadata annotation and
        # uses Python's set logic to de-duplicate. There should only be one.
        explicit_pkgs = set()
        for fd in file_descriptors:
            pkg = fd.options.Extensions[client_pb2.client_package]
            naming = cls(
                name=pkg.title or pkg.product_title,
                namespace=tuple(pkg.namespace),
                version=pkg.version,
            )
            if naming:
                explicit_pkgs.add(naming)

        # Sanity check: Ensure that any google.api.metadata provisions were
        # consistent.
        if len(explicit_pkgs) > 1:
            raise ValueError(
                'If the google.api.client_package annotation is provided in '
                'more than one file, it must be consistent.',
            )

        # Merge the package naming information and the metadata naming
        # information, with the latter being preferred.
        # Return a Naming object which effectively merges them.
        if len(explicit_pkgs):
            return dataclasses.replace(package_info,
                **dataclasses.asdict(explicit_pkgs.pop()),
            )
        return package_info

    def __bool__(self):
        """Return True if any of the fields are truthy, False otherwise."""
        return any(
            [getattr(self, i.name) for i in dataclasses.fields(self)],
        )

    @property
    def long_name(self) -> str:
        """Return an appropriate title-cased long name."""
        return ' '.join(tuple(self.namespace) + (self.name,))

    @property
    def module_name(self) -> str:
        """Return the appropriate Python module name."""
        return utils.to_valid_module_name(self.name)

    @property
    def module_namespace(self) -> Sequence[str]:
        """Return the appropriate Python module namespace as a tuple."""
        return tuple(utils.to_valid_module_name(i) for i in self.namespace)

    @property
    def namespace_packages(self) -> Tuple[str]:
        """Return the appropriate Python namespace packages."""
        answer = []
        for cursor in [i.lower() for i in self.namespace]:
            answer.append(f'{answer[-1]}.{cursor}' if answer else cursor)
        return tuple(answer)

    @property
    def versioned_module_name(self) -> str:
        """Return the versiond module name (e.g. ``apiname_v1``).

        If there is no version, this is the same as ``module_name``.
        """
        if self.version:
            return f'{self.module_name}_{self.version}'
        return self.module_name

    @property
    def warehouse_package_name(self) -> str:
        """Return the appropriate Python package name for Warehouse."""

        # Piece the name and namespace together to come up with the
        # proper package name.
        answer = list(self.namespace) + self.name.split(' ')
        return '-'.join(answer).lower()
