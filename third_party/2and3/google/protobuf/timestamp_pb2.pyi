# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.internal import well_known_types

from typing import (
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class Timestamp(google___protobuf___message___Message, well_known_types.Timestamp):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    seconds: builtin___int = ...
    nanos: builtin___int = ...

    def __init__(self,
        *,
        seconds : typing___Optional[builtin___int] = None,
        nanos : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"nanos",b"nanos",u"seconds",b"seconds"]) -> None: ...
type___Timestamp = Timestamp
