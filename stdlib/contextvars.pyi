import sys
from typing import Any, Callable, ClassVar, Generic, Iterator, Mapping, TypeVar, overload
from typing_extensions import ParamSpec

if sys.version_info >= (3, 9):
    from types import GenericAlias

_T = TypeVar("_T")
_D = TypeVar("_D")
_P = ParamSpec("_P")

class ContextVar(Generic[_T]):
    def __init__(self, name: str, *, default: _T = ...) -> None: ...
    @property
    def name(self) -> str: ...
    @overload
    def get(self) -> _T: ...
    @overload
    def get(self, default: _D | _T) -> _D | _T: ...
    def set(self, value: _T) -> Token[_T]: ...
    def reset(self, token: Token[_T]) -> None: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...

class Token(Generic[_T]):
    @property
    def var(self) -> ContextVar[_T]: ...
    @property
    def old_value(self) -> Any: ...  # returns either _T or MISSING, but that's hard to express
    MISSING: ClassVar[object]
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...

def copy_context() -> Context: ...

# It doesn't make sense to make this generic, because for most Contexts each ContextVar will have
# a different value.
class Context(Mapping[ContextVar[Any], Any]):
    def __init__(self) -> None: ...
    @overload
    def get(self, __key: ContextVar[_T]) -> _T | None: ...
    @overload
    def get(self, __key: ContextVar[_T], __default: _D) -> _T | _D: ...
    def run(self, callable: Callable[_P, _T], *args: _P.args, **kwargs: _P.kwargs) -> _T: ...
    def copy(self) -> Context: ...
    def __getitem__(self, key: ContextVar[_T]) -> _T: ...
    def __iter__(self) -> Iterator[ContextVar[Any]]: ...
    def __len__(self) -> int: ...
