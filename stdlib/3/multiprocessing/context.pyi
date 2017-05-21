# Stubs for multiprocessing.context

from logging import Logger
import multiprocessing
import sys
from typing import Any, Callable, Optional, List, Sequence, Tuple, Type, Union

class ProcessError(Exception): ...

class BufferTooShort(ProcessError): ...

class TimeoutError(ProcessError): ...

class AuthenticationError(ProcessError): ...

class BaseContext(object):
    ProcessError = ...  # type: Type[Exception]
    BufferTooShort = ...  # type: Type[Exception]
    TimeoutError = ...  # type: Type[Exception]
    AuthenticationError = ...  # type: Type[Exception]

    @staticmethod
    def current_process() -> multiprocessing.Process: ...
    @staticmethod
    def active_children() -> List[multiprocessing.Process]: ...
    def cpu_count(self) -> int: ...
    # TODO: change return to SyncManager once a stub exists in multiprocessing.managers
    def Manager(self) -> Any: ...
    # TODO: change return to Pipe once a stub exists in multiprocessing.connection
    def Pipe(self, duplex: bool) -> Any: ...
    # TODO: change return to Lock once a stub exists in multiprocessing.synchronize
    def Lock(self) -> Any: ...
    # TODO: change return to RLock once a stub exists in multiprocessing.synchronize
    def RLock(self) -> Any: ...
    # TODO: change lock param to Optional[Union[Lock, RLock]] when stubs exists in multiprocessing.synchronize
    # TODO: change return to Condition once a stub exists in multiprocessing.synchronize
    def Condition(self, lock: Optional[Any] = ...) -> Any: ...
    # TODO: change return to Semaphore once a stub exists in multiprocessing.synchronize
    def Semaphore(self, value: int = ...) -> Any: ...
    # TODO: change return to BoundedSemaphore once a stub exists in multiprocessing.synchronize
    def BoundedSemaphore(self, value: int = ...) -> Any: ...
    # TODO: change return to Event once a stub exists in multiprocessing.synchronize
    def Event(self) -> Any: ...
    # TODO: change return to Barrier once a stub exists in multiprocessing.synchronize
    def Barrier(self, parties: int, action: Optional[Callable[..., Any]] = ..., timeout: Optional[int] = ...) -> Any: ...
    # TODO: change return to Queue once a stub exists in multiprocessing.queues
    def Queue(self, maxsize: int = ...) -> Any: ...
    # TODO: change return to Queue once a stub exists in multiprocessing.queues
    def JoinableQueue(self, maxsize: int = ...) -> Any: ...
    # TODO: change return to SimpleQueue once a stub exists in multiprocessing.queues
    def SimpleQueue(self) -> Any: ...
    # TODO: change return to Pool once a stub exists in multiprocessing.pool
    def Pool(
        self,
        processes: Optional[int] = ...,
        initializer: Optional[Callable[..., Any]] = ...,
        initargs: Tuple = ...,
        maxtasksperchild: Optional[int] = ...
    ) -> Any: ...
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
    Process = ...  # type: Type[multiprocessing.Process]

    def __init__(self, context: BaseContext) -> None: ...
    def get_context(self, method: Optional[str] = ...) -> BaseContext: ...
    def set_start_method(self, method: str, force: bool = ...) -> None: ...
    def get_start_method(self, allow_none: bool = ...) -> str: ...
    def get_all_start_methods(self) -> List[str]: ...

if sys.platform != 'win32':
    # TODO: type should be BaseProcess once a stub in multiprocessing.process exists
    class ForkProcess:
        _start_method: str
        @staticmethod
        def _Popen(process_obj: Any) -> Any: ...

    # TODO: type should be BaseProcess once a stub in multiprocessing.process exists
    class SpawnProcess:
        _start_method: str
        @staticmethod
        def _Popen(process_obj: Any) -> SpawnProcess: ...

    # TODO: type should be BaseProcess once a stub in multiprocessing.process exists
    class ForkServerProcess:
        _start_method: str
        @staticmethod
        def _Popen(process_obj: Any) -> Any: ...

    class ForkContext(BaseContext):
        _name: str
        Process = ...  # type: Type[ForkProcess]

    class SpawnContext(BaseContext):
        _name: str
        Process = ...  # type: Type[SpawnProcess]

    class ForkServerContext(BaseContext):
        _name: str
        Process = ...  # type: Type[ForkServerProcess]
else:
    # TODO: type should be BaseProcess once a stub in multiprocessing.process exists
    class SpawnProcess:
        _start_method: str
        @staticmethod
        # TODO: type should be BaseProcess once a stub in multiprocessing.process exists
        def _Popen(process_obj: Process) -> Any: ...

    class SpawnContext(BaseContext):
        _name: str
        Process = ...  # type: Type[SpawnProcess]

def _force_start_method(method: str) -> None: ...
# TODO: type should be BaseProcess once a stub in multiprocessing.process exists
def get_spawning_popen() -> Optional[Any]: ...
# TODO: type should be BaseProcess once a stub in multiprocessing.process exists
def set_spawning_popen(popen: Any) -> None: ...
def assert_spawning(obj: Any) -> None: ...
