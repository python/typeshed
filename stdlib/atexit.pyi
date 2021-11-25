from typing import Any, Callable, TypeVar
from typing_extensions import ParamSpec

_T = TypeVar("_T")
_P = ParamSpec("_P")

def _clear() -> None: ...
def _ncallbacks() -> int: ...
def _run_exitfuncs() -> None: ...
def register(func: Callable[_P, _T], *args: _P.args, **kwargs: _P.kwargs) -> Callable[_P, _T]: ...  # type: ignore[name-defined]
def unregister(func: Callable[..., Any]) -> None: ...
