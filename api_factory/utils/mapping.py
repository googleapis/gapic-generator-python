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

import collections
from typing import Sequence


def recursive_update(target: collections.Mapping,
        *sources: Sequence[collections.Mapping],
        ) -> None:
    """Recursively update a dictionary.

    This is similar to dict.update, but applied recursively when dictionaries
    are found as values.

    Args:
        target (dict): A dictionary to be updated.
        sources (Sequence[dict]): Dictionaries with new key/value pairs to be
            applied to the target dictionary. These are processed in order,
            so in the event of a conflict, values in dictionaries passed later
            will take precedence.
    """
    for src in sources:
        for k, v in src.items():
            if isinstance(v, collections.Mapping):
                target[k] = recursive_update(target.get(k, {}), v)
            else:
                target[k] = v
