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
import dataclasses
import os
import re
import sys
from typing import Callable, List, Mapping, Sequence, Tuple

from google.api import annotations_pb2
from google.longrunning import operations_pb2
from google.protobuf import descriptor_pb2

from api_factory import utils
from api_factory.schema import metadata
from api_factory.schema import wrappers


@dataclasses.dataclass(frozen=True)
class APINaming:
    """Naming data for an API.

    This class contains the naming nomenclature used for this API
    within templates.

    An instance of this object is made available to every template
    (as ``api.naming``).
    """
    name: str
    namespace: Tuple[str]
    version: str
    product_name: str
    product_url: str

    def __bool__(self):
        """Return True if any of the fields are truthy, False otherwise."""
        return any(
            [getattr(self, k) for k in dataclasses.fields(self).keys()],
        )

    @classmethod
    def build(
            cls,
            file_descriptors: Sequence[descriptor_pb2.FileDescriptorProto],
            ) -> 'APINaming':
        """Return a full APINaming instance based on these file descriptors.

        This is pieced together from the proto package names as well as the
        ``google.api.metadata`` file annotation. This information may be
        present in one or many files; this method is tolerant as long as
        the data does not conflict.

        Args:
            file_descriptors (Sequence[~.FileDescriptorProto]): A list of
                file descriptor protos. This list should only include the
                files actually targeted for output (not their imports).

        Returns:
            APINaming: An APINaming instance which is provided to templates.

        Raises:
            ValueError: If the provided file descriptors contain contradictory
                information.
        """
        # Determine the set of proto packages.
        proto_packages = {fd.package for fd in file_descriptors}
        root_package = os.path.commonprefix(proto_packages)

        # Define the valid regex to split the package.
        #
        # It is not necessary for the regex to be as particular about package
        # name validity (e.g. avoiding .. or segments starting with numbers)
        # because protoc is guaranteed to give us valid package names.
        match = re.search(pattern=''.join((
            r'^(?P<namespace>[a-z0-9_.]+\.)?',
            r'(?P<name>[a-z0-9_]+)',
            r'(\.(?P<version>v[0-9]+(p[0-9]+)?((alpha|beta|test)[0-9])*))?',
        )), string=root_package).groupdict()
        package_info = cls(
            name=match['name'].capitalize(),
            namespace=[i.capitalize() for i in match['namespace'].split('.')],
            product_name=match['name'].capitalize(),
            product_url='',
            version=match['version'],
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
        metadata_info = set()
        for fd in file_descriptors:
            meta = fd.options.Extensions[annotations_pb2.metadata]
            naming = cls(
                name=meta.package_name or meta.product_name,
                namespace=tuple(meta.package_namespace),
                product_name=meta.product_name,
                product_url=meta.product_url,
                version='',
            )
            if naming:
                metadata_info.add(naming)

        # Sanity check: Ensure that any google.api.metadata provisions were
        # consistent.
        if len(metadata_info) > 1:
            raise ValueError(
                'If the google.api.metadata annotation is provided in more '
                'than one file, it must be consistent.',
            )

        # Merge the package naming information and the metadata naming
        # information, with the latter being preferred.
        return package_info.replace(**dataclasses.asdict(metadata_info.pop()))
