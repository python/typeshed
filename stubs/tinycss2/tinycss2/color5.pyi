from collections.abc import Iterable
from typing import Literal

from . import color4
from .ast import Node

class Color(color4.Color):
    COLOR_SPACES: set[str]

def parse_color(
    input: str | Iterable[Node], color_schemes: Literal["normal"] | Iterable[str] = ...
) -> color4.Color | Color | Literal["currentcolor"] | None: ...
