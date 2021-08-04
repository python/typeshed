import sys
from _csv import QUOTE_ALL as QUOTE_ALL
from _csv import QUOTE_MINIMAL as QUOTE_MINIMAL
from _csv import QUOTE_NONE as QUOTE_NONE
from _csv import QUOTE_NONNUMERIC as QUOTE_NONNUMERIC
from _csv import Dialect as Dialect
from _csv import Error as Error
from _csv import _DialectLike, _reader, _writer
from _csv import field_size_limit as field_size_limit
from _csv import get_dialect as get_dialect
from _csv import list_dialects as list_dialects
from _csv import reader as reader
from _csv import register_dialect as register_dialect
from _csv import unregister_dialect as unregister_dialect
from _csv import writer as writer
from typing import (Any, Generic, Iterable, Iterator, List, Mapping, Optional,
                    Sequence, Type, TypeVar, overload)

if sys.version_info >= (3, 8):
    from typing import Dict as _DictReadMapping
else:
    from collections import OrderedDict as _DictReadMapping

_T = TypeVar("_T")

class excel(Dialect):
    delimiter: str
    quotechar: str
    doublequote: bool
    skipinitialspace: bool
    lineterminator: str
    quoting: int

class excel_tab(excel):
    delimiter: str

class unix_dialect(Dialect):
    delimiter: str
    quotechar: str
    doublequote: bool
    skipinitialspace: bool
    lineterminator: str
    quoting: int

class DictReader(Generic[_T], Iterator[_DictReadMapping[_T, str]]):
    fieldnames: Optional[Sequence[_T]]
    restkey: Optional[str]
    restval: Optional[str]
    reader: _reader
    dialect: _DialectLike
    line_num: int
    @overload
    def __init__(
        self,
        f: Iterable[str],
        fieldnames: Sequence[_T],
        restkey: Optional[str] = ...,
        restval: Optional[str] = ...,
        dialect: _DialectLike = ...,
        *args: Any,
        **kwds: Any,
    ) -> None: ...
    @overload
    def __init__(
        self: DictReader[str],
        f: Iterable[str],
        fieldnames: Optional[Sequence[str]] = ...,
        restkey: Optional[str] = ...,
        restval: Optional[str] = ...,
        dialect: _DialectLike = ...,
        *args: Any,
        **kwds: Any,
    ) -> None: ...
    def __iter__(self) -> DictReader[_T]: ...
    def __next__(self) -> _DictReadMapping[_T, str]: ...

class DictWriter(Generic[_T]):
    fieldnames: Sequence[_T]
    restval: Optional[Any]
    extrasaction: str
    writer: _writer
    def __init__(
        self,
        f: Any,
        fieldnames: Sequence[_T],
        restval: Optional[Any] = ...,
        extrasaction: str = ...,
        dialect: _DialectLike = ...,
        *args: Any,
        **kwds: Any,
    ) -> None: ...
    if sys.version_info >= (3, 8):
        def writeheader(self) -> Any: ...
    else:
        def writeheader(self) -> None: ...
    def writerow(self, rowdict: Mapping[_T, Any]) -> Any: ...
    def writerows(self, rowdicts: Iterable[Mapping[_T, Any]]) -> None: ...

class Sniffer(object):
    preferred: List[str]
    def __init__(self) -> None: ...
    def sniff(self, sample: str, delimiters: Optional[str] = ...) -> Type[Dialect]: ...
    def has_header(self, sample: str) -> bool: ...
