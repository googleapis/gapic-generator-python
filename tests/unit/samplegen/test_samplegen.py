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

from collections import namedtuple

import unittest
import gapic.samplegen.samplegen as samplegen
import gapic.samplegen.utils as utils


class TestValidateResponse(unittest.TestCase):
    def test_define(self):
        define = {"define": "squid=$resp"}
        self.assertTrue(samplegen.validate_response([define]))

    def test_define_undefined_var(self):
        define = {"define": "squid=humboldt"}
        self.assertRaises(samplegen.UndefinedVariableReference,
                          samplegen.validate_response, [define])

    def test_define_reserved_varname(self):
        define = {"define": "class=$resp"}
        self.assertRaises(samplegen.ReservedVariableName,
                          samplegen.validate_response, [define])

    def test_define_add_var(self):
        self.assertTrue(samplegen.validate_response([{"define": "squid=$resp"},
                                                     {"define": "name=squid.name"}]))

    def test_define_bad_form(self):
        define = {"define": "mollusc=$resp.squid=$resp.clam"}
        self.assertRaises(samplegen.BadAssignment,
                          samplegen.validate_response, [define])

    def test_print_basic(self):
        print_statement = {"print": ["This is a squid"]}
        self.assertTrue(samplegen.validate_response([print_statement]))

    def test_print_fmt_str(self):
        print_statement = {"print": ["This is a squid named %s", "$resp.name"]}
        self.assertTrue(samplegen.validate_response([print_statement]))

    def test_print_fmt_mismatch(self):
        print_statement = {"print": ["This is a squid named %s"]}
        self.assertRaises(samplegen.MismatchedPrintStatement,
                          samplegen.validate_response, [print_statement])

    def test_print_fmt_mismatch2(self):
        print_statement = {"print": ["This is a squid", "$resp.name"]}
        self.assertRaises(samplegen.MismatchedPrintStatement,
                          samplegen.validate_response, [print_statement])

    def test_print_undefined_var(self):
        print_statement = {"print": ["This mollusc is a %s", "mollusc.type"]}
        self.assertRaises(samplegen.UndefinedVariableReference,
                          samplegen.validate_response, [print_statement])

    def test_comment(self):
        comment = {"comment": ["This is a mollusc"]}
        self.assertTrue(samplegen.validate_response([comment]))

    def test_comment_fmt_str(self):
        comment = {"comment": ["This is a mollusc of class %s", "$resp.class"]}
        self.assertTrue(samplegen.validate_response([comment]))

    def test_comment_fmt_undefined_var(self):
        comment = {"comment": ["This is a mollusc of class %s", "cephalopod"]}
        self.assertRaises(samplegen.UndefinedVariableReference,
                          samplegen.validate_response, [comment])

    def test_comment_fmt_mismatch(self):
        comment = {"comment": ["This is a mollusc of class %s"]}
        self.assertRaises(samplegen.MismatchedPrintStatement,
                          samplegen.validate_response, [comment])

    def test_comment_fmt_mismatch2(self):
        comment = {"comment": ["This is a mollusc of class ", "$resp.class"]}
        self.assertRaises(samplegen.MismatchedPrintStatement,
                          samplegen.validate_response, [comment])

    def test_loop_collection(self):
        loop = {"loop": {"collection": "$resp.molluscs",
                         "variable": "m",
                         "body": [{"print":
                                   ["Mollusc of class: %s", "m.class"]}]}}
        self.assertTrue(samplegen.validate_response([loop]))

    def test_loop_undefined_collection(self):
        loop = {"loop": {"collection": "squid",
                         "variable": "s",
                         "body": [{"print":
                                   ["Squid: %s", "s"]}]}}
        self.assertRaises(samplegen.UndefinedVariableReference,
                          samplegen.validate_response, [loop])

    def test_loop_collection_extra_kword(self):
        loop = {"loop": {"collection": "$resp.molluscs",
                         "squid": "$resp.squids",
                         "variable": "m",
                         "body": [{"print":
                                   ["Mollusc of class: %s", "m.class"]}]}}
        self.assertRaises(samplegen.BadLoop,
                          samplegen.validate_response, [loop])

    def test_loop_collection_missing_kword(self):
        loop = {"loop": {"collection": "$resp.molluscs",
                         "body": [{"print":
                                   ["Mollusc of class: %s", "m.class"]}]}}
        self.assertRaises(samplegen.BadLoop,
                          samplegen.validate_response, [loop])

    def test_loop_collection_missing_kword2(self):
        loop = {"loop": {"collection": "$resp.molluscs",
                         "body": [{"print":
                                   ["Mollusc: %s", "m.class"]}]}}
        self.assertRaises(samplegen.BadLoop,
                          samplegen.validate_response, [loop])

    def test_loop_collection_missing_kword3(self):
        loop = {"loop": {"collection": "$resp.molluscs",
                         "variable": "r"}}
        self.assertRaises(samplegen.BadLoop,
                          samplegen.validate_response, [loop])

    def test_loop_collection_reserved_loop_var(self):
        loop = {"loop": {"collection": "$resp.molluscs",
                         "variable": "class",
                         "body": [{"print":
                                   ["Mollusc: %s", "class.name"]}]}}
        self.assertRaises(samplegen.ReservedVariableName,
                          samplegen.validate_response, [loop])

    def test_loop_map(self):
        loop = {"loop": {"map": "$resp.molluscs",
                         "key": "cls",
                         "value": "mollusc",
                         "body": [{"print": ["A %s is a %s", "mollusc", "cls"]}]}}
        self.assertTrue(samplegen.validate_response([loop]))

    def test_loop_map_reserved_key(self):
        loop = {"loop": {"map": "$resp.molluscs",
                         "key": "class",
                         "value": "mollusc",
                         "body": [{"print": ["A %s is a %s", "mollusc", "class"]}]}}
        self.assertRaises(samplegen.ReservedVariableName,
                          samplegen.validate_response, [loop])

    def test_loop_map_reserved_val(self):
        loop = {"loop": {"map": "$resp.molluscs",
                         "key": "m",
                         "value": "class",
                         "body": [{"print": ["A %s is a %s", "m", "class"]}]}}
        self.assertRaises(samplegen.ReservedVariableName,
                          samplegen.validate_response, [loop])

    def test_loop_map_undefined(self):
        loop = {"loop": {"map": "molluscs",
                         "key": "name",
                         "value": "mollusc",
                         "body": [{"print": ["A %s is a %s", "mollusc", "name"]}]}}
        self.assertRaises(samplegen.UndefinedVariableReference,
                          samplegen.validate_response, [loop])

    def test_loop_map_no_key(self):
        loop = {"loop": {"map": "$resp.molluscs",
                         "value": "mollusc",
                         "body": [{"print": ["Mollusc: %s", "mollusc"]}]}}
        self.assertTrue(samplegen.validate_response([loop]))

    def test_loop_map_no_value(self):
        loop = {"loop": {"map": "$resp.molluscs",
                         "key": "mollusc",
                         "body": [{"print": ["Mollusc: %s", "mollusc"]}]}}
        self.assertTrue(samplegen.validate_response([loop]))

    def test_loop_map_no_key_or_value(self):
        loop = {"loop": {"map": "$resp.molluscs",
                         "body": [{"print": ["Dead loop"]}]}}
        self.assertRaises(samplegen.BadLoop,
                          samplegen.validate_response, [loop])

    def test_loop_map_no_map(self):
        loop = {"loop": {"key": "name",
                         "value": "mollusc",
                         "body": [{"print": ["A %s is a %s", "mollusc", "name"]}]}}
        self.assertRaises(samplegen.BadLoop,
                          samplegen.validate_response, [loop])

    def test_loop_map_no_body(self):
        loop = {"loop": {"map": "$resp.molluscs",
                         "key": "name",
                         "value": "mollusc"}}
        self.assertRaises(samplegen.BadLoop,
                          samplegen.validate_response, [loop])

    def test_loop_map_extra_kword(self):
        loop = {"loop": {"map": "$resp.molluscs",
                         "key": "name",
                         "value": "mollusc",
                         "phylum": "$resp.phylum",
                         "body": [{"print": ["A %s is a %s", "mollusc", "name"]}]}}
        self.assertRaises(samplegen.BadLoop,
                          samplegen.validate_response, [loop])

    def test_invalid_statement(self):
        statement = {"print": ["Name"], "comment": ["Value"]}
        self.assertRaises(samplegen.InvalidStatement,
                          samplegen.validate_response, [statement])

    def test_invalid_statement2(self):
        statement = {"squidify": ["Statement body"]}
        self.assertRaises(samplegen.InvalidStatement,
                          samplegen.validate_response, [statement])


class TestValidateRequest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(samplegen.validate_and_transform_request(
            [{"field": "squid.mantle_length", "value": "100 cm"},
             {"field": "squid.mantle_mass", "value": "10 kg"}]),

            [{"base": "squid", "body": [{"field": "mantle_length",
                                         "value": "100 cm"},
                                        {"field": "mantle_mass",
                                         "value": "10 kg"}]}]
        )

    def test_no_field_parameter(self):
        self.assertRaises(samplegen.InvalidRequestSetup,
                          samplegen.validate_and_transform_request,
                          [{"squid": "humboldt"}])

    def test_malformed_field_attr(self):
        self.assertRaises(samplegen.InvalidRequestSetup,
                          samplegen.validate_and_transform_request,
                          [{"field": "squid"}])

    def test_multiple_arguments(self):
        self.assertEqual(samplegen.validate_and_transform_request(
            [{"field": "squid.mantle_length",
              "value": "100 cm",
              "value_is_file": True},
             {"field": "clam.shell_mass",
              "value": "100 kg",
              "comment": "Clams can be large"}]),

            [{"base": "squid", "body": [{"field": "mantle_length",
                                         "value": "100 cm",
                                         "value_is_file": True}]},
             {"base": "clam",  "body": [{"field": "shell_mass",
                                         "value": "100 kg",
                                         "comment": "Clams can be large"}]}]
        )

    def test_reserved_request_name(self):
        self.assertRaises(samplegen.ReservedVariableName,
                          samplegen.validate_and_transform_request,
                          [{"field": "class.order", "value": "coleoidea"}])

    def test_duplicate_input_param(self):
        self.assertRaises(samplegen.DuplicateInputParameter,
                          samplegen.validate_and_transform_request,
                          [{"field": "squid.mantle_mass",
                            "value": "10 kg",
                            "input_parameter": "mantle_mass"},
                           {"field": "clam.mantle_mass",
                            "value": "1 kg",
                            "input_parameter": "mantle_mass"}])

    def test_reserved_input_param(self):
        self.assertRaises(samplegen.ReservedVariableName,
                          samplegen.validate_and_transform_request,
                          [{"field": "mollusc.class",
                            "value": "cephalopoda",
                            "input_parameter": "class"}])


class Snakify(unittest.TestCase):
    """split_caps_and_downcase is a small utility function
    that is the first part of turning CamelCase into snake_case"""

    def test_basic(self):
        self.assertEqual(utils.split_caps_and_downcase("SquidClamWhelk"),
                         ["squid", "clam", "whelk"])

    def test_basic2(self):
        self.assertEqual(utils.split_caps_and_downcase("squidClamWhelk"),
                         ["squid", "clam", "whelk"])

    def test_basic3(self):
        self.assertEqual(utils.split_caps_and_downcase("SquidClamWhelK"),
                         ["squid", "clam", "whel", "k"])

    def test_basic4(self):
        self.assertEqual(utils.split_caps_and_downcase("Squid"),
                         ["squid"])

    def test_basic5(self):
        self.assertEqual(utils.split_caps_and_downcase("squid"),
                         ["squid"])

    def test_basic6(self):
        self.assertEqual(utils.split_caps_and_downcase("SQUID"),
                         ["s", "q", "u", "i", "d"])


class TestCallingForm(unittest.TestCase):
    def test_calling_form(self):
        DummyMethod = namedtuple("DummyMethod",
                                 ["lro",
                                  "paged_result_field",
                                  "client_streaming",
                                  "server_streaming"])

        self.assertEqual(utils.CallingForm.method_default(
            DummyMethod(True, False, False, False)),
            utils.CallingForm.LongRunningRequestAsync)

        self.assertEqual(utils.CallingForm.method_default(
            DummyMethod(False, True, False, False)),
            utils.CallingForm.RequestPagedAll)

        self.assertEqual(utils.CallingForm.method_default(
            DummyMethod(False, False, True, False)),
            utils.CallingForm.RequestStreamingClient)

        self.assertEqual(utils.CallingForm.method_default(
            DummyMethod(False, False, False, True)),
            utils.CallingForm.RequestStreamingServer)

        self.assertEqual(utils.CallingForm.method_default(
            DummyMethod(False, False, False, False)),
            utils.CallingForm.Request)

        self.assertEqual(utils.CallingForm.method_default(
            DummyMethod(False, False, True, True)),
            utils.CallingForm.RequestStreamingBidi)


if __name__ == "__main__":
    unittest.main()
