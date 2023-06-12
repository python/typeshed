from _typeshed import Incomplete
from re import Pattern
from typing_extensions import Final

INVALID_TITLE_REGEX: Final[Pattern[str]]

def avoid_duplicate_name(names, value): ...

class _WorkbookChild:
    HeaderFooter: Incomplete
    def __init__(self, parent: Incomplete | None = None, title: Incomplete | None = None) -> None: ...
    @property
    def parent(self): ...
    @property
    def encoding(self): ...
    @property
    def title(self) -> str: ...
    @title.setter
    def title(self, value: str | bytes) -> None: ...
    @property
    def oddHeader(self): ...
    @oddHeader.setter
    def oddHeader(self, value) -> None: ...
    @property
    def oddFooter(self): ...
    @oddFooter.setter
    def oddFooter(self, value) -> None: ...
    @property
    def evenHeader(self): ...
    @evenHeader.setter
    def evenHeader(self, value) -> None: ...
    @property
    def evenFooter(self): ...
    @evenFooter.setter
    def evenFooter(self, value) -> None: ...
    @property
    def firstHeader(self): ...
    @firstHeader.setter
    def firstHeader(self, value) -> None: ...
    @property
    def firstFooter(self): ...
    @firstFooter.setter
    def firstFooter(self, value) -> None: ...
    @property
    def path(self): ...
