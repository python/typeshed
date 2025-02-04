from _typeshed import Incomplete
from collections.abc import Callable, Generator
from typing import Any, TypeVar
from typing_extensions import ParamSpec, TypeAlias

_P = ParamSpec("_P")
_T = TypeVar("_T")
_GS = TypeVar("_GS")
_GR = TypeVar("_GR")
_CoroPipelineArgs: TypeAlias = tuple[Callable[..., Any], tuple[Any, ...], dict[str, Any]]

def coroutine(func: Callable[_P, Generator[_T, _GS, _GR]]) -> Callable[_P, Generator[_T, _GS, _GR]]: ...
def chain(sink: list[Any], *coro_pipeline: _CoroPipelineArgs) -> list[Any]: ...

class sendable_list(list[_T]):
    # send = list.append
    def send(self, object: _T, /) -> None: ...

def coros2gen(source, *coro_pipeline: _CoroPipelineArgs) -> Generator[Incomplete]: ...
