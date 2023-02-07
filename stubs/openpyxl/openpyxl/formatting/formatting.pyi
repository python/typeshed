from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class ConditionalFormatting(Serialisable):
    tagname: str
    sqref: Incomplete
    cells: Incomplete
    pivot: Incomplete
    cfRule: Incomplete
    rules: Incomplete
    def __init__(self, sqref=..., pivot: Incomplete | None = ..., cfRule=..., extLst: Incomplete | None = ...) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self) -> int: ...
    def __contains__(self, coord): ...

class ConditionalFormattingList:
    max_priority: int
    def __init__(self) -> None: ...
    def add(self, range_string, cfRule) -> None: ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __getitem__(self, key): ...
    def __delitem__(self, key) -> None: ...
    def __setitem__(self, key, rule) -> None: ...
