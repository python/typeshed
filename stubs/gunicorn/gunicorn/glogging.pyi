import logging
import threading
from datetime import timedelta
from socket import SocketKind
from typing import Annotated, Any, Literal, TypeAlias, TypedDict, override, type_check_only

from gunicorn.http import Request
from gunicorn.http.wsgi import Response

from ._types import _EnvironType
from .config import Config

SYSLOG_FACILITIES: dict[str, int]

@type_check_only
class _AtomsDict(TypedDict, total=False):
    h: str
    l: str
    u: str
    t: str
    r: str
    s: str
    m: str | None
    U: str | None
    q: str | None
    H: str | None
    b: str
    B: int | None
    f: str
    a: str
    T: int
    D: int
    M: int
    L: str
    p: str

_CriticalIntType: TypeAlias = Annotated[int, "50"]
_ErrorIntType: TypeAlias = Annotated[int, "40"]
_WarningIntType: TypeAlias = Annotated[int, "30"]
_InfoIntType: TypeAlias = Annotated[int, "20"]
_DebugIntType: TypeAlias = Annotated[int, "10"]
_LogLevelIntType: TypeAlias = _CriticalIntType | _ErrorIntType | _WarningIntType | _InfoIntType | _DebugIntType
_LogLevelStrType: TypeAlias = Literal["critical", "error", "warning", "info", "debug"]
_LogLevelType: TypeAlias = _LogLevelIntType | _LogLevelStrType

@type_check_only
class _RootConfig(TypedDict):
    level: str
    handlers: list[str]

@type_check_only
class _LoggerConfig(TypedDict):
    level: _LogLevelStrType
    handlers: list[str]
    propagate: bool
    qualname: str

@type_check_only
class _HandlerConfig(TypedDict, total=False):
    # class: str [Should be provided!]
    formatter: str
    stream: str

@type_check_only
class _FormatterConfig(TypedDict, total=False):
    # class: str [Should be provided!]
    format: str
    datefmt: str

@type_check_only
class _ConfigDefaults(TypedDict):
    version: int
    disable_existing_loggers: bool
    root: _RootConfig
    loggers: dict[str, _LoggerConfig]
    handlers: dict[str, _HandlerConfig]
    formatters: dict[str, _FormatterConfig]

CONFIG_DEFAULTS: _ConfigDefaults

def loggers() -> list[logging.Logger]: ...

class SafeAtoms(dict[str, Any]):
    def __init__(self, atoms: dict[str, Any]) -> None: ...
    @override
    def __getitem__(self, k: str) -> str: ...

_SyslogAddressType: TypeAlias = (
    tuple[Literal[SocketKind.SOCK_DGRAM] | None, str]  # Unix Socket
    | tuple[Literal[SocketKind.SOCK_DGRAM, SocketKind.SOCK_STREAM], tuple[str, int]]  # TCP/UDP Socket
)

def parse_syslog_address(addr: str) -> _SyslogAddressType: ...
@type_check_only
class _LogLevels(TypedDict):
    critical: _CriticalIntType
    error: _ErrorIntType
    warning: _WarningIntType
    info: _InfoIntType
    debug: _DebugIntType

class Logger:
    LOG_LEVELS: _LogLevels
    loglevel: _LogLevelIntType
    error_fmt: str
    datefmt: str
    access_fmt: str
    syslog_fmt: str
    atoms_wrapper_class: type[SafeAtoms]
    error_log: logging.Logger
    access_log: logging.Logger
    error_handlers: list[logging.Handler]
    access_handlers: list[logging.Handler]
    logfile: Any | None
    lock: threading.Lock
    cfg: Config

    def __init__(self, cfg: Config) -> None: ...
    def setup(self, cfg: Config) -> None: ...
    def critical(self, msg: str, *args: Any, **kwargs: Any) -> None: ...
    def error(self, msg: str, *args: Any, **kwargs: Any) -> None: ...
    def warning(self, msg: str, *args: Any, **kwargs: Any) -> None: ...
    def info(self, msg: str, *args: Any, **kwargs: Any) -> None: ...
    def debug(self, msg: str, *args: Any, **kwargs: Any) -> None: ...
    def exception(self, msg: str, *args: Any, **kwargs: Any) -> None: ...
    def log(self, lvl: _LogLevelType, msg: str, *args: Any, **kwargs: Any) -> None: ...
    def atoms(self, resp: Response, req: Request, environ: _EnvironType, request_time: timedelta) -> _AtomsDict: ...
    def access(self, resp: Response, req: Request, environ: _EnvironType, request_time: timedelta) -> None: ...
    def now(self) -> str: ...
    def reopen_files(self) -> None: ...
    def close_on_exec(self) -> None: ...
