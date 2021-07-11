from pygments.plugin import find_plugin_styles as find_plugin_styles
from pygments.util import ClassNotFound as ClassNotFound
from typing import Any

STYLE_MAP: Any

def get_style_by_name(name): ...
def get_all_styles() -> None: ...

# Having every style class here doesn't seem to be worth it
def __getattr__(name: str) -> Any: ...
