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

import re


def is_str(expr: str) -> bool:
    """Determine if the expression stored in expr is a string literal.

    Args:
        expr (str): An expression of any type stored in a string.
    """
    return re.fullmatch(r'\'.*\'|\".*\"', expr)


def is_call(expr: str) -> bool:
    """Determine if the expression stored in expr is a constructor or method call.

    Args:
        expr (str): An expression of any type stored in a string.
    """
    return re.fullmatch(r'\w+(\.\w+)*\(.*\)', expr)


def is_int(expr: str) -> bool:
    """Determine if the expression stored in expr is an int.

    Args:
        expr (str): An expression of any type stored in a string.
    """
    return re.fullmatch(r'[0-9]+', expr)
