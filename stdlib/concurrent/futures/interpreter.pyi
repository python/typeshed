import sys
from collections.abc import Mapping
from concurrent.futures import BrokenExecutor, ThreadPoolExecutor
from typing import Any, Callable, Final, overload
from typing_extensions import Concatenate, ParamSpec, Self, TypeAlias, TypeVar, TypeVarTuple, Unpack

_Task: TypeAlias = tuple[Callable[..., Any], tuple[Any, ...], dict[str, Any]]
_ResolveTaskFunc: TypeAlias = Callable[
    Concatenate[Callable[_P, _R], _P], tuple[Callable[_P, _R], tuple[Any, ...], dict[str, Any]]
]

_Ts = TypeVarTuple("_Ts")
_P = ParamSpec("_P")
_R = TypeVar("_R")

if sys.version_info >= (3, 14):
    from _interpreters import InterpreterError

    class ExecutionFailed(InterpreterError): ...

UNBOUND: Final = 2

if sys.version_info >= (3, 14):
    from concurrent.futures.thread import WorkerContext as ThreadWorkerContext

    class WorkerContext(ThreadWorkerContext):
        @overload
        @classmethod
        def prepare(
            cls, initializer: Callable[[Unpack[_Ts]], object], initargs: tuple[Unpack[_Ts]], shared: Mapping[str, object]
        ) -> tuple[Callable[[], Self], _ResolveTaskFunc[_P, _R]]: ...
        @overload
        @classmethod
        def prepare(
            cls, initializer: Callable[[], object], initargs: tuple[()], shared: Mapping[str, object]
        ) -> tuple[Callable[[], Self], _ResolveTaskFunc[_P, _R]]: ...
        def __init__(self, initdata: _Task, shared: Mapping[str, object] | None = None) -> None: ...

class BrokenInterpreterPool(BrokenExecutor): ...

class InterpreterPoolExecutor(ThreadPoolExecutor):
    BROKEN: Final[type[BrokenInterpreterPool]]

    @overload
    def __init__(
        self,
        max_workers: int | None = None,
        thread_name_prefix: str = "",
        initializer: Callable[[], object] | None = None,
        initargs: tuple[()] = (),
        shared: Mapping[str, object] | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        max_workers: int | None = None,
        thread_name_prefix: str = "",
        *,
        initializer: Callable[[Unpack[_Ts]], object],
        initargs: tuple[Unpack[_Ts]],
        shared: Mapping[str, object] | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        max_workers: int | None,
        thread_name_prefix: str,
        initializer: Callable[[Unpack[_Ts]], object],
        initargs: tuple[Unpack[_Ts]],
        shared: Mapping[str, object] | None = None,
    ) -> None: ...
