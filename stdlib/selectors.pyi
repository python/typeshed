import sys
from _typeshed import FileDescriptor, FileDescriptorLike, Unused
from abc import ABCMeta, abstractmethod
from collections.abc import Mapping
from typing import Any, NamedTuple
from typing_extensions import Self, TypeAlias

_EventMask: TypeAlias = int

EVENT_READ: _EventMask
EVENT_WRITE: _EventMask

class SelectorKey(NamedTuple):
    fileobj: FileDescriptorLike
    fd: FileDescriptor
    events: _EventMask
    data: Any

class BaseSelector(metaclass=ABCMeta):
    @abstractmethod
    def register(self, fileobj: FileDescriptorLike, events: _EventMask, data: Any = None) -> SelectorKey: ...
    @abstractmethod
    def unregister(self, fileobj: FileDescriptorLike) -> SelectorKey: ...
    def modify(self, fileobj: FileDescriptorLike, events: _EventMask, data: Any = None) -> SelectorKey: ...
    @abstractmethod
    def select(self, timeout: float | None = None) -> list[tuple[SelectorKey, _EventMask]]: ...
    def close(self) -> None: ...
    def get_key(self, fileobj: FileDescriptorLike) -> SelectorKey: ...
    @abstractmethod
    def get_map(self) -> Mapping[FileDescriptorLike, SelectorKey]: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: Unused) -> None: ...

class _BaseSelectorImpl(BaseSelector, metaclass=ABCMeta):
    def __init__(self) -> None: ...
    def register(self, fileobj: FileDescriptorLike, events: _EventMask, data: Any = None) -> SelectorKey: ...
    def unregister(self, fileobj: FileDescriptorLike) -> SelectorKey: ...
    def modify(self, fileobj: FileDescriptorLike, events: _EventMask, data: Any = None) -> SelectorKey: ...
    def close(self) -> None: ...
    def get_map(self) -> Mapping[FileDescriptorLike, SelectorKey]: ...

class SelectSelector(_BaseSelectorImpl):
    def register(self, fileobj: FileDescriptorLike, events: _EventMask, data: Any = None) -> SelectorKey: ...
    def unregister(self, fileobj: FileDescriptorLike) -> SelectorKey: ...
    def select(self, timeout: float | None = None) -> list[tuple[SelectorKey, _EventMask]]: ...

class _PollLikeSelector(_BaseSelectorImpl):
    def select(self, timeout: float | None = None) -> list[tuple[SelectorKey, _EventMask]]: ...

if sys.platform != "win32":
    class PollSelector(_PollLikeSelector): ...

if sys.platform == "linux":
    class EpollSelector(_PollLikeSelector):
        def fileno(self) -> int: ...

class DevpollSelector(_PollLikeSelector):
    def fileno(self) -> int: ...

if sys.platform != "win32":
    class KqueueSelector(_BaseSelectorImpl):
        def fileno(self) -> int: ...
        def select(self, timeout: float | None = None) -> list[tuple[SelectorKey, _EventMask]]: ...

# Not a real class at runtime, it is just a conditional alias to other real selectors.
# The runtime logic is more fine-grained than a `sys.platform` check;
# not really expressible in the stubs
class DefaultSelector(_BaseSelectorImpl):
    def select(self, timeout: float | None = None) -> list[tuple[SelectorKey, _EventMask]]: ...
    if sys.platform != "win32":
        def fileno(self) -> int: ...
