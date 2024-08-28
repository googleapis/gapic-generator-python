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
from typing import Optional

import pypandoc  # type: ignore

from gapic.utils.lines import wrap


def rst(text: str, width: int = 72, indent: int = 0, nl: Optional[bool] = None,
        source_format: str = 'commonmark'):
    """Convert the given text to ReStructured Text.

    Args:
        text (str): The text to convert.
        width (int): The number of columns.
        indent (int): The number of columns to indent each line of text
            (except the first).
        nl (bool): Whether to append a trailing newline.
            Defaults to appending a newline if the result is more than
            one line long.
        source_format (str): The source format. This is ``commonmark`` by
            default, which is what is used by convention in protocol buffers.

    Returns:
        str: The same text, in RST format.
    """
    answer = wrap(
        text,
        indent=indent,
        offset=indent + 3,
        width=width - indent,
    )

    # Add a newline to the end of the document if any line breaks are
    # already present.
    #
    # This causes the closing """ to be on the subsequent line only when
    # appropriate.
    if nl or ('\n' in answer and nl is None):
        answer += '\n' + ' ' * indent

    # If the text ends in a double-quote, append a period.
    # This ensures that we do not get a parse error when this output is
    # followed by triple-quotes.
    if answer.endswith('"'):
        answer += '.'

    # Done; return the answer.
    return answer
