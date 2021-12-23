import sys
from typing import Any, Callable, Generic, Iterator, NamedTuple, Pattern, Text, Tuple, TypeVar
from typing_extensions import ParamSpec

_Func = TypeVar("_Func", bound=Callable[..., Any])
_P = ParamSpec("_P")
_T_co = TypeVar("_T_co", covariant=True)
_T = TypeVar("_T")

def get_init(cls: type) -> None: ...

if sys.version_info >= (3,):
    from inspect import getfullargspec as getfullargspec, iscoroutinefunction as iscoroutinefunction
else:
    class FullArgSpec(NamedTuple):
        args: list[str]
        varargs: str | None
        varkw: str | None
        defaults: Tuple[Any, ...]
        kwonlyargs: list[str]
        kwonlydefaults: dict[str, Any]
        annotations: dict[str, Any]
    def iscoroutinefunction(f: Callable[..., Any]) -> bool: ...
    def getfullargspec(func: Any) -> FullArgSpec: ...

if sys.version_info >= (3, 2):
    from contextlib import _GeneratorContextManager
else:
    from contextlib import GeneratorContextManager as _GeneratorContextManager

DEF: Pattern[str]

_dict = dict  # conflicts with attribute name

class FunctionMaker(object):
    args: list[Text]
    varargs: Text | None
    varkw: Text | None
    defaults: Tuple[Any, ...]
    kwonlyargs: list[Text]
    kwonlydefaults: Text | None
    shortsignature: Text | None
    name: Text
    doc: Text | None
    module: Text | None
    annotations: _dict[Text, Any]
    signature: Text
    dict: _dict[Text, Any]
    def __init__(
        self,
        func: Callable[..., Any] | None = ...,
        name: Text | None = ...,
        signature: Text | None = ...,
        defaults: Tuple[Any, ...] | None = ...,
        doc: Text | None = ...,
        module: Text | None = ...,
        funcdict: _dict[Text, Any] | None = ...,
    ) -> None: ...
    def update(self, func: Any, **kw: Any) -> None: ...
    def make(
        self, src_templ: Text, evaldict: _dict[Text, Any] | None = ..., addsource: bool = ..., **attrs: Any
    ) -> Callable[..., Any]: ...
    @classmethod
    def create(
        cls,
        obj: Any,
        body: Text,
        evaldict: _dict[Text, Any],
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

class ContextManager(_GeneratorContextManager[_T_co], Generic[_T_co]): ...

def contextmanager(func: Callable[_P, Iterator[_T_co]]) -> Callable[_P, ContextManager[_T_co]]: ...
def dispatch_on(*dispatch_args: Any) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
