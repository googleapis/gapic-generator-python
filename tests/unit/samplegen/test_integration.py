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

import jinja2
import os.path as path
import pytest

import gapic.utils as utils

from gapic.samplegen import samplegen
from gapic.samplegen_utils import (types, utils as gapic_utils)
from gapic.schema import (naming, wrappers)

from common_types import (DummyMethod, DummyService,
                          DummyApiSchema, DummyNaming, message_factory, enum_factory)

from collections import namedtuple
from textwrap import dedent


env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        searchpath=path.realpath(path.join(path.dirname(__file__),
                                           "..", "..", "..",
                                           "gapic", "templates")
                                 )),
    undefined=jinja2.StrictUndefined,
    extensions=["jinja2.ext.do"],
    trim_blocks=True, lstrip_blocks=True
)
env.filters['snake_case'] = utils.to_snake_case
env.filters['coerce_response_name'] = gapic_utils.coerce_response_name


def test_generate_sample_basic():
    # Note: the sample integration tests are needfully large
    # and difficult to eyeball parse. They are intended to be integration tests
    # that catch errors in behavior that is emergent from combining smaller features
    # or in features that are sufficiently small and trivial that it doesn't make sense
    # to have standalone tests.
    api_naming = naming.Naming(name="MolluscClient", namespace=("molluscs", "v1"))
    service = wrappers.Service(
        service_pb=namedtuple('service_pb', ['name'])('MolluscClient'),
        methods={
            "Classify": DummyMethod(
                input=message_factory(
                    "mollusc.classify_request.video"),
                output=message_factory("$resp.taxonomy")
            )
        }
    )

    schema = DummyApiSchema(
        services={"animalia.mollusca.v1.Mollusc": service},
        naming=api_naming,
    )

    sample = {"service": "animalia.mollusca.v1.Mollusc",
              "rpc": "Classify",
              "id": "mollusc_classify_sync",
              "description": "Determine the full taxonomy of input mollusc",
              "request": [{"field": "classify_request.video",
                           "value": "path/to/mollusc/video.mkv",
                           "input_parameter": "video",
                           "value_is_file": True}],
              "response": [{"print": ["Mollusc is a %s", "$resp.taxonomy"]}]}

    sample_str = samplegen.generate_sample(
        sample,
        env,
        schema,
        env.get_template('examples/sample.py.j2')
    )

    sample_id = ("mollusc_classify_sync")
    expected_str = '''# TODO: add a copyright
# TODO: add a license
#
# DO NOT EDIT! This is a generated sample ("request",  "%s")
#
# To install the latest published package dependency, execute the following:
#   pip3 install molluscs-v1-molluscclient


# [START %s]
from google import auth
from google.auth import credentials
from molluscs.v1.molluscclient.services.mollusc_client import MolluscClient

def sample_classify(video):
    """Determine the full taxonomy of input mollusc"""

    client = MolluscClient(
        credentials=credentials.AnonymousCredentials(),
        transport="grpc",
    )

    classify_request = {}
    # video = "path/to/mollusc/video.mkv"
    with open(video, "rb") as f:
        classify_request["video"] = f.read()


    response = client.classify(classify_request)
    print("Mollusc is a {}".format(response.taxonomy))

# [END %s]

def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--video",
                        type=str,
                        default="path/to/mollusc/video.mkv")
    args = parser.parse_args()

    sample_classify(args.video)


if __name__ == "__main__":
    main()
''' % (sample_id, sample_id, sample_id)

    assert sample_str == expected_str


def test_generate_sample_service_not_found():
    schema = DummyApiSchema({}, DummyNaming("pkg_name"))
    sample = {"service": "Mollusc"}

    with pytest.raises(types.UnknownService):
        samplegen.generate_sample(
            sample,
            env,
            schema,
            env.get_template('examples/sample.py.j2'),
        )


def test_generate_sample_rpc_not_found():
    schema = DummyApiSchema(
        {"Mollusc": DummyService({})}, DummyNaming("pkg_name"))
    sample = {"service": "Mollusc", "rpc": "Classify"}

    with pytest.raises(types.RpcMethodNotFound):
        list(samplegen.generate_sample(
            sample,
            env,
            schema,
            env.get_template('examples/sample.py.j2')),
        )


def test_generate_sample_config_fpaths(fs):
    expected_path = 'cfgs/sample_config.yaml'
    fs.create_file(
        expected_path,
        contents=dedent(
            '''
            ---
            type: com.google.api.codegen.SampleConfigProto
            schema_version: 1.2.0
            samples:
            - service: google.cloud.language.v1.LanguageService
            '''
        )
    )
    actual_paths = list(gapic_utils.generate_all_sample_fpaths(expected_path))

    assert actual_paths == [expected_path]


def test_generate_sample_config_fpaths_not_yaml(fs):
    expected_path = 'cfgs/sample_config.not_yaml'
    fs.create_file(expected_path)

    with pytest.raises(types.InvalidConfig):
        list(gapic_utils.generate_all_sample_fpaths(expected_path))


def test_generate_sample_config_fpaths_bad_contents(
        fs,
        # Note the typo: SampleConfigPronto
        contents=dedent(
            '''
            ---
            type: com.google.api.codegen.SampleConfigPronto
            schema_version: 1.2.0
            samples:
            - service: google.cloud.language.v1.LanguageService
            '''
        )
):
    expected_path = 'cfgs/sample_config.yaml'
    fs.create_file(expected_path, contents=contents)

    with pytest.raises(types.InvalidConfig):
        list(gapic_utils.generate_all_sample_fpaths(expected_path))


def test_generate_sample_config_fpaths_bad_contents_old(fs):
    test_generate_sample_config_fpaths_bad_contents(
        fs,
        contents=dedent(
            '''
            ---
            type: com.google.api.codegen.SampleConfigProto
            schema_version: 1.1.0
            samples:
            - service: google.cloud.language.v1.LanguageService
            '''
        )
    )


def test_generate_sample_config_fpaths_bad_contents_no_samples(fs):
    test_generate_sample_config_fpaths_bad_contents(
        fs,
        contents=dedent(
            '''
            ---
            type: com.google.api.codegen.SampleConfigProto
            schema_version: 1.2.0
            '''
        )
    )


def test_generate_sample_config_partial_config(fs):
    expected_path = 'sample.yaml'
    fs.create_file(
        expected_path,
        # Note the typo: SampleConfigPronto
        contents=dedent(
            '''
            ---
            type: com.google.api.codegen.SampleConfigPronto
            schema_version: 1.2.0
            samples:
            - service: google.cloud.language.v1.LanguageService
            ---
            # Note: this one IS a valid config
            type: com.google.api.codegen.SampleConfigProto
            schema_version: 1.2.0
            samples:
            - service: google.cloud.language.v1.LanguageService
            '''
        )
    )
    expected_paths = [expected_path]

    actual_paths = list(gapic_utils.generate_all_sample_fpaths(expected_path))

    assert actual_paths == expected_paths


def test_generate_sample_config_fpaths_no_such_file(fs):
    with pytest.raises(types.InvalidConfig):
        list(gapic_utils.generate_all_sample_fpaths('cfgs/sample_config.yaml'))
