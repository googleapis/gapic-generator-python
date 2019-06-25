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

import pytest
from collections import namedtuple

import gapic.samplegen.samplegen as samplegen
import gapic.samplegen.utils as utils


def test_define():
    define = {"define": "squid=$resp"}
    assert samplegen.validate_response([define])


def test_define_undefined_var():
    define = {"define": "squid=humboldt"}
    with pytest.raises(samplegen.UndefinedVariableReference):
        samplegen.validate_response([define])


def test_define_reserved_varname():
    define = {"define": "class=$resp"}
    with pytest.raises(samplegen.ReservedVariableName):
        samplegen.validate_response([define])


def test_define_add_var():
    assert samplegen.validate_response([{"define": "squid=$resp"},
                                        {"define": "name=squid.name"}])


def test_define_bad_form():
    define = {"define": "mollusc=$resp.squid=$resp.clam"}
    with pytest.raises(samplegen.BadAssignment):
        samplegen.validate_response([define])


def test_print_basic():
    print_statement = {"print": ["This is a squid"]}
    assert samplegen.validate_response([print_statement])


def test_print_fmt_str():
    print_statement = {"print": ["This is a squid named %s", "$resp.name"]}
    assert samplegen.validate_response([print_statement])


def test_print_fmt_mismatch():
    print_statement = {"print": ["This is a squid named %s"]}
    with pytest.raises(samplegen.MismatchedPrintStatement):
        samplegen.validate_response([print_statement])


def test_print_fmt_mismatch2():
    print_statement = {"print": ["This is a squid", "$resp.name"]}
    with pytest.raises(samplegen.MismatchedPrintStatement):
        samplegen.validate_response([print_statement])


def test_print_undefined_var():
    print_statement = {"print": ["This mollusc is a %s", "mollusc.type"]}
    with pytest.raises(samplegen.UndefinedVariableReference):
        samplegen.validate_response([print_statement])


def test_comment():
    comment = {"comment": ["This is a mollusc"]}
    assert samplegen.validate_response([comment])


def test_comment_fmt_str():
    comment = {"comment": ["This is a mollusc of class %s", "$resp.class"]}
    assert samplegen.validate_response([comment])


def test_comment_fmt_undefined_var():
    comment = {"comment": ["This is a mollusc of class %s", "cephalopod"]}
    with pytest.raises(samplegen.UndefinedVariableReference):
        samplegen.validate_response([comment])


def test_comment_fmt_mismatch():
    comment = {"comment": ["This is a mollusc of class %s"]}
    with pytest.raises(samplegen.MismatchedPrintStatement):
        samplegen.validate_response([comment])


def test_comment_fmt_mismatch2():
    comment = {"comment": ["This is a mollusc of class ", "$resp.class"]}
    with pytest.raises(samplegen.MismatchedPrintStatement):
        samplegen.validate_response([comment])


def test_loop_collection():
    loop = {"loop": {"collection": "$resp.molluscs",
                     "variable": "m",
                     "body": [{"print":
                               ["Mollusc of class: %s", "m.class"]}]}}
    assert samplegen.validate_response([loop])


def test_loop_undefined_collection():
    loop = {"loop": {"collection": "squid",
                     "variable": "s",
                     "body": [{"print":
                               ["Squid: %s", "s"]}]}}
    with pytest.raises(samplegen.UndefinedVariableReference):
        samplegen.validate_response([loop])


def test_loop_collection_extra_kword():
    loop = {"loop": {"collection": "$resp.molluscs",
                     "squid": "$resp.squids",
                     "variable": "m",
                     "body": [{"print":
                               ["Mollusc of class: %s", "m.class"]}]}}
    with pytest.raises(samplegen.BadLoop):
        samplegen.validate_response([loop])


def test_loop_collection_missing_kword():
    loop = {"loop": {"collection": "$resp.molluscs",
                     "body": [{"print":
                               ["Mollusc of class: %s", "m.class"]}]}}
    with pytest.raises(samplegen.BadLoop):
        samplegen.validate_response([loop])


def test_loop_collection_missing_kword2():
    loop = {"loop": {"collection": "$resp.molluscs",
                     "body": [{"print":
                               ["Mollusc: %s", "m.class"]}]}}
    with pytest.raises(samplegen.BadLoop):
        samplegen.validate_response([loop])


def test_loop_collection_missing_kword3():
    loop = {"loop": {"collection": "$resp.molluscs",
                     "variable": "r"}}
    with pytest.raises(samplegen.BadLoop):
        samplegen.validate_response([loop])


def test_loop_collection_reserved_loop_var():
    loop = {"loop": {"collection": "$resp.molluscs",
                     "variable": "class",
                     "body": [{"print":
                               ["Mollusc: %s", "class.name"]}]}}
    with pytest.raises(samplegen.ReservedVariableName):
        samplegen.validate_response([loop])


def test_loop_map():
    loop = {"loop": {"map": "$resp.molluscs",
                     "key": "cls",
                     "value": "mollusc",
                     "body": [{"print": ["A %s is a %s", "mollusc", "cls"]}]}}
    assert samplegen.validate_response([loop])


def test_loop_map_reserved_key():
    loop = {"loop": {"map": "$resp.molluscs",
                     "key": "class",
                     "value": "mollusc",
                     "body": [{"print": ["A %s is a %s", "mollusc", "class"]}]}}
    with pytest.raises(samplegen.ReservedVariableName):
        samplegen.validate_response([loop])


def test_loop_map_reserved_val():
    loop = {"loop": {"map": "$resp.molluscs",
                     "key": "m",
                     "value": "class",
                     "body": [{"print": ["A %s is a %s", "m", "class"]}]}}
    with pytest.raises(samplegen.ReservedVariableName):
        samplegen.validate_response([loop])


def test_loop_map_undefined():
    loop = {"loop": {"map": "molluscs",
                     "key": "name",
                     "value": "mollusc",
                     "body": [{"print": ["A %s is a %s", "mollusc", "name"]}]}}
    with pytest.raises(samplegen.UndefinedVariableReference):
        samplegen.validate_response([loop])


def test_loop_map_no_key():
    loop = {"loop": {"map": "$resp.molluscs",
                     "value": "mollusc",
                     "body": [{"print": ["Mollusc: %s", "mollusc"]}]}}
    assert samplegen.validate_response([loop])


def test_loop_map_no_value():
    loop = {"loop": {"map": "$resp.molluscs",
                     "key": "mollusc",
                     "body": [{"print": ["Mollusc: %s", "mollusc"]}]}}
    assert samplegen.validate_response([loop])


def test_loop_map_no_key_or_value():
    loop = {"loop": {"map": "$resp.molluscs",
                     "body": [{"print": ["Dead loop"]}]}}
    with pytest.raises(samplegen.BadLoop):
        samplegen.validate_response([loop])


def test_loop_map_no_map():
    loop = {"loop": {"key": "name",
                     "value": "mollusc",
                     "body": [{"print": ["A %s is a %s", "mollusc", "name"]}]}}
    with pytest.raises(samplegen.BadLoop):
        samplegen.validate_response([loop])


def test_loop_map_no_body():
    loop = {"loop": {"map": "$resp.molluscs",
                     "key": "name",
                     "value": "mollusc"}}
    with pytest.raises(samplegen.BadLoop):
        samplegen.validate_response([loop])


def test_loop_map_extra_kword():
    loop = {"loop": {"map": "$resp.molluscs",
                     "key": "name",
                     "value": "mollusc",
                     "phylum": "$resp.phylum",
                     "body": [{"print": ["A %s is a %s", "mollusc", "name"]}]}}
    with pytest.raises(samplegen.BadLoop):
        samplegen.validate_response([loop])


def test_invalid_statement():
    statement = {"print": ["Name"], "comment": ["Value"]}
    with pytest.raises(samplegen.InvalidStatement):
        samplegen.validate_response([statement])


def test_invalid_statement2():
    statement = {"squidify": ["Statement body"]}
    with pytest.raises(samplegen.InvalidStatement):
        samplegen.validate_response([statement])


def test_basic():
    assert samplegen.validate_and_transform_request(
        [{"field": "squid.mantle_length",
          "value": "100 cm"},
         {"field": "squid.mantle_mass",
          "value": "10 kg"}]) == [{"base": "squid",
                                   "body": [{"field": "mantle_length",
                                             "value": "100 cm"},
                                            {"field": "mantle_mass",
                                             "value": "10 kg"}]}]


def test_no_field_parameter():
    with pytest.raises(samplegen.InvalidRequestSetup):
        samplegen.validate_and_transform_request([{"squid": "humboldt"}])


def test_malformed_field_attr():
    with pytest.raises(samplegen.InvalidRequestSetup):
        samplegen.validate_and_transform_request([{"field": "squid"}])


def test_multiple_arguments():
    assert samplegen.validate_and_transform_request(
        [{"field": "squid.mantle_length",
          "value": "100 cm",
          "value_is_file": True},
         {"field": "clam.shell_mass",
          "value": "100 kg",
          "comment": "Clams can be large"}]) == [{"base": "squid",
                                                  "body": [{"field": "mantle_length",
                                                            "value": "100 cm",
                                                            "value_is_file": True}]},
                                                 {"base": "clam",
                                                  "body": [{"field": "shell_mass",
                                                            "value": "100 kg",
                                                            "comment": "Clams can be large"}]}]


def test_reserved_request_name():
    with pytest.raises(samplegen.ReservedVariableName):
        samplegen.validate_and_transform_request(
            [{"field": "class.order", "value": "coleoidea"}])


def test_duplicate_input_param():
    with pytest.raises(samplegen.DuplicateInputParameter):
        samplegen.validate_and_transform_request([{"field": "squid.mantle_mass",
                                                   "value": "10 kg",
                                                   "input_parameter": "mantle_mass"},
                                                  {"field": "clam.mantle_mass",
                                                   "value": "1 kg",
                                                   "input_parameter": "mantle_mass"}])


def test_reserved_input_param():
    with pytest.raises(samplegen.ReservedVariableName):
        samplegen.validate_and_transform_request([{"field": "mollusc.class",
                                                   "value": "cephalopoda",
                                                   "input_parameter": "class"}])


# split_caps_and_downcase is a small utility function
# that is the first part of turning CamelCase into snake_case

def test_split_caps_and_downcase():
    assert utils.split_caps_and_downcase("SquidClamWhelk") == [
        "squid", "clam", "whelk"]


def test_split_caps_and_downcase2():
    assert utils.split_caps_and_downcase("squidClamWhelk") == [
        "squid", "clam", "whelk"]


def test_split_caps_and_downcase3():
    assert utils.split_caps_and_downcase("SquidClamWhelK") == [
        "squid", "clam", "whel", "k"]


def test_split_caps_and_downcase4():
    assert utils.split_caps_and_downcase("Squid") == ["squid"]


def test_split_caps_and_downcase5():
    assert utils.split_caps_and_downcase("squid") == ["squid"]


def test_split_caps_and_downcase6():
    assert utils.split_caps_and_downcase("SQUID") == ["s", "q", "u", "i", "d"]


def test_calling_form():
    DummyMethod = namedtuple("DummyMethod",
                             ["lro",
                              "paged_result_field",
                              "client_streaming",
                              "server_streaming"])

    assert utils.CallingForm.method_default(DummyMethod(
        True, False, False, False)) == utils.CallingForm.LongRunningRequestAsync

    assert utils.CallingForm.method_default(DummyMethod(
        False, True, False, False)) == utils.CallingForm.RequestPagedAll

    assert utils.CallingForm.method_default(DummyMethod(
        False, False, True, False)) == utils.CallingForm.RequestStreamingClient

    assert utils.CallingForm.method_default(DummyMethod(
        False, False, False, True)) == utils.CallingForm.RequestStreamingServer

    assert utils.CallingForm.method_default(DummyMethod(
        False, False, False, False)) == utils.CallingForm.Request

    assert utils.CallingForm.method_default(DummyMethod(
        False, False, True, True)) == utils.CallingForm.RequestStreamingBidi
