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

import copy
import dataclasses
from typing import List

from google.protobuf import descriptor_pb2


@dataclasses.dataclass(frozen=True)
class Address:
    package: List[str] = dataclasses.field(default_factory=list)
    module: str = ''
    parent: List[str] = dataclasses.field(default_factory=list)

    def __str__(self):
        return '.'.join(self.package + self.parent)

    def child(self, child_name: str) -> 'Address':
        """Return a new Address with ``child_name`` appended to its parent.

        Args:
            child_name (str): The child name to be appended to ``parent``.
                The period-separator is added automatically if ``parent``
                is non-empty.

        Returns:
            Address: The new address object.
        """
        answer = copy.deepcopy(self)
        answer.parent.append(child_name)
        return answer


@dataclasses.dataclass(frozen=True)
class Metadata:
    address: Address = dataclasses.field(default_factory=Address)
    documentation: descriptor_pb2.SourceCodeInfo.Location = dataclasses.field(
        default_factory=descriptor_pb2.SourceCodeInfo.Location,
    )

    @property
    def doc(self):
        """Return the best comment."""
        if self.documentation.leading_comments:
            return self.documentation.leading_comments.strip()
        if self.documentation.trailing_comments:
            return self.documentation.trailing_comments.strip()
        if self.documentation.leading_detached_comments:
            return '\n\n'.join(self.documentation.leading_detached_comments)
        return ''
