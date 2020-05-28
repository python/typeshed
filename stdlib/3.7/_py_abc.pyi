
from typing import Type, TypeVar, Tuple, Any, Dict, NewType

_T = TypeVar('_T')
_CacheType = NewType('_CacheType', int)

def get_cache_token() -> _CacheType: ...

class ABCMeta(type):
    def __new__(mcls, __name: str, __bases: Tuple[Type[Any]], __namespace: Dict[str, Any]) -> ABCMeta: ...
    def register(cls: ABCMeta, subclass: Type[_T]) -> Type[_T]: ...
