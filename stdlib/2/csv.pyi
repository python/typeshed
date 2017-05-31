from typing import Any, Dict, Iterable, List, Sequence, Type, Union

# Public interface of _csv.reader's return type
class _Reader(Iterable[List[str]]):
    dialect = ...  # type: Dialect
    line_num = ...  # type: int

    def next(self) -> List[str]: ...

_Row = Sequence[Any]  # May contain anything: csv calls str() on the elements that are not None

# Public interface of _csv.writer's return type
class _Writer:
    dialect = ...  # type: Dialect

    def writerow(self, row: _Row) -> None: ...
    def writerows(self, rows: Iterable[_Row]) -> None: ...

QUOTE_ALL = ...  # type: int
QUOTE_MINIMAL = ...  # type: int
QUOTE_NONE = ...  # type: int
QUOTE_NONNUMERIC = ...  # type: int

class Error(Exception): ...

_Dialect = Union[str, Dialect, Type[Dialect]]

def writer(csvfile: Any, dialect: _Dialect = ..., **fmtparams) -> _Writer: ...
def reader(csvfile: Iterable[str], dialect: _Dialect = ..., **fmtparams) -> _Reader: ...
def register_dialect(name, dialect=..., **fmtparams): ...
def unregister_dialect(name): ...
def get_dialect(name: str) -> Dialect: ...
def list_dialects(): ...
def field_size_limit(new_limit: int = ...) -> int: ...

class Dialect:
    delimiter = ...  # type: str
    quotechar = ...  # type: str
    escapechar = ...  # type: str
    doublequote = ...  # type: bool
    skipinitialspace = ...  # type: bool
    lineterminator = ...  # type: str
    quoting = ...  # type: int
    def __init__(self) -> None: ...

class excel(Dialect):
    pass

class excel_tab(excel):
    pass

class unix_dialect(Dialect):
    pass

class DictReader(Iterable):
    restkey = ...  # type: Any
    restval = ...  # type: Any
    reader = ...  # type: Any
    dialect = ...  # type: _Dialect
    line_num = ...  # type: int
    fieldnames = ...  # type: Sequence[Any]
    def __init__(self, f: Iterable[str], fieldnames: Sequence[Any] = ..., restkey=...,
                 restval=..., dialect: _Dialect = ..., *args, **kwds) -> None: ...
    def __iter__(self): ...
    def next(self): ...

_DictRow = Dict[Any, Union[str, int]]

class DictWriter:
    fieldnames = ...  # type: Any
    restval = ...  # type: Any
    extrasaction = ...  # type: Any
    writer = ...  # type: Any
    def __init__(self, f: Any, fieldnames: Sequence[Any], restval=..., extrasaction: str = ...,
                 dialect: _Dialect = ..., *args, **kwds) -> None: ...
    def writeheader(self) -> None: ...
    def writerow(self, rowdict: _DictRow) -> None: ...
    def writerows(self, rowdicts: Iterable[_DictRow]) -> None: ...

class Sniffer:
    preferred = ...  # type: Any
    def __init__(self) -> None: ...
    def sniff(self, sample: str, delimiters: str = ...) -> Dialect: ...
    def has_header(self, sample: str) -> bool: ...
