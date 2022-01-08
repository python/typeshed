from typing import Any, TypeVar

_T = TypeVar("_T")

# TODO: Change the return into a NewType bound to int after pytype/#597
def get_cache_token() -> object: ...

class ABCMeta(type):
    def __new__(__mcls, __name: str, __bases: tuple[type[Any], ...], __namespace: dict[str, Any]) -> ABCMeta: ...
    def register(cls, subclass: type[_T]) -> type[_T]: ...
