from collections.abc import Generator, Iterable
from re import Pattern
from typing import Any, Final, TypeAlias

from xmldiff.actions import _Action

_Element: TypeAlias = Any  # lxml.etree._Element
_ElementTree: TypeAlias = Any  # lxml.etree._ElementTree

DIFF_SPLIT: Final[Pattern[str]]

class Patcher:
    @property
    def nsmap(self) -> dict[str | None, str]: ...
    def patch(self, actions: Iterable[_Action], tree: _Element | _ElementTree) -> _Element: ...
    def handle_action(self, action: _Action, tree: _Element) -> None: ...

class DiffParser:
    def parse(self, diff: str) -> Generator[_Action]: ...
    def make_action(self, line: str) -> _Action: ...
