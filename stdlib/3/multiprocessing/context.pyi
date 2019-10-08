# Stubs for multiprocessing.context

from logging import Logger
import multiprocessing
from multiprocessing import synchronize
from multiprocessing import queues
import sys
from typing import Any, Callable, Iterable, Optional, List, Mapping, Sequence, Type, Union

_LockLike = Union[synchronize.Lock, synchronize.RLock]

class ProcessError(Exception): ...

class BufferTooShort(ProcessError): ...

class TimeoutError(ProcessError): ...

class AuthenticationError(ProcessError): ...

class BaseContext(object):
    ProcessError: Type[Exception]
    BufferTooShort: Type[Exception]
    TimeoutError: Type[Exception]
    AuthenticationError: Type[Exception]

    # N.B. The methods below are applied at runtime to generate
    # multiprocessing.*, so the signatures should be identical (modulo self).

    @staticmethod
    def current_process() -> multiprocessing.Process: ...
    @staticmethod
    def active_children() -> List[multiprocessing.Process]: ...
    def cpu_count(self) -> int: ...
    # TODO: change return to SyncManager once a stub exists in multiprocessing.managers
    def Manager(self) -> Any: ...
    # TODO: change return to Pipe once a stub exists in multiprocessing.connection
    def Pipe(self, duplex: bool) -> Any: ...

    def Barrier(self,
                parties: int,
                action: Optional[Callable[..., Any]] = ...,
                timeout: Optional[float] = ...) -> synchronize.Barrier: ...
    def BoundedSemaphore(self,
                         value: int = ...) -> synchronize.BoundedSemaphore: ...
    def Condition(self,
                  lock: Optional[_LockLike] = ...) -> synchronize.Condition: ...
    def Event(self, lock: Optional[_LockLike] = ...) -> synchronize.Event: ...
    def Lock(self) -> synchronize.Lock: ...
    def RLock(self) -> synchronize.RLock: ...
    def Semaphore(self, value: int = ...) -> synchronize.Semaphore: ...

    def Queue(self, maxsize: int = ...) -> queues.Queue[Any]: ...
    def JoinableQueue(self, maxsize: int = ...) -> queues.JoinableQueue[Any]: ...
    def SimpleQueue(self) -> queues.SimpleQueue[Any]: ...
    def Pool(
        self,
        processes: Optional[int] = ...,
        initializer: Optional[Callable[..., Any]] = ...,
        initargs: Iterable[Any] = ...,
        maxtasksperchild: Optional[int] = ...
    ) -> multiprocessing.pool.Pool: ...
    def Process(
        self,
        group: Any = ...,
        target: Optional[Callable[..., Any]] = ...,
        name: Optional[str] = ...,
        args: Iterable[Any] = ...,
        kwargs: Mapping[Any, Any] = ...,
        *,
        daemon: Optional[bool] = ...
    ) -> multiprocessing.Process: ...
    # TODO: typecode_or_type param is a ctype with a base class of _SimpleCData or array.typecode Need to figure out
    # how to handle the ctype
    # TODO: change return to RawValue once a stub exists in multiprocessing.sharedctypes
    def RawValue(self, typecode_or_type: Any, *args: Any) -> Any: ...
    # TODO: typecode_or_type param is a ctype with a base class of _SimpleCData or array.typecode Need to figure out
    # how to handle the ctype
    # TODO: change return to RawArray once a stub exists in multiprocessing.sharedctypes
    def RawArray(self, typecode_or_type: Any, size_or_initializer: Union[int, Sequence[Any]]) -> Any: ...
    # TODO: typecode_or_type param is a ctype with a base class of _SimpleCData or array.typecode Need to figure out
    # how to handle the ctype
    # TODO: change return to Value once a stub exists in multiprocessing.sharedctypes
    def Value(
        self,
        typecode_or_type: Any,
        *args: Any,
        lock: bool = ...
    ) -> Any: ...
    # TODO: typecode_or_type param is a ctype with a base class of _SimpleCData or array.typecode Need to figure out
    # how to handle the ctype
    # TODO: change return to Array once a stub exists in multiprocessing.sharedctypes
    def Array(
        self,
        typecode_or_type: Any,
        size_or_initializer: Union[int, Sequence[Any]],
        *,
        lock: bool = ...
    ) -> Any: ...
    def freeze_support(self) -> None: ...
    def get_logger(self) -> Logger: ...
    def log_to_stderr(self, level: Optional[str] = ...) -> Logger: ...
    def allow_connection_pickling(self) -> None: ...
    def set_executable(self, executable: str) -> None: ...
    def set_forkserver_preload(self, module_names: List[str]) -> None: ...
    def get_context(self, method: Optional[str] = ...) -> BaseContext: ...
    def get_start_method(self, allow_none: bool = ...) -> str: ...
    def set_start_method(self, method: Optional[str] = ...) -> None: ...
    @property
    def reducer(self) -> str: ...
    @reducer.setter
    def reducer(self, reduction: str) -> None: ...
    def _check_available(self) -> None: ...

class Process(object):
    _start_method: Optional[str]
    @staticmethod
    # TODO: type should be BaseProcess once a stub in multiprocessing.process exists
    def _Popen(process_obj: Any) -> DefaultContext: ...

class DefaultContext(object):
    Process: Type[multiprocessing.Process]

    def __init__(self, context: BaseContext) -> None: ...
    def get_context(self, method: Optional[str] = ...) -> BaseContext: ...
    def set_start_method(self, method: str, force: bool = ...) -> None: ...
    def get_start_method(self, allow_none: bool = ...) -> str: ...
    def get_all_start_methods(self) -> List[str]: ...

if sys.platform != 'win32':
    # TODO: type should be BaseProcess once a stub in multiprocessing.process exists
    class ForkProcess(Any):  # type: ignore
        _start_method: str
        @staticmethod
        def _Popen(process_obj: Any) -> Any: ...

    # TODO: type should be BaseProcess once a stub in multiprocessing.process exists
    class SpawnProcess(Any):  # type: ignore
        _start_method: str
        @staticmethod
        def _Popen(process_obj: Any) -> SpawnProcess: ...

    # TODO: type should be BaseProcess once a stub in multiprocessing.process exists
    class ForkServerProcess(Any):  # type: ignore
        _start_method: str
        @staticmethod
        def _Popen(process_obj: Any) -> Any: ...

    class ForkContext(BaseContext):
        _name: str
        Process: Type[ForkProcess]

    class SpawnContext(BaseContext):
        _name: str
        Process: Type[SpawnProcess]

    class ForkServerContext(BaseContext):
        _name: str
        Process: Type[ForkServerProcess]
else:
    # TODO: type should be BaseProcess once a stub in multiprocessing.process exists
    class SpawnProcess(Any):  # type: ignore
        _start_method: str
        @staticmethod
        # TODO: type should be BaseProcess once a stub in multiprocessing.process exists
        def _Popen(process_obj: Process) -> Any: ...

    class SpawnContext(BaseContext):
        _name: str
        Process: Type[SpawnProcess]

def _force_start_method(method: str) -> None: ...
# TODO: type should be BaseProcess once a stub in multiprocessing.process exists
def get_spawning_popen() -> Optional[Any]: ...
# TODO: type should be BaseProcess once a stub in multiprocessing.process exists
def set_spawning_popen(popen: Any) -> None: ...
def assert_spawning(obj: Any) -> None: ...
