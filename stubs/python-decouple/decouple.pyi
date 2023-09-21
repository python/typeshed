from _typeshed import Incomplete
from collections import OrderedDict
from collections.abc import Callable, Sequence
from configparser import ConfigParser
from typing import Any, Generic, TextIO, TypeVar, overload

_T = TypeVar("_T")
_TCsv = TypeVar("_TCsv", bound=Sequence[Any])

PYVERSION: Incomplete  # undocumented
DEFAULT_ENCODING: str  # undocumented
TRUE_VALUES: set[str]  # undocumented
FALSE_VALUES: set[str]  # undocumented

def read_config(parser: ConfigParser, file: TextIO) -> None: ...  # undocumented
def strtobool(value: str | bool) -> bool: ...  # undocumented

class UndefinedValueError(Exception): ...
class Undefined: ...

undefined: Undefined

class Config:
    repository: RepositoryEmpty
    def __init__(self, repository: RepositoryEmpty) -> None: ...
    @overload
    def get(self, option: str, default: str = ...) -> str: ...
    @overload
    def get(self, option: str, cast: Callable[..., _T]) -> _T: ...
    @overload
    def get(self, option: str, default: str, cast: Callable[..., _T]) -> _T: ...
    @overload
    def __call__(self, option: str, default: str = ...) -> str: ...
    @overload
    def __call__(self, option: str, cast: Callable[..., _T]) -> _T: ...
    @overload
    def __call__(self, option: str, default: str, cast: Callable[..., _T]) -> _T: ...

class RepositoryEmpty:  # undocumented
    def __init__(self, source: str = ..., encoding: str = ...) -> None: ...
    def __contains__(self, key: str) -> bool: ...
    def __getitem__(self, key: str) -> str: ...

class RepositoryIni(RepositoryEmpty):
    SECTION: str
    parser: ConfigParser
    def __init__(self, source: str, encoding: str = ...) -> None: ...
    def __contains__(self, key: str) -> bool: ...
    def __getitem__(self, key: str) -> str: ...

class RepositoryEnv(RepositoryEmpty):
    data: dict[str, str]
    def __init__(self, source: str, encoding: str = ...) -> None: ...
    def __contains__(self, key: str) -> bool: ...
    def __getitem__(self, key: str) -> str: ...

class RepositorySecret(RepositoryEmpty):
    data: dict[str, str]
    def __init__(self, source: str = ...) -> None: ...
    def __contains__(self, key: str) -> bool: ...
    def __getitem__(self, key: str) -> str: ...

class AutoConfig:
    SUPPORTED: OrderedDict[str, RepositoryEmpty]
    encoding: str
    search_path: str | None
    config: Config | None
    def __init__(self, search_path: str | None = None) -> None: ...
    @overload
    def __call__(self, option: str, default: str = ...) -> str: ...
    @overload
    def __call__(self, option: str, cast: Callable[..., _T]) -> _T: ...
    @overload
    def __call__(self, option: str, default: str, cast: Callable[..., _T]) -> _T: ...

config: AutoConfig

class Csv(Generic[_T, _TCsv]):
    cast: Callable[..., _T]
    delimiter: str
    strip: str
    post_process: Callable[..., _TCsv]
    def __call__(self, value: str) -> _TCsv: ...
    def __init__(
        self, cast: Callable[..., _T] = str, delimiter: str = ..., strip: str = ..., post_process: Callable[..., _TCsv] = list[_T]
    ) -> None: ...

class Choices(Generic[_T]):
    flat: Sequence[_T]
    cast: Callable[..., _T]
    choices: Sequence[_T]
    def __init__(
        self,
        flat: Sequence[_T] | None = None,
        cast: Callable[..., _T] = ...,
        choices: Sequence[_T | tuple[Incomplete, _T]] | None = None,
    ) -> None: ...
    def __call__(self, value: str) -> _T: ...
