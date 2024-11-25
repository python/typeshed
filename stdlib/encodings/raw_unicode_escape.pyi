import codecs
import sys
from _typeshed import ReadableBuffer

class Codec(codecs.Codec):
    encode = codecs.raw_unicode_escape_encode  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
    decode = codecs.raw_unicode_escape_decode  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input: str, final: bool = False) -> bytes: ...

if sys.version_info >= (3, 9):
    class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
        def _buffer_decode(self, input: str | ReadableBuffer, errors: str | None, final: bool) -> tuple[str, int]: ...

else:
    class IncrementalDecoder(codecs.IncrementalDecoder):
        def decode(self, input: str | ReadableBuffer, final: bool = False) -> str: ...

class StreamWriter(Codec, codecs.StreamWriter): ...

class StreamReader(Codec, codecs.StreamReader):
    if sys.version_info >= (3, 9):
        def decode(self, input: str | ReadableBuffer, errors: str = "strict") -> tuple[str, int]: ...  # type: ignore[override]

def getregentry() -> codecs.CodecInfo: ...
