import sys
from _typeshed import FileDescriptor, FileDescriptorLike, Self, Unused
from abc import ABCMeta, abstractmethod
from collections.abc import Mapping
from typing import Any, NamedTuple
from typing_extensions import TypeAlias

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
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args: Unused) -> None: ...

class SelectSelector(BaseSelector):
    def register(self, fileobj: FileDescriptorLike, events: _EventMask, data: Any = None) -> SelectorKey: ...
    def unregister(self, fileobj: FileDescriptorLike) -> SelectorKey: ...
    def select(self, timeout: float | None = None) -> list[tuple[SelectorKey, _EventMask]]: ...
    def get_map(self) -> Mapping[FileDescriptorLike, SelectorKey]: ...

if sys.platform != "win32":
    class PollSelector(BaseSelector):
        def register(self, fileobj: FileDescriptorLike, events: _EventMask, data: Any = None) -> SelectorKey: ...
        def unregister(self, fileobj: FileDescriptorLike) -> SelectorKey: ...
        def select(self, timeout: float | None = None) -> list[tuple[SelectorKey, _EventMask]]: ...
        def get_map(self) -> Mapping[FileDescriptorLike, SelectorKey]: ...

if sys.platform == "linux":
    class EpollSelector(BaseSelector):
        def fileno(self) -> int: ...
        def register(self, fileobj: FileDescriptorLike, events: _EventMask, data: Any = ...) -> SelectorKey: ...
        def unregister(self, fileobj: FileDescriptorLike) -> SelectorKey: ...
        def select(self, timeout: float | None = ...) -> list[tuple[SelectorKey, _EventMask]]: ...
        def get_map(self) -> Mapping[FileDescriptorLike, SelectorKey]: ...

class DevpollSelector(BaseSelector):
    def fileno(self) -> int: ...
    def register(self, fileobj: FileDescriptorLike, events: _EventMask, data: Any = ...) -> SelectorKey: ...
    def unregister(self, fileobj: FileDescriptorLike) -> SelectorKey: ...
    def select(self, timeout: float | None = ...) -> list[tuple[SelectorKey, _EventMask]]: ...
    def get_map(self) -> Mapping[FileDescriptorLike, SelectorKey]: ...

class KqueueSelector(BaseSelector):
    def fileno(self) -> int: ...
    def register(self, fileobj: FileDescriptorLike, events: _EventMask, data: Any = None) -> SelectorKey: ...
    def unregister(self, fileobj: FileDescriptorLike) -> SelectorKey: ...
    def select(self, timeout: float | None = None) -> list[tuple[SelectorKey, _EventMask]]: ...
    def get_map(self) -> Mapping[FileDescriptorLike, SelectorKey]: ...

class DefaultSelector(BaseSelector):
    def register(self, fileobj: FileDescriptorLike, events: _EventMask, data: Any = None) -> SelectorKey: ...
    def unregister(self, fileobj: FileDescriptorLike) -> SelectorKey: ...
    def select(self, timeout: float | None = None) -> list[tuple[SelectorKey, _EventMask]]: ...
    def get_map(self) -> Mapping[FileDescriptorLike, SelectorKey]: ...
