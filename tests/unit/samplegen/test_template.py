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
import unittest
import gapic.samplegen.samplegen as samplegen
import gapic.samplegen.utils as utils


class TestTemplating(unittest.TestCase):

    def check_template(self, template_fragment, expected_output):
        # Making a new environment for every unit test seems wasteful,
        # but the obvious alternative (make env an instance attribute
        # and passing a FunctionLoader whose load function returns
        # a constantly reassigned string attribute) isn't any faster
        # and is less clear.
        env = jinja2.Environment(
            loader=jinja2.ChoiceLoader(
                [jinja2.FileSystemLoader(
                    searchpath=path.realpath(path.join(path.dirname(__file__),
                                                       "..", "..", "..",
                                                       "gapic", "templates", "examples"))),
                 jinja2.DictLoader({"template_fragment": template_fragment}),
                 ]),

            undefined=jinja2.StrictUndefined,
            extensions=["jinja2.ext.do"],
            trim_blocks=True, lstrip_blocks=True
        )

        env.filters["split_downcase"] = utils.split_caps_and_downcase

        template = env.get_template("template_fragment")
        text = template.render()
        self.assertEqual(text, expected_output)

    def test_handle_attr_value(self):
        self.check_template(
            '''{% import "feature_fragments.j2" as frags %}
{{ frags.handleRequestAttr("mollusc", {"field": "order",
                                       "value": "Molluscs.Cephalopoda.Coleoidea"}) }}
''',
            'mollusc["order"] = Molluscs.Cephalopoda.Coleoidea\n'
        )

    def test_handle_attr_input_parameter(self):
        self.check_template(
            '''{% import "feature_fragments.j2" as frags %}
{{ frags.handleRequestAttr("squid", {"field": "species",
                                     "value": "Humboldt",
                                     "input_parameter": "species"}) }}
''',
            '# species = "Humboldt"\nsquid["species"] = species\n')

    def test_handle_attr_file(self):
        self.check_template(
            '''{% import "feature_fragments.j2" as frags %}
{{ frags.handleRequestAttr("classify_mollusc_request",
                           {"field": "mollusc_video",
                            "value": "path/to/mollusc/video.mkv",
                            "input_parameter" : "mollusc_video_path",
                            "value_is_file": True})
}}
''',
            '''# mollusc_video_path = "path/to/mollusc/video.mkv"
with open(mollusc_video_path, "rb") as f:
  classify_mollusc_request["mollusc_video"] = f.read()
'''
        )

    def test_handle_request_basic(self):
        self.maxDiff = None
        self.check_template(
            '''{% import "feature_fragments.j2" as frags %}

{{ frags.handleRequest([{"base": "cephalopod",
                         "body": [{"field": "mantle_mass",
                                   "value": "10 kg",
                                   "input_parameter": "cephalopod_mass"},
                                  {"field": "photo",
                                   "value": "path/to/cephalopod/photo.jpg",
                                   "input_parameter": "photo_path",
                                   "value_is_file": True},
                                  {"field": "order",
                                   "value": "Molluscs.Cephalopoda.Coleoidea"}, ]},
                        {"base": "gastropod",
                         "body": [{"field": "mantle_mass",
                                   "value": "1 kg",
                                   "input_parameter": "gastropod_mass"},
                                  {"field": "order",
                                   "value": "Molluscs.Gastropoda.Pulmonata"},
                                  {"field": "movie",
                                   "value": "path/to/gastropod/movie.mkv",
                                   "input_parameter": "movie_path",
                                   "value_is_file": True}]}, ]) }}
''',
            '''
cephalopod = {}
# cephalopod_mass = "10 kg"
cephalopod["mantle_mass"] = cephalopod_mass

# photo_path = "path/to/cephalopod/photo.jpg"
with open(photo_path, "rb") as f:
  cephalopod["photo"] = f.read()

cephalopod["order"] = Molluscs.Cephalopoda.Coleoidea

gastropod = {}
# gastropod_mass = "1 kg"
gastropod["mantle_mass"] = gastropod_mass

gastropod["order"] = Molluscs.Gastropoda.Pulmonata

# movie_path = "path/to/gastropod/movie.mkv"
with open(movie_path, "rb") as f:
  gastropod["movie"] = f.read()

'''
        )

    def test_handle_print(self):
        self.check_template(
            '''{% import "feature_fragments.j2" as frags %}
{{ frags.handlePrint(["Mollusc"]) }}
''',
            '''print("Mollusc")
'''
        )

    def test_handle_print_args(self):
        self.check_template(
            '''{% import "feature_fragments.j2" as frags %}
{{ frags.handlePrint(["Molluscs: %s, %s, %s", "squid", "clam", "whelk"]) }}
''',
            '''print("Molluscs: {}, {}, {}", squid, clam, whelk)
'''
        )

    def test_handle_comment(self):
        self.check_template(
            '''{% import "feature_fragments.j2" as frags %}
{{ frags.handleComment(["Mollusc"]) }}
''',
            '''# Mollusc
'''
        )

    def test_handle_comment_args(self):
        self.check_template(
            '''{% import "feature_fragments.j2" as frags %}
{{ frags.handleComment(["Molluscs: %s, %s, %s", "squid", "clam", "whelk"]) }}
''',
            '''# Molluscs: squid, clam, whelk
'''
        )

    def test_define(self):
        self.check_template(
            '''{% import "feature_fragments.j2" as frags %}
{{ frags.handleDefine("squid=humboldt") }}
''',
            '''squid = humboldt
'''
        )

    def test_dispatch_print(self):
        self.check_template(
            '''{% import "feature_fragments.j2" as frags %}
{{ frags.dispatchStatement({"print" : ["Squid"] }) }}
''',
            '''print("Squid")
'''
        )

    def test_dispatch_comment(self):
        self.check_template(
            '''{% import "feature_fragments.j2" as frags %}
{{ frags.dispatchStatement({"comment" : ["Squid"] }) }}
''',
            '''# Squid
'''
        )

    def test_collection_loop(self):
        self.check_template(
            '''{% import "feature_fragments.j2" as frags %}

{{ frags.handleCollectionLoop({"collection": "molluscs",
                               "variable": "m",
                               "body": {"print": ["Mollusc: %s", "m"]}}) }}''',
            '''
for m in molluscs:
  print("Mollusc: {}", m)
'''
        )

    def test_dispatch_collection_loop(self):
        self.check_template(
            '''{% import "feature_fragments.j2" as frags %}

{{ frags.dispatchStatement({"loop": {"collection": "molluscs",
                               "variable": "m",
                               "body": {"print": ["Mollusc: %s", "m"]}}}) }}''',
            '''
for m in molluscs:
  print("Mollusc: {}", m)
'''
        )

    def test_map_loop(self):
        self.check_template(
            '''{% import "feature_fragments.j2" as frags %}

{{ frags.handleMapLoop({"map": "molluscs",
                        "key":"cls",
                        "value":"example",
                        "body": {"print": ["A %s is a %s", "example", "cls"] }})
}}''',
            '''
for cls, example in molluscs.items():
  print("A {} is a {}", example, cls)
'''
        )

    def test_map_loop_no_key(self):
        self.check_template(
            '''{% import "feature_fragments.j2" as frags %}

{{ frags.handleMapLoop({"map": "molluscs",
                        "value":"example",
                        "body": {"print": ["A %s is a mollusc", "example"] }})
}}''',
            '''
for _, example in molluscs.items():
  print("A {} is a mollusc", example)
'''
        )

    def test_map_loop_no_value(self):
        self.check_template(
            '''{% import "feature_fragments.j2" as frags %}

{{ frags.handleMapLoop({"map": "molluscs",
                        "key":"cls",
                        "body": {"print": ["A %s is a mollusc", "cls"] }})
}}''',
            '''
for cls, _ in molluscs.items():
  print("A {} is a mollusc", cls)
'''
        )

    def test_dispatch_map_loop(self):
        self.check_template(
            '''{% import "feature_fragments.j2" as frags %}

{{ frags.dispatchStatement({"loop":{"map": "molluscs",
                                    "key":"cls",
                                    "value":"example",
                                    "body": {
                                      "print": ["A %s is a %s", "example", "cls"] }}})
}}
''',
            '''
for cls, example in molluscs.items():
  print("A {} is a {}", example, cls)
'''
        )

    def test_main_block(self):
        self.check_template(
            '''{% import "feature_fragments.j2" as frags %}
{{ frags.handleMainBlock("ListMolluscs", [{"field": "list_molluscs.order",
                                           "value": "coleoidea",
                                           "input_parameter": "order"},
                                          {"field ": "list_molluscs.mass",
                                           "value": "60kg",
                                           "input_parameter": "mass"},
                                          {"field": "list_molluscs.zone",
                                           "value": "MESOPELAGIC"},]) }}
''',
            '''def main():
  import argparse

  parser = argparse.ArgumentParser()
  parser.add_argument("--order",
                      type=str,
                      default="coleoidea")
  parser.add_argument("--mass",
                      type=str,
                      default="60kg")
  args = parser.parse_args()

  sample_list_molluscs(args.order, args.mass)


if __name__ == "__main__":
  main()
'''
        )


if __name__ == "__main__":
    unittest.main()
