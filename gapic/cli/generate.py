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

import os
import sys
import typing
import time

import click

from google.protobuf.compiler import plugin_pb2

from gapic import generator
from gapic.schema import api
from gapic.utils import Options

# <--- Profiling Global --->
LOG_FILE = "/tmp/gapic_profile.log"

def _log(msg):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%H:%M:%S')}] [CLI] {msg}\n")
# <--- End Profiling Global --->

@click.command()
@click.option(
    "--request",
    type=click.File("rb"),
    default=sys.stdin.buffer,
    help="Location of the `CodeGeneratorRequest` to be processed. "
    "This defaults to stdin (which is what protoc uses) "
    "but this option can be set for testing/debugging.",
)
@click.option(
    "--output",
    type=click.File("wb"),
    default=sys.stdout.buffer,
    help="Where to output the `CodeGeneratorResponse`. " "Defaults to stdout.",
)
def generate(request: typing.BinaryIO, output: typing.BinaryIO) -> None:
    """Generate a full API client description."""
    
    # <--- Start Profiling --->
    # We clear the file here since this is the entry point
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("--- CLI PROCESS START ---\n")
    
    t_start_script = time.time()
    # <--- End Profiling --->

    # Load the protobuf CodeGeneratorRequest.
    t0 = time.time()
    req = plugin_pb2.CodeGeneratorRequest.FromString(request.read())
    _log(f"Load CodeGeneratorRequest took {time.time() - t0:.4f}s")

    # Pull apart arguments in the request.
    opts = Options.build(req.parameter)

    # Determine the appropriate package.
    # This generator uses a slightly different mechanism for determining
    # which files to generate; it tracks at package level rather than file
    # level.
    package = os.path.commonprefix(
        [p.package for p in req.proto_file if p.name in req.file_to_generate]
    ).rstrip(".")

    # Build the API model object.
    # This object is a frozen representation of the whole API, and is sent
    # to each template in the rendering step.
    # <--- Profile API Build --->
    _log("Starting API.build (Parsing Protos)...")
    t0 = time.time()
    
    api_schema = api.API.build(req.proto_file, opts=opts, package=package)
    
    _log(f"API.build took {time.time() - t0:.4f}s")
    # <--- End Profile API Build --->

    # Translate into a protobuf CodeGeneratorResponse; this reads the
    # individual templates and renders them.
    # If there are issues, error out appropriately.
    # <--- Profile Generator --->
    _log("Starting generator.get_response (Rendering Templates)...")
    t0 = time.time()
    
    res = generator.Generator(opts).get_response(api_schema, opts)
    
    _log(f"generator.get_response took {time.time() - t0:.4f}s")
    # <--- End Profile Generator --->

    # Output the serialized response.
    t0 = time.time()
    output.write(res.SerializeToString())
    _log(f"Serialization/Write took {time.time() - t0:.4f}s")
    
    _log(f"TOTAL CLI RUNTIME: {time.time() - t_start_script:.4f}s")


if __name__ == "__main__":
    generate()
