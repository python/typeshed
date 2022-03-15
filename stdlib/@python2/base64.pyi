from typing import IO

_encodable = bytes | unicode
_decodable = bytes | unicode

def b64encode(s: _encodable, altchars: bytes | None = ...) -> bytes: ...
def b64decode(s: _decodable, altchars: bytes | None = ..., validate: bool = ...) -> bytes: ...
def standard_b64encode(s: _encodable) -> bytes: ...
def standard_b64decode(s: _decodable) -> bytes: ...
def urlsafe_b64encode(s: _encodable) -> bytes: ...
def urlsafe_b64decode(s: _decodable) -> bytes: ...
def b32encode(s: _encodable) -> bytes: ...
def b32decode(s: _decodable, casefold: bool = ..., map01: bytes | None = ...) -> bytes: ...
def b16encode(s: _encodable) -> bytes: ...
def b16decode(s: _decodable, casefold: bool = ...) -> bytes: ...
def decode(input: IO[bytes], output: IO[bytes]) -> None: ...
def encode(input: IO[bytes], output: IO[bytes]) -> None: ...
def encodestring(s: bytes) -> bytes: ...
def decodestring(s: bytes) -> bytes: ...
