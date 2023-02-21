from . import token as token
from _typeshed import Incomplete

class Grammar:
    symbol2number: Incomplete
    number2symbol: Incomplete
    states: Incomplete
    dfas: Incomplete
    labels: Incomplete
    keywords: Incomplete
    tokens: Incomplete
    symbol2label: Incomplete
    start: int
    def __init__(self) -> None: ...
    def dump(self, filename) -> None: ...
    def load(self, filename) -> None: ...
    def loads(self, pkl) -> None: ...
    def copy(self): ...
    def report(self) -> None: ...

opmap_raw: str
opmap: Incomplete
op: Incomplete
name: Incomplete
