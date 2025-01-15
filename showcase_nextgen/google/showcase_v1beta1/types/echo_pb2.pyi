from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import routing_pb2 as _routing_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNNECESSARY: _ClassVar[Severity]
    NECESSARY: _ClassVar[Severity]
    URGENT: _ClassVar[Severity]
    CRITICAL: _ClassVar[Severity]
UNNECESSARY: Severity
NECESSARY: Severity
URGENT: Severity
CRITICAL: Severity

class EchoRequest(_message.Message):
    __slots__ = ("content", "error", "severity", "header", "other_header", "request_id", "other_request_id")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    OTHER_HEADER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    OTHER_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    content: str
    error: _status_pb2.Status
    severity: Severity
    header: str
    other_header: str
    request_id: str
    other_request_id: str
    def __init__(self, content: _Optional[str] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., severity: _Optional[_Union[Severity, str]] = ..., header: _Optional[str] = ..., other_header: _Optional[str] = ..., request_id: _Optional[str] = ..., other_request_id: _Optional[str] = ...) -> None: ...

class EchoResponse(_message.Message):
    __slots__ = ("content", "severity", "request_id", "other_request_id")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    OTHER_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    content: str
    severity: Severity
    request_id: str
    other_request_id: str
    def __init__(self, content: _Optional[str] = ..., severity: _Optional[_Union[Severity, str]] = ..., request_id: _Optional[str] = ..., other_request_id: _Optional[str] = ...) -> None: ...

class EchoErrorDetailsRequest(_message.Message):
    __slots__ = ("single_detail_text", "multi_detail_text")
    SINGLE_DETAIL_TEXT_FIELD_NUMBER: _ClassVar[int]
    MULTI_DETAIL_TEXT_FIELD_NUMBER: _ClassVar[int]
    single_detail_text: str
    multi_detail_text: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, single_detail_text: _Optional[str] = ..., multi_detail_text: _Optional[_Iterable[str]] = ...) -> None: ...

class EchoErrorDetailsResponse(_message.Message):
    __slots__ = ("single_detail", "multiple_details")
    class SingleDetail(_message.Message):
        __slots__ = ("error",)
        ERROR_FIELD_NUMBER: _ClassVar[int]
        error: ErrorWithSingleDetail
        def __init__(self, error: _Optional[_Union[ErrorWithSingleDetail, _Mapping]] = ...) -> None: ...
    class MultipleDetails(_message.Message):
        __slots__ = ("error",)
        ERROR_FIELD_NUMBER: _ClassVar[int]
        error: ErrorWithMultipleDetails
        def __init__(self, error: _Optional[_Union[ErrorWithMultipleDetails, _Mapping]] = ...) -> None: ...
    SINGLE_DETAIL_FIELD_NUMBER: _ClassVar[int]
    MULTIPLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    single_detail: EchoErrorDetailsResponse.SingleDetail
    multiple_details: EchoErrorDetailsResponse.MultipleDetails
    def __init__(self, single_detail: _Optional[_Union[EchoErrorDetailsResponse.SingleDetail, _Mapping]] = ..., multiple_details: _Optional[_Union[EchoErrorDetailsResponse.MultipleDetails, _Mapping]] = ...) -> None: ...

class ErrorWithSingleDetail(_message.Message):
    __slots__ = ("details",)
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    details: _any_pb2.Any
    def __init__(self, details: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class ErrorWithMultipleDetails(_message.Message):
    __slots__ = ("details",)
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    details: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, details: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class ExpandRequest(_message.Message):
    __slots__ = ("content", "error", "stream_wait_time")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STREAM_WAIT_TIME_FIELD_NUMBER: _ClassVar[int]
    content: str
    error: _status_pb2.Status
    stream_wait_time: _duration_pb2.Duration
    def __init__(self, content: _Optional[str] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., stream_wait_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class PagedExpandRequest(_message.Message):
    __slots__ = ("content", "page_size", "page_token")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    content: str
    page_size: int
    page_token: str
    def __init__(self, content: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class PagedExpandLegacyRequest(_message.Message):
    __slots__ = ("content", "max_results", "page_token")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    content: str
    max_results: int
    page_token: str
    def __init__(self, content: _Optional[str] = ..., max_results: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class PagedExpandResponse(_message.Message):
    __slots__ = ("responses", "next_page_token")
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    responses: _containers.RepeatedCompositeFieldContainer[EchoResponse]
    next_page_token: str
    def __init__(self, responses: _Optional[_Iterable[_Union[EchoResponse, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class PagedExpandResponseList(_message.Message):
    __slots__ = ("words",)
    WORDS_FIELD_NUMBER: _ClassVar[int]
    words: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, words: _Optional[_Iterable[str]] = ...) -> None: ...

class PagedExpandLegacyMappedResponse(_message.Message):
    __slots__ = ("alphabetized", "next_page_token")
    class AlphabetizedEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: PagedExpandResponseList
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PagedExpandResponseList, _Mapping]] = ...) -> None: ...
    ALPHABETIZED_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    alphabetized: _containers.MessageMap[str, PagedExpandResponseList]
    next_page_token: str
    def __init__(self, alphabetized: _Optional[_Mapping[str, PagedExpandResponseList]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class WaitRequest(_message.Message):
    __slots__ = ("end_time", "ttl", "error", "success")
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    end_time: _timestamp_pb2.Timestamp
    ttl: _duration_pb2.Duration
    error: _status_pb2.Status
    success: WaitResponse
    def __init__(self, end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., success: _Optional[_Union[WaitResponse, _Mapping]] = ...) -> None: ...

class WaitResponse(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class WaitMetadata(_message.Message):
    __slots__ = ("end_time",)
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class BlockRequest(_message.Message):
    __slots__ = ("response_delay", "error", "success")
    RESPONSE_DELAY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    response_delay: _duration_pb2.Duration
    error: _status_pb2.Status
    success: BlockResponse
    def __init__(self, response_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., success: _Optional[_Union[BlockResponse, _Mapping]] = ...) -> None: ...

class BlockResponse(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...
