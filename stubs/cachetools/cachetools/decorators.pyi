from _typeshed import IdentityFunction
from typing import Any, Callable, ContextManager, MutableMapping, Optional, TypeVar

_KT = TypeVar("_KT")

def cached(
    cache: MutableMapping[_KT, Any] | None, key: Callable[..., _KT] = ..., lock: ContextManager[Any] | None = ...
) -> IdentityFunction: ...
def cachedmethod(
    cache: Callable[[Any], MutableMapping[_KT, Any] | None],
    key: Callable[..., _KT] = ...,
    lock: ContextManager[Any] | None = ...,
) -> IdentityFunction: ...
