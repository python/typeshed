from collections.abc import Mapping
from concurrent.futures import BrokenExecutor, ThreadPoolExecutor
from typing import Callable, Final, Self, overload
from typing_extensions import ParamSpec, TypeVar, TypeVarTuple, Unpack

import thread
from _interpreters import InterpreterError
from thread import _ResolveTaskFunc, _Task

_Ts = TypeVarTuple("_Ts")
_P = ParamSpec("_P")
_R = TypeVar("_R")

class ExecutionFailed(InterpreterError): ...

UNBOUND: Final = 2

class WorkerContext(thread.WorkerContext):
    @overload
    @classmethod
    def prepare(
        cls,
        initializer: Callable[[Unpack[_Ts]], object],
        initargs: tuple[Unpack[_Ts]],
        shared: Mapping[str, object],
    ) -> tuple[Callable[[], Self], _ResolveTaskFunc[_P, _R]]: ...
    @overload
    @classmethod
    def prepare(
        cls,
        initializer: Callable[[], object],
        initargs: tuple[()],
        shared: Mapping[str, object],
    ) -> tuple[Callable[[], Self], _ResolveTaskFunc[_P, _R]]: ...
    def __init__(
        self,
        initdata: _Task[_P, _R],
        shared: Mapping[str, object] | None = None,
    ) -> None: ...

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
