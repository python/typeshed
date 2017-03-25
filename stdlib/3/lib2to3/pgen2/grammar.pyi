# Stubs for lib2to3.pgen2.grammar (Python 3.6)

from typing import Any, Dict, List, Optional, Tuple, TypeVar

_P = TypeVar('_P')
_Label = Tuple[int, Optional[str]]
_States = List[List[Tuple[int, int]]]

class Grammar:
    symbol2number: Dict[str, int]
    number2symbol: Dict[int, str]
    states: _States
    dfas: Dict[int, _States]
    labels: List[_Label]
    keywords: Dict[str, int]
    tokens: Dict[int, int]
    symbol2label: Dict[str, int]
    start: int
    def __init__(self) -> None: ...
    def dump(self, filename: str) -> None: ...
    def load(self, filename: str) -> None: ...
    def copy(self: _P) -> _P: ...
    def report(self) -> None: ...

opmap_raw: str
opmap: Dict[str, str]
