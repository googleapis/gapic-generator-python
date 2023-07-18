import pytest
import os
import subprocess
import sys

if __name__ == '__main__':
    # The source is in the directory with suffix `srcjar.py`
    src_directory = os.path.abspath(__file__).replace("pydocstest.py", "srcjar.py")

    # Update permissions so that docs can be created
    os.chmod(
        str(
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                src_directory,
                "docs",
            )
        ),
        0o744,
    )

    result = subprocess.run(
        [
            "python3",
            "-m",
            "sphinx.cmd.build",
            "-W",  # warnings as errors
            "-T",  # show full traceback on exception
            "-N",  # no colors
            "-b",
            "html",
            "-d",
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                src_directory,
                "docs",
                "_build",
                "doctrees",
                "",
            ),
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                src_directory,
                "docs",
                "",
            ),
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                src_directory,
                "docs",
                "_build",
                "html",
                "",
            ),
        ]
    )
    if result.returncode != 0:
        sys.exit(result)
