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

import functools

from gapic.utils.lines import wrap

@functools.lru_cache(maxsize=None)
def _convert_pandoc(text: str, columns: int, source_format: str) -> str:
    """Cached helper to run pypandoc with specific column width.
    
    Args:
        columns: Must be positive. Enforced by caller.
    """
    return pypandoc.convert_text(text, 'rst',
        format=source_format,
        extra_args=['--columns=%d' % columns],
        verify_format=False,
    ).strip()



def rst(
    text: str,
    width: int = 72,
    indent: int = 0,
    nl: Optional[bool] = None,
    source_format: str = "commonmark",
):
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
    # Quick check: If the text block does not appear to have any formatting,
    # do not convert it.
    # (This makes code generation significantly faster; calling out to pandoc
    # is by far the most expensive thing we do.)
    if not re.search(r"[|*`_[\]]", text):
        answer = wrap(
            text,
            indent=indent,
            offset=indent + 3,
            width=width - indent,
        )
    else:
        # Check if snake_case-only AND NOT a list.
        # This regex excludes underscores surrounded by word characters, meaning it finds "real" formatting.
        has_real_formatting = re.search(r"(?<!\w)_|_(?!\w)|[|*`\[\]]", text)
        is_list = re.search(r"^\s*([-+*]|\d+\.)\s+", text, re.MULTILINE)

        if not has_real_formatting and not is_list:
            # Mimic Pandoc behavior for plain text with snake_case:
            # 1. Collapse multiple spaces (Markdown behavior)
            text_normalized = re.sub(r'[ \t]+', ' ', text)
            # 2. Wrap without the specific 'docstring first line' offset
            answer = wrap(
                text_normalized,
                indent=indent,
                offset=0,
                width=width - indent,
            )
        else:
            # Convert from CommonMark to ReStructured Text.
            answer = _convert_pandoc(
                str(text), 
                width - indent, 
                str(source_format)
            ).replace('\n', f"\n{' ' * indent}")

    # Add a newline to the end of the document if any line breaks are
    # already present.
    #
    # This causes the closing """ to be on the subsequent line only when
    # appropriate.
    if nl or ("\n" in answer and nl is None):
        answer += "\n" + " " * indent

    # If the text ends in a double-quote, append a period.
    # This ensures that we do not get a parse error when this output is
    # followed by triple-quotes.
    if answer.endswith('"'):
        answer += "."

    # Done; return the answer.
    return answer
