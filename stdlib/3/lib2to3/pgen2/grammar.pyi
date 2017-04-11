# Stubs for lib2to3.pgen2.grammar (Python 3.6)

from typing import Any, Dict, List, Optional, Text, Tuple, TypeVar

_P = TypeVar('_P')
_Label = Tuple[int, Optional[Text]]
_States = List[List[Tuple[int, int]]]

class Grammar:
    symbol2number: Dict[Text, int]
    number2symbol: Dict[int, Text]
    states: _States
    dfas: Dict[int, _States]
    labels: List[_Label]
    keywords: Dict[Text, int]
    tokens: Dict[int, int]
    symbol2label: Dict[Text, int]
    start: int
    def __init__(self) -> None: ...
    def dump(self, filename: Text) -> None: ...
    def load(self, filename: Text) -> None: ...
    def copy(self: _P) -> _P: ...
    def report(self) -> None: ...

opmap_raw: Text
opmap: Dict[Text, Text]
