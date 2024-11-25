import codecs
from _typeshed import ReadableBuffer

class Codec(codecs.Codec):
    encode = codecs.raw_unicode_escape_encode  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
    decode = codecs.raw_unicode_escape_decode  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input: str, final: bool = False) -> bytes: ...

class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    def _buffer_decode(self, input: str | ReadableBuffer, errors: str | None, final: bool) -> tuple[str, int]: ...

class StreamWriter(Codec, codecs.StreamWriter): ...

class StreamReader(Codec, codecs.StreamReader):
    def decode(self, input: str | ReadableBuffer, errors: str = "strict") -> tuple[str, int]: ...  # type: ignore[override]

def getregentry() -> codecs.CodecInfo: ...
