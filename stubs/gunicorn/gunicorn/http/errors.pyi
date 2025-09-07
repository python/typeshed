from _typeshed import Incomplete

class ParseException(Exception): ...

class NoMoreData(IOError):
    buf: Incomplete
    def __init__(self, buf=None) -> None: ...

class ConfigurationProblem(ParseException):
    info: Incomplete
    code: int
    def __init__(self, info) -> None: ...

class InvalidRequestLine(ParseException):
    req: Incomplete
    code: int
    def __init__(self, req) -> None: ...

class InvalidRequestMethod(ParseException):
    method: Incomplete
    def __init__(self, method) -> None: ...

class InvalidHTTPVersion(ParseException):
    version: Incomplete
    def __init__(self, version) -> None: ...

class InvalidHeader(ParseException):
    hdr: Incomplete
    req: Incomplete
    def __init__(self, hdr, req=None) -> None: ...

class ObsoleteFolding(ParseException):
    hdr: Incomplete
    def __init__(self, hdr) -> None: ...

class InvalidHeaderName(ParseException):
    hdr: Incomplete
    def __init__(self, hdr) -> None: ...

class UnsupportedTransferCoding(ParseException):
    hdr: Incomplete
    code: int
    def __init__(self, hdr) -> None: ...

class InvalidChunkSize(IOError):
    data: Incomplete
    def __init__(self, data) -> None: ...

class ChunkMissingTerminator(IOError):
    term: Incomplete
    def __init__(self, term) -> None: ...

class LimitRequestLine(ParseException):
    size: Incomplete
    max_size: Incomplete
    def __init__(self, size, max_size) -> None: ...

class LimitRequestHeaders(ParseException):
    msg: Incomplete
    def __init__(self, msg) -> None: ...

class InvalidProxyLine(ParseException):
    line: Incomplete
    code: int
    def __init__(self, line) -> None: ...

class ForbiddenProxyRequest(ParseException):
    host: Incomplete
    code: int
    def __init__(self, host) -> None: ...

class InvalidSchemeHeaders(ParseException): ...
