# Copyright 2019 Google LLC
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

from collections import defaultdict
from typing import DefaultDict, List, Tuple

import dataclasses
import os
import warnings

from gapic.samplegen_utils import (types, utils as samplegen_utils)


@dataclasses.dataclass(frozen=True)
class Options:
    """A representation of CLI options passed through protoc.

    To maximize interoperability with other languages, we are permissive
    on unrecognized arguments (essentially, we throw them away, but we do
    warn if it looks like it was meant for us).
    """
    templates: Tuple[str, ...] = dataclasses.field(default=('DEFAULT',))
    namespace: Tuple[str, ...] = dataclasses.field(default=())
    sample_configs: Tuple[str, ...] = dataclasses.field(default=())
    name: str = ''

    # Class constants
    SAMPLES_OPT: str = 'samples'
    PYTHON_GAPIC_PREFIX: str = 'python-gapic-'

    @classmethod
    def build(cls, opt_string: str) -> 'Options':
        """Build an Options instance based on a protoc opt string.

        Args:
            opt_string (str): A string, as passed from the protoc interface
                (through ``--python_gapic_opt``). If multiple options are
                passed, then protoc joins the values with ``,``.
                By convention, we use ``key=value`` strings for such
                options, with an absent value defaulting to ``True``.

        Returns:
            ~.Options: The Options instance.

        Raises:
            gapic.samplegen_utils.types.InvalidConfig:
                        If paths to files or directories that should contain sample
                        configs are passed and no valid sample config is found.
        """
        # Parse out every option beginning with `python-gapic`
        opts: DefaultDict[str, List[str]] = defaultdict(list)
        for opt in opt_string.split(','):
            # Parse out the key and value.
            value = 'true'
            if '=' in opt:
                opt, value = opt.split('=')

            if opt == cls.SAMPLES_OPT:
                opts[cls.SAMPLES_OPT].append(value)

            # Throw away other options not meant for us.
            if not opt.startswith(cls.PYTHON_GAPIC_PREFIX):
                continue

            # Set the option, using a key with the "python-gapic-" prefix
            # stripped.
            #
            # Just assume everything is a list at this point, and the
            # final instantiation step can de-list-ify where appropriate.
            opts[opt[len(cls.PYTHON_GAPIC_PREFIX):]].append(value)

        # If templates are specified, one of the specified directories
        # may be our default; perform that replacement.
        templates = opts.pop('templates', ['DEFAULT'])
        while 'DEFAULT' in templates:
            templates[templates.index('DEFAULT')] = os.path.realpath(
                os.path.join(os.path.dirname(__file__), '..', 'templates'),
            )

        # Build the options instance.
        sample_paths = opts.pop(cls.SAMPLES_OPT, [])
        answer = Options(
            name=opts.pop('name', ['']).pop(),
            namespace=tuple(opts.pop('namespace', [])),
            templates=tuple(os.path.expanduser(i) for i in templates),
            sample_configs=tuple(
                cfg_path
                for s in sample_paths
                for cfg_path in samplegen_utils.generate_all_sample_fpaths(s)
            ),
        )

        if sample_paths and not answer.sample_configs:
            raise types.InvalidConfig(
                ("No valid sample config found in any of the following: "
                 "{}".format(", ".join(sample_paths)))
            )

        # If there are any options remaining, then we failed to recognize
        # them -- complain.
        for key in opts.keys():
            warnings.warn(f'Unrecognized option: `python-gapic-{key}`.')

        # Done; return the built options.
        return answer
