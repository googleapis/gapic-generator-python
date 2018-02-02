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

from api_factory.normalizer.schema import APIDescriptor
from api_factory.translator.loader import TemplateLoader
from api_factory.translator.schema import ClientLibrary
from api_factory.translator.schema import OutputFile
from api_factory import utils


def translate(api_desc: APIDescriptor) -> ClientLibrary:
    """Generate a client library.

    This function pieces together a client library (which is really just
    a collection of output files) and returns it.

    Args:
        api_desc (~.normalizer.schema.APIDescriptor): The API descriptor
            from which to generate the library.

    Returns:
        ~.translator.schema.ClientLibrary: An in-memory object representing
            the complete client library.
    """
    answer = ClientLibrary()
    env = jinja2.Environment(loader=TemplateLoader(
        searchpath=os.path.join(_dirname, 'templates'),
    ))
    env.filters['snake_case'] = utils.to_snake_case
    env.filters['subsequent_indent'] = utils.subsequent_indent
    env.filters['wrap'] = utils.wrap

    # For every service, generate a client module.
    # (The term "service" here refers to the proto3 keyword, not the
    # service configuration.)
    service_templates = [i for i in env.loader.remaining_templates
                         if i.startswith('service/')]
    for service in api_desc.services:
        for filename in service_templates:
            # Get the output filename for this service and template.
            output_filename = filename[:-len('.j2')].replace(
                'service/',
                f'{utils.to_snake_case(service.label)}/',
            )
            answer.output_files.append(OutputFile(
                contents=env.get_template(filename).render(
                    api=api_desc,
                    service=service,
                ),
                filename=output_filename,
            ))

    # Create boilerplate metadata files.
    for filename in env.loader.remaining_templates:
        answer.output_files.append(OutputFile(
            contents=env.get_template(filename).render(
                api=api_desc,
            ),
            filename=filename[:-len('.j2')],
        ))

    # Some files are direct files and not templates; simply read them
    # into output files directly.
    #
    # Rather than expect an enumeration of these, we simply grab everything
    # in the `files/` directory atuo
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
                answer.output_files.append(OutputFile(
                    contents=f.read(),
                    filename=relative_filename,
                ))

    # Done; return the full library object, containing each individual
    # file to be written.
    return answer


_dirname = os.path.realpath(os.path.dirname(__file__))
