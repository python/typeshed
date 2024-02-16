from _typeshed import Incomplete, SupportsRead
from typing import Any, overload
from typing_extensions import TypeAlias

_UnicodeInputStream: TypeAlias = str | SupportsRead[str]
_BinaryInputStream: TypeAlias = bytes | SupportsRead[bytes]
_InputStream: TypeAlias = _UnicodeInputStream  # noqa: Y7047  # used in other files

spaceCharactersBytes: Any
asciiLettersBytes: Any
asciiUppercaseBytes: Any
spacesAngleBrackets: Any
invalid_unicode_no_surrogate: str
invalid_unicode_re: Any
non_bmp_invalid_codepoints: Any
ascii_punctuation_re: Any
charsUntilRegEx: Any

class BufferedStream:
    stream: Any
    buffer: Any
    position: Any
    def __init__(self, stream) -> None: ...
    def tell(self): ...
    def seek(self, pos) -> None: ...
    def read(self, bytes): ...

@overload
def HTMLInputStream(source: _UnicodeInputStream) -> HTMLUnicodeInputStream: ...
@overload
def HTMLInputStream(
    source: _BinaryInputStream,
    *,
    override_encoding: str | bytes | None = None,
    transport_encoding: str | bytes | None = None,
    same_origin_parent_encoding: str | bytes | None = None,
    likely_encoding: str | bytes | None = None,
    default_encoding: str = "windows-1252",
    useChardet: bool = True,
) -> HTMLBinaryInputStream: ...

class HTMLUnicodeInputStream:
    reportCharacterErrors: Any
    newLines: Any
    charEncoding: Any
    dataStream: Any
    def __init__(self, source: _UnicodeInputStream) -> None: ...
    chunk: str
    chunkSize: int
    chunkOffset: int
    errors: Any
    prevNumLines: int
    prevNumCols: int
    def reset(self) -> None: ...
    def openStream(self, source): ...
    def position(self) -> tuple[int, int]: ...
    def char(self): ...
    def readChunk(self, chunkSize: Incomplete | None = None): ...
    def characterErrorsUCS4(self, data) -> None: ...
    def characterErrorsUCS2(self, data) -> None: ...
    def charsUntil(self, characters, opposite: bool = False): ...
    def unget(self, char) -> None: ...

class HTMLBinaryInputStream(HTMLUnicodeInputStream):
    rawStream: Any
    numBytesMeta: int
    numBytesChardet: int
    override_encoding: Any
    transport_encoding: Any
    same_origin_parent_encoding: Any
    likely_encoding: Any
    default_encoding: Any
    charEncoding: Any
    def __init__(
        self,
        source: _BinaryInputStream,
        override_encoding: str | bytes | None = None,
        transport_encoding: str | bytes | None = None,
        same_origin_parent_encoding: str | bytes | None = None,
        likely_encoding: str | bytes | None = None,
        default_encoding: str = "windows-1252",
        useChardet: bool = True,
    ) -> None: ...
    dataStream: Any
    def reset(self) -> None: ...
    def openStream(self, source): ...
    def determineEncoding(self, chardet: bool = True): ...
    def changeEncoding(self, newEncoding) -> None: ...
    def detectBOM(self): ...
    def detectEncodingMeta(self): ...

class EncodingBytes(bytes):
    def __new__(self, value): ...
    def __init__(self, value) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    def next(self): ...
    def previous(self): ...
    def setPosition(self, position) -> None: ...
    def getPosition(self): ...
    position: Any
    def getCurrentByte(self): ...
    @property
    def currentByte(self): ...
    def skip(self, chars=...): ...
    def skipUntil(self, chars): ...
    def matchBytes(self, bytes): ...
    def jumpTo(self, bytes): ...

class EncodingParser:
    data: Any
    encoding: Any
    def __init__(self, data) -> None: ...
    def getEncoding(self): ...
    def handleComment(self): ...
    def handleMeta(self): ...
    def handlePossibleStartTag(self): ...
    def handlePossibleEndTag(self): ...
    def handlePossibleTag(self, endTag): ...
    def handleOther(self): ...
    def getAttribute(self): ...

class ContentAttrParser:
    data: Any
    def __init__(self, data) -> None: ...
    def parse(self): ...

def lookupEncoding(encoding: str | bytes | None) -> str | None: ...
