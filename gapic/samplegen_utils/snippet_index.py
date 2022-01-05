# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Optional, Dict
import re
from google.protobuf import json_format

from gapic.schema import api, metadata
from gapic.samplegen_utils import snippet_metadata_pb2  # type: ignore
from gapic.samplegen_utils import types


CLIENT_INIT_RE = re.compile(r"^\s+# Create a client")
REQUEST_INIT_RE = re.compile(r"^\s+# Initialize request argument\(s\)")
REQUEST_EXEC_RE = re.compile(r"^\s+# Make the request")
RESPONSE_HANDLING_RE = re.compile(r"^\s+# Handle response")


class Snippet:
    """A single snippet and its metadata"""

    def __init__(self, sample_str: str, sample_metadata):
        self.sample_str = sample_str
        self.metadata = sample_metadata
        self._parse_snippet_segments()

    def _parse_snippet_segments(self):
        """Parse sections of the snippet and update metadata"""
        self.sample_lines = self.sample_str.splitlines(keepends=True)

        self._full_snippet = snippet_metadata_pb2.Snippet.Segment(
            type=snippet_metadata_pb2.Snippet.Segment.SegmentType.FULL)
        self._short_snippet = snippet_metadata_pb2.Snippet.Segment(
            type=snippet_metadata_pb2.Snippet.Segment.SegmentType.SHORT)
        self._client_init = snippet_metadata_pb2.Snippet.Segment(
            type=snippet_metadata_pb2.Snippet.Segment.SegmentType.CLIENT_INITIALIZATION)
        self._request_init = snippet_metadata_pb2.Snippet.Segment(
            type=snippet_metadata_pb2.Snippet.Segment.SegmentType.REQUEST_INITIALIZATION)
        self._request_exec = snippet_metadata_pb2.Snippet.Segment(
            type=snippet_metadata_pb2.Snippet.Segment.SegmentType.REQUEST_EXECUTION)
        self._response_handling = snippet_metadata_pb2.Snippet.Segment(
            type=snippet_metadata_pb2.Snippet.Segment.SegmentType.RESPONSE_HANDLING,
            end=len(self.sample_lines)
        )

        # Index starts at 1 since these represent line numbers
        for i, line in enumerate(self.sample_lines, start=1):
            if line.startswith("# [START"):  # do not include region tag lines
                self._full_snippet.start = i + 1
                self._short_snippet.start = self._full_snippet.start
            elif line.startswith("# [END"):
                self._full_snippet.end = i - 1
                self._short_snippet.end = self._full_snippet.end
            elif CLIENT_INIT_RE.match(line):
                self._client_init.start = i
            elif REQUEST_INIT_RE.match(line):
                self._client_init.end = i - 1
                self._request_init.start = i
            elif REQUEST_EXEC_RE.match(line):
                self._request_init.end = i - 1
                self._request_exec.start = i
            elif RESPONSE_HANDLING_RE.match(line):
                self._request_exec.end = i - 1
                self._response_handling.start = i

        for segment in [self._full_snippet,
        self._short_snippet, self._client_init, self._request_init, self._request_exec, self._response_handling]:
            self.metadata.segments.append(segment)

    @property
    def full_snippet(self) -> str:
        """The portion between the START and END region tags"""
        start_idx = self._full_snippet.start - 1
        end_idx = self._full_snippet.end
        short_sample = "".join(self.sample_lines[start_idx:end_idx])

        return short_sample


class SnippetIndex:

    def __init__(self, api_schema: api.API):
        self.metadata_index = snippet_metadata_pb2.Index()  # type: ignore
        # Construct a dictionary to insert samples into based on the API schema
        self._index: Dict[str, Dict[str, Dict[str, Optional[Snippet]]]] = {}

        for service in api_schema.services.values():
            self._index[service.name] = {}
            # This will be need to be re-structured when one method can have
            # more than one sample variant
            for method in service.methods.keys():
                self._index[service.name][method] = {
                    "sync": None,
                    "async": None
                }

    def add_snippet(self, snippet: Snippet) -> None:
        """Add a single snippet to the index.

        Args:
            snippet (Snippet): The code snippet to be added.

        Raises:
            UnknownService: If the service indicated by the snippet metadata is not found.
            RpcMethodNotFound: If the method indicated by the snippet metadata is not found.
        """
        service_name = snippet.metadata.client_method.method.service.short_name
        rpc_name = snippet.metadata.client_method.method.full_name

        service = self._index.get(service_name)
        if service is None:
            raise types.UnknownService(
                "API does not have a service named '{}'.".format(service_name))

        method = service.get(rpc_name)
        if method is None:
            raise types.RpcMethodNotFound(
                "API does not have method '{}' in service '{}'".format(rpc_name, service_name))

        if getattr(snippet.metadata.client_method, "async"):
            method["async"] = snippet
        else:
            method["sync"] = snippet

        self.metadata_index.snippets.append(snippet.metadata)

    def get_snippet(self, service_name: str, rpc_name: str, sync: bool = True) -> Optional[Snippet]:
        """Fetch a single snippet from the index.

        Args:
            service_name (str): The name of the service.
            rpc_name (str): The name of the RPC.
            sync (bool): True for the sync version of the snippet, False for the async version.

        Returns:
            Optional[Ssnippet]: The snippet if it exists, or None.
        """
        # Fetch a snippet from the snippet metadata index
        service = self._index.get(service_name)
        if service is None:
            raise types.UnknownService(
                "API does not have a service named '{}'.".format(service_name))
        method = service.get(rpc_name)
        if method is None:
            raise types.RpcMethodNotFound(
                "API does not have method '{}' in service '{}'".format(rpc_name, service_name))

        return method["sync" if sync else "async"]

    def get_metadata_json(self):
        """JSON representation of Snippet Index."""
        return json_format.MessageToJson(self.metadata_index, sort_keys=True)
