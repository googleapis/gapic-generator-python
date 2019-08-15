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

import os
import time
from typing import Tuple

from gapic.samplegen_utils import yaml


BASE_PATH_KEY = "base_path"
DEFAULT_SAMPLE_DIR = "samples"

PYTHON3_ENVIRONMENT = yaml.Map(
    name="python",
    anchor_name="python",
    elements=[
        yaml.KeyVal("environment", "python"),
        yaml.KeyVal("bin", "python3"),
        yaml.KeyVal(BASE_PATH_KEY, DEFAULT_SAMPLE_DIR),
        yaml.KeyVal("invocation", "'{bin} {path} @args'"),
    ],
)


def generate_manifest(
        fpaths_and_samples,
        base_path: str,
        api_schema,
        *,
        environment: yaml.Map = PYTHON3_ENVIRONMENT,
        manifest_time: int = None
) -> Tuple[str, yaml.Doc]:
    """Generate a samplegen manifest for use by sampletest

    Args:
        fpaths_and_samples (Iterable[Tuple[str, Mapping[str, Any]]]):
                         The file paths and samples to be listed in the manifest
        base_path (str): The base directory where the samples are generated.
        api_schema (~.api.API): An API schema object.
        environment (yaml.Map): Optional custom sample execution environment.
                                Set this if the samples are being generated for
                                a custom language.
        manifest_time (int): Optional. An override for the timestamp in the name of the manifest filename.
                             Primarily used for testing.

    Returns:
        Tuple[str, yaml.Doc]: The filename of the manifest and the manifest data as a dictionary.

    """
    # Use iter([]) instead of a generator expression due to a bug in pytest.
    # See https://github.com/pytest-dev/pytest-cov/issues/310 for details.
    base_path = next(
        iter(
            [e.val  # type: ignore
             for e in environment.elements
             if e.key == BASE_PATH_KEY]  # type: ignore
        ),
        DEFAULT_SAMPLE_DIR
    )
    doc = yaml.Doc(
        [
            yaml.KeyVal("type", "manifest/samples"),
            yaml.KeyVal("schema_version", "3"),
            environment,
            yaml.Collection(
                name="samples",
                elements=[
                    [  # type: ignore
                        # Mypy doesn't correctly intuit the type of the
                        # "region_tag" conditional expression.
                        yaml.Alias(environment.anchor_name or ""),
                        yaml.KeyVal("sample", sample["id"]),
                        yaml.KeyVal(
                            "path",
                            "'{base_path}/%s'" % os.path.relpath(fpath, base_path)
                        ),
                        (yaml.KeyVal("region_tag", sample["region_tag"])
                         if "region_tag" in sample else
                         yaml.Null),
                    ]
                    for fpath, sample in fpaths_and_samples
                ],
            ),
        ]
    )

    dt = time.gmtime(manifest_time)
    manifest_fname_template = (
        "{api}.{version}.{language}."
        "{year:04d}{month:02d}{day:02d}."
        "{hour:02d}{minute:02d}{second:02d}."
        "manifest.yaml"
    )

    manifest_fname = manifest_fname_template.format(
        api=api_schema.naming.name,
        version=api_schema.naming.version,
        language=environment.name,
        year=dt.tm_year,
        month=dt.tm_mon,
        day=dt.tm_mday,
        hour=dt.tm_hour,
        minute=dt.tm_min,
        second=dt.tm_sec,
    )

    return manifest_fname, doc
