# Copyright 2020 Google LLC
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

import builtins
import itertools
import keyword


# The filter and map builtins are a historical artifact;
# they are not used in modern, idiomatic python,
# nor are they used in the gapic surface.
# They are too useful to reserve.
RESERVED_NAMES = frozenset(
    itertools.chain(
        keyword.kwlist,
        set(dir(builtins)) - {"filter", "map", "id"},
    )
)
