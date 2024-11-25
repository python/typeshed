import codecs
from _typeshed import ReadableBuffer

encode = codecs.utf_32_le_encode

def decode(input: ReadableBuffer, errors: str | None = "strict") -> tuple[str, int]: ...

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input: str, final: bool = False) -> bytes: ...

class IncrementalDecoder(codecs.BufferedIncrementalDecoder): ...

class StreamWriter(codecs.StreamWriter):
    encode = codecs.utf_32_le_encode

class StreamReader(codecs.StreamReader):
    decode = codecs.utf_32_le_decode

def getregentry() -> codecs.CodecInfo: ...
