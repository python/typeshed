# Stubs for multiprocessing.pool

# NOTE: These are incomplete!

from typing import (
    Any, Callable, ContextManager, Iterable, Mapping, Optional, Dict, List,
)

class AsyncResult():
    def get(self, timeout: float = ...) -> Any: ...
    def wait(self, timeout: float = ...) -> None: ...
    def ready(self) -> bool: ...
    def successful(self) -> bool: ...

class ThreadPool(ContextManager[ThreadPool]):
    def __init__(self, processes: Optional[int] = None,
                 initializer: Optional[Callable[..., Any]] = None,
                 initargs: Iterable[Any] = ...) -> None: ...
    def apply(self,
              func: Callable[..., Any],
              args: Iterable[Any] = ...,
              kwds: Dict[str, Any] = ...) -> Any: ...
    def apply_async(self,
                func: Callable[..., Any],
                args: Iterable[Any] = ...,
                kwds: Dict[str, Any] = ...,
                callback: Optional[Callable[..., None]] = None,
                error_callback: Optional[Callable[[BaseException], None]] = None) -> AsyncResult: ...
    def map(self,
            func: Callable[..., Any],
            iterable: Iterable[Any] = ...,
            chunksize: Optional[int] = None) -> List[Any]: ...
    def map_async(self, func: Callable[..., Any],
                  iterable: Iterable[Any] = ...,
                  chunksize: Optional[Optional[int]] = None,
                  callback: Optional[Callable[..., None]] = None,
                  error_callback: Optional[Callable[[BaseException], None]] = None) -> AsyncResult: ...
    def imap(self,
             func: Callable[..., Any],
             iterable: Iterable[Any] = ...,
             chunksize: Optional[int] = None) -> Iterable[Any]: ...
    def imap_unordered(self,
                       func: Callable[..., Any],
                       iterable: Iterable[Any] = ...,
                       chunksize: Optional[int] = None) -> Iterable[Any]: ...
    def starmap(self,
                func: Callable[..., Any],
                iterable: Iterable[Iterable[Any]] = ...,
                chunksize: Optional[int] = None) -> List[Any]: ...
    def starmap_async(self,
                      func: Callable[..., Any],
                      iterable: Iterable[Iterable[Any]] = ...,
                      chunksize: Optional[int] = None,
                      callback: Optional[Callable[..., None]] = None,
                      error_callback: Optional[Callable[[BaseException], None]] = None) -> AsyncResult: ...
    def close(self) -> None: ...
    def terminate(self) -> None: ...
    def join(self) -> None: ...
