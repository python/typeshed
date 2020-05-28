
from typing import Type, TypeVar, Tuple, Any, Dict

_T = TypeVar('_T')

def get_cache_token() -> object: ...

class ABCMeta(type):
    def __new__(mcls, __name: str, __bases: Tuple[Type[Any]], __namespace: Dict[str, object], **kwargs) -> ABCMeta: ...
    def register(cls: ABCMeta, subclass: Type[_T]) -> Type[_T]: ...
