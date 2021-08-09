from typing import Any, Callable
from typing_extensions import ParamSpec

_P = ParamSpec("_P")

def _clear() -> None: ...
def _ncallbacks() -> int: ...
def _run_exitfuncs() -> None: ...
def register(func: Callable[_P, Any], *args: Any, **kwargs: Any) -> Callable[_P, Any]: ...  # type: ignore
def unregister(func: Callable[_P, Any]) -> None: ...  # type: ignore
