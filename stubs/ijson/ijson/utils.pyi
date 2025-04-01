from _typeshed import Incomplete
from collections.abc import Callable, Generator
from typing import Iterable, TypeVar
from typing_extensions import ParamSpec, TypeAlias

_P = ParamSpec("_P")
_T = TypeVar("_T")
_GS = TypeVar("_GS")
_GR = TypeVar("_GR")
_CoroPipelineArgs: TypeAlias = tuple[Callable[..., Incomplete], tuple[Incomplete, ...], dict[str, Incomplete]]

def coroutine(func: Callable[_P, Generator[_T, _GS, _GR]]) -> Callable[_P, Generator[_T, _GS, _GR]]: ...
def chain(sink: list[Incomplete], *coro_pipeline: _CoroPipelineArgs) -> list[Incomplete]: ...

class sendable_list(list[_T]):
    # send = list.append
    def send(self, object: _T, /) -> None: ...

def coros2gen(source: Iterable[_T], *coro_pipeline: _CoroPipelineArgs) -> Generator[_T, Incomplete, None]: ...
