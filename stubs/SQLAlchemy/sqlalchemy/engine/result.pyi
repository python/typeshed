from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Generator, Iterator, KeysView
from typing import Any
from typing_extensions import Self

from ..sql.base import InPlaceGenerative
from .row import Row

class ResultMetaData:
    @property
    def keys(self): ...

class RMKeyView(KeysView[Any]):
    def __init__(self, parent) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __contains__(self, item) -> bool: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...

class SimpleResultMetaData(ResultMetaData):
    def __init__(
        self,
        keys,
        extra: Incomplete | None = None,
        _processors: Incomplete | None = None,
        _tuplefilter: Incomplete | None = None,
        _translated_indexes: Incomplete | None = None,
        _unique_filters: Incomplete | None = None,
    ) -> None: ...

def result_tuple(fields, extra: Incomplete | None = None): ...

class ResultInternal(InPlaceGenerative): ...

class _WithKeys:
    def keys(self): ...

class Result(_WithKeys, ResultInternal):
    def __init__(self, cursor_metadata) -> None: ...
    def close(self) -> None: ...
    @property
    @abstractmethod
    def closed(self) -> bool: ...
    def yield_per(self, num: int) -> Self: ...
    def unique(self, strategy: Incomplete | None = None) -> Self: ...
    def columns(self, *col_expressions): ...
    def scalars(self, index: int = 0) -> ScalarResult: ...
    def mappings(self) -> MappingResult: ...
    def __iter__(self) -> Iterator[Row]: ...
    def __next__(self) -> Row: ...
    def partitions(self, size: int | None = None) -> Generator[list[Row], None, None]: ...
    def fetchall(self) -> list[Row]: ...
    def fetchone(self) -> Row | None: ...
    def fetchmany(self, size: int | None = None) -> list[Row]: ...
    def all(self) -> list[Row]: ...
    def first(self) -> Row | None: ...
    def one_or_none(self) -> Row | None: ...
    def scalar_one(self) -> Any: ...
    def scalar_one_or_none(self) -> Incomplete | None: ...
    def one(self) -> Row: ...
    # Note: The return type `Any` should be a DB API 2 value type once defined
    # TODO: See #1037
    def scalar(self) -> Incomplete | None: ...
    def freeze(self) -> FrozenResult: ...
    def merge(self, *others) -> MergedResult: ...

class FilterResult(ResultInternal):
    @property
    def closed(self) -> bool: ...
    def yield_per(self, num) -> Self: ...

class ScalarResult(FilterResult):
    def __init__(self, real_result, index) -> None: ...
    def unique(self, strategy: Incomplete | None = None): ...
    def partitions(self, size: Incomplete | None = None) -> None: ...
    def fetchall(self): ...
    def fetchmany(self, size: Incomplete | None = None): ...
    def all(self): ...
    def __iter__(self): ...
    def __next__(self): ...
    def first(self): ...
    def one_or_none(self): ...
    def one(self): ...

class MappingResult(_WithKeys, FilterResult):
    def __init__(self, result) -> None: ...
    def unique(self, strategy: Incomplete | None = None): ...
    def columns(self, *col_expressions): ...
    def partitions(self, size: Incomplete | None = None) -> None: ...
    def fetchall(self): ...
    def fetchone(self): ...
    def fetchmany(self, size: Incomplete | None = None): ...
    def all(self): ...
    def __iter__(self): ...
    def __next__(self): ...
    def first(self): ...
    def one_or_none(self): ...
    def one(self): ...

class FrozenResult:
    metadata: Any
    data: Any
    def __init__(self, result) -> None: ...
    def rewrite_rows(self): ...
    def with_new_rows(self, tuple_data): ...
    def __call__(self): ...

class IteratorResult(Result):
    iterator: Any
    raw: Any
    @property
    def closed(self) -> bool: ...
    def __init__(self, cursor_metadata, iterator, raw: Incomplete | None = None, _source_supports_scalars: bool = False) -> None: ...

def null_result() -> IteratorResult: ...

class ChunkedIteratorResult(IteratorResult):
    chunks: Any
    raw: Any
    iterator: Any
    dynamic_yield_per: Any
    def __init__(
        self,
        cursor_metadata,
        chunks,
        source_supports_scalars: bool = False,
        raw: Incomplete | None = None,
        dynamic_yield_per: bool = False,
    ) -> None: ...
    def yield_per(self, num) -> Self: ...

class MergedResult(IteratorResult):
    closed: bool
    def __init__(self, cursor_metadata, results) -> None: ...
