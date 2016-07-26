# Stubs for contextlib (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from typing import Callable, Generic, Iterator, TypeVar

class ContextDecorator:
    def __call__(self, func): ...

class _GeneratorContextManager(ContextDecorator):
    gen = ...  # type: Any
    __doc__ = ...  # type: Any
    def __init__(self, func, *args, **kwds) -> None: ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback): ...

def contextmanager(func): ...

class closing:
    thing = ...  # type: Any
    def __init__(self, thing) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *exc_info): ...

class redirect_stdout:
    def __init__(self, new_target) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exctype, excinst, exctb): ...

class suppress:
    def __init__(self, *exceptions) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exctype, excinst, exctb): ...

class ExitStack:
    def __init__(self) -> None: ...
    def pop_all(self): ...
    def push(self, exit): ...
    def callback(self, callback, *args, **kwds): ...
    def enter_context(self, cm): ...
    def close(self): ...
    def __enter__(self): ...
    def __exit__(self, *exc_details): ...


#_T = TypeVar('_T')
#
#class ContextManager(Generic[_T]):
#    def __enter__(self) -> _T: ...
#    def __exit__(self, *exc_info) -> None: ...
#
## TODO this doesn't capture the relationship that the returned function's args are the same as func's.
#def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., ContextManager[_T]]: ...
#
#class closing(ContextManager[_T], Generic[_T]):
#    def __init__(self, thing: _T) -> None: ...
