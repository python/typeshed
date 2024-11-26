import codecs
import sys
from _typeshed import ReadableBuffer

if sys.platform == "win32":
    encode = codecs.mbcs_encode

    def decode(input: ReadableBuffer, errors: str | None = "strict") -> tuple[str, int]: ...

    class IncrementalEncoder(codecs.IncrementalEncoder):
        def encode(self, input: str, final: bool = False) -> bytes: ...

    class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
        _buffer_decode = codecs.mbcs_decode  # type: ignore[assignment]

    class StreamWriter(codecs.StreamWriter):
        encode = codecs.mbcs_encode  # type: ignore[assignment]

    class StreamReader(codecs.StreamReader):
        decode = codecs.mbcs_decode  # type: ignore[assignment]

    def getregentry() -> codecs.CodecInfo: ...
