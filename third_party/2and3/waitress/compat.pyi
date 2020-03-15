from typing import Any, Optional

PY2: Any
PY3: Any
WIN: Any
string_types: Any
integer_types: Any
class_types: Any
text_type = str
binary_type = bytes
long = int

def unquote_bytes_to_wsgi(bytestring: Any): ...
def text_(s: Any, encoding: str = ..., errors: str = ...): ...
def tostr(s: Any): ...
def tobytes(s: Any): ...

exec_: Any

def reraise(tp: Any, value: Any, tb: Optional[Any] = ...) -> None: ...

MAXINT: Any
HAS_IPV6: Any
IPPROTO_IPV6: Any
IPV6_V6ONLY: Any

def set_nonblocking(fd: Any) -> None: ...
ResourceWarning = ResourceWarning

def qualname(cls): ...
