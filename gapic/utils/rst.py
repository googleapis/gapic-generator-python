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
from typing import Optional, List, Dict

import pypandoc  # type: ignore

from gapic.utils.lines import wrap

# --- PERFORMANCE CACHE ---
_RAW_RST_CACHE: Dict[str, str] = {}


def _aggressive_fast_convert(text: str) -> Optional[str]:
    """
    Converts common Markdown (Code, Links, Lists) to RST using pure Python.
    Only gives up (returns None) for complex structures like Tables.
    """
    # 1. TABLE CHECK (The only thing we strictly need Pandoc for)
    # If we see a pipe surrounded by spaces, it's likely a table.
    if re.search(r" \| ", text) or re.search(r"\|\n", text):
        return None

    # 2. CODE BLOCKS: `code` -> ``code``
    # RST requires double backticks. Markdown uses one.
    # We look for backticks that aren't already double.
    # Regex: Negative lookbehind/lookahead to ensure we don't match ``already rst``.
    converted = re.sub(r"(?<!`)`([^`]+)`(?!`)", r"``\1``", text)

    # 3. LINKS: [Text](URL) -> `Text <URL>`__
    # We use anonymous links (__) to avoid collision issues.
    converted = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"`\1 <\2>`__", converted)

    # 4. BOLD: **text** -> **text** (Compatible, no change needed)
    
    # 5. HEADINGS: # Heading -> Heading\n=======
    # (Simple fix for H1/H2, mostly sufficient for docstrings)
    converted = re.sub(r"^# (.*)$", r"\1\n" + "=" * 10, converted, flags=re.MULTILINE)
    converted = re.sub(r"^## (.*)$", r"\1\n" + "-" * 10, converted, flags=re.MULTILINE)

    # 6. LISTS: Markdown lists (- item) work in RST mostly fine.
    # We just ensure there's a newline before a list starts to satisfy RST strictness.
    converted = re.sub(r"(\n[^-*].*)\n\s*[-*] ", r"\1\n\n- ", converted)

    return converted


def batch_convert_docstrings(docstrings: List[str]):
    """
    Optimized Batch Processor.
    1. Tries Aggressive Python Conversion first.
    2. Only sends Tables/Complex items to Pandoc.
    """
    unique_docs = set(docstrings)
    
    # Filter: Only keep strings that need conversion and aren't in cache
    candidates = [
        d for d in unique_docs 
        if d 
        and d not in _RAW_RST_CACHE 
        and re.search(r"[|*`_[\]#]", d) # Only interesting chars
    ]
    
    if not candidates:
        return

    pandoc_batch: List[str] = []

    # 1. Try Python Conversion
    for doc in candidates:
        fast_result = _aggressive_fast_convert(doc)
        if fast_result is not None:
            # Success: Saved ~50ms per call
            _RAW_RST_CACHE[doc] = fast_result.strip()
        else:
            # Failed: Must use Pandoc (Tables, etc)
            pandoc_batch.append(doc)

    # 2. Process Remainder with Pandoc (Likely < 10 items)
    if not pandoc_batch:
        return

    separator = "\n\n__GAPIC_BATCH_SPLIT__\n\n"
    giant_payload = separator.join(pandoc_batch)

    try:
        converted_payload = pypandoc.convert_text(
            giant_payload,
            "rst",
            format="commonmark",
            extra_args=["--columns=1000"] 
        )
    except Exception:
        return

    split_marker = "__GAPIC_BATCH_SPLIT__"
    results = converted_payload.split(split_marker)

    if len(results) == len(pandoc_batch):
        for original, converted in zip(pandoc_batch, results):
            _RAW_RST_CACHE[original] = converted.strip()


def rst(
    text: str,
    width: int = 72,
    indent: int = 0,
    nl: Optional[bool] = None,
    source_format: str = "commonmark",
):
    """Convert the given text to ReStructured Text."""
    
    # 1. Super Fast Path: No special chars? Just wrap.
    if not re.search(r"[|*`_[\]#]", text):
        answer = wrap(
            text,
            indent=indent,
            offset=indent + 3,
            width=width - indent,
        )
        return _finalize(answer, nl, indent)

    # 2. Check Cache
    if text in _RAW_RST_CACHE:
        raw_rst = _RAW_RST_CACHE[text]
    else:
        # Slow Path: Missed by batch or new string.
        # TRY PYTHON CONVERT FIRST.
        # This prevents the 'Slow Path' from actually being slow.
        fast_result = _aggressive_fast_convert(text)
        
        if fast_result is not None:
            raw_rst = fast_result.strip()
        else:
            # The absolute last resort: Shell out to Pandoc
            raw_rst = pypandoc.convert_text(
                text,
                "rst",
                format=source_format,
                extra_args=["--columns=1000"]
            ).strip()
            
        _RAW_RST_CACHE[text] = raw_rst

    # 3. Python Formatting
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