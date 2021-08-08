from typing import Any, Dict, List, Tuple, Type, overload

_defaultaction: str
_onceregistry: Dict[Any, Any]
filters: List[Tuple[Any, ...]]

@overload
def warn(message: str, category: Type[Warning] | None = ..., stacklevel: int = ..., source: Any | None = ...) -> None: ...
@overload
def warn(message: Warning, category: Any = ..., stacklevel: int = ..., source: Any | None = ...) -> None: ...
@overload
def warn_explicit(
    message: str,
    category: Type[Warning],
    filename: str,
    lineno: int,
    module: str | None = ...,
    registry: Dict[str | Tuple[str, Type[Warning], int], int] | None = ...,
    module_globals: Dict[str, Any] | None = ...,
    source: Any | None = ...,
) -> None: ...
@overload
def warn_explicit(
    message: Warning,
    category: Any,
    filename: str,
    lineno: int,
    module: str | None = ...,
    registry: Dict[str | Tuple[str, Type[Warning], int], int] | None = ...,
    module_globals: Dict[str, Any] | None = ...,
    source: Any | None = ...,
) -> None: ...
