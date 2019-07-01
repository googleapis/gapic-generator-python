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

import gapic.samplegen.samplegen as samplegen
import gapic.utils as utils

from collections import namedtuple
from textwrap import dedent

# Injected dummy test types
dummy_method_fields = ["lro",
                       "paged_result_field",
                       "client_streaming",
                       "server_streaming"]
DummyMethod = namedtuple("DummyMethod",
                         dummy_method_fields)
DummyMethod.__new__.__defaults__ = (False,)*len(dummy_method_fields)

DummyService = namedtuple("DummyService", ["methods"])

DummyApiSchema = namedtuple("DummyApiSchema", ["services"])

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        searchpath=path.realpath(path.join(path.dirname(__file__),
                                           "..", "..", "..",
                                           "gapic", "templates", "examples"))),
    undefined=jinja2.StrictUndefined,
    extensions=["jinja2.ext.do"],
    trim_blocks=True, lstrip_blocks=True
)
env.filters['snake_case'] = utils.to_snake_case


def test_generate_sample_basic():
    # Note: the sample integration tests are needfully large
    # and difficult to eyeball parse. They
    schema = DummyApiSchema(
        {"animalia.mollusca.v1.Mollusc": DummyService({"Classify": DummyMethod()})})

    sample = {"service": "animalia.mollusca.v1.Mollusc",
              "rpc": "Classify",
              "region_tag": "mollusc_classify_sync",
              "description": "Determine the full taxonomy of input mollusc",
              "request": [{"field": "classify_request.video",
                           "value": "path/to/mollusc/video.mkv",
                           "input_parameter": "video",
                           "value_is_file": True}],
              "response": [{"print": ["Mollusc is a %s", "$resp.taxonomy"]}]}

    fpath, template_stream = samplegen.generate_sample(sample, env, schema)
    sample_str = "".join(iter(template_stream))

    with open("/usr/local/google/home/dovs/tmp/sample.py", "w") as f:
        f.write(sample_str)

    assert sample_str == '''# -*- coding: utf-8 -*-
#
# Copyright (C) 2019  Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# DO NOT EDIT! This is a generated sample ("CallingForm.Request",  "mollusc_classify_sync")
#
# To install the latest published package dependency, execute the following:
#   pip3 install TODO


# [START mollusc_classify_sync]

def sample_classify(video):
    """Determine the full taxonomy of input mollusc"""

    # [START mollusc_classify_sync_core]

    client = mollusca_v1.MolluscClient()

    classify_request = {}
    # video = "path/to/mollusc/video.mkv"
    with open(video, "rb") as f:
        classify_request["video"] = f.read()



    response = client.Classify(classify_request)

    print("Mollusc is a {}", response.taxonomy)


    # [END mollusc_classify_sync_core]

# [END mollusc_classify_sync]

def main():
    import argparse

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    sample_classify()


if __name__ == "__main__":
    main()
'''


def test_generate_sample_service_not_found():
    schema = DummyApiSchema({})
    sample = {"service": "Mollusc"}

    with pytest.raises(samplegen.UnknownService):
        samplegen.generate_sample(sample, env, schema)


def test_generate_sample_rpc_not_found():
    schema = DummyApiSchema({"Mollusc": DummyService({})})
    sample = {"service": "Mollusc", "rpc": "Classify"}

    with pytest.raises(samplegen.RpcMethodNotFound):
        samplegen.generate_sample(sample, env, schema)
