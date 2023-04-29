from _typeshed import Incomplete
from collections.abc import Callable
from typing import TypeVar
from typing_extensions import Final

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
    def __init__(self, text_type: TypeEngine | None = None) -> None: ...

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
    name: Final = "hstore"
    inherit_cache: bool

class _HStoreDefinedFunction(sqlfunc.GenericFunction):
    @memoized_property
    def type(self) -> type[sqltypes.Boolean]: ...  # type: ignore[override]  # @memoized_property causes override issue
    name: Final = "defined"
    inherit_cache: bool

class _HStoreDeleteFunction(sqlfunc.GenericFunction):
    @memoized_property
    def type(self) -> type[HSTORE]: ...  # type: ignore[override]  # @memoized_property causes override issue
    name: Final = "delete"
    inherit_cache: bool

class _HStoreSliceFunction(sqlfunc.GenericFunction):
    @memoized_property
    def type(self) -> type[HSTORE]: ...  # type: ignore[override]  # @memoized_property causes override issue
    name: Final = "slice"
    inherit_cache: bool

class _HStoreKeysFunction(sqlfunc.GenericFunction):
    @memoized_property
    def type(self) -> ARRAY: ...  # type: ignore[override]  # @memoized_property causes override issue
    name: Final = "akeys"
    inherit_cache: bool

class _HStoreValsFunction(sqlfunc.GenericFunction):
    @memoized_property
    def type(self) -> ARRAY: ...  # type: ignore[override]  # @memoized_property causes override issue
    name: Final = "avals"
    inherit_cache: bool

class _HStoreArrayFunction(sqlfunc.GenericFunction):
    @memoized_property
    def type(self) -> ARRAY: ...  # type: ignore[override]  # @memoized_property causes override issue
    name: Final = "hstore_to_array"
    inherit_cache: bool

class _HStoreMatrixFunction(sqlfunc.GenericFunction):
    @memoized_property
    def type(self) -> ARRAY: ...  # type: ignore[override]  # @memoized_property causes override issue
    name: Final = "hstore_to_matrix"
    inherit_cache: bool
