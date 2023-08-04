import os
import pathlib
import requests
import subprocess
import sys

INTERSPHINX_CACHE = "/tmp/intersphinx_inventories/"

# Download intersphinx inventories to workaround rate limits
# related to fetching intersphinx inventories from the internet during
# the docs build. The error when rate limits occur is shown below:
# `not fetchable due to HTTPError 429 Client Error: Too Many Requests for url`
intersphinx_mapping = [
    {"package": "python", "url": "https://python.readthedocs.io/en/latest/"},
    {"package": "google-auth", "url": "https://googleapis.dev/python/google-auth/latest/"},
    {"package": "google.api_core", "url": "https://googleapis.dev/python/google-api-core/latest/"},
    {"package": "grpc", "url": "https://grpc.github.io/grpc/python/"},
    {"package": "requests", "url": "https://requests.kennethreitz.org/en/stable/"},
    {"package": "proto", "url": "https://googleapis.dev/python/proto-plus/latest/"},
    {"package": "protobuf", "url": "https://googleapis.dev/python/protobuf/latest/"},
]

def cache_intersphinx_inventory(package: str, url: str):
    if not pathlib.Path(f"{INTERSPHINX_CACHE}/{package}").exists():
        os.mkdir(f"{INTERSPHINX_CACHE}/{package}")
    if not pathlib.Path(f"{INTERSPHINX_CACHE}/{package}/objects.inv").exists():
        response = requests.get(f"{url}objects.inv", allow_redirects=True, stream=True)
        if response.status_code == 200:
            with open(f"{INTERSPHINX_CACHE}/{package}/objects.inv", "wb") as f:
                f.write(response.content)


if __name__ == '__main__':
    if not pathlib.Path(INTERSPHINX_CACHE).exists():
        os.mkdir(INTERSPHINX_CACHE)
    for item in intersphinx_mapping:
        cache_intersphinx_inventory(item['package'], item['url'])
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
