import sys
from _typeshed import StrOrBytesPath, StrPath
from collections.abc import Callable
from configparser import RawConfigParser
from threading import Thread
from typing import IO, Any, Pattern
from . import _FormatStyle, _Level

if sys.version_info >= (3, 8):
    from typing import Literal, TypedDict
else:
    from typing_extensions import Literal, TypedDict

if sys.version_info >= (3, 7):
    _Path = StrOrBytesPath
else:
    _Path = StrPath

DEFAULT_LOGGING_CONFIG_PORT: int
RESET_ERROR: int  # undocumented
IDENTIFIER: Pattern[str]  # undocumented

# can't have a class attribute called "class"
_OptionalClassKey = TypedDict("_OptionalClassKey", {"class": str}, total=False)

if sys.version_info >= (3, 8):
    class _FormatterConfiguration(_OptionalClassKey, TypedDict, total=False):
        format: str
        datefmt: str
        style: _FormatStyle
        validate: bool

else:
    class _FormatterConfiguration(_OptionalClassKey, TypedDict, total=False):
        format: str
        datefmt: str
        style: _FormatStyle

class _FilterConfiguration(TypedDict, total=False):
    name: str

class _RootLoggerConfiguration(TypedDict, total=False):
    level: _Level
    filters: Sequence[str]
    handlers: Sequence[str]

class _LoggerConfiguration(_RootLoggerConfiguration, TypedDict, total=False):
    propagate: bool

class _OptionalDictConfigArgs(TypedDict, total=False):
    formatters: dict[str, _FormatterConfiguration]
    filters: dict[str, _FilterConfiguration]
    # type checkers would warn about extra keys if this was a TypedDict
    handlers: dict[str, dict[str, Any]]
    loggers: dict[str, _LoggerConfiguration]
    root: _RootLoggerConfiguration
    incremental: bool
    disable_existing_loggers: bool

class _DictConfigArgs(_OptionalDictConfigArgs, TypedDict):
    version: Literal[1]

def dictConfig(config: _DictConfigArgs) -> None: ...

if sys.version_info >= (3, 10):
    def fileConfig(
        fname: _Path | IO[str] | RawConfigParser,
        defaults: dict[str, str] | None = ...,
        disable_existing_loggers: bool = ...,
        encoding: str | None = ...,
    ) -> None: ...

else:
    def fileConfig(
        fname: _Path | IO[str] | RawConfigParser, defaults: dict[str, str] | None = ..., disable_existing_loggers: bool = ...
    ) -> None: ...

def valid_ident(s: str) -> Literal[True]: ...  # undocumented
def listen(port: int = ..., verify: Callable[[bytes], bytes | None] | None = ...) -> Thread: ...
def stopListening() -> None: ...
