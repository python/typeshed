import codecs
from _codecs import _CharMap
from _typeshed import ReadableBuffer

class Codec(codecs.Codec):
    encode = codecs.charmap_encode  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
    decode = codecs.charmap_decode  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

class IncrementalEncoder(codecs.IncrementalEncoder):
    mapping: _CharMap
    def __init__(self, errors: str = "strict", mapping: _CharMap | None = None) -> None: ...
    def encode(self, input: str, final: bool = False) -> bytes: ...

class IncrementalDecoder(codecs.IncrementalDecoder):
    mapping: _CharMap
    def __init__(self, errors: str = "strict", mapping: _CharMap | None = None) -> None: ...
    def decode(self, input: ReadableBuffer, final: bool = False) -> str: ...

class StreamWriter(Codec, codecs.StreamWriter):
    mapping: _CharMap
    def __init__(self, stream, errors: str = "strict", mapping: _CharMap | None = None) -> None: ...
    def encode(self, input: str, errors: str = "strict") -> tuple[bytes, int]: ...  # type: ignore[override]

class StreamReader(Codec, codecs.StreamReader):
    mapping: _CharMap
    def __init__(self, stream, errors: str = "strict", mapping: _CharMap | None = None) -> None: ...
    def decode(self, input: ReadableBuffer, errors: str = "strict") -> tuple[str, int]: ...  # type: ignore[override]

def getregentry() -> codecs.CodecInfo: ...
