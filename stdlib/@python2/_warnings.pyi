from typing import Any, Dict, List, Optional, Tuple, Type, Union, overload

default_action: str
once_registry: Dict[Any, Any]

filters: List[Tuple[Any, ...]]

@overload
def warn(message: str, category: Type[Warning] | None = ..., stacklevel: int = ...) -> None: ...
@overload
def warn(message: Warning, category: Any = ..., stacklevel: int = ...) -> None: ...
@overload
def warn_explicit(
    message: str,
    category: Type[Warning],
    filename: str,
    lineno: int,
    module: str | None = ...,
    registry: Optional[Dict[Union[str, Tuple[str, Type[Warning], int]], int]] = ...,
    module_globals: Dict[str, Any] | None = ...,
) -> None: ...
@overload
def warn_explicit(
    message: Warning,
    category: Any,
    filename: str,
    lineno: int,
    module: str | None = ...,
    registry: Optional[Dict[Union[str, Tuple[str, Type[Warning], int]], int]] = ...,
    module_globals: Dict[str, Any] | None = ...,
) -> None: ...
