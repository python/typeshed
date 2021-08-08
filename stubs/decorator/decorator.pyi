import sys
from typing import Any, Callable, Dict, Iterator, List, NamedTuple, Pattern, Text, Tuple, TypeVar

_C = TypeVar("_C", bound=Callable[..., Any])
_Func = TypeVar("_Func", bound=Callable[..., Any])
_T = TypeVar("_T")

def get_init(cls: type) -> None: ...

if sys.version_info >= (3,):
    from inspect import getfullargspec as getfullargspec, iscoroutinefunction as iscoroutinefunction
else:
    class FullArgSpec(NamedTuple):
        args: List[str]
        varargs: str | None
        varkw: str | None
        defaults: Tuple[Any, ...]
        kwonlyargs: List[str]
        kwonlydefaults: Dict[str, Any]
        annotations: Dict[str, Any]
    def iscoroutinefunction(f: Callable[..., Any]) -> bool: ...
    def getfullargspec(func: Any) -> FullArgSpec: ...

if sys.version_info >= (3, 2):
    from contextlib import _GeneratorContextManager
else:
    from contextlib import GeneratorContextManager as _GeneratorContextManager

DEF: Pattern[str]

class FunctionMaker(object):
    args: List[Text]
    varargs: Text | None
    varkw: Text | None
    defaults: Tuple[Any, ...]
    kwonlyargs: List[Text]
    kwonlydefaults: Text | None
    shortsignature: Text | None
    name: Text
    doc: Text | None
    module: Text | None
    annotations: Dict[Text, Any]
    signature: Text
    dict: Dict[Text, Any]
    def __init__(
        self,
        func: Callable[..., Any] | None = ...,
        name: Text | None = ...,
        signature: Text | None = ...,
        defaults: Tuple[Any, ...] | None = ...,
        doc: Text | None = ...,
        module: Text | None = ...,
        funcdict: Dict[Text, Any] | None = ...,
    ) -> None: ...
    def update(self, func: Any, **kw: Any) -> None: ...
    def make(
        self, src_templ: Text, evaldict: Dict[Text, Any] | None = ..., addsource: bool = ..., **attrs: Any
    ) -> Callable[..., Any]: ...
    @classmethod
    def create(
        cls,
        obj: Any,
        body: Text,
        evaldict: Dict[Text, Any],
        defaults: Tuple[Any, ...] | None = ...,
        doc: Text | None = ...,
        module: Text | None = ...,
        addsource: bool = ...,
        **attrs: Any,
    ) -> Callable[..., Any]: ...

def decorate(func: _Func, caller: Callable[..., Any], extras: Any = ...) -> _Func: ...
def decorator(
    caller: Callable[..., Any], _func: Callable[..., Any] | None = ...
) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...

class ContextManager(_GeneratorContextManager[_T]):
    def __call__(self, func: _C) -> _C: ...

def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., ContextManager[_T]]: ...
def dispatch_on(*dispatch_args: Any) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
