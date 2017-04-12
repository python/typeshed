# Stubs for dateutil.tz.tz (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional, Union, IO, Tuple, List
import datetime
from ._common import tzname_in_python2 as tzname_in_python2, _tzinfo as _tzinfo
from ._common import tzrangebase as tzrangebase, enfold as enfold
from ..relativedelta import relativedelta

ZERO = ...  # type: datetime.timedelta
EPOCH = ...  # type: datetime.datetime
EPOCHORDINAL = ...  # type: int

class tzutc(datetime.tzinfo):
    def utcoffset(self, dt: Optional[datetime.datetime]) -> Optional[datetime.timedelta]: ...
    def dst(self, dt: Optional[datetime.datetime]) -> Optional[datetime.timedelta]: ...
    def tzname(self, dt: Optional[datetime.datetime]) -> str: ...
    def is_ambiguous(self, dt: Optional[datetime.datetime]) -> bool: ...
    def __eq__(self, other): ...
    __hash__ = ...  # type: Any
    def __ne__(self, other): ...
    __reduce__ = ...  # type: Any

class tzoffset(datetime.tzinfo):
    def __init__(self, name, offset) -> None: ...
    def utcoffset(self, dt: Optional[datetime.datetime]) -> Optional[datetime.timedelta]: ...
    def dst(self, dt: Optional[datetime.datetime]) -> Optional[datetime.timedelta]: ...
    def is_ambiguous(self, dt: Optional[datetime.datetime]) -> bool: ...
    def tzname(self, dt: Optional[datetime.datetime]) -> str: ...
    def __eq__(self, other): ...
    __hash__ = ...  # type: Any
    def __ne__(self, other): ...
    __reduce__ = ...  # type: Any

class tzlocal(_tzinfo):
    def __init__(self) -> None: ...
    def utcoffset(self, dt: Optional[datetime.datetime]) -> Optional[datetime.timedelta]: ...
    def dst(self, dt: Optional[datetime.datetime]) -> Optional[datetime.timedelta]: ...
    def tzname(self, dt: Optional[datetime.datetime]) -> str: ...
    def is_ambiguous(self, dt: Optional[datetime.datetime]) -> bool: ...
    def __eq__(self, other): ...
    __hash__ = ...  # type: Any
    def __ne__(self, other): ...
    __reduce__ = ...  # type: Any

class _ttinfo:
    def __init__(self) -> None: ...
    def __eq__(self, other): ...
    __hash__ = ...  # type: Any
    def __ne__(self, other): ...

class tzfile(_tzinfo):
    def __init__(self, fileobj: Union[str, IO[str]], filename: Optional[str] = ...) -> None: ...
    def is_ambiguous(self, dt: Optional[datetime.datetime], idx: Optional[int] = ...) -> bool: ...
    def utcoffset(self, dt: Optional[datetime.datetime]) -> Optional[datetime.timedelta]: ...
    def dst(self, dt: Optional[datetime.datetime]) -> Optional[datetime.timedelta]: ...
    def tzname(self, dt: Optional[datetime.datetime]) -> str: ...
    def __eq__(self, other): ...
    __hash__ = ...  # type: Any
    def __ne__(self, other): ...
    def __reduce__(self): ...
    def __reduce_ex__(self, protocol): ...

class tzrange(tzrangebase):
    hasdst = ...  # type: bool
    def __init__(self, stdabbr: str, stdoffset: Union[int, datetime.timedelta, None] = ..., dstabbr: Optional[str] = ..., dstoffset: Union[int, datetime.timedelta, None] = ..., start: Optional[relativedelta] = ..., end: Optional[relativedelta] = ...) -> None: ...
    def transitions(self, year: int) -> Tuple[datetime.datetime, datetime.datetime]: ...
    def __eq__(self, other): ...

class tzstr(tzrange):
    hasdst = ...  # type: bool
    def __init__(self, s: Union[bytes, str, IO[str]], posix_offset: bool = ...) -> None: ...

class tzical:
    def __init__(self, fileobj: Union[str, IO[str]]) -> None: ...
    def keys(self): ...
    def get(self, tzid: Optional[Any] = ...): ...

TZFILES = ...  # type: List[str]
TZPATHS = ...  # type: List[str]

def gettz(name: Optional[str] = ...) -> Optional[datetime.tzinfo]: ...
def datetime_exists(dt: datetime.datetime, tz: Optional[datetime.tzinfo] = ...) -> bool: ...
def datetime_ambiguous(dt: datetime.datetime, tz: Optional[datetime.tzinfo] = ...) -> bool: ...
