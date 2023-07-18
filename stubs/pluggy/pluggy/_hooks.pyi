import sys
from collections.abc import Callable, Generator, Mapping, Sequence, Set as AbstractSet
from types import ModuleType
from typing import Any, TypeVar, overload

from ._result import _Result

from typing_extensions import Final, TypedDict, TypeAlias

_T = TypeVar("_T")
_F = TypeVar("_F", bound=Callable[..., object])
_Namespace: TypeAlias = ModuleType | type
_Plugin = object
_HookExec: TypeAlias = Callable[[str, Sequence[HookImpl], Mapping[str, object], bool], object | list[object]]
_HookImplFunction: TypeAlias = Callable[..., _T | Generator[None, _Result[_T], None]]

class _HookSpecOpts(TypedDict):
    firstresult: bool
    historic: bool
    warn_on_impl: Warning | None

class _HookImplOpts(TypedDict):
    wrapper: bool
    hookwrapper: bool
    optionalhook: bool
    tryfirst: bool
    trylast: bool
    specname: str | None

class HookspecMarker:
    project_name: Final[str]
    def __init__(self, project_name: str) -> None: ...
    @overload
    def __call__(self, function: _F, firstresult: bool = ..., historic: bool = ..., warn_on_impl: Warning | None = ...) -> _F: ...
    @overload
    def __call__(
        self, function: None = ..., firstresult: bool = ..., historic: bool = ..., warn_on_impl: Warning | None = ...
    ) -> Callable[[_F], _F]: ...

class HookimplMarker:
    project_name: Final[str]
    def __init__(self, project_name: str) -> None: ...
    @overload
    def __call__(
        self,
        function: _F,
        hookwrapper: bool = ...,
        optionalhook: bool = ...,
        tryfirst: bool = ...,
        trylast: bool = ...,
        specname: str | None = ...,
        wrapper: bool = ...,
    ) -> _F: ...
    @overload
    def __call__(
        self,
        function: None = ...,
        hookwrapper: bool = ...,
        optionalhook: bool = ...,
        tryfirst: bool = ...,
        trylast: bool = ...,
        specname: str | None = ...,
        wrapper: bool = ...,
    ) -> Callable[[_F], _F]: ...

def normalize_hookimpl_opts(opts: _HookImplOpts) -> None: ...
def varnames(func: object) -> tuple[tuple[str, ...], tuple[str, ...]]: ...

class _HookRelay:
    def __getattr__(self, name: str) -> _HookCaller: ...

class _HookCaller:
    name: Final[str]
    spec: HookSpec | None
    def __init__(
        self,
        name: str,
        hook_execute: _HookExec,
        specmodule_or_class: _Namespace | None = ...,
        spec_opts: _HookSpecOpts | None = ...,
    ) -> None: ...
    def has_spec(self) -> bool: ...
    def set_specification(self, specmodule_or_class: _Namespace, spec_opts: _HookSpecOpts) -> None: ...
    def is_historic(self) -> bool: ...
    def get_hookimpls(self) -> list[HookImpl]: ...
    def __call__(self, **kwargs: object) -> Any: ...
    def call_historic(
        self, result_callback: Callable[[Any], None] | None = ..., kwargs: Mapping[str, object] | None = ...
    ) -> None: ...
    def call_extra(self, methods: Sequence[Callable[..., object]], kwargs: Mapping[str, object]) -> Any: ...

class _SubsetHookCaller(_HookCaller):
    def __init__(self, orig: _HookCaller, remove_plugins: AbstractSet[_Plugin]) -> None: ...

class HookImpl:
    function: Final[_HookImplFunction[object]]
    plugin: _Plugin
    opts: _HookImplOpts
    plugin_name: str
    wrapper: bool
    hookwrapper: bool
    optionalhook: bool
    tryfirst: bool
    trylast: bool
    argnames: tuple[str, ...]
    kwargnames: tuple[str, ...]
    def __init__(
        self, plugin: _Plugin, plugin_name: str, function: _HookImplFunction[object], hook_impl_opts: _HookImplOpts
    ) -> None: ...

class HookSpec:
    namespace: _Namespace
    function: Callable[..., object]
    name: str
    opts: _HookSpecOpts
    warn_on_impl: Warning | None
    argnames: tuple[str, ...]
    kwargnames: tuple[str, ...]
    def __init__(self, namespace: _Namespace, name: str, opts: _HookSpecOpts) -> None: ...
