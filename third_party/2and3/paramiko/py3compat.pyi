import sys
from typing import Any, Text

PY2: bool

string_types = Text
text_type = Text
integer_types = int
bytes_types = bytes

if sys.version_info < (3, 0):
    import cStringIO

    StringIO = cStringIO.StringIO
    BytesIO = StringIO
else:
    import io

    StringIO = io.StringIO
    BytesIO = io.BytesIO

def bytestring(s: Any) -> Any: ...
def byte_ord(c: int) -> Any: ...
def byte_chr(c: int) -> Any: ...
def byte_mask(c: Any, mask: Any) -> Any: ...
def b(s: Any, encoding: str = ...) -> bytes: ...
def u(s: Any, encoding: str = ...) -> Text: ...
def b2s(s: Any) -> str: ...
def is_callable(c: Any) -> bool: ...

MAXSIZE: int
