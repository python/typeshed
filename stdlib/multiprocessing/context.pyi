import ctypes
import multiprocessing
import sys
from collections.abc import Callable, Iterable, Sequence
from ctypes import _CData
from logging import Logger
from multiprocessing import queues, synchronize
from multiprocessing.pool import Pool as _Pool
from multiprocessing.process import BaseProcess
from multiprocessing.sharedctypes import SynchronizedArray, SynchronizedBase
from typing import Any, TypeVar, Union, overload
from typing_extensions import Literal

_LockLike = Union[synchronize.Lock, synchronize.RLock]
_CT = TypeVar("_CT", bound=_CData)

class ProcessError(Exception): ...
class BufferTooShort(ProcessError): ...
class TimeoutError(ProcessError): ...
class AuthenticationError(ProcessError): ...

class BaseContext(object):
    Process: type[BaseProcess]
    ProcessError: type[Exception]
    BufferTooShort: type[Exception]
    TimeoutError: type[Exception]
    AuthenticationError: type[Exception]

    # N.B. The methods below are applied at runtime to generate
    # multiprocessing.*, so the signatures should be identical (modulo self).
    @staticmethod
    def current_process() -> BaseProcess: ...
    if sys.version_info >= (3, 8):
        @staticmethod
        def parent_process() -> BaseProcess | None: ...
    @staticmethod
    def active_children() -> list[BaseProcess]: ...
    def cpu_count(self) -> int: ...
    # TODO: change return to SyncManager once a stub exists in multiprocessing.managers
    def Manager(self) -> Any: ...
    # TODO: change return to Pipe once a stub exists in multiprocessing.connection
    def Pipe(self, duplex: bool = ...) -> Any: ...
    def Barrier(
        self, parties: int, action: Callable[..., Any] | None = ..., timeout: float | None = ...
    ) -> synchronize.Barrier: ...
    def BoundedSemaphore(self, value: int = ...) -> synchronize.BoundedSemaphore: ...
    def Condition(self, lock: _LockLike | None = ...) -> synchronize.Condition: ...
    def Event(self) -> synchronize.Event: ...
    def Lock(self) -> synchronize.Lock: ...
    def RLock(self) -> synchronize.RLock: ...
    def Semaphore(self, value: int = ...) -> synchronize.Semaphore: ...
    def Queue(self, maxsize: int = ...) -> queues.Queue[Any]: ...
    def JoinableQueue(self, maxsize: int = ...) -> queues.JoinableQueue[Any]: ...
    def SimpleQueue(self) -> queues.SimpleQueue[Any]: ...
    def Pool(
        self,
        processes: int | None = ...,
        initializer: Callable[..., Any] | None = ...,
        initargs: Iterable[Any] = ...,
        maxtasksperchild: int | None = ...,
    ) -> _Pool: ...
    @overload
    def RawValue(self, typecode_or_type: type[_CT], *args: Any) -> _CT: ...
    @overload
    def RawValue(self, typecode_or_type: str, *args: Any) -> Any: ...
    @overload
    def RawArray(self, typecode_or_type: type[_CT], size_or_initializer: int | Sequence[Any]) -> ctypes.Array[_CT]: ...
    @overload
    def RawArray(self, typecode_or_type: str, size_or_initializer: int | Sequence[Any]) -> Any: ...
    @overload
    def Value(self, typecode_or_type: type[_CT], *args: Any, lock: Literal[False]) -> _CT: ...
    @overload
    def Value(self, typecode_or_type: type[_CT], *args: Any, lock: Literal[True] | _LockLike) -> SynchronizedBase[_CT]: ...
    @overload
    def Value(self, typecode_or_type: str, *args: Any, lock: Literal[True] | _LockLike) -> SynchronizedBase[Any]: ...
    @overload
    def Value(self, typecode_or_type: str | type[_CData], *args: Any, lock: bool | _LockLike = ...) -> Any: ...
    @overload
    def Array(self, typecode_or_type: type[_CT], size_or_initializer: int | Sequence[Any], *, lock: Literal[False]) -> _CT: ...
    @overload
    def Array(
        self, typecode_or_type: type[_CT], size_or_initializer: int | Sequence[Any], *, lock: Literal[True] | _LockLike
    ) -> SynchronizedArray[_CT]: ...
    @overload
    def Array(
        self, typecode_or_type: str, size_or_initializer: int | Sequence[Any], *, lock: Literal[True] | _LockLike
    ) -> SynchronizedArray[Any]: ...
    @overload
    def Array(
        self, typecode_or_type: str | type[_CData], size_or_initializer: int | Sequence[Any], *, lock: bool | _LockLike = ...
    ) -> Any: ...
    def freeze_support(self) -> None: ...
    def get_logger(self) -> Logger: ...
    def log_to_stderr(self, level: str | None = ...) -> Logger: ...
    def allow_connection_pickling(self) -> None: ...
    def set_executable(self, executable: str) -> None: ...
    def set_forkserver_preload(self, module_names: list[str]) -> None: ...
    if sys.platform != "win32":
        @overload
        def get_context(self, method: None = ...) -> DefaultContext: ...
        @overload
        def get_context(self, method: Literal["spawn"]) -> SpawnContext: ...
        @overload
        def get_context(self, method: Literal["fork"]) -> ForkContext: ...
        @overload
        def get_context(self, method: Literal["forkserver"]) -> ForkServerContext: ...
        @overload
        def get_context(self, method: str) -> BaseContext: ...
    else:
        @overload
        def get_context(self, method: None = ...) -> DefaultContext: ...
        @overload
        def get_context(self, method: Literal["spawn"]) -> SpawnContext: ...
        @overload
        def get_context(self, method: str) -> BaseContext: ...
    def get_start_method(self, allow_none: bool = ...) -> str: ...
    def set_start_method(self, method: str | None, force: bool = ...) -> None: ...
    @property
    def reducer(self) -> str: ...
    @reducer.setter
    def reducer(self, reduction: str) -> None: ...
    def _check_available(self) -> None: ...

class Process(BaseProcess):
    _start_method: str | None
    @staticmethod
    def _Popen(process_obj: BaseProcess) -> DefaultContext: ...

class DefaultContext(BaseContext):
    Process: type[multiprocessing.Process]
    def __init__(self, context: BaseContext) -> None: ...
    def set_start_method(self, method: str | None, force: bool = ...) -> None: ...
    def get_start_method(self, allow_none: bool = ...) -> str: ...
    def get_all_start_methods(self) -> list[str]: ...

_default_context: DefaultContext

if sys.platform != "win32":
    class ForkProcess(BaseProcess):
        _start_method: str
        @staticmethod
        def _Popen(process_obj: BaseProcess) -> Any: ...
    class SpawnProcess(BaseProcess):
        _start_method: str
        @staticmethod
        def _Popen(process_obj: BaseProcess) -> SpawnProcess: ...
    class ForkServerProcess(BaseProcess):
        _start_method: str
        @staticmethod
        def _Popen(process_obj: BaseProcess) -> Any: ...
    class ForkContext(BaseContext):
        _name: str
        Process: type[ForkProcess]
    class SpawnContext(BaseContext):
        _name: str
        Process: type[SpawnProcess]
    class ForkServerContext(BaseContext):
        _name: str
        Process: type[ForkServerProcess]

else:
    class SpawnProcess(BaseProcess):
        _start_method: str
        @staticmethod
        def _Popen(process_obj: BaseProcess) -> Any: ...
    class SpawnContext(BaseContext):
        _name: str
        Process: type[SpawnProcess]

def _force_start_method(method: str) -> None: ...
def get_spawning_popen() -> Any | None: ...
def set_spawning_popen(popen: Any) -> None: ...
def assert_spawning(obj: Any) -> None: ...
