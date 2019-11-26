import sys
from typing import Any, Dict, List, Optional, Tuple, Type

if sys.version_info >= (3, 0):
    _defaultaction: str
    _onceregistry: Dict[Any, Any]
else:
    default_action: str
    once_registry: Dict[Any, Any]
filters: List[Tuple[Any, ...]]

def warn(message: Warning, category: Optional[Type[Warning]] = ..., stacklevel: int = ...) -> None: ...
def warn_explicit(
    message: Warning,
    category: Optional[Type[Warning]],
    filename: str,
    lineno: int,
    module: Any = ...,
    registry: Dict[Any, Any] = ...,
    module_globals: Dict[Any, Any] = ...,
) -> None: ...
