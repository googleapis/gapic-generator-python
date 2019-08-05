# Copyright (C) 2019  Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module containing miscellaneous utilities
that will eventually move somewhere else (probably)."""

import os
import yaml

from typing import (Generator, Tuple)

from gapic.samplegen_utils import types


MIN_SCHEMA_VERSION = (1, 2, 0)

VALID_CONFIG_TYPE = "com.google.api.codegen.SampleConfigProto"


def generate_all_sample_fpaths(path: str) -> Generator[str, None, None]:
    """Given file or directory path, yield all valid sample config fpaths recursively.

    Arguments:
        path (str): The file or directory path to check
                    for valid samplegen config files.
                    Directories are checked recursively.

    Raises:
        types.InvalidConfig: If 'path' is an invalid sampleconfig file
                             or 'path' is not a file or directory.

    Returns:
        Generator[str, None, None]: All valid samplegen config files
                                    starting at 'path'.
    """
    def parse_version(version_str: str) -> Tuple[int, ...]:
        return tuple(int(tok) for tok in version_str.split("."))

    def is_valid_sampleconfig_p(doc) -> bool:
        version_token = "config_schema_version"
        return bool(
            # Yaml may return a dict, a list, or a str
            isinstance(doc, dict)
            and doc.get("type") == VALID_CONFIG_TYPE
            and parse_version(doc.get(version_token, "")) >= MIN_SCHEMA_VERSION
            and doc.get("samples")
        )

    # If a user passes in a directory to search for sample configs,
    # it is required to ignore any non-sample-config files so as to avoid
    # being unhelpfully strict.
    # Directly named files, however, should generate an error, because silently
    # ignoring them is less helpful than failing loudly.
    if os.path.isfile(path):
        if not path.endswith('.yaml'):
            raise types.InvalidConfig(f"Not a yaml file: {path}")

        with open(path) as f:
            if not all(is_valid_sampleconfig_p(doc)
                       for doc in yaml.safe_load_all(f.read())):
                raise types.InvalidConfig(
                    f"Not a valid sampleconfig file: {path}")

        yield path

    elif os.path.isdir(path):
        yaml_file_generator = (os.path.join(dirpath, fname)
                               for dirpath, _, fnames in os.walk(path)
                               for fname in fnames if fname.endswith(".yaml"))

        for fullpath in yaml_file_generator:
            with open(fullpath) as f:
                if all(is_valid_sampleconfig_p(doc)
                       for doc in yaml.safe_load_all(f.read())):
                    yield fullpath

    else:
        raise types.InvalidConfig(f"No such file or directory: {path}")
