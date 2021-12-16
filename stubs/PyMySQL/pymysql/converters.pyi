import datetime
import time
from collections.abc import Callable, Mapping, Sequence
from decimal import Decimal
from typing import Any,  Type, TypeVar

_EscaperMapping = Mapping[Type[object], Callable[..., str]] | None
_T = TypeVar("_T")

def escape_item(val: object, charset: object, mapping: _EscaperMapping = ...) -> str: ...
def escape_dict(val: Mapping[str, object], charset: object, mapping: _EscaperMapping = ...) -> dict[str, str]: ...
def escape_sequence(val: Sequence[object], charset: object, mapping: _EscaperMapping = ...) -> str: ...
def escape_set(val: set[object], charset: object, mapping: _EscaperMapping = ...) -> str: ...
def escape_bool(value: bool, mapping: _EscaperMapping = ...) -> str: ...
def escape_int(value: int, mapping: _EscaperMapping = ...) -> str: ...
def escape_float(value: float, mapping: _EscaperMapping = ...) -> str: ...
def escape_string(value: str, mapping: _EscaperMapping = ...) -> str: ...
def escape_bytes_prefixed(value: bytes, mapping: _EscaperMapping = ...) -> str: ...
def escape_bytes(value: bytes, mapping: _EscaperMapping = ...) -> str: ...
def escape_str(value: str, mapping: _EscaperMapping = ...) -> str: ...
def escape_None(value: None, mapping: _EscaperMapping = ...) -> str: ...
def escape_timedelta(obj: datetime.timedelta, mapping: _EscaperMapping = ...) -> str: ...
def escape_time(obj: datetime.time, mapping: _EscaperMapping = ...) -> str: ...
def escape_datetime(obj: datetime.datetime, mapping: _EscaperMapping = ...) -> str: ...
def escape_date(obj: datetime.date, mapping: _EscaperMapping = ...) -> str: ...
def escape_struct_time(obj: time.struct_time, mapping: _EscaperMapping = ...) -> str: ...
def Decimal2Literal(o: Decimal, d: object) -> str: ...
def convert_datetime(obj: str | bytes) -> datetime.datetime | str: ...
def convert_timedelta(obj: str | bytes) -> datetime.timedelta | str: ...
def convert_time(obj: str | bytes) -> datetime.time | str: ...
def convert_date(obj: str | bytes) -> datetime.date | str: ...
def through(x: _T) -> _T: ...

convert_bit = through

encoders: dict[Type[object], Callable[..., str]]
decoders: dict[int, Callable[[str | bytes], Any]]
conversions: dict[Type[object] | int, Callable[..., Any]]
Thing2Literal = escape_str
