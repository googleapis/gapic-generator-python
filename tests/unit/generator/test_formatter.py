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

from gapic.generator import formatter


def test_fix_whitespace_top_level():
    expected = textwrap.dedent("""\
    import something
    class Correct:
        pass
    class TooFarDown:
        pass
    class TooClose:  # remains too close
        pass
    """)

    result = formatter.fix_whitespace(textwrap.dedent("""\
    import something
    class Correct:
        pass
    class TooFarDown:
        pass
    class TooClose:  # remains too close
        pass
    """))
    assert result == expected, f"Expected {expected!r} but got {result!r}"


def test_fix_whitespace_nested():
    expected = textwrap.dedent("""\
    class JustAClass:
        def foo(self):
            pass
        def too_far_down(self):
            pass
    """)

    result = formatter.fix_whitespace(textwrap.dedent("""\
    class JustAClass:
        def foo(self):
            pass
        def too_far_down(self):
            pass
    """))
    assert result == expected, f"Expected {expected!r} but got {result!r}"


def test_fix_whitespace_decorators():
    expected = textwrap.dedent("""\
    class JustAClass:
        def foo(self):
            pass
        @property
        def too_far_down(self):
            return 42
    """)

    result = formatter.fix_whitespace(textwrap.dedent("""\
    class JustAClass:
        def foo(self):
            pass
        @property
        def too_far_down(self):
            return 42
    """))
    assert result == expected, f"Expected {expected!r} but got {result!r}"


def test_fix_whitespace_intermediate_whitespace():
    expected = textwrap.dedent("""\
    class JustAClass:
        def foo(self):
            pass
        @property
        def too_far_down(self):
            return 42
    """)

    result = formatter.fix_whitespace(textwrap.dedent("""\
    class JustAClass:
        def foo(self):
            pass
        \
        @property
        def too_far_down(self):
            return 42
    """))
    assert result == expected, f"Expected {expected!r} but got {result!r}"


def test_fix_whitespace_comment():
    expected = textwrap.dedent("""\
    def do_something():
        do_first_thing()
        # Something something something.
        do_second_thing()
    """)

    result = formatter.fix_whitespace(textwrap.dedent("""\
    def do_something():
        do_first_thing()
        # Something something something.
        do_second_thing()
    """))
    assert result == expected, f"Expected {expected!r} but got {result!r}"
    
    
 def test_fix_whitespace_trailing_whitespace():
    assert formatter.fix_whitespace("no trailing whitespace   \n") == "no trailing whitespace\n"

def test_fix_whitespace_empty_lines():
    assert formatter.fix_whitespace("\n\n\n") == "\n"

def test_fix_whitespace_multiline_comments():
    assert formatter.fix_whitespace(textwrap.dedent("""\
    class JustAClass:
        def foo(self):
            pass
        # This is a multi-line comment
        # with extra whitespaces
        @property
        def too_far_down(self):
            return 42
    """)) == textwrap.dedent("""\
    class JustAClass:
        def foo(self):
            pass
        # This is a multi-line comment
        # with extra whitespaces
        @property
        def too_far_down(self):
            return 42
    """)
   



