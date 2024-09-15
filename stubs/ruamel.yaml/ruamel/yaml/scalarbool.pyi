from typing_extensions import Self

from .anchor import Anchor

__all__ = ["ScalarBoolean"]

class ScalarBoolean(int):
    def __new__(cls, value: bool, /, *, anchor: str | None = None) -> Self: ...
    @property
    def anchor(self) -> Anchor: ...
    def yaml_anchor(self, *, any: bool = False) -> Anchor | None: ...
    def yaml_set_anchor(self, value: str, /, *, always_dump: bool = False) -> None: ...
