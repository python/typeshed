# ModuleSpec is in its own file to deal with import loops; defined in
# importlib.machinery.
import importlib.abc
import sys
from typing import Any, Optional

if sys.version_info >= (3, 4):
    class ModuleSpec:
        def __init__(self, name: str, loader: Optional[importlib.abc.Loader], *,
                     origin: str = None, loader_state: Any = None,
                     is_package: bool = None) -> None: ...
        name = ... # type: str
        loader = ... # type: Optional[importlib.abc.Loader]
        origin = ... # type: Optional[str]
        submodule_search_locations = ... # type: Optional[List[str]]
        loader_state = ... # type: Any
        cached = ... # type: Optional[str]
        parent = ... # type: Optional[str]
        has_location = ... # type: bool
