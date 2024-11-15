from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import error_details_pb2 as _error_details_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Room(_message.Message):
    __slots__ = ("name", "display_name", "description", "create_time", "update_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateRoomRequest(_message.Message):
    __slots__ = ("room",)
    ROOM_FIELD_NUMBER: _ClassVar[int]
    room: Room
    def __init__(self, room: _Optional[_Union[Room, _Mapping]] = ...) -> None: ...

class GetRoomRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateRoomRequest(_message.Message):
    __slots__ = ("room", "update_mask")
    ROOM_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    room: Room
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, room: _Optional[_Union[Room, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteRoomRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListRoomsRequest(_message.Message):
    __slots__ = ("page_size", "page_token")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListRoomsResponse(_message.Message):
    __slots__ = ("rooms", "next_page_token")
    ROOMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    rooms: _containers.RepeatedCompositeFieldContainer[Room]
    next_page_token: str
    def __init__(self, rooms: _Optional[_Iterable[_Union[Room, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class Blurb(_message.Message):
    __slots__ = ("name", "user", "text", "image", "create_time", "update_time", "legacy_room_id", "legacy_user_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LEGACY_ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    LEGACY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    user: str
    text: str
    image: bytes
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    legacy_room_id: str
    legacy_user_id: str
    def __init__(self, name: _Optional[str] = ..., user: _Optional[str] = ..., text: _Optional[str] = ..., image: _Optional[bytes] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., legacy_room_id: _Optional[str] = ..., legacy_user_id: _Optional[str] = ...) -> None: ...

class CreateBlurbRequest(_message.Message):
    __slots__ = ("parent", "blurb")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BLURB_FIELD_NUMBER: _ClassVar[int]
    parent: str
    blurb: Blurb
    def __init__(self, parent: _Optional[str] = ..., blurb: _Optional[_Union[Blurb, _Mapping]] = ...) -> None: ...

class GetBlurbRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateBlurbRequest(_message.Message):
    __slots__ = ("blurb", "update_mask")
    BLURB_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    blurb: Blurb
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, blurb: _Optional[_Union[Blurb, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteBlurbRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListBlurbsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListBlurbsResponse(_message.Message):
    __slots__ = ("blurbs", "next_page_token")
    BLURBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    blurbs: _containers.RepeatedCompositeFieldContainer[Blurb]
    next_page_token: str
    def __init__(self, blurbs: _Optional[_Iterable[_Union[Blurb, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class SearchBlurbsRequest(_message.Message):
    __slots__ = ("query", "parent", "page_size", "page_token")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    query: str
    parent: str
    page_size: int
    page_token: str
    def __init__(self, query: _Optional[str] = ..., parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class SearchBlurbsMetadata(_message.Message):
    __slots__ = ("retry_info",)
    RETRY_INFO_FIELD_NUMBER: _ClassVar[int]
    retry_info: _error_details_pb2.RetryInfo
    def __init__(self, retry_info: _Optional[_Union[_error_details_pb2.RetryInfo, _Mapping]] = ...) -> None: ...

class SearchBlurbsResponse(_message.Message):
    __slots__ = ("blurbs", "next_page_token")
    BLURBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    blurbs: _containers.RepeatedCompositeFieldContainer[Blurb]
    next_page_token: str
    def __init__(self, blurbs: _Optional[_Iterable[_Union[Blurb, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class StreamBlurbsRequest(_message.Message):
    __slots__ = ("name", "expire_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    expire_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StreamBlurbsResponse(_message.Message):
    __slots__ = ("blurb", "action")
    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_UNSPECIFIED: _ClassVar[StreamBlurbsResponse.Action]
        CREATE: _ClassVar[StreamBlurbsResponse.Action]
        UPDATE: _ClassVar[StreamBlurbsResponse.Action]
        DELETE: _ClassVar[StreamBlurbsResponse.Action]
    ACTION_UNSPECIFIED: StreamBlurbsResponse.Action
    CREATE: StreamBlurbsResponse.Action
    UPDATE: StreamBlurbsResponse.Action
    DELETE: StreamBlurbsResponse.Action
    BLURB_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    blurb: Blurb
    action: StreamBlurbsResponse.Action
    def __init__(self, blurb: _Optional[_Union[Blurb, _Mapping]] = ..., action: _Optional[_Union[StreamBlurbsResponse.Action, str]] = ...) -> None: ...

class SendBlurbsResponse(_message.Message):
    __slots__ = ("names",)
    NAMES_FIELD_NUMBER: _ClassVar[int]
    names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, names: _Optional[_Iterable[str]] = ...) -> None: ...

class ConnectRequest(_message.Message):
    __slots__ = ("config", "blurb")
    class ConnectConfig(_message.Message):
        __slots__ = ("parent",)
        PARENT_FIELD_NUMBER: _ClassVar[int]
        parent: str
        def __init__(self, parent: _Optional[str] = ...) -> None: ...
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    BLURB_FIELD_NUMBER: _ClassVar[int]
    config: ConnectRequest.ConnectConfig
    blurb: Blurb
    def __init__(self, config: _Optional[_Union[ConnectRequest.ConnectConfig, _Mapping]] = ..., blurb: _Optional[_Union[Blurb, _Mapping]] = ...) -> None: ...
