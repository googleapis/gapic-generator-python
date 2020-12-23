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

from gapic.utils import checks


def test_is_str():
    assert checks.is_str("'some string'")
    assert not checks.is_str("234")


def test_is_int():
    assert checks.is_int("234")
    assert not checks.is_str("23.4")


def test_is_call():
    assert checks.is_call("module.foo('bar')")
    assert not checks.is_call("{'some':'dict'}")
