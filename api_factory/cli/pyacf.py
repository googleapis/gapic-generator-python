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

import io
import os
import sys
import typing

import click

from api_factory import normalizer
from api_factory import translator


@click.command()
# @click.argument('proto_files', type=click.File('rb'), nargs=-1)
@click.argument('service', type=click.File('rb'))
@click.option('--output', type=click.File('wb'), default=sys.stdout)
@click.option('list_filenames', '--list', is_flag=True, default=False,
              help='List filenames only, in lieu of full output.')
@click.option('--only-file', default=None,
              help='Restrict output to the contents of the given filename. '
                   'Must match the filename as specified by --list.')
@click.option('--output-dir', default=None,
              help='Output client library files to the given directory.')
def pyacf(
        output: typing.BinaryIO,
        service: typing.BinaryIO,
        list_filenames: bool = False,
        only_file: str = None,
        output_dir: str = None) -> None:
    """Convert a Service descriptor into a client library object."""

    # Load the binary into an API Desciptor proto.
    # FIXME: Use af.n.parser for this.
    api_desc = normalizer.parse(service.read())

    # Generate a client library object with the translated artifacts.
    client_library = translator.translate(api_desc)

    # Sanity check: If we are just to list filenames, do that.
    if list_filenames:
        for output_file in client_library.output_files:
            output.write(f'{output_file.filename}\n')
        return

    # Sanity check: If we are dumping out to disk, do that.
    if output_dir:
        output_dir = os.path.realpath(os.path.expanduser(output_dir))
        for output_file in client_library.output_files:
            target = os.path.join(output_dir, output_file.filename)
            if not os.path.isdir(os.path.dirname(target)):
                os.makedirs(os.path.dirname(target))
            with io.open(target, 'w+') as f:
                f.write(output_file.contents)
        click.secho('Success. Client library written to {dir}.'.format(
            dir=output_dir,
        ), fg='green')
        return

    # Print the output.
    for output_file in client_library.output_files:
        if not only_file or only_file == output_file.filename:
            output.write(output_file.contents)
