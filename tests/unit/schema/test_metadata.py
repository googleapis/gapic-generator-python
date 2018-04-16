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

from api_factory.schema import metadata


def test_address_str_no_parent():
    addr = metadata.Address(package=['foo', 'bar'], module='baz')
    assert str(addr) == 'foo.bar'


def test_address_str_parent():
    addr = metadata.Address(package=['foo', 'bar'], module='baz',
                            parent=['spam', 'eggs'])
    assert str(addr) == 'foo.bar.spam.eggs'


def test_address_child():
    addr = metadata.Address(package=['foo', 'bar'], module='baz')
    child = addr.child('bacon')
    assert child.parent == ['bacon']
    assert str(child) == 'foo.bar.bacon'
    grandchild = child.child('ham')
    assert grandchild.parent == ['bacon', 'ham']
    assert str(grandchild) == 'foo.bar.bacon.ham'
