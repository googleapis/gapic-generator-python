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

import jinja2

from google.protobuf.compiler.plugin_pb2 import CodeGeneratorRequest
from google.protobuf.compiler.plugin_pb2 import CodeGeneratorResponse

from api_factory.schema import API
from api_factory.generator.loader import TemplateLoader
from api_factory import utils


def generate(request: CodeGeneratorRequest) -> CodeGeneratorResponse:
    """Generate a code generator response to provide to protoc.

    Args:
        request (CodeGeneratorRequest): A request protocol buffer as provided
            by protoc.

    Returns:
        CodeGeneratorResponse: A complete response to be written to (usually)
            stdout and thus read by protoc.
    """
    # Parse the CodeGeneratorRequest into this plugin's internal schema.
    api_desc = API()
    for fdp in request.proto_file:
        api_desc.load(fdp)

    # Instantiate a CodeGeneratorResponse object.
    output_files = []

    # Create the jinja environment with which to render templates.
    env = jinja2.Environment(loader=TemplateLoader(
        searchpath=os.path.join(_dirname, 'templates'),
    ))
    env.filters['snake_case'] = utils.to_snake_case
    env.filters['subsequent_indent'] = utils.subsequent_indent
    env.filters['wrap'] = utils.wrap

    # For every protocol buffer service, generate a client module.
    service_templates = [i for i in env.loader.remaining_templates
                         if i.startswith('service/')]
    for service in api_desc.services.values():
        for filename in service_templates:
            # Get the output filename for this service and template.
            output_filename = filename[:-len('.j2')].replace(
                'service/',
                f'{utils.to_snake_case(service.name)}/',
            )
            output_files.append(CodeGeneratorResponse.File(
                content=env.get_template(filename).render(
                    api=api_desc,
                    service=service,
                ).strip() + '\n',
                name=output_filename,
            ))

    # Create boilerplate metadata files.
    for filename in env.loader.remaining_templates:
        output_files.append(CodeGeneratorResponse.File(
            content=env.get_template(filename).render(
                api=api_desc,
            ).strip() + '\n',
            name=filename[:-len('.j2')],
        ))

    # Some files are direct files and not templates; simply read them
    # into output files directly.
    #
    # Rather than expect an enumeration of these, we simply grab everything
    # in the `files/` directory automatically.
    for path, _, filenames in os.walk(os.path.join(_dirname, 'files')):
        relative_path = path[len(_dirname) + len('/files/'):]
        for filename in filenames:
            # Determine the "relative filename" (the filename against the
            # files/ subdirectory and repository root).
            relative_filename = filename
            if relative_path:
                relative_filename = os.path.join(relative_path, filename)

            # Read the file from disk and create an appropriate OutputFile.
            with io.open(os.path.join(path, filename), 'r') as f:
                output_files.append(CodeGeneratorResponse.File(
                    content=f.read(),
                    name=relative_filename,
                ))

    # Done; return the full library object, containing each individual
    # file to be written.
    return CodeGeneratorResponse(file=output_files)


_dirname = os.path.realpath(os.path.dirname(__file__))
