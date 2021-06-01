import datetime
import sys
from email.charset import Charset
from typing import List, Tuple, Union, overload

_ParamType = Union[str, Tuple[str | None, str | None, str]]
_PDTZ = Tuple[int, int, int, int, int, int, int, int, int, int | None]

def quote(str: str) -> str: ...
def unquote(str: str) -> str: ...
def parseaddr(addr: str | None) -> Tuple[str, str]: ...
def formataddr(pair: Tuple[str | None, str], charset: str | Charset = ...) -> str: ...
def getaddresses(fieldvalues: List[str]) -> List[Tuple[str, str]]: ...
@overload
def parsedate(data: None) -> None: ...
@overload
def parsedate(data: str) -> Tuple[int, int, int, int, int, int, int, int, int] | None: ...
@overload
def parsedate_tz(data: None) -> None: ...
@overload
def parsedate_tz(data: str) -> _PDTZ | None: ...

if sys.version_info >= (3, 10):
    @overload
    def parsedate_to_datetime(data: None) -> None: ...
    @overload
    def parsedate_to_datetime(data: str) -> datetime.datetime: ...

else:
    def parsedate_to_datetime(data: str) -> datetime.datetime: ...

def mktime_tz(data: _PDTZ) -> int: ...
def formatdate(timeval: float | None = ..., localtime: bool = ..., usegmt: bool = ...) -> str: ...
def format_datetime(dt: datetime.datetime, usegmt: bool = ...) -> str: ...
def localtime(dt: datetime.datetime | None = ..., isdst: int = ...) -> datetime.datetime: ...
def make_msgid(idstring: str | None = ..., domain: str | None = ...) -> str: ...
def decode_rfc2231(s: str) -> Tuple[str | None, str | None, str]: ...
def encode_rfc2231(s: str, charset: str | None = ..., language: str | None = ...) -> str: ...
def collapse_rfc2231_value(value: _ParamType, errors: str = ..., fallback_charset: str = ...) -> str: ...
def decode_params(params: List[Tuple[str, str]]) -> List[Tuple[str, _ParamType]]: ...
