from google.protobuf.message import (
    Message,
)
from typing import (
    Optional,
    Text,
)


class DoubleValue(Message):
    value = ...  # type: float

    def __init__(self,
                 value: Optional[float] = ...,
                 ) -> None: ...


class FloatValue(Message):
    value = ...  # type: float

    def __init__(self,
                 value: Optional[float] = ...,
                 ) -> None: ...


class Int64Value(Message):
    value = ...  # type: int

    def __init__(self,
                 value: Optional[int] = ...,
                 ) -> None: ...


class UInt64Value(Message):
    value = ...  # type: int

    def __init__(self,
                 value: Optional[int] = ...,
                 ) -> None: ...


class Int32Value(Message):
    value = ...  # type: int

    def __init__(self,
                 value: Optional[int] = ...,
                 ) -> None: ...


class UInt32Value(Message):
    value = ...  # type: int

    def __init__(self,
                 value: Optional[int] = ...,
                 ) -> None: ...


class BoolValue(Message):
    value = ...  # type: bool

    def __init__(self,
                 value: Optional[bool] = ...,
                 ) -> None: ...


class StringValue(Message):
    value = ...  # type: Text

    def __init__(self,
                 value: Optional[Text] = ...,
                 ) -> None: ...


class BytesValue(Message):
    value = ...  # type: bytes

    def __init__(self,
                 value: Optional[bytes] = ...,
                 ) -> None: ...
