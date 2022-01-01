import queue
import sys
import threading
from contextlib import AbstractContextManager
from typing import Any, AnyStr, Callable, Generic, Iterable, Mapping, Sequence, TypeVar

from .connection import Connection
from .context import BaseContext

if sys.version_info >= (3, 8):
    from .shared_memory import _SLT, ShareableList, SharedMemory

    _SharedMemory = SharedMemory
    _ShareableList = ShareableList

if sys.version_info >= (3, 9):
    from types import GenericAlias

_T = TypeVar("_T")
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

class Namespace:
    def __init__(self, **kwds: Any) -> None: ...
    def __getattr__(self, __name: str) -> Any: ...
    def __setattr__(self, __name: str, __value: Any) -> None: ...

_Namespace = Namespace

class Token:
    typeid: str | bytes | None
    address: tuple[str | bytes, int]
    id: str | bytes | int | None
    def __init__(self, typeid: bytes | str | None, address: tuple[str | bytes, int], id: str | bytes | int | None) -> None: ...
    def __repr__(self) -> str: ...
    def __getstate__(self) -> tuple[str | bytes | None, tuple[str | bytes, int], str | bytes | int | None]: ...
    def __setstate__(self, state: tuple[str | bytes | None, tuple[str | bytes, int], str | bytes | int | None]) -> None: ...

class BaseProxy:
    _address_to_local: dict[Any, Any]
    _mutex: Any
    def __init__(
        self,
        token: Any,
        serializer: str,
        manager: Any = ...,
        authkey: AnyStr | None = ...,
        exposed: Any = ...,
        incref: bool = ...,
        manager_owned: bool = ...,
    ) -> None: ...
    def __deepcopy__(self, memo: Any | None) -> Any: ...
    def _callmethod(self, methodname: str, args: tuple[Any, ...] = ..., kwds: dict[Any, Any] = ...) -> None: ...
    def _getvalue(self) -> Any: ...
    def __reduce__(self) -> tuple[Any, tuple[Any, Any, str, dict[Any, Any]]]: ...

class ValueProxy(BaseProxy, Generic[_T]):
    def get(self) -> _T: ...
    def set(self, value: _T) -> None: ...
    value: _T
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...

# Returned by BaseManager.get_server()
class Server:
    address: Any
    def __init__(
        self, registry: dict[str, tuple[Callable[..., Any], Any, Any, Any]], address: Any, authkey: bytes, serializer: str
    ) -> None: ...
    def serve_forever(self) -> None: ...
    def accept_connection(self, c: Connection, name: str) -> None: ...

class BaseManager(AbstractContextManager[BaseManager]):
    def __init__(
        self, address: Any | None = ..., authkey: bytes | None = ..., serializer: str = ..., ctx: BaseContext | None = ...
    ) -> None: ...
    def get_server(self) -> Server: ...
    def connect(self) -> None: ...
    def start(self, initializer: Callable[..., Any] | None = ..., initargs: Iterable[Any] = ...) -> None: ...
    def shutdown(self) -> None: ...  # only available after start() was called
    def join(self, timeout: float | None = ...) -> None: ...  # undocumented
    @property
    def address(self) -> Any: ...
    @classmethod
    def register(
        cls,
        typeid: str,
        callable: Callable[..., Any] | None = ...,
        proxytype: Any = ...,
        exposed: Sequence[str] | None = ...,
        method_to_typeid: Mapping[str, str] | None = ...,
        create_method: bool = ...,
    ) -> None: ...

# Conflicts with method names
_dict = dict
_list = list

class SyncManager(BaseManager, AbstractContextManager[SyncManager]):
    def BoundedSemaphore(self, value: Any = ...) -> threading.BoundedSemaphore: ...
    def Condition(self, lock: Any = ...) -> threading.Condition: ...
    def Event(self) -> threading.Event: ...
    def Lock(self) -> threading.Lock: ...
    def Namespace(self) -> _Namespace: ...
    def Queue(self, maxsize: int = ...) -> queue.Queue[Any]: ...
    def RLock(self) -> threading.RLock: ...
    def Semaphore(self, value: Any = ...) -> threading.Semaphore: ...
    def Array(self, typecode: Any, sequence: Sequence[_T]) -> Sequence[_T]: ...
    def Value(self, typecode: Any, value: _T) -> ValueProxy[_T]: ...
    def dict(self, sequence: Mapping[_KT, _VT] = ...) -> _dict[_KT, _VT]: ...
    def list(self, sequence: Sequence[_T] = ...) -> _list[_T]: ...

class RemoteError(Exception): ...

if sys.version_info >= (3, 8):
    class SharedMemoryServer(Server): ...
    class SharedMemoryManager(BaseManager):
        def get_server(self) -> SharedMemoryServer: ...
        def SharedMemory(self, size: int) -> _SharedMemory: ...
        def ShareableList(self, sequence: Iterable[_SLT] | None) -> _ShareableList[_SLT]: ...
