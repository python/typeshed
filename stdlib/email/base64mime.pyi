def header_length(bytearray: str | bytes) -> int: ...
def header_encode(header_bytes: str | bytes, charset: str = ...) -> str: ...
def body_encode(s: bytes, maxlinelen: int = ..., eol: str = ...) -> str: ...
def decode(string: str | bytes) -> bytes: ...

body_decode = decode
decodestring = decode
