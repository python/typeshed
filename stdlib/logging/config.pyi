import sys
from _typeshed import StrOrBytesPath, StrPath
from collections.abc import Callable
from configparser import RawConfigParser
from logging import Filter, Filterer, Formatter, Handler, Logger
from threading import Thread
from typing import IO, Any, ClassVar, Dict, Generic, Iterable, List, Optional, Pattern, Sequence, Tuple, TypeVar, Union, overload

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 7):
    _Path = StrOrBytesPath
else:
    _Path = StrPath

_TKey = TypeVar("_TKey", bound=str)
_TValue = TypeVar("_TValue")

DEFAULT_LOGGING_CONFIG_PORT: int
RESET_ERROR: int  # undocumented
IDENTIFIER: Pattern[str]  # undocumented
_listener: Optional[Any]
dictConfigClass = DictConfigurator

class ConvertingMixin(Generic[_TKey, _TValue]):
    def convert_with_key(self, key: _TKey, value: _TValue, replace: bool = ...) -> Dict[_TKey, _TValue]: ...
    def convert(self, value: _TValue) -> Dict[_TKey, _TValue]: ...

class ConvertingDict(ConvertingMixin[_TKey, _TValue]):
    def __getitem__(self, key: _TKey) -> _TValue: ...
    def get(self, key: _TKey, default: Optional[_TKey]) -> Union[_TValue, _TKey]: ...
    def pop(self, key: _TKey, default: Optional[_TKey] = ...) -> Union[_TValue, _TKey]: ...

class ConvertingList(ConvertingMixin[_TKey, _TValue]):
    @overload
    def __getitem__(self, key: int) -> _TKey: ...
    @overload
    def __getitem__(self, key: slice) -> Sequence[_TKey]: ...
    def pop(self, idx: int = ...) -> _TKey: ...

class ConvertingTuple(ConvertingMixin[_TKey, _TValue]):
    @overload
    def __getitem__(self, key: int) -> _TKey: ...
    @overload
    def __getitem__(self, key: slice) -> Tuple[_TKey]: ...

class DictConfigurator(BaseConfigurator[_TKey, _TValue]):
    def configure(self) -> None: ...
    def configure_formatter(self, config: Dict[_TKey, _TValue]) -> Union[_TValue, Formatter]: ...
    def configure_filter(self, config: Dict[_TKey, _TValue]) -> Union[_TValue, Filter]: ...
    def add_filters(self, filterer: Filterer, filters: Iterable[Filter]) -> None: ...
    def configure_handler(self, config: Dict[_TKey, _TValue]) -> Union[_TValue, Filter]: ...
    def add_handlers(self, logger: Logger, handlers: Iterable[Handler]) -> None: ...
    def common_logger_config(self, logger: Logger, config: Dict[_TKey, _TValue], incremental: Optional[bool] = ...) -> None: ...
    def configure_logger(self, name: str, config: Dict[_TKey, _TValue], incremental: Optional[bool] = ...) -> None: ...
    def configure_root(self, config: Dict[_TKey, _TValue], incremental: Optional[bool] = ...) -> None: ...

def dictConfig(config: dict[str, Any]) -> None: ...

if sys.version_info >= (3, 10):
    def fileConfig(
        fname: Union[_Path, IO[str], RawConfigParser],
        defaults: Optional[dict[str, str]] = ...,
        disable_existing_loggers: bool = ...,
        encoding: Optional[str] = ...,
    ) -> None: ...

else:
    def fileConfig(
        fname: Union[_Path, IO[str], RawConfigParser],
        defaults: Optional[dict[str, str]] = ...,
        disable_existing_loggers: bool = ...,
    ) -> None: ...

def valid_ident(s: str) -> Literal[True]: ...  # undocumented
def listen(port: int = ..., verify: Optional[Callable[[bytes], Optional[bytes]]] = ...) -> Thread: ...
def stopListening() -> None: ...

class BaseConfigurator(Generic[_TKey, _TValue]):
    CONVERT_PATTERN: ClassVar[Pattern[str]]
    WORD_PATTERN: ClassVar[Pattern[str]]
    DOT_PATTERN: ClassVar[Pattern[str]]
    INDEX_PATTERN: ClassVar[Pattern[str]]
    DIGIT_PATTERN: ClassVar[Pattern[str]]
    value_converters: ClassVar[Dict[str, str]]
    config: ClassVar[ConvertingDict[_TKey, _TValue]]
    def __init__(self, config: Dict[_TKey, _TValue]) -> None: ...
    def resolve(self, s: str) -> _TValue: ...
    def ext_convert(self, value: str) -> _TValue: ...
    def cfg_convert(self, value: str) -> _TValue: ...
    def convert(self, value: Union[str, Dict[_TKey, _TValue], List[str]]) -> _TValue: ...
    def configure_custom(self, config: Dict[_TKey, _TValue]) -> _TValue: ...
