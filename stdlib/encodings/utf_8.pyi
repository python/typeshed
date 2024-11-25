import codecs
from _typeshed import ReadableBuffer

encode = codecs.utf_8_encode

def decode(input: ReadableBuffer, errors: str | None = "strict") -> tuple[str, int]: ...

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input: str, final: bool = False) -> bytes: ...

class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    _buffer_decode = codecs.utf_8_decode  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

class StreamWriter(codecs.StreamWriter):
    encode = codecs.utf_8_encode  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

class StreamReader(codecs.StreamReader):
    decode = codecs.utf_8_decode  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

def getregentry() -> codecs.CodecInfo: ...
