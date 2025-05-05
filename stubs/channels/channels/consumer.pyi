from collections.abc import Awaitable
from typing import Any, ClassVar, Protocol, type_check_only

from asgiref.typing import ASGIReceiveCallable, ASGISendCallable, Scope, WebSocketScope
from channels.auth import UserLazyObject
from channels.db import database_sync_to_async
from channels.layers import BaseChannelLayer
from django.contrib.sessions.backends.base import SessionBase
from django.utils.functional import LazyObject

@type_check_only
class _LazySession(SessionBase, LazyObject):  # type: ignore[misc]
    _wrapped: SessionBase

# Base ASGI Scope definition
@type_check_only
class _ChannelScope(WebSocketScope, total=False):
    # Channel specific
    channel: str
    url_route: dict[str, Any]
    path_remaining: str

    # Auth specific
    cookies: dict[str, str]
    session: _LazySession
    user: UserLazyObject | None

def get_handler_name(message: dict[str, Any]) -> str: ...
@type_check_only
class _ASGIApplicationProtocol(Protocol):
    consumer_class: Any
    consumer_initkwargs: dict[str, Any]

    def __call__(self, scope: Scope, receive: ASGIReceiveCallable, send: ASGISendCallable) -> Awaitable[None]: ...

class AsyncConsumer:
    _sync: ClassVar[bool] = ...
    channel_layer_alias: ClassVar[str] = ...

    scope: _ChannelScope
    channel_layer: BaseChannelLayer
    channel_name: str
    channel_receive: ASGIReceiveCallable
    base_send: ASGISendCallable

    async def __call__(self, scope: _ChannelScope, receive: ASGIReceiveCallable, send: ASGISendCallable) -> None: ...
    async def dispatch(self, message: dict[str, Any]) -> None: ...
    async def send(self, message: dict[str, Any]) -> None: ...
    @classmethod
    def as_asgi(cls, **initkwargs: Any) -> _ASGIApplicationProtocol: ...

class SyncConsumer(AsyncConsumer):
    _sync: ClassVar[bool] = ...

    @database_sync_to_async
    def dispatch(self, message: dict[str, Any]) -> None: ...  # type: ignore[override]
    def send(self, message: dict[str, Any]) -> None: ...  # type: ignore[override]
