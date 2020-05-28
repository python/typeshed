
from typing import Type, TypeVar

_T = TypeVar('_T')

def get_cache_token() -> object: ...

class ABCMeta(type):
    def register(cls: ABCMeta, subclass: Type[_T]) -> Type[_T]: ...
