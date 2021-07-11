from pygments.util import ClassNotFound as ClassNotFound
from typing import Any, Type
from collections.abc import Mapping, Iterator
from pygments.style import Style, StyleMeta

STYLE_MAP: Mapping[str, str]

def get_style_by_name(name) -> StyleMeta: ...
def get_all_styles() -> Iterator[str]: ...

# Having every style class here doesn't seem to be worth it
def __getattr__(name: str) -> Any: ...
