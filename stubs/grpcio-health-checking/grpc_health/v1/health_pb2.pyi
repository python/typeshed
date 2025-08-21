from _typeshed import Incomplete
from typing import ClassVar, final

from google._upb._message import Descriptor, FileDescriptor, MessageMeta
from google.protobuf import message

DESCRIPTOR: FileDescriptor

@final
class HealthCheckRequest(message.Message, metaclass=MessageMeta):
    __slots__ = ()
    SERVICE_FIELD_NUMBER: ClassVar[int]
    service: str
    def __init__(self, service: str | None = ...) -> None: ...
    DESCRIPTOR: Descriptor

@final
class HealthCheckResponse(message.Message, metaclass=MessageMeta):
    __slots__ = ()
    ServingStatus: Incomplete
    UNKNOWN: Incomplete
    SERVING: Incomplete
    NOT_SERVING: Incomplete
    SERVICE_UNKNOWN: Incomplete
    STATUS_FIELD_NUMBER: ClassVar[int]
    status: Incomplete
    def __init__(self, status: Incomplete | str | None = ...) -> None: ...
    DESCRIPTOR: Descriptor
