from _typeshed import FloatInt
from collections.abc import Iterable
from typing import NamedTuple

from .ast import Node

class RGBA(NamedTuple):
    red: FloatInt
    green: FloatInt
    blue: FloatInt
    alpha: FloatInt

def parse_color(input: str | Iterable[Node]) -> str | RGBA | None: ...
