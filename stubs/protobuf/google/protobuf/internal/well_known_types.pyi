from collections.abc import Iterable, Iterator, Mapping, Sequence
from datetime import datetime, timedelta, tzinfo
from typing import Any as tAny
from typing_extensions import TypeAlias

from google.protobuf import struct_pb2

class Any:
    type_url: tAny = ...
    value: tAny = ...
    def Pack(self, msg: tAny, type_url_prefix: str = ..., deterministic: tAny | None = ...) -> None: ...
    def Unpack(self, msg: tAny) -> bool: ...
    def TypeName(self) -> str: ...
    def Is(self, descriptor: tAny) -> bool: ...

class Timestamp:
    def ToJsonString(self) -> str: ...
    seconds: int = ...
    nanos: int = ...
    def FromJsonString(self, value: str) -> None: ...
    def GetCurrentTime(self) -> None: ...
    def ToNanoseconds(self) -> int: ...
    def ToMicroseconds(self) -> int: ...
    def ToMilliseconds(self) -> int: ...
    def ToSeconds(self) -> int: ...
    def FromNanoseconds(self, nanos: int) -> None: ...
    def FromMicroseconds(self, micros: int) -> None: ...
    def FromMilliseconds(self, millis: int) -> None: ...
    def FromSeconds(self, seconds: int) -> None: ...
    def ToDatetime(self, tzinfo: tzinfo | None = ...) -> datetime: ...
    def FromDatetime(self, dt: datetime) -> None: ...

class Duration:
    def ToJsonString(self) -> str: ...
    seconds: int = ...
    nanos: int = ...
    def FromJsonString(self, value: tAny) -> None: ...
    def ToNanoseconds(self) -> int: ...
    def ToMicroseconds(self) -> int: ...
    def ToMilliseconds(self) -> int: ...
    def ToSeconds(self) -> int: ...
    def FromNanoseconds(self, nanos: int) -> None: ...
    def FromMicroseconds(self, micros: int) -> None: ...
    def FromMilliseconds(self, millis: int) -> None: ...
    def FromSeconds(self, seconds: int) -> None: ...
    def ToTimedelta(self) -> timedelta: ...
    def FromTimedelta(self, td: timedelta) -> None: ...

class FieldMask:
    def ToJsonString(self) -> str: ...
    def FromJsonString(self, value: tAny) -> None: ...
    def IsValidForDescriptor(self, message_descriptor: tAny): ...
    def AllFieldsFromDescriptor(self, message_descriptor: tAny) -> None: ...
    def CanonicalFormFromMask(self, mask: tAny) -> None: ...
    def Union(self, mask1: tAny, mask2: tAny) -> None: ...
    def Intersect(self, mask1: tAny, mask2: tAny) -> None: ...
    def MergeMessage(
        self, source: tAny, destination: tAny, replace_message_field: bool = ..., replace_repeated_field: bool = ...
    ) -> None: ...

class _FieldMaskTree:
    def __init__(self, field_mask: tAny | None = ...) -> None: ...
    def MergeFromFieldMask(self, field_mask: tAny) -> None: ...
    def AddPath(self, path: tAny): ...
    def ToFieldMask(self, field_mask: tAny) -> None: ...
    def IntersectPath(self, path: tAny, intersection: tAny): ...
    def AddLeafNodes(self, prefix: tAny, node: tAny) -> None: ...
    def MergeMessage(self, source: tAny, destination: tAny, replace_message: tAny, replace_repeated: tAny) -> None: ...

_StructValue: TypeAlias = struct_pb2.Struct | struct_pb2.ListValue | str | float | bool | None
_StructValueArg: TypeAlias = _StructValue | Mapping[str, _StructValueArg] | Sequence[_StructValueArg]

class Struct:
    def __getitem__(self, key: str) -> _StructValue: ...
    def __contains__(self, item: _StructValueArg) -> bool: ...
    def __setitem__(self, key: str, value: _StructValueArg) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[str]: ...
    def keys(self) -> Iterator[str]: ...
    def values(self) -> Iterator[_StructValue]: ...
    def items(self) -> Iterator[tuple[str, _StructValue]]: ...
    def get_or_create_list(self, key: str) -> struct_pb2.ListValue: ...
    def get_or_create_struct(self, key: str) -> struct_pb2.Struct: ...
    def update(self, dictionary: Mapping[str, _StructValueArg]) -> None: ...

class ListValue:
    def __len__(self) -> int: ...
    def append(self, value: _StructValue) -> None: ...
    def extend(self, elem_seq: Iterable[_StructValue]) -> None: ...
    def __getitem__(self, index: int) -> _StructValue: ...
    def __setitem__(self, index: int, value: _StructValueArg) -> None: ...
    def __delitem__(self, key: int) -> None: ...
    def items(self) -> Iterator[_StructValue]: ...
    def add_struct(self) -> struct_pb2.Struct: ...
    def add_list(self) -> struct_pb2.ListValue: ...

WKTBASES: dict[str, type[tAny]]
