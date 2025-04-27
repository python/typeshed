from typing import ClassVar

from google.protobuf import descriptor, message
from google.protobuf.internal import enum_type_wrapper

DESCRIPTOR: descriptor.FileDescriptor

class HealthCheckRequest(message.Message):
    __slots__ = ("service",)
    SERVICE_FIELD_NUMBER: ClassVar[int]
    service: str
    def __init__(self, service: str | None = ...) -> None: ...

class HealthCheckResponse(message.Message):
    __slots__ = ("status",)
    class ServingStatus(int, metaclass=enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: ClassVar[HealthCheckResponse.ServingStatus]
        SERVING: ClassVar[HealthCheckResponse.ServingStatus]
        NOT_SERVING: ClassVar[HealthCheckResponse.ServingStatus]
        SERVICE_UNKNOWN: ClassVar[HealthCheckResponse.ServingStatus]
    UNKNOWN: HealthCheckResponse.ServingStatus
    SERVING: HealthCheckResponse.ServingStatus
    NOT_SERVING: HealthCheckResponse.ServingStatus
    SERVICE_UNKNOWN: HealthCheckResponse.ServingStatus
    STATUS_FIELD_NUMBER: ClassVar[int]
    status: HealthCheckResponse.ServingStatus
    def __init__(self, status: HealthCheckResponse.ServingStatus | str | None = ...) -> None: ...
