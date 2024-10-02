from _typeshed import Incomplete
from collections import OrderedDict
from collections.abc import Callable, Iterable, Sequence
from configparser import ConfigParser
from typing import Any, Generic, Protocol, TypeVar, overload

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_TCsv = TypeVar("_TCsv")
_TCsv_co = TypeVar("_TCsv_co", covariant=True)

PYVERSION: Incomplete  # undocumented
DEFAULT_ENCODING: str  # undocumented
TRUE_VALUES: set[str]  # undocumented
FALSE_VALUES: set[str]  # undocumented

def read_config(parser: ConfigParser, file: Iterable[str]) -> None: ...  # undocumented
def strtobool(value: str | bool) -> bool: ...  # undocumented

class UndefinedValueError(Exception): ...
class Undefined: ...

undefined: Undefined

class Config:
    repository: _Repository
    def __init__(self, repository: _Repository) -> None: ...
    @overload
    def get(self, option: str, default: str = ...) -> str: ...
    @overload
    def get(self, option: str, default: _T) -> str | _T: ...
    @overload
    def get(self, option: str, *, cast: Callable[[str], _T]) -> _T: ...
    @overload
    def get(self, option: str, default: str | _T, cast: Callable[[str], _T]) -> _T: ...
    @overload
    def __call__(self, option: str, default: str = ...) -> str: ...
    @overload
    def __call__(self, option: str, default: _T) -> str | _T: ...
    @overload
    def __call__(self, option: str, *, cast: Callable[[str], _T]) -> _T: ...
    @overload
    def __call__(self, option: str, default: str | _T, cast: Callable[[str], _T]) -> _T: ...

class _Repository(Protocol):  # undocumented
    def __contains__(self, key: str) -> bool: ...
    def __getitem__(self, key: str) -> str: ...

class RepositoryEmpty:  # undocumented
    def __init__(self, source: str = ..., encoding: str = ...) -> None: ...
    def __contains__(self, key: str) -> bool: ...
    # Implementation detail: the return type is actually `None`, but that doesn't match the subclasses or the protocol.
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
    def __call__(self, option: str, default: _T) -> str | _T: ...
    @overload
    def __call__(self, option: str, *, cast: Callable[[str], _T]) -> _T: ...
    @overload
    def __call__(self, option: str, default: str | _T, cast: Callable[[str], _T]) -> _T: ...

config: AutoConfig

class _PostProcess(Protocol[_TCsv_co]):  # undocumented
    @overload
    def __call__(self) -> _TCsv_co: ...
    @overload
    def __call__(self, /, __value: Iterable[Any]) -> _TCsv_co: ...

_TPostProcess = TypeVar("_TPostProcess")

class Csv(Generic[_T, _TCsv, _TPostProcess]):
    cast: Callable[[str], _T]
    delimiter: str
    strip: str
    post_process: _TPostProcess
    def __call__(self, value: str | None) -> _TCsv: ...
    @overload
    def __init__(
        self: Csv[str, list[str], _PostProcess[list[str]]],
        cast: Callable[[str], str] = ...,
        delimiter: str = ...,
        strip: str = ...,
        post_process: _PostProcess[list[str]] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Csv[_T, list[_T], _PostProcess[list[_T]]],
        cast: Callable[[str], _T],
        delimiter: str = ...,
        strip: str = ...,
        post_process: _PostProcess[list[_T]] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Csv[str, _TCsv, _PostProcess[_TCsv]],
        cast: Callable[[str], str] = ...,
        delimiter: str = ...,
        strip: str = ...,
        *,
        post_process: _PostProcess[_TCsv],
    ) -> None: ...
    @overload
    def __init__(
        self: Csv[_T, _TCsv, _PostProcess[_TCsv]],
        cast: Callable[[str], _T],
        delimiter: str = ",",
        strip: str = ...,
        *,
        post_process: _PostProcess[_T, _TCsv],
    ) -> None: ...
    @overload
    def __init__(
        self: Csv[_T, _TCsv, _PostProcess[_TCsv]],
        cast: Callable[[str], _T],
        delimiter: str,
        strip: str,
        post_process: _PostProcess[_TCsv],
    ) -> None: ...

class Choices(Generic[_T]):
    flat: Sequence[_T]
    cast: Callable[[str], _T]
    choices: Sequence[tuple[_T, str]]
    @overload
    def __init__(
        self: Choices[str],
        flat: Sequence[str] | None = None,
        cast: Callable[[str], str] = ...,
        choices: Sequence[tuple[str, str]] | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self: Choices[_T], flat: Sequence[_T], cast: Callable[[str], _T] = ..., choices: Sequence[tuple[_T, str]] | None = None
    ) -> None: ...
    @overload
    def __init__(
        self: Choices[_T], flat: None, cast: Callable[[str], _T], choices: Sequence[tuple[_T, str]] | None = None
    ) -> None: ...
    @overload
    def __init__(
        self: Choices[_T], flat: None = None, cast: Callable[[str], _T] = ..., *, choices: Sequence[tuple[_T, str]]
    ) -> None: ...
    @overload
    def __init__(
        self: Choices[_T],
        flat: Sequence[_T] | None = None,
        *,
        cast: Callable[[str], _T],
        choices: Sequence[tuple[_T, str]] | None = None,
    ) -> None: ...
    def __call__(self, value: str) -> _T: ...
