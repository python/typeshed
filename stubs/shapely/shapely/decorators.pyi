from collections.abc import Callable, Container
from typing import TypeVar
from typing_extensions import deprecated

_F = TypeVar("_F", bound=Callable[..., object])

class requires_geos:
    version: tuple[int, int, int]
    def __init__(self, version: str) -> None: ...
    def __call__(self, func: _F) -> _F: ...

@deprecated("'multithreading_enabled' is deprecated and will be removed in a future version.")
def multithreading_enabled(func: _F) -> _F: ...
def deprecate_positional(should_be_kwargs: Container[str], category: type[Warning] = ...) -> Callable[..., object]: ...
