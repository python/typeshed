import sys
from _typeshed import StrOrBytesPath
from collections.abc import Callable, Hashable, Iterable, Sequence
from configparser import RawConfigParser
from re import Pattern
from threading import Thread
from typing import IO, Any, overload
from typing_extensions import Literal, SupportsIndex TypedDict

from . import Filter, Filterer, Formatter, Handler, Logger, _FilterType, _FormatStyle, _Level

DEFAULT_LOGGING_CONFIG_PORT: int
RESET_ERROR: int  # undocumented
IDENTIFIER: Pattern[str]  # undocumented

if sys.version_info >= (3, 11):
    class _RootLoggerConfiguration(TypedDict, total=False):
        level: _Level
        filters: Sequence[str | _FilterType]
        handlers: Sequence[str]

else:
    class _RootLoggerConfiguration(TypedDict, total=False):
        level: _Level
        filters: Sequence[str]
        handlers: Sequence[str]

class _LoggerConfiguration(_RootLoggerConfiguration, TypedDict, total=False):
    propagate: bool

if sys.version_info >= (3, 8):
    _FormatterConfigurationTypedDict = TypedDict(
        "_FormatterConfigurationTypedDict", {"class": str, "format": str, "datefmt": str, "style": _FormatStyle}, total=False
    )
else:
    _FormatterConfigurationTypedDict = TypedDict(
        "_FormatterConfigurationTypedDict",
        {"class": str, "format": str, "datefmt": str, "style": _FormatStyle, "validate": bool},
        total=False,
    )

class _FilterConfigurationTypedDict(TypedDict):
    name: str

# Formatter and filter configs can specify custom factories via the special `()` key.
# If that is the case, the dictionary can contain any additional keys
# https://docs.python.org/3/library/logging.config.html#user-defined-objects
_FormatterConfiguration: TypeAlias = _FormatterConfigurationTypedDict | dict[str, Any]
_FilterConfiguration: TypeAlias = _FilterConfigurationTypedDict | dict[str, Any]
# Handler config can have additional keys even when not providing a custom factory so we just use `dict`.
_HandlerConfiguration: TypeAlias = dict[str, Any]

class _OptionalDictConfigArgs(TypedDict, total=False):
    formatters: dict[str, _FormatterConfiguration]
    filters: dict[str, _FilterConfiguration]
    handlers: dict[str, _HandlerConfiguration]
    loggers: dict[str, _LoggerConfiguration]
    root: _RootLoggerConfiguration | None
    incremental: bool
    disable_existing_loggers: bool

class _DictConfigArgs(_OptionalDictConfigArgs, TypedDict):
    version: Literal[1]

# Accept dict[str, Any] to avoid false positives if called with a dict
# type, since dict types are not compatible with TypedDicts.
#
# Also accept a TypedDict type, to allow callers to use TypedDict
# types, and for somewhat stricter type checking of dict literals.
def dictConfig(config: _DictConfigArgs | dict[str, Any]) -> None: ...

if sys.version_info >= (3, 10):
    def fileConfig(
        fname: StrOrBytesPath | IO[str] | RawConfigParser,
        defaults: dict[str, str] | None = None,
        disable_existing_loggers: bool = True,
        encoding: str | None = None,
    ) -> None: ...

else:
    def fileConfig(
        fname: StrOrBytesPath | IO[str] | RawConfigParser,
        defaults: dict[str, str] | None = None,
        disable_existing_loggers: bool = True,
    ) -> None: ...

def valid_ident(s: str) -> Literal[True]: ...  # undocumented
def listen(port: int = 9030, verify: Callable[[bytes], bytes | None] | None = None) -> Thread: ...
def stopListening() -> None: ...

class ConvertingMixin:  # undocumented
    def convert_with_key(self, key: Any, value: Any, replace: bool = True) -> Any: ...
    def convert(self, value: Any) -> Any: ...

class ConvertingDict(dict[Hashable, Any], ConvertingMixin):  # undocumented
    def __getitem__(self, key: Hashable) -> Any: ...
    def get(self, key: Hashable, default: Any = None) -> Any: ...
    def pop(self, key: Hashable, default: Any = None) -> Any: ...

class ConvertingList(list[Any], ConvertingMixin):  # undocumented
    @overload
    def __getitem__(self, key: SupportsIndex) -> Any: ...
    @overload
    def __getitem__(self, key: slice) -> Any: ...
    def pop(self, idx: SupportsIndex = -1) -> Any: ...

class ConvertingTuple(tuple[Any], ConvertingMixin):  # undocumented
    @overload
    def __getitem__(self, key: SupportsIndex) -> Any: ...
    @overload
    def __getitem__(self, key: slice) -> Any: ...

class BaseConfigurator:  # undocumented
    CONVERT_PATTERN: Pattern[str]
    WORD_PATTERN: Pattern[str]
    DOT_PATTERN: Pattern[str]
    INDEX_PATTERN: Pattern[str]
    DIGIT_PATTERN: Pattern[str]
    value_converters: dict[str, str]
    importer: Callable[..., Any]

    def __init__(self, config: _DictConfigArgs | dict[str, Any]) -> None: ...
    def resolve(self, s: str) -> Any: ...
    def ext_convert(self, value: str) -> Any: ...
    def cfg_convert(self, value: str) -> Any: ...
    def convert(self, value: Any) -> Any: ...
    def configure_custom(self, config: dict[str, Any]) -> Any: ...
    def as_tuple(self, value: list[Any] | tuple[Any]) -> tuple[Any]: ...

class DictConfigurator(BaseConfigurator):
    def configure(self) -> None: ...  # undocumented
    def configure_formatter(self, config: _FormatterConfiguration) -> Formatter | Any: ...  # undocumented
    def configure_filter(self, config: _FilterConfiguration) -> Filter | Any: ...  # undocumented
    def add_filters(self, filterer: Filterer, filters: Iterable[_FilterType]) -> None: ...  # undocumented
    def configure_handler(self, config: _HandlerConfiguration) -> Handler | Any: ...  # undocumented
    def add_handlers(self, logger: Logger, handlers: Iterable[str]) -> None: ...  # undocumented
    def common_logger_config(
        self, logger: Logger, config: _LoggerConfiguration, incremental: bool = False
    ) -> None: ...  # undocumented
    def configure_logger(self, name: str, config: _LoggerConfiguration, incremental: bool = False) -> None: ...  # undocumented
    def configure_root(self, config: _LoggerConfiguration, incremental: bool = False) -> None: ...  # undocumented

dictConfigClass = DictConfigurator
