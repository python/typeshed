from collections.abc import Awaitable, Callable
from typing import Any, Protocol, type_check_only
from typing_extensions import TypeAlias

from asgiref.typing import ASGIApplication, ASGIReceiveCallable

def name_that_thing(thing: Any) -> str: ...
async def await_many_dispatch(
    consumer_callables: list[Callable[[], Awaitable[ASGIReceiveCallable]]], dispatch: Callable[[dict[str, Any]], Awaitable[None]]
) -> None: ...
@type_check_only
class _MiddlewareProtocol(Protocol):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    async def __call__(self, scope: Any, receive: Any, send: Any) -> Any: ...

_ChannelApplication: TypeAlias = _MiddlewareProtocol | ASGIApplication  # noqa: Y047
