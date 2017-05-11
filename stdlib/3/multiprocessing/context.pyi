# Stubs for multiprocessing.context

# NOTE: These are incomplete!

from logging import Logger
from typing import Any, Callable, Optional, List, Sequence, Tuple, Union

class BaseContext(object):
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
    def Condition(self, lock: Optional[Any] = None) -> Any: ...

    # TODO: change return to Semaphore once a stub exists in multiprocessing.synchronize
    def Semaphore(self, value: Optional[int] = 1) -> Any: ...

    # TODO: change return to BoundedSemaphore once a stub exists in multiprocessing.synchronize
    def BoundedSemaphore(self, value: Optional[int] = 1) -> Any: ...

    # TODO: change return to Event once a stub exists in multiprocessing.synchronize
    def Event(self) -> Any: ...

    # TODO: change return to Barrier once a stub exists in multiprocessing.synchronize
    def Barrier(self, parties: int, action: Optional[Callable] = None, timeout: Optional[int] = None) -> Any: ...

    # TODO: change return to Queue once a stub exists in multiprocessing.queues
    def Event(self, maxsize: Optional[int] = 0) -> Any: ...

    # TODO: change return to Queue once a stub exists in multiprocessing.queues
    def JoinableQueue(self, maxsize: Optional[int] = 0) -> Any: ...

    # TODO: change return to SimpleQueue once a stub exists in multiprocessing.queues
    def SimpleQueue(self) -> Any: ...

    # TODO: change return to Pool once a stub exists in multiprocessing.pool
    def Pool(
        self,
        processes: Optional[int] = None,
        initializer: Optional[Callable] = None,
        initargs: Optional[Tuple] = (),
        maxtasksperchild: Optional[int] = None
    ) -> Any: ...

    # TODO: typecode_or_type param is a ctype with a base class of _SimpleCData or array.typecode Need to figure out
    # how to handle the ctype
    # TODO: change *args to type
    # TODO: change return to RawValue once a stub exists in multiprocessing.sharedctypes
    def RawValue(self, typecode_or_type: Any, *args: Any) -> Any: ...

    # TODO: typecode_or_type param is a ctype with a base class of _SimpleCData or array.typecode Need to figure out
    # how to handle the ctype
    # TODO: change return to RawArray once a stub exists in multiprocessing.sharedctypes
    def RawArray(self, typecode_or_type: Any, size_or_initializer: int) -> Any: ...

    # TODO: typecode_or_type param is a ctype with a base class of _SimpleCData or array.typecode Need to figure out
    # how to handle the ctype
    # TODO: change return to Value once a stub exists in multiprocessing.sharedctypes
    def Value(
        self,
        typecode_or_type: Any,
        *args: Any,
        lock: Optional[bool] = True
    ) -> Any: ...

    # TODO: typecode_or_type param is a ctype with a base class of _SimpleCData or array.typecode Need to figure out
    # how to handle the ctype
    # TODO: change return to Array once a stub exists in multiprocessing.sharedctypes
    def Array(
        self,
        typecode_or_type: Any,
        size_or_initializer: Union[int, Sequence],
        *,
        lock: Optional[bool] = True
    ) -> Any: ...

    def freeze_support(self) -> None: ...

    def get_logger(self) -> Logger: ...

    def log_to_stderr(self, level: Optional[str] = None) -> Logger: ...

    def allow_connection_pickling(self) -> None: ...

    def set_executable(self, executable: str) -> None: ...

    def set_forkserver_preload(self, module_names: List[str]) -> None: ...

    def get_context(self, method: Optional[str] = None) -> BaseContext: ...

    def get_start_method(self, allow_none: Optional[bool] = False) -> str: ...

    def set_start_method(self, method: Optional[str] = None) -> None: ...

    @property
    def reducer(self) -> str: ...

    @reducer.setter
    def reducer(self, reduction: str) -> None: ...

    def _check_available(self) -> None: ...








