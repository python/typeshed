from _typeshed import ReadableBuffer, SupportsNoArgReadline, SupportsRead, SupportsWrite
from typing import Final, Protocol

__all__ = ["encode", "decode", "encodestring", "decodestring"]

ESCAPE: Final = b"="  # undocumented
MAXLINESIZE: Final = 76  # undocumented
HEX: Final = b"0123456789ABCDEF"  # undocumented
EMPTYSTRING: Final = b""  # undocumented

class _Input(SupportsRead[bytes], SupportsNoArgReadline[bytes], Protocol): ...

def encode(input: _Input, output: SupportsWrite[bytes], quotetabs: int, header: bool = False) -> None: ...
def encodestring(s: ReadableBuffer, quotetabs: bool = False, header: bool = False) -> bytes: ...
def decode(input: _Input, output: SupportsWrite[bytes], header: bool = False) -> None: ...
def decodestring(s: str | ReadableBuffer, header: bool = False) -> bytes: ...
def needsquoting(c: bytes, quotetabs: bool, header: bool) -> bool: ...  # undocumented
def quote(c: bytes) -> bytes: ...  # undocumented
def ishex(c: bytes) -> bool: ...  # undocumented
def unhex(s: bytes) -> int: ...  # undocumented
def main() -> None: ...  # undocumented
