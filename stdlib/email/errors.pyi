import sys

class MessageError(Exception): ...
class MessageParseError(MessageError): ...
class HeaderParseError(MessageParseError): ...
class BoundaryError(MessageParseError): ...
class MultipartConversionError(MessageError, TypeError): ...
class CharsetError(MessageError): ...

# Added in Python 3.8.20, 3.9.20, 3.10.15, 3.11.10, 3.12.5
class HeaderWriteError(MessageError): ...

class MessageDefect(ValueError):
    def __init__(self, line: str | None = None) -> None: ...

class NoBoundaryInMultipartDefect(MessageDefect): ...
class StartBoundaryNotFoundDefect(MessageDefect): ...
class FirstHeaderLineIsContinuationDefect(MessageDefect): ...
class MisplacedEnvelopeHeaderDefect(MessageDefect): ...
class MultipartInvariantViolationDefect(MessageDefect): ...
class InvalidMultipartContentTransferEncodingDefect(MessageDefect): ...
class UndecodableBytesDefect(MessageDefect): ...
class InvalidBase64PaddingDefect(MessageDefect): ...
class InvalidBase64CharactersDefect(MessageDefect): ...
class InvalidBase64LengthDefect(MessageDefect): ...
class CloseBoundaryNotFoundDefect(MessageDefect): ...
class MissingHeaderBodySeparatorDefect(MessageDefect): ...

MalformedHeaderDefect = MissingHeaderBodySeparatorDefect

class HeaderDefect(MessageDefect): ...
class InvalidHeaderDefect(HeaderDefect): ...
class HeaderMissingRequiredValue(HeaderDefect): ...

class NonPrintableDefect(HeaderDefect):
    def __init__(self, non_printables: str | None) -> None: ...

class ObsoleteHeaderDefect(HeaderDefect): ...
class NonASCIILocalPartDefect(HeaderDefect): ...

if sys.version_info >= (3, 10):
    class InvalidDateDefect(HeaderDefect): ...
