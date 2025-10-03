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

from unittest import mock

from gapic import utils


def test_rst_unformatted():
    assert utils.rst("The hail in Wales") == "The hail in Wales"


def test_rst_formatted():
    assert utils.rst("The hail in `Wales`") == "The hail in `Wales`"


def test_rst_add_newline():
    s = "The hail in Wales\nfalls mainly on the snails."
    assert utils.rst(s) == s + "\n"


def test_rst_force_add_newline():
    s = "The hail in Wales"
    assert utils.rst(s, nl=True) == s + "\n"


def test_rst_disable_add_newline():
    s = "The hail in Wales\nfalls mainly on the snails."
    assert utils.rst(s, nl=False) == s


def test_rst_pad_close_quote():
    s = 'A value, as in "foo"'
    assert utils.rst(s) == s + "."
