import pytest
import os
import subprocess


if __name__ == "__main__":
    pytest.main(
        [
            "--disable-pytest-warnings",
            "--quiet",
            os.path.dirname(os.path.abspath(__file__)),
        ]
    )

    # The source is in the directory with suffix `srcjar.py`
    src_directory = os.path.abspath(__file__).replace("pytest.py", "srcjar.py")

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

    subprocess.run(
        [
            "sphinx-build",
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
