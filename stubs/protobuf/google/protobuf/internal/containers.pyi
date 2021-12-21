from typing import (
    Any,
    Callable,
    Iterable,
    Iterator,
    List,
    Mapping as Mapping,
    MutableMapping as MutableMapping,
    Optional,
    Sequence,
    Text,
    TypeVar,
    Union,
    overload,
)
from typing_extensions import SupportsIndex

from google.protobuf.descriptor import Descriptor
from google.protobuf.internal.message_listener import MessageListener
from google.protobuf.internal.python_message import GeneratedProtocolMessageType
from google.protobuf.message import Message

_T = TypeVar("_T")
_K = TypeVar("_K", bound=Union[bool, int, Text])
_ScalarV = TypeVar("_ScalarV", bound=Union[bool, int, float, Text, bytes])
_MessageV = TypeVar("_MessageV", bound=Message)
_M = TypeVar("_M")

class BaseContainer(Sequence[_T]):
    def __init__(self, message_listener: MessageListener) -> None: ...
    def __len__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def sort(self, *, key: Optional[Callable[[_T], Any]] = ..., reverse: bool = ...) -> None: ...
    @overload
    def __getitem__(self, key: SupportsIndex) -> _T: ...
    @overload
    def __getitem__(self, key: slice) -> List[_T]: ...

class RepeatedScalarFieldContainer(BaseContainer[_ScalarV]):
    def __init__(self, message_listener: MessageListener, message_descriptor: Descriptor) -> None: ...
    def append(self, value: _ScalarV) -> None: ...
    def insert(self, key: int, value: _ScalarV) -> None: ...
    def extend(self, elem_seq: Optional[Iterable[_ScalarV]]) -> None: ...
    def MergeFrom(self: _M, other: _M) -> None: ...
    def remove(self, elem: _ScalarV) -> None: ...
    def pop(self, key: int = ...) -> _ScalarV: ...
    @overload
    def __setitem__(self, key: int, value: _ScalarV) -> None: ...
    @overload
    def __setitem__(self, key: slice, value: Iterable[_ScalarV]) -> None: ...
    def __getslice__(self, start: int, stop: int) -> List[_ScalarV]: ...
    def __setslice__(self, start: int, stop: int, values: Iterable[_ScalarV]) -> None: ...
    def __delitem__(self, key: Union[int, slice]) -> None: ...
    def __delslice__(self, start: int, stop: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...

class RepeatedCompositeFieldContainer(BaseContainer[_MessageV]):
    def __init__(self, message_listener: MessageListener, type_checker: Any) -> None: ...
    def add(self, **kwargs: Any) -> _MessageV: ...
    def append(self, value: _MessageV) -> None: ...
    def insert(self, key: int, value: _MessageV) -> None: ...
    def extend(self, elem_seq: Iterable[_MessageV]) -> None: ...
    def MergeFrom(self: _M, other: _M) -> None: ...
    def remove(self, elem: _MessageV) -> None: ...
    def pop(self, key: int = ...) -> _MessageV: ...
    def __getslice__(self, start: int, stop: int) -> List[_MessageV]: ...
    def __delitem__(self, key: Union[int, slice]) -> None: ...
    def __delslice__(self, start: int, stop: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...

class ScalarMap(MutableMapping[_K, _ScalarV]):
    def __setitem__(self, k: _K, v: _ScalarV) -> None: ...
    def __delitem__(self, v: _K) -> None: ...
    def __getitem__(self, k: _K) -> _ScalarV: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_K]: ...
    def __eq__(self, other: object) -> bool: ...
    def MergeFrom(self: _M, other: _M): ...
    def InvalidateIterators(self) -> None: ...
    def GetEntryClass(self) -> GeneratedProtocolMessageType: ...

class MessageMap(MutableMapping[_K, _MessageV]):
    def __setitem__(self, k: _K, v: _MessageV) -> None: ...
    def __delitem__(self, v: _K) -> None: ...
    def __getitem__(self, k: _K) -> _MessageV: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_K]: ...
    def __eq__(self, other: object) -> bool: ...
    def get_or_create(self, key: _K) -> _MessageV: ...
    def MergeFrom(self: _M, other: _M): ...
    def InvalidateIterators(self) -> None: ...
    def GetEntryClass(self) -> GeneratedProtocolMessageType: ...
