from collections.abc import Callable
from email.message import Message
from email.policy import Policy
from typing import Generic, Protocol, TypeVar, overload

__all__ = ["FeedParser", "BytesFeedParser"]

_MessageT = TypeVar("_MessageT", bound=Message)
_T_contra = TypeVar("_T_contra", contravariant=True)

class _SupportsFeed(Protocol[_T_contra]):
    def feed(self, data: _T_contra) -> None: ...

class FeedParser(Generic[_MessageT], _SupportsFeed[str]):
    @overload
    def __init__(self: FeedParser[Message], _factory: None = None, *, policy: Policy = ...) -> None: ...
    @overload
    def __init__(self, _factory: Callable[[], _MessageT], *, policy: Policy = ...) -> None: ...
    def close(self) -> _MessageT: ...

class BytesFeedParser(FeedParser[_MessageT], _SupportsFeed[bytes | bytearray]):
    @overload
    def __init__(self: BytesFeedParser[Message], _factory: None = None, *, policy: Policy = ...) -> None: ...
    @overload
    def __init__(self, _factory: Callable[[], _MessageT], *, policy: Policy = ...) -> None: ...
