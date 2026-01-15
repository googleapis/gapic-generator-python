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
from typing import Optional, Dict

import pypandoc  # type: ignore

from gapic.utils.lines import wrap

# Cache for the few complex items we actually send to pandoc
_RAW_RST_CACHE: Dict[str, str] = {}

def _tuned_fast_convert(text: str) -> Optional[str]:
    """
    Converts Markdown to RST using pure Python.
    Only falls back to Pandoc for Tables and Images.
    """
    # --- 1. FALLBACKS ---
    # Tables (pipe surrounded by spaces) or Images (![).
    # We allow "][" (Reference Links) to be handled by Python now.
    if (re.search(r" \| ", text) or re.search(r"\|\n", text)) or "![" in text:
        return None

    # --- 2. CONVERSION ---

    # A. CODE BLOCKS: `code` -> ``code``
    # CRITICAL: Run this FIRST. This ensures we handle existing backticks
    # before we create NEW backticks for links.
    # (?<!:) ensures we don't break Sphinx roles like :class:`MyClass`
    converted = re.sub(r"(?<!:|`)`([^`]+)`(?!`)", r"``\1``", text)
    
    # B. REFERENCE LINKS: [Text][Ref] -> `Text <Ref>`__
    # We fix the broken documentation by converting these to valid RST links.
    # Since step A is done, these new backticks will NOT be doubled.
    converted = re.sub(r"\[([^\]]+)\]\[([^\]]+)\]", r"`\1 <\2>`__", converted)

    # C. STANDARD LINKS: [Text](URL) -> `Text <URL>`__
    converted = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"`\1 <\2>`__", converted)

    # D. BOLD/ITALICS:
    converted = re.sub(r"(?<!_)\b_([^_]+)_\b(?!_)", r"*\1*", converted)

    # E. HEADINGS: # Heading -> Heading\n=======
    converted = re.sub(r"^# (.*)$", r"\1\n" + "=" * 10, converted, flags=re.MULTILINE)
    converted = re.sub(r"^## (.*)$", r"\1\n" + "-" * 10, converted, flags=re.MULTILINE)

    # F. LISTS: Markdown (- item) needs a preceding newline for RST.
    converted = re.sub(r"(\n[^-*].*)\n\s*([-*] )", r"\1\n\n\2", converted)

    return converted

def rst(
    text: str,
    width: int = 72,
    indent: int = 0,
    nl: Optional[bool] = None,
    source_format: str = "commonmark",
):
    # 1. Super Fast Path: No special chars? Just wrap.
    if not re.search(r"[|*`_[\]#]", text):
        answer = wrap(text, indent=indent, offset=indent + 3, width=width - indent)
        return _finalize(answer, nl, indent)

    # 2. Check Cache
    if text in _RAW_RST_CACHE:
        raw_rst = _RAW_RST_CACHE[text]
    else:
        # 3. Try Tuned Python Convert (Fastest)
        fast_result = _tuned_fast_convert(text)
        
        if fast_result is not None:
            raw_rst = fast_result.strip()
        else:
            # 4. Fallback to Pandoc (Only for Tables/Images)
            raw_rst = pypandoc.convert_text(
                text, "rst", format=source_format, extra_args=["--columns=1000"]
            ).strip()
            
        _RAW_RST_CACHE[text] = raw_rst

    # 5. Python Formatting
    if "::" in raw_rst or ".. code" in raw_rst:
        answer = raw_rst.replace("\n", f"\n{' ' * indent}")
    else:
        answer = wrap(raw_rst, indent=indent, offset=indent, width=width - indent)

    return _finalize(answer, nl, indent)


def _finalize(answer, nl, indent):
    """Helper to handle trailing newlines and quotes."""
    if nl or ("\n" in answer and nl is None):
        answer += "\n" + " " * indent
    if answer.endswith('"'):
        answer += "."
    return answer
