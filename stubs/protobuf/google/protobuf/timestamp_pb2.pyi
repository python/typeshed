"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.well_known_types import (
    Timestamp as google___protobuf___internal___well_known_types___Timestamp,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

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

class Timestamp(google___protobuf___message___Message, google___protobuf___internal___well_known_types___Timestamp):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    seconds: builtin___int = ...
    nanos: builtin___int = ...

    def __init__(self,
        *,
        seconds : typing___Optional[builtin___int] = ...,
        nanos : typing___Optional[builtin___int] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"nanos",b"nanos",u"seconds",b"seconds"]) -> None: ...
type___Timestamp = Timestamp
