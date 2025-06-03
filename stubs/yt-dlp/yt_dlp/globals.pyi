from collections import defaultdict
from typing import Generic, TypeVar

_T = TypeVar("_T")

class Indirect(Generic[_T]):
    value: _T
    def __init__(self, initial: _T, /) -> None: ...

postprocessors: Indirect[dict[str, object]]
extractors: Indirect[dict[str, object]]
all_plugins_loaded: Indirect[bool]
plugin_specs: Indirect[dict[str, object]]
plugin_dirs: Indirect[list[str]]
plugin_ies: Indirect[dict[str, object]]
plugin_pps: Indirect[dict[str, object]]
plugin_ies_overrides: Indirect[defaultdict[str, object]]
IN_CLI: Indirect[bool]
LAZY_EXTRACTORS: Indirect[None | bool]
