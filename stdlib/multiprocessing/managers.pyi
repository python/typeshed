import queue
import sys
import threading
from _typeshed import SupportsKeysAndGetItem, SupportsRichComparison, SupportsRichComparisonT
from collections.abc import Callable, Iterable, Iterator, Mapping, MutableMapping, MutableSequence, Sequence
from types import TracebackType
from typing import Any, AnyStr, ClassVar, Generic, SupportsIndex, TypeVar, overload
from typing_extensions import Self, TypeAlias

from . import pool
from .connection import Connection, _Address
from .context import BaseContext
from .shared_memory import _SLT, ShareableList as _ShareableList, SharedMemory as _SharedMemory
from .util import Finalize as _Finalize

__all__ = ["BaseManager", "SyncManager", "BaseProxy", "Token", "SharedMemoryManager"]

if sys.version_info >= (3, 9):
    from types import GenericAlias

_T = TypeVar("_T")
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

class Namespace:
    def __init__(self, **kwds: Any) -> None: ...
    def __getattr__(self, name: str, /) -> Any: ...
    def __setattr__(self, name: str, value: Any, /) -> None: ...

_Namespace: TypeAlias = Namespace

class Token:
    typeid: str | bytes | None
    address: _Address | None
    id: str | bytes | int | None
    def __init__(self, typeid: bytes | str | None, address: _Address | None, id: str | bytes | int | None) -> None: ...
    def __getstate__(self) -> tuple[str | bytes | None, tuple[str | bytes, int], str | bytes | int | None]: ...
    def __setstate__(self, state: tuple[str | bytes | None, tuple[str | bytes, int], str | bytes | int | None]) -> None: ...

class BaseProxy:
    _address_to_local: dict[_Address, Any]
    _mutex: Any
    def __init__(
        self,
        token: Any,
        serializer: str,
        manager: Any = None,
        authkey: AnyStr | None = None,
        exposed: Any = None,
        incref: bool = True,
        manager_owned: bool = False,
    ) -> None: ...
    def __deepcopy__(self, memo: Any | None) -> Any: ...
    def _callmethod(self, methodname: str, args: tuple[Any, ...] = (), kwds: dict[Any, Any] = {}) -> None: ...
    def _getvalue(self) -> Any: ...
    def __reduce__(self) -> tuple[Any, tuple[Any, Any, str, dict[Any, Any]]]: ...

class ValueProxy(BaseProxy, Generic[_T]):
    def get(self) -> _T: ...
    def set(self, value: _T) -> None: ...
    value: _T
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...

if sys.version_info >= (3, 13):
    class _BaseDictProxy(BaseProxy, MutableMapping[_KT, _VT]):
        __builtins__: ClassVar[dict[str, Any]]
        def __len__(self) -> int: ...
        def __getitem__(self, key: _KT, /) -> _VT: ...
        def __setitem__(self, key: _KT, value: _VT, /) -> None: ...
        def __delitem__(self, key: _KT, /) -> None: ...
        def __iter__(self) -> Iterator[_KT]: ...
        def copy(self) -> dict[_KT, _VT]: ...
        @overload  # type: ignore[override]
        def get(self, key: _KT, /) -> _VT | None: ...
        @overload
        def get(self, key: _KT, default: _VT, /) -> _VT: ...
        @overload
        def get(self, key: _KT, default: _T, /) -> _VT | _T: ...
        @overload
        def pop(self, key: _KT, /) -> _VT: ...
        @overload
        def pop(self, key: _KT, default: _VT, /) -> _VT: ...
        @overload
        def pop(self, key: _KT, default: _T, /) -> _VT | _T: ...
        def keys(self) -> list[_KT]: ...  # type: ignore[override]
        def items(self) -> list[tuple[_KT, _VT]]: ...  # type: ignore[override]
        def values(self) -> list[_VT]: ...  # type: ignore[override]

    class DictProxy(_BaseDictProxy[_KT, _VT]):
        def __class_getitem__(cls, args: Any, /) -> GenericAlias: ...

else:
    class DictProxy(BaseProxy, MutableMapping[_KT, _VT]):
        __builtins__: ClassVar[dict[str, Any]]
        def __len__(self) -> int: ...
        def __getitem__(self, key: _KT, /) -> _VT: ...
        def __setitem__(self, key: _KT, value: _VT, /) -> None: ...
        def __delitem__(self, key: _KT, /) -> None: ...
        def __iter__(self) -> Iterator[_KT]: ...
        def copy(self) -> dict[_KT, _VT]: ...
        @overload  # type: ignore[override]
        def get(self, key: _KT, /) -> _VT | None: ...
        @overload
        def get(self, key: _KT, default: _VT, /) -> _VT: ...
        @overload
        def get(self, key: _KT, default: _T, /) -> _VT | _T: ...
        @overload
        def pop(self, key: _KT, /) -> _VT: ...
        @overload
        def pop(self, key: _KT, default: _VT, /) -> _VT: ...
        @overload
        def pop(self, key: _KT, default: _T, /) -> _VT | _T: ...
        def keys(self) -> list[_KT]: ...  # type: ignore[override]
        def items(self) -> list[tuple[_KT, _VT]]: ...  # type: ignore[override]
        def values(self) -> list[_VT]: ...  # type: ignore[override]

class BaseListProxy(BaseProxy, MutableSequence[_T]):
    __builtins__: ClassVar[dict[str, Any]]
    def __len__(self) -> int: ...
    def __add__(self, x: list[_T], /) -> list[_T]: ...
    def __delitem__(self, i: SupportsIndex | slice, /) -> None: ...
    @overload
    def __getitem__(self, i: SupportsIndex, /) -> _T: ...
    @overload
    def __getitem__(self, s: slice, /) -> list[_T]: ...
    @overload
    def __setitem__(self, i: SupportsIndex, o: _T, /) -> None: ...
    @overload
    def __setitem__(self, s: slice, o: Iterable[_T], /) -> None: ...
    def __mul__(self, n: SupportsIndex, /) -> list[_T]: ...
    def __rmul__(self, n: SupportsIndex, /) -> list[_T]: ...
    def __reversed__(self) -> Iterator[_T]: ...
    def append(self, object: _T, /) -> None: ...
    def extend(self, iterable: Iterable[_T], /) -> None: ...
    def pop(self, index: SupportsIndex = ..., /) -> _T: ...
    def index(self, value: _T, start: SupportsIndex = ..., stop: SupportsIndex = ..., /) -> int: ...
    def count(self, value: _T, /) -> int: ...
    def insert(self, index: SupportsIndex, object: _T, /) -> None: ...
    def remove(self, value: _T, /) -> None: ...
    # Use BaseListProxy[SupportsRichComparisonT] for the first overload rather than [SupportsRichComparison]
    # to work around invariance
    @overload
    def sort(self: BaseListProxy[SupportsRichComparisonT], *, key: None = None, reverse: bool = ...) -> None: ...
    @overload
    def sort(self, *, key: Callable[[_T], SupportsRichComparison], reverse: bool = ...) -> None: ...

class ListProxy(BaseListProxy[_T]):
    def __iadd__(self, value: Iterable[_T], /) -> Self: ...  # type: ignore[override]
    def __imul__(self, value: SupportsIndex, /) -> Self: ...  # type: ignore[override]
    if sys.version_info >= (3, 13):
        def __class_getitem__(cls, args: Any, /) -> Any: ...

# Send is (kind, result)
# Receive is (id, methodname, args, kwds)
_ServerConnection: TypeAlias = Connection[tuple[str, Any], tuple[str, str, Iterable[Any], Mapping[str, Any]]]

# Returned by BaseManager.get_server()
class Server:
    address: _Address | None
    id_to_obj: dict[str, tuple[Any, set[str], dict[str, str]]]
    fallback_mapping: dict[str, Callable[[_ServerConnection, str, Any], Any]]
    public: list[str]
    # Registry values are (callable, exposed, method_to_typeid, proxytype)
    def __init__(
        self,
        registry: dict[str, tuple[Callable[..., Any], Iterable[str], dict[str, str], Any]],
        address: _Address | None,
        authkey: bytes,
        serializer: str,
    ) -> None: ...
    def serve_forever(self) -> None: ...
    def accepter(self) -> None: ...
    if sys.version_info >= (3, 10):
        def handle_request(self, conn: _ServerConnection) -> None: ...
    else:
        def handle_request(self, c: _ServerConnection) -> None: ...

    def serve_client(self, conn: _ServerConnection) -> None: ...
    def fallback_getvalue(self, conn: _ServerConnection, ident: str, obj: _T) -> _T: ...
    def fallback_str(self, conn: _ServerConnection, ident: str, obj: Any) -> str: ...
    def fallback_repr(self, conn: _ServerConnection, ident: str, obj: Any) -> str: ...
    def dummy(self, c: _ServerConnection) -> None: ...
    def debug_info(self, c: _ServerConnection) -> str: ...
    def number_of_objects(self, c: _ServerConnection) -> int: ...
    def shutdown(self, c: _ServerConnection) -> None: ...
    def create(self, c: _ServerConnection, typeid: str, /, *args: Any, **kwds: Any) -> tuple[str, tuple[str, ...]]: ...
    def get_methods(self, c: _ServerConnection, token: Token) -> set[str]: ...
    def accept_connection(self, c: _ServerConnection, name: str) -> None: ...
    def incref(self, c: _ServerConnection, ident: str) -> None: ...
    def decref(self, c: _ServerConnection, ident: str) -> None: ...

class BaseManager:
    if sys.version_info >= (3, 11):
        def __init__(
            self,
            address: _Address | None = None,
            authkey: bytes | None = None,
            serializer: str = "pickle",
            ctx: BaseContext | None = None,
            *,
            shutdown_timeout: float = 1.0,
        ) -> None: ...
    else:
        def __init__(
            self,
            address: _Address | None = None,
            authkey: bytes | None = None,
            serializer: str = "pickle",
            ctx: BaseContext | None = None,
        ) -> None: ...

    def get_server(self) -> Server: ...
    def connect(self) -> None: ...
    def start(self, initializer: Callable[..., object] | None = None, initargs: Iterable[Any] = ()) -> None: ...
    shutdown: _Finalize  # only available after start() was called
    def join(self, timeout: float | None = None) -> None: ...  # undocumented
    @property
    def address(self) -> _Address | None: ...
    @classmethod
    def register(
        cls,
        typeid: str,
        callable: Callable[..., object] | None = None,
        proxytype: Any = None,
        exposed: Sequence[str] | None = None,
        method_to_typeid: Mapping[str, str] | None = None,
        create_method: bool = True,
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...

class SyncManager(BaseManager):
    def Barrier(
        self, parties: int, action: Callable[[], None] | None = None, timeout: float | None = None
    ) -> threading.Barrier: ...
    def BoundedSemaphore(self, value: int = 1) -> threading.BoundedSemaphore: ...
    def Condition(self, lock: threading.Lock | threading._RLock | None = None) -> threading.Condition: ...
    def Event(self) -> threading.Event: ...
    def Lock(self) -> threading.Lock: ...
    def Namespace(self) -> _Namespace: ...
    def Pool(
        self,
        processes: int | None = None,
        initializer: Callable[..., object] | None = None,
        initargs: Iterable[Any] = (),
        maxtasksperchild: int | None = None,
        context: Any | None = None,
    ) -> pool.Pool: ...
    def Queue(self, maxsize: int = ...) -> queue.Queue[Any]: ...
    def JoinableQueue(self, maxsize: int = ...) -> queue.Queue[Any]: ...
    def RLock(self) -> threading.RLock: ...
    def Semaphore(self, value: int = 1) -> threading.Semaphore: ...
    def Array(self, typecode: Any, sequence: Sequence[_T]) -> Sequence[_T]: ...
    def Value(self, typecode: Any, value: _T) -> ValueProxy[_T]: ...
    # Overloads are copied from builtins.dict.__init__
    @overload
    def dict(self) -> DictProxy[Any, Any]: ...
    @overload
    def dict(self, **kwargs: _VT) -> DictProxy[str, _VT]: ...
    @overload
    def dict(self, map: SupportsKeysAndGetItem[_KT, _VT], /) -> DictProxy[_KT, _VT]: ...
    @overload
    def dict(self, map: SupportsKeysAndGetItem[str, _VT], /, **kwargs: _VT) -> DictProxy[str, _VT]: ...
    @overload
    def dict(self, iterable: Iterable[tuple[_KT, _VT]], /) -> DictProxy[_KT, _VT]: ...
    @overload
    def dict(self, iterable: Iterable[tuple[str, _VT]], /, **kwargs: _VT) -> DictProxy[str, _VT]: ...
    @overload
    def dict(self, iterable: Iterable[list[str]], /) -> DictProxy[str, str]: ...
    @overload
    def dict(self, iterable: Iterable[list[bytes]], /) -> DictProxy[bytes, bytes]: ...
    @overload
    def list(self, sequence: Sequence[_T], /) -> ListProxy[_T]: ...
    @overload
    def list(self) -> ListProxy[Any]: ...

class RemoteError(Exception): ...

class SharedMemoryServer(Server):
    def track_segment(self, c: _ServerConnection, segment_name: str) -> None: ...
    def release_segment(self, c: _ServerConnection, segment_name: str) -> None: ...
    def list_segments(self, c: _ServerConnection) -> list[str]: ...

class SharedMemoryManager(BaseManager):
    def get_server(self) -> SharedMemoryServer: ...
    def SharedMemory(self, size: int) -> _SharedMemory: ...
    def ShareableList(self, sequence: Iterable[_SLT] | None) -> _ShareableList[_SLT]: ...
    def __del__(self) -> None: ...
