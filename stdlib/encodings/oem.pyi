import codecs
import sys
from _typeshed import ReadableBuffer

if sys.platform == "win32":
    from codecs import oem_decode, oem_encode

    encode = oem_encode

    def decode(input: ReadableBuffer, errors: str | None = "strict") -> tuple[str, int]: ...

    class IncrementalEncoder(codecs.IncrementalEncoder):
        def encode(self, input: str, final: bool = False) -> bytes: ...

    class IncrementalDecoder(codecs.BufferedIncrementalDecoder): ...

    class StreamWriter(codecs.StreamWriter):
        encode = oem_encode

    class StreamReader(codecs.StreamReader):
        decode = oem_decode

    def getregentry() -> codecs.CodecInfo: ...
