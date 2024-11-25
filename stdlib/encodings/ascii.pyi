import codecs
from _typeshed import ReadableBuffer

class Codec(codecs.Codec):
    encode = codecs.ascii_encode  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
    decode = codecs.ascii_decode  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input: str, final: bool = False) -> bytes: ...

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input: ReadableBuffer, final: bool = False) -> str: ...

class StreamWriter(Codec, codecs.StreamWriter): ...
class StreamReader(Codec, codecs.StreamReader): ...

class StreamConverter(StreamWriter, StreamReader):  # type: ignore[misc]  # incompatible methods in base classes
    encode = codecs.ascii_decode  # type: ignore[assignment]
    decode = codecs.ascii_encode  # type: ignore[assignment]

def getregentry() -> codecs.CodecInfo: ...
