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

import typing


Needle = typing.TypeVar('Needle')


def find_in_sequence(
        haystack: typing.Sequence[Needle],
        condition: typing.Callable[[Needle], bool]) -> typing.Optional[Needle]:
    """Find an item satisfying the condition in the list and return it.

    Args:
        haystack: Sequence[Any]: A sequence containing presumably-homogenous
            items.
        condition: Callable: A callable accepting one item in the sequence
            and returning a boolean. The first time the condition callable
            returns True, that item will be returned.

    Returns:
        Any: The first item to pass the condition.
    """
    for needle in haystack:
        if condition(needle):
            return needle
    return None
