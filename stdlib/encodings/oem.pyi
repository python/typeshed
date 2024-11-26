import codecs
import sys
from _typeshed import ReadableBuffer

if sys.platform == "win32":
    encode = codecs.oem_encode

    def decode(input: ReadableBuffer, errors: str | None = "strict") -> tuple[str, int]: ...

    class IncrementalEncoder(codecs.IncrementalEncoder):
        def encode(self, input: str, final: bool = False) -> bytes: ...

    class IncrementalDecoder(codecs.BufferedIncrementalDecoder): ...

    class StreamWriter(codecs.StreamWriter):
        encode = codecs.oem_encode  # type: ignore[assignment]

    class StreamReader(codecs.StreamReader):
        decode = codecs.oem_decode  # type: ignore[assignment]

    def getregentry() -> codecs.CodecInfo: ...
