from typing import Any

from asgiref.typing import ASGIReceiveCallable, ASGISendCallable
from channels.middleware import BaseMiddleware
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AnonymousUser
from django.utils.functional import LazyObject

from .consumer import _ChannelScope, _LazySession
from .db import database_sync_to_async
from .utils import _ChannelApplication

@database_sync_to_async
def get_user(scope: _ChannelScope) -> AbstractBaseUser | AnonymousUser: ...
@database_sync_to_async
def login(scope: _ChannelScope, user: AbstractBaseUser, backend: BaseBackend | None = ...) -> None: ...
@database_sync_to_async
def logout(scope: _ChannelScope) -> None: ...
def _get_user_session_key(session: _LazySession) -> Any: ...

class UserLazyObject(AbstractBaseUser, LazyObject):
    def _setup(self) -> None: ...

class AuthMiddleware(BaseMiddleware):
    def populate_scope(self, scope: _ChannelScope) -> None: ...
    async def resolve_scope(self, scope: _ChannelScope) -> None: ...
    async def __call__(
        self, scope: _ChannelScope, receive: ASGIReceiveCallable, send: ASGISendCallable
    ) -> _ChannelApplication: ...

def AuthMiddlewareStack(inner: _ChannelApplication) -> _ChannelApplication: ...
