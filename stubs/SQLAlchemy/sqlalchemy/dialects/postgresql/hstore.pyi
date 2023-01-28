from _typeshed import Incomplete
from collections.abc import Callable
from typing import TypeVar

from ...sql import functions as sqlfunc, sqltypes
from ...sql.elements import BinaryExpression
from ...sql.type_api import TypeEngine
from ...util.langhelpers import memoized_property
from .array import ARRAY

_T = TypeVar("_T")

class HSTORE(sqltypes.Indexable, sqltypes.Concatenable, sqltypes.TypeEngine):
    __visit_name__: str
    hashable: bool
    text_type: TypeEngine
    def __init__(self, text_type: TypeEngine | None = ...) -> None: ...

    class Comparator(sqltypes.Indexable.Comparator[_T], sqltypes.Concatenable.Comparator[_T]):
        def has_key(self, other) -> BinaryExpression: ...
        def has_all(self, other) -> BinaryExpression: ...
        def has_any(self, other) -> BinaryExpression: ...
        def contains(self, other: str, **kwargs) -> BinaryExpression: ...
        def contained_by(self, other) -> BinaryExpression: ...
        def defined(self, key) -> _HStoreDefinedFunction: ...
        def delete(self, key) -> _HStoreDefinedFunction: ...
        def slice(self, array) -> _HStoreDefinedFunction: ...
        def keys(self) -> _HStoreDefinedFunction: ...
        def vals(self) -> _HStoreDefinedFunction: ...
        def array(self) -> _HStoreDefinedFunction: ...
        def matrix(self) -> _HStoreDefinedFunction: ...
    comparator_factory: Callable[[Incomplete], Comparator[Incomplete]]
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class hstore(sqlfunc.GenericFunction):
    @memoized_property
    def type(self) -> type[HSTORE]: ...  # type: ignore[override]  # @memoized_property causes override issue
    name = "hstore"
    inherit_cache = True

class _HStoreDefinedFunction(sqlfunc.GenericFunction):
    @memoized_property
    def type(self) -> type[sqltypes.Boolean]: ...  # type: ignore[override]  # @memoized_property causes override issue
    name = "defined"
    inherit_cache = True

class _HStoreDeleteFunction(sqlfunc.GenericFunction):
    @memoized_property
    def type(self) -> type[HSTORE]: ...  # type: ignore[override]  # @memoized_property causes override issue
    name = "delete"
    inherit_cache = True

class _HStoreSliceFunction(sqlfunc.GenericFunction):
    @memoized_property
    def type(self) -> type[HSTORE]: ...  # type: ignore[override]  # @memoized_property causes override issue
    name = "slice"
    inherit_cache = True

class _HStoreKeysFunction(sqlfunc.GenericFunction):
    @memoized_property
    def type(self) -> ARRAY: ...  # type: ignore[override]  # @memoized_property causes override issue
    name = "akeys"
    inherit_cache = True

class _HStoreValsFunction(sqlfunc.GenericFunction):
    @memoized_property
    def type(self) -> ARRAY: ...  # type: ignore[override]  # @memoized_property causes override issue
    name = "avals"
    inherit_cache = True

class _HStoreArrayFunction(sqlfunc.GenericFunction):
    @memoized_property
    def type(self) -> ARRAY: ...  # type: ignore[override]  # @memoized_property causes override issue
    name = "hstore_to_array"
    inherit_cache = True

class _HStoreMatrixFunction(sqlfunc.GenericFunction):
    @memoized_property
    def type(self) -> ARRAY: ...  # type: ignore[override]  # @memoized_property causes override issue
    name = "hstore_to_matrix"
    inherit_cache = True
