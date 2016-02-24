from typing import Callable, Any, TypeVar

__all__ = ['coroutine',
           'iscoroutinefunction', 'iscoroutine']

_T = TypeVar('_T')

def coroutine(func: _T) -> _T: ...
def iscoroutinefunction(func: Callable[..., Any]) -> bool: ...
def iscoroutine(obj: Any) -> bool: ...
