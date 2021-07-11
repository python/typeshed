from pygments.plugin import find_plugin_styles as find_plugin_styles
from pygments.util import ClassNotFound as ClassNotFound
from typing import Any

STYLE_MAP: Any

def get_style_by_name(name: Any): ...
def get_all_styles() -> None: ...
