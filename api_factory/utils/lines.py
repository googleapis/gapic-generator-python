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

import textwrap
from typing import Tuple, Union


def subsequent_indent(text: str, prefix: str) -> str:
    """Decorates the text string with the given prefix on hanging lines.

    A "hanging" line is any line except for the first one. After prefixing,
    if any lines end in whitespace, that whitespace is stripped.

    This is provided to all templates as the ``subsequent_indent`` filter.

    Args:
        text (str): The text string.
        prefix (str): The prefix to use.

    Returns:
        str: The string with all hanging lines prefixed.
    """
    lines = text.split('\n')
    lines[1:] = [f'{prefix}{s}'.rstrip() for s in lines[1:]]
    return '\n'.join(lines)


def wrap(text: str, width: int, offset: Union[int, Tuple[int,int]] = 0) -> str:
    """Wrap the given string to the given width.

    This uses :meth:`textwrap.fill` under the hood, but provides useful
    offset functionality for Jinja templates.

    This is provided to all templates as the ``wrap`` filter.

    Args:
        text (str): The initial text string.
        width (int): The width at which to wrap the text. If offset is
            provided, these are automatically counted against this.
        offset (Union[int, Tuple[int, int]]): An offset for the text.
            This can be specified as an int or a tuple or two ints (using an
            int is identical to a tuple with that int specified twice);
            the tuple form is ``(first_line, subsequent_lines)``.

            The first line value applies to the first line; this value is
            subtracted from ``width`` for the first line only. No leading
            whitespace is added (the template is assumed to have it).

            The subsequent lines value applies to all subsequent lines; each
            line will be indented by this many characters.

    Returns:
        str: The wrapped string.
    """
    # Sanity check: If there is empty text, abort.
    if not text:
        return ''

    # Coerce the offset value into a tuple.
    if isinstance(offset, int):
        offset = (offset, offset)

    # Protocol buffers preserves single initial spaces after line breaks
    # when parsing comments (such as the space before the "w" in "when" here).
    # Re-wrapping causes these to be two spaces; correct for this.
    text = text.replace('\n ', '\n')

    # If the initial width is different (in other words, the initial offset
    # is non-zero), break off the beginning of the string.
    first = ''
    if offset[0] > 0:
        initial = textwrap.wrap(text,
            break_long_words=False,
            width=width - offset[0],
        )
        first = f'{initial[0]}\n'
        text = ' '.join(initial[1:])

    # Wrap the remainder of the string at the desired width.
    return '{first}{text}'.format(
        first=first,
        text=textwrap.fill(
            break_long_words=False,
            initial_indent=' ' * offset[1] if first else '',
            subsequent_indent=' ' * offset[1],
            text=text,
            width=width,
        ),
    ).rstrip('\n')
