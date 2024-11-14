from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import dayofweek_pb2 as _dayofweek_pb2
from google.type import timeofday_pb2 as _timeofday_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NodeInfo(_message.Message):
    __slots__ = ("id", "zone")
    ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    id: str
    zone: str
    def __init__(self, id: _Optional[str] = ..., zone: _Optional[str] = ...) -> None: ...

class Instance(_message.Message):
    __slots__ = ("name", "display_name", "labels", "location_id", "alternative_location_id", "redis_version", "reserved_ip_range", "secondary_ip_range", "host", "port", "current_location_id", "create_time", "state", "status_message", "redis_configs", "tier", "memory_size_gb", "authorized_network", "persistence_iam_identity", "connect_mode", "auth_enabled", "server_ca_certs", "transit_encryption_mode", "maintenance_policy", "maintenance_schedule", "replica_count", "nodes", "read_endpoint", "read_endpoint_port", "read_replicas_mode", "customer_managed_key", "persistence_config", "suspension_reasons", "maintenance_version", "available_maintenance_versions")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Instance.State]
        CREATING: _ClassVar[Instance.State]
        READY: _ClassVar[Instance.State]
        UPDATING: _ClassVar[Instance.State]
        DELETING: _ClassVar[Instance.State]
        REPAIRING: _ClassVar[Instance.State]
        MAINTENANCE: _ClassVar[Instance.State]
        IMPORTING: _ClassVar[Instance.State]
        FAILING_OVER: _ClassVar[Instance.State]
    STATE_UNSPECIFIED: Instance.State
    CREATING: Instance.State
    READY: Instance.State
    UPDATING: Instance.State
    DELETING: Instance.State
    REPAIRING: Instance.State
    MAINTENANCE: Instance.State
    IMPORTING: Instance.State
    FAILING_OVER: Instance.State
    class Tier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIER_UNSPECIFIED: _ClassVar[Instance.Tier]
        BASIC: _ClassVar[Instance.Tier]
        STANDARD_HA: _ClassVar[Instance.Tier]
    TIER_UNSPECIFIED: Instance.Tier
    BASIC: Instance.Tier
    STANDARD_HA: Instance.Tier
    class ConnectMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONNECT_MODE_UNSPECIFIED: _ClassVar[Instance.ConnectMode]
        DIRECT_PEERING: _ClassVar[Instance.ConnectMode]
        PRIVATE_SERVICE_ACCESS: _ClassVar[Instance.ConnectMode]
    CONNECT_MODE_UNSPECIFIED: Instance.ConnectMode
    DIRECT_PEERING: Instance.ConnectMode
    PRIVATE_SERVICE_ACCESS: Instance.ConnectMode
    class TransitEncryptionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRANSIT_ENCRYPTION_MODE_UNSPECIFIED: _ClassVar[Instance.TransitEncryptionMode]
        SERVER_AUTHENTICATION: _ClassVar[Instance.TransitEncryptionMode]
        DISABLED: _ClassVar[Instance.TransitEncryptionMode]
    TRANSIT_ENCRYPTION_MODE_UNSPECIFIED: Instance.TransitEncryptionMode
    SERVER_AUTHENTICATION: Instance.TransitEncryptionMode
    DISABLED: Instance.TransitEncryptionMode
    class ReadReplicasMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        READ_REPLICAS_MODE_UNSPECIFIED: _ClassVar[Instance.ReadReplicasMode]
        READ_REPLICAS_DISABLED: _ClassVar[Instance.ReadReplicasMode]
        READ_REPLICAS_ENABLED: _ClassVar[Instance.ReadReplicasMode]
    READ_REPLICAS_MODE_UNSPECIFIED: Instance.ReadReplicasMode
    READ_REPLICAS_DISABLED: Instance.ReadReplicasMode
    READ_REPLICAS_ENABLED: Instance.ReadReplicasMode
    class SuspensionReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUSPENSION_REASON_UNSPECIFIED: _ClassVar[Instance.SuspensionReason]
        CUSTOMER_MANAGED_KEY_ISSUE: _ClassVar[Instance.SuspensionReason]
    SUSPENSION_REASON_UNSPECIFIED: Instance.SuspensionReason
    CUSTOMER_MANAGED_KEY_ISSUE: Instance.SuspensionReason
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class RedisConfigsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    ALTERNATIVE_LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    REDIS_VERSION_FIELD_NUMBER: _ClassVar[int]
    RESERVED_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    CURRENT_LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REDIS_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    MEMORY_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_NETWORK_FIELD_NUMBER: _ClassVar[int]
    PERSISTENCE_IAM_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    CONNECT_MODE_FIELD_NUMBER: _ClassVar[int]
    AUTH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SERVER_CA_CERTS_FIELD_NUMBER: _ClassVar[int]
    TRANSIT_ENCRYPTION_MODE_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_POLICY_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    READ_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    READ_ENDPOINT_PORT_FIELD_NUMBER: _ClassVar[int]
    READ_REPLICAS_MODE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_MANAGED_KEY_FIELD_NUMBER: _ClassVar[int]
    PERSISTENCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SUSPENSION_REASONS_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_MAINTENANCE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    labels: _containers.ScalarMap[str, str]
    location_id: str
    alternative_location_id: str
    redis_version: str
    reserved_ip_range: str
    secondary_ip_range: str
    host: str
    port: int
    current_location_id: str
    create_time: _timestamp_pb2.Timestamp
    state: Instance.State
    status_message: str
    redis_configs: _containers.ScalarMap[str, str]
    tier: Instance.Tier
    memory_size_gb: int
    authorized_network: str
    persistence_iam_identity: str
    connect_mode: Instance.ConnectMode
    auth_enabled: bool
    server_ca_certs: _containers.RepeatedCompositeFieldContainer[TlsCertificate]
    transit_encryption_mode: Instance.TransitEncryptionMode
    maintenance_policy: MaintenancePolicy
    maintenance_schedule: MaintenanceSchedule
    replica_count: int
    nodes: _containers.RepeatedCompositeFieldContainer[NodeInfo]
    read_endpoint: str
    read_endpoint_port: int
    read_replicas_mode: Instance.ReadReplicasMode
    customer_managed_key: str
    persistence_config: PersistenceConfig
    suspension_reasons: _containers.RepeatedScalarFieldContainer[Instance.SuspensionReason]
    maintenance_version: str
    available_maintenance_versions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., location_id: _Optional[str] = ..., alternative_location_id: _Optional[str] = ..., redis_version: _Optional[str] = ..., reserved_ip_range: _Optional[str] = ..., secondary_ip_range: _Optional[str] = ..., host: _Optional[str] = ..., port: _Optional[int] = ..., current_location_id: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[Instance.State, str]] = ..., status_message: _Optional[str] = ..., redis_configs: _Optional[_Mapping[str, str]] = ..., tier: _Optional[_Union[Instance.Tier, str]] = ..., memory_size_gb: _Optional[int] = ..., authorized_network: _Optional[str] = ..., persistence_iam_identity: _Optional[str] = ..., connect_mode: _Optional[_Union[Instance.ConnectMode, str]] = ..., auth_enabled: bool = ..., server_ca_certs: _Optional[_Iterable[_Union[TlsCertificate, _Mapping]]] = ..., transit_encryption_mode: _Optional[_Union[Instance.TransitEncryptionMode, str]] = ..., maintenance_policy: _Optional[_Union[MaintenancePolicy, _Mapping]] = ..., maintenance_schedule: _Optional[_Union[MaintenanceSchedule, _Mapping]] = ..., replica_count: _Optional[int] = ..., nodes: _Optional[_Iterable[_Union[NodeInfo, _Mapping]]] = ..., read_endpoint: _Optional[str] = ..., read_endpoint_port: _Optional[int] = ..., read_replicas_mode: _Optional[_Union[Instance.ReadReplicasMode, str]] = ..., customer_managed_key: _Optional[str] = ..., persistence_config: _Optional[_Union[PersistenceConfig, _Mapping]] = ..., suspension_reasons: _Optional[_Iterable[_Union[Instance.SuspensionReason, str]]] = ..., maintenance_version: _Optional[str] = ..., available_maintenance_versions: _Optional[_Iterable[str]] = ...) -> None: ...

class PersistenceConfig(_message.Message):
    __slots__ = ("persistence_mode", "rdb_snapshot_period", "rdb_next_snapshot_time", "rdb_snapshot_start_time")
    class PersistenceMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERSISTENCE_MODE_UNSPECIFIED: _ClassVar[PersistenceConfig.PersistenceMode]
        DISABLED: _ClassVar[PersistenceConfig.PersistenceMode]
        RDB: _ClassVar[PersistenceConfig.PersistenceMode]
    PERSISTENCE_MODE_UNSPECIFIED: PersistenceConfig.PersistenceMode
    DISABLED: PersistenceConfig.PersistenceMode
    RDB: PersistenceConfig.PersistenceMode
    class SnapshotPeriod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SNAPSHOT_PERIOD_UNSPECIFIED: _ClassVar[PersistenceConfig.SnapshotPeriod]
        ONE_HOUR: _ClassVar[PersistenceConfig.SnapshotPeriod]
        SIX_HOURS: _ClassVar[PersistenceConfig.SnapshotPeriod]
        TWELVE_HOURS: _ClassVar[PersistenceConfig.SnapshotPeriod]
        TWENTY_FOUR_HOURS: _ClassVar[PersistenceConfig.SnapshotPeriod]
    SNAPSHOT_PERIOD_UNSPECIFIED: PersistenceConfig.SnapshotPeriod
    ONE_HOUR: PersistenceConfig.SnapshotPeriod
    SIX_HOURS: PersistenceConfig.SnapshotPeriod
    TWELVE_HOURS: PersistenceConfig.SnapshotPeriod
    TWENTY_FOUR_HOURS: PersistenceConfig.SnapshotPeriod
    PERSISTENCE_MODE_FIELD_NUMBER: _ClassVar[int]
    RDB_SNAPSHOT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    RDB_NEXT_SNAPSHOT_TIME_FIELD_NUMBER: _ClassVar[int]
    RDB_SNAPSHOT_START_TIME_FIELD_NUMBER: _ClassVar[int]
    persistence_mode: PersistenceConfig.PersistenceMode
    rdb_snapshot_period: PersistenceConfig.SnapshotPeriod
    rdb_next_snapshot_time: _timestamp_pb2.Timestamp
    rdb_snapshot_start_time: _timestamp_pb2.Timestamp
    def __init__(self, persistence_mode: _Optional[_Union[PersistenceConfig.PersistenceMode, str]] = ..., rdb_snapshot_period: _Optional[_Union[PersistenceConfig.SnapshotPeriod, str]] = ..., rdb_next_snapshot_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rdb_snapshot_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RescheduleMaintenanceRequest(_message.Message):
    __slots__ = ("name", "reschedule_type", "schedule_time")
    class RescheduleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESCHEDULE_TYPE_UNSPECIFIED: _ClassVar[RescheduleMaintenanceRequest.RescheduleType]
        IMMEDIATE: _ClassVar[RescheduleMaintenanceRequest.RescheduleType]
        NEXT_AVAILABLE_WINDOW: _ClassVar[RescheduleMaintenanceRequest.RescheduleType]
        SPECIFIC_TIME: _ClassVar[RescheduleMaintenanceRequest.RescheduleType]
    RESCHEDULE_TYPE_UNSPECIFIED: RescheduleMaintenanceRequest.RescheduleType
    IMMEDIATE: RescheduleMaintenanceRequest.RescheduleType
    NEXT_AVAILABLE_WINDOW: RescheduleMaintenanceRequest.RescheduleType
    SPECIFIC_TIME: RescheduleMaintenanceRequest.RescheduleType
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESCHEDULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    reschedule_type: RescheduleMaintenanceRequest.RescheduleType
    schedule_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., reschedule_type: _Optional[_Union[RescheduleMaintenanceRequest.RescheduleType, str]] = ..., schedule_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MaintenancePolicy(_message.Message):
    __slots__ = ("create_time", "update_time", "description", "weekly_maintenance_window")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_MAINTENANCE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    weekly_maintenance_window: _containers.RepeatedCompositeFieldContainer[WeeklyMaintenanceWindow]
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., description: _Optional[str] = ..., weekly_maintenance_window: _Optional[_Iterable[_Union[WeeklyMaintenanceWindow, _Mapping]]] = ...) -> None: ...

class WeeklyMaintenanceWindow(_message.Message):
    __slots__ = ("day", "start_time", "duration")
    DAY_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    day: _dayofweek_pb2.DayOfWeek
    start_time: _timeofday_pb2.TimeOfDay
    duration: _duration_pb2.Duration
    def __init__(self, day: _Optional[_Union[_dayofweek_pb2.DayOfWeek, str]] = ..., start_time: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class MaintenanceSchedule(_message.Message):
    __slots__ = ("start_time", "end_time", "can_reschedule", "schedule_deadline_time")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    CAN_RESCHEDULE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_DEADLINE_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    can_reschedule: bool
    schedule_deadline_time: _timestamp_pb2.Timestamp
    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., can_reschedule: bool = ..., schedule_deadline_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListInstancesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListInstancesResponse(_message.Message):
    __slots__ = ("instances", "next_page_token", "unreachable")
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[Instance]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, instances: _Optional[_Iterable[_Union[Instance, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetInstanceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetInstanceAuthStringRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class InstanceAuthString(_message.Message):
    __slots__ = ("auth_string",)
    AUTH_STRING_FIELD_NUMBER: _ClassVar[int]
    auth_string: str
    def __init__(self, auth_string: _Optional[str] = ...) -> None: ...

class CreateInstanceRequest(_message.Message):
    __slots__ = ("parent", "instance_id", "instance")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    instance_id: str
    instance: Instance
    def __init__(self, parent: _Optional[str] = ..., instance_id: _Optional[str] = ..., instance: _Optional[_Union[Instance, _Mapping]] = ...) -> None: ...

class UpdateInstanceRequest(_message.Message):
    __slots__ = ("update_mask", "instance")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    instance: Instance
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., instance: _Optional[_Union[Instance, _Mapping]] = ...) -> None: ...

class UpgradeInstanceRequest(_message.Message):
    __slots__ = ("name", "redis_version")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REDIS_VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    redis_version: str
    def __init__(self, name: _Optional[str] = ..., redis_version: _Optional[str] = ...) -> None: ...

class DeleteInstanceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GcsSource(_message.Message):
    __slots__ = ("uri",)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str
    def __init__(self, uri: _Optional[str] = ...) -> None: ...

class InputConfig(_message.Message):
    __slots__ = ("gcs_source",)
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    gcs_source: GcsSource
    def __init__(self, gcs_source: _Optional[_Union[GcsSource, _Mapping]] = ...) -> None: ...

class ImportInstanceRequest(_message.Message):
    __slots__ = ("name", "input_config")
    NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    input_config: InputConfig
    def __init__(self, name: _Optional[str] = ..., input_config: _Optional[_Union[InputConfig, _Mapping]] = ...) -> None: ...

class GcsDestination(_message.Message):
    __slots__ = ("uri",)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str
    def __init__(self, uri: _Optional[str] = ...) -> None: ...

class OutputConfig(_message.Message):
    __slots__ = ("gcs_destination",)
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: GcsDestination
    def __init__(self, gcs_destination: _Optional[_Union[GcsDestination, _Mapping]] = ...) -> None: ...

class ExportInstanceRequest(_message.Message):
    __slots__ = ("name", "output_config")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    output_config: OutputConfig
    def __init__(self, name: _Optional[str] = ..., output_config: _Optional[_Union[OutputConfig, _Mapping]] = ...) -> None: ...

class FailoverInstanceRequest(_message.Message):
    __slots__ = ("name", "data_protection_mode")
    class DataProtectionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_PROTECTION_MODE_UNSPECIFIED: _ClassVar[FailoverInstanceRequest.DataProtectionMode]
        LIMITED_DATA_LOSS: _ClassVar[FailoverInstanceRequest.DataProtectionMode]
        FORCE_DATA_LOSS: _ClassVar[FailoverInstanceRequest.DataProtectionMode]
    DATA_PROTECTION_MODE_UNSPECIFIED: FailoverInstanceRequest.DataProtectionMode
    LIMITED_DATA_LOSS: FailoverInstanceRequest.DataProtectionMode
    FORCE_DATA_LOSS: FailoverInstanceRequest.DataProtectionMode
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_PROTECTION_MODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    data_protection_mode: FailoverInstanceRequest.DataProtectionMode
    def __init__(self, name: _Optional[str] = ..., data_protection_mode: _Optional[_Union[FailoverInstanceRequest.DataProtectionMode, str]] = ...) -> None: ...

class OperationMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "target", "verb", "status_detail", "cancel_requested", "api_version")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_DETAIL_FIELD_NUMBER: _ClassVar[int]
    CANCEL_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_detail: str
    cancel_requested: bool
    api_version: str
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., target: _Optional[str] = ..., verb: _Optional[str] = ..., status_detail: _Optional[str] = ..., cancel_requested: bool = ..., api_version: _Optional[str] = ...) -> None: ...

class LocationMetadata(_message.Message):
    __slots__ = ("available_zones",)
    class AvailableZonesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ZoneMetadata
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ZoneMetadata, _Mapping]] = ...) -> None: ...
    AVAILABLE_ZONES_FIELD_NUMBER: _ClassVar[int]
    available_zones: _containers.MessageMap[str, ZoneMetadata]
    def __init__(self, available_zones: _Optional[_Mapping[str, ZoneMetadata]] = ...) -> None: ...

class ZoneMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TlsCertificate(_message.Message):
    __slots__ = ("serial_number", "cert", "create_time", "expire_time", "sha1_fingerprint")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CERT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    SHA1_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    cert: str
    create_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    sha1_fingerprint: str
    def __init__(self, serial_number: _Optional[str] = ..., cert: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sha1_fingerprint: _Optional[str] = ...) -> None: ...
