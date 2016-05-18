# Stubs for logging.handlers (Python 2.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import logging
import socket

threading = ...  # type: Any
DEFAULT_TCP_LOGGING_PORT = ...  # type: Any
DEFAULT_UDP_LOGGING_PORT = ...  # type: Any
DEFAULT_HTTP_LOGGING_PORT = ...  # type: Any
DEFAULT_SOAP_LOGGING_PORT = ...  # type: Any
SYSLOG_UDP_PORT = ...  # type: Any
SYSLOG_TCP_PORT = ...  # type: Any

class BaseRotatingHandler(logging.FileHandler):
    mode = ...  # type: Any
    encoding = ...  # type: Any
    namer = ...  # type: Any
    rotator = ...  # type: Any
    def __init__(self, filename: unicode, mode: unicode, encoding: unicode =..., delay: int =...) -> None: ...
    def emit(self, record: Any) -> None: ...
    def rotation_filename(self, default_name: unicode) -> Any: ...
    def rotate(self, source: Any, dest: Any) -> Any: ...

class RotatingFileHandler(BaseRotatingHandler):
    maxBytes = ...  # type: Any
    backupCount = ...  # type: Any
    def __init__(self, filename: unicode, mode: unicode = ..., maxBytes: int = ..., backupCount:int = ...,
                 encoding: str = ..., delay: int = ...) -> None: ...
    stream = ...  # type: Any
    def doRollover(self) -> None: ...
    def shouldRollover(self, record: Any) -> int: ...

class TimedRotatingFileHandler(BaseRotatingHandler):
    when = ...  # type: Any
    backupCount = ...  # type: Any
    utc = ...  # type: Any
    atTime = ...  # type: Any
    interval = ...  # type: Any
    suffix = ...  # type: Any
    extMatch = ...  # type: Any
    dayOfWeek = ...  # type: Any
    rolloverAt = ...  # type: Any
    def __init__(self, filename: unicode, when: unicode =..., interval: int =..., backupCount: int =...,
                 encoding: unicode =..., delay: bool =..., utc: bool =..., atTime: Any =...) -> None: ...
    def computeRollover(self, currentTime: int) -> int: ...
    def shouldRollover(self, record: Any) -> int: ...
    def getFilesToDelete(self) -> list[str]: ...
    stream = ...  # type: Any
    def doRollover(self) -> None: ...

class WatchedFileHandler(logging.FileHandler):
    def __init__(self, filename: str, mode: str = ..., encoding: str = ..., delay: int = ...) -> None: ...
    stream = ...  # type: Any
    def emit(self, record: Any) -> None: ...

class SocketHandler(logging.Handler):
    host = ...  # type: Any
    port = ...  # type: Any
    address = ...  # type: Any
    sock = ...  # type: Any
    closeOnError = ...  # type: Any
    retryTime = ...  # type: Any
    retryStart = ...  # type: Any
    retryMax = ...  # type: Any
    retryFactor = ...  # type: Any
    def __init__(self, host: Any, port: Any) -> None: ...
    def makeSocket(self, timeout: int =...) -> socket._socketsocket: ...
    retryPeriod = ...  # type: Any
    def createSocket(self) -> None: ...
    def send(self, s: str) -> None: ...
    def makePickle(self, record: Any) -> str: ...
    def handleError(self, record: Any) -> None: ...
    def emit(self, record: Any) -> None: ...
    def close(self) -> None: ...

class DatagramHandler(SocketHandler):
    closeOnError = ...  # type: Any
    def __init__(self, host: Any, port: Any) -> None: ...
    def makeSocket(self) -> None: ...
    def send(self, s: str) -> None: ...

class SysLogHandler(logging.Handler):
    LOG_EMERG = ...  # type: Any
    LOG_ALERT = ...  # type: Any
    LOG_CRIT = ...  # type: Any
    LOG_ERR = ...  # type: Any
    LOG_WARNING = ...  # type: Any
    LOG_NOTICE = ...  # type: Any
    LOG_INFO = ...  # type: Any
    LOG_DEBUG = ...  # type: Any
    LOG_KERN = ...  # type: Any
    LOG_USER = ...  # type: Any
    LOG_MAIL = ...  # type: Any
    LOG_DAEMON = ...  # type: Any
    LOG_AUTH = ...  # type: Any
    LOG_SYSLOG = ...  # type: Any
    LOG_LPR = ...  # type: Any
    LOG_NEWS = ...  # type: Any
    LOG_UUCP = ...  # type: Any
    LOG_CRON = ...  # type: Any
    LOG_AUTHPRIV = ...  # type: Any
    LOG_FTP = ...  # type: Any
    LOG_LOCAL0 = ...  # type: Any
    LOG_LOCAL1 = ...  # type: Any
    LOG_LOCAL2 = ...  # type: Any
    LOG_LOCAL3 = ...  # type: Any
    LOG_LOCAL4 = ...  # type: Any
    LOG_LOCAL5 = ...  # type: Any
    LOG_LOCAL6 = ...  # type: Any
    LOG_LOCAL7 = ...  # type: Any
    priority_names = ...  # type: Any
    facility_names = ...  # type: Any
    priority_map = ...  # type: Any
    address = ...  # type: Any
    facility = ...  # type: Any
    socktype = ...  # type: Any
    unixsocket = ...  # type: Any
    socket = ...  # type: Any
    formatter = ...  # type: Any
    def __init__(self, address: tuple[str,int] =..., facility: int =..., socktype: int =...) -> None: ...
    def encodePriority(self, facility: int, priority: Union[basestring,integer]) -> int: ...
    def close(self) -> None: ...
    def mapPriority(self, levelName: str) -> str: ...
    ident = ...  # type: Any
    append_nul = ...  # type: Any
    def emit(self, record: Any) -> None: ...

class SMTPHandler(logging.Handler):
    username = ...  # type: Any
    fromaddr = ...  # type: Any
    toaddrs = ...  # type: Any
    subject = ...  # type: Any
    secure = ...  # type: Any
    timeout = ...  # type: Any
    def __init__(self, mailhost: Any, fromaddr: Any, toaddrs: Any, subject: unicode, credentials: Tuple[Any,Any]=...,
                 secure: Any =...) -> None: ...
    def getSubject(self, record: Any) -> unicode: ...
    def emit(self, record: Any) -> None: ...

class NTEventLogHandler(logging.Handler):
    appname = ...  # type: Any
    dllname = ...  # type: Any
    logtype = ...  # type: Any
    deftype = ...  # type: Any
    typemap = ...  # type: Any
    def __init__(self, appname: Any, dllname: Any =..., logtype: str =...) -> None: ...
    def getMessageID(self, record: Any) -> int: ...
    def getEventCategory(self, record: Any) -> int: ...
    def getEventType(self, record: Any) -> Any: ...
    def emit(self, record: Any) -> None: ...
    def close(self) -> None: ...

class HTTPHandler(logging.Handler):
    host = ...  # type: Any
    url = ...  # type: Any
    method = ...  # type: Any
    secure = ...  # type: Any
    credentials = ...  # type: Any
    def __init__(self, host: Any, url: Any, method: str =..., secure: Any =..., credentials: Any=...) -> None: ...
    def mapLogRecord(self, record: Any) -> dict[Any,Any]: ...
    def emit(self, record: Any) -> None: ...

class BufferingHandler(logging.Handler):
    capacity = ...  # type: Any
    buffer = ...  # type: Any
    def __init__(self, capacity: int) -> None: ...
    def shouldFlush(self, record: Any) -> bool: ...
    def emit(self, record: Any) -> None: ...
    def flush(self) -> None: ...
    def close(self) -> None: ...

class MemoryHandler(BufferingHandler):
    flushLevel = ...  # type: Any
    target = ...  # type: Any
    def __init__(self, capacity: int, flushLevel: int =..., target: Any=...) -> None: ...
    def shouldFlush(self, record: Any) -> bool: ...
    def setTarget(self, target: Any) -> None: ...
    buffer = ...  # type: Any
    def flush(self) -> None: ...
    def close(self) -> None: ...

class QueueHandler(logging.Handler):
    queue = ...  # type: Any
    def __init__(self, queue: Any) -> None: ...
    def enqueue(self, record: Any) -> Any: ...
    def prepare(self, record: Any) -> Any: ...
    def emit(self, record: Any) -> None: ...

class QueueListener:
    queue = ...  # type: Any
    handlers = ...  # type: Any
    def __init__(self, queue: Any, *handlers: Any) -> None: ...
    def dequeue(self, block: Any) -> Any: ...
    def start(self) -> None: ...
    def prepare(self, record: Any) -> Any: ...
    def handle(self, record: Any) -> Any: ...
    def enqueue_sentinel(self) -> Any: ...
    def stop(self) -> None: ...
