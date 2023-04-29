import decimal
from _typeshed import Incomplete, SupportsGetItem, Unused
from collections.abc import Callable
from datetime import date, datetime, time, timedelta
from pickle import Pickler
from typing import Any, Generic, TypeVar, overload
from typing_extensions import Literal, Self

from ..engine import Connection, Engine
from ..engine.interfaces import Connectable, Dialect
from ..sql.elements import BinaryExpression, quoted_name
from ..sql.schema import MetaData
from .base import SchemaEventTarget
from .traversals import HasCacheKey
from .type_api import (
    Emulated as Emulated,
    NativeForEmulated as NativeForEmulated,
    TypeDecorator as TypeDecorator,
    TypeEngine as TypeEngine,
    Variant as Variant,
    to_instance as to_instance,
)

_T = TypeVar("_T")

class _LookupExpressionAdapter:
    class Comparator(TypeEngine.Comparator[_T]): ...
    comparator_factory: Callable[[Incomplete], Comparator[Incomplete]]

class Concatenable:
    class Comparator(TypeEngine.Comparator[_T]): ...
    comparator_factory: Callable[[Incomplete], Comparator[Incomplete]]

class Indexable:
    class Comparator(TypeEngine.Comparator[_T]):
        def __getitem__(self, index: SupportsGetItem[Any, _T]) -> BinaryExpression: ...  # type: ignore[override]  # _T doesn't match
    comparator_factory: Callable[[Incomplete], Comparator[Incomplete]]

class String(Concatenable, TypeEngine):
    __visit_name__: str
    RETURNS_UNICODE: Any
    RETURNS_BYTES: Any
    RETURNS_CONDITIONAL: Any
    RETURNS_UNKNOWN: Any
    length: int | None
    collation: str | None
    # If unicode_error is not None, convert_unicode must be "force"
    @overload
    def __init__(
        self,
        length: int | None = None,
        collation: str | None = None,
        *,
        convert_unicode: Literal["force"],
        unicode_error: str,
        _warn_on_bytestring: bool = False,
        _expect_unicode: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self,
        length: int | None = None,
        collation: str | None = None,
        convert_unicode: str | bool = False,
        unicode_error: None = None,
        _warn_on_bytestring: bool = False,
        _expect_unicode: bool = False,
    ) -> None: ...
    def literal_processor(self, dialect: Dialect) -> Callable[[str], str]: ...
    def bind_processor(self, dialect: Dialect) -> Callable[[str], str] | None: ...
    def result_processor(self, dialect: Dialect, coltype) -> Callable[[Incomplete | None], str | None] | None: ...
    @property
    def python_type(self) -> type[str]: ...
    def get_dbapi_type(self, dbapi): ...

class Text(String):
    __visit_name__: str

class Unicode(String):
    __visit_name__: str
    def __init__(self, length: int | None = None, **kwargs) -> None: ...

class UnicodeText(Text):
    __visit_name__: str
    def __init__(self, length: int | None = None, **kwargs) -> None: ...

class Integer(_LookupExpressionAdapter, TypeEngine):
    __visit_name__: str
    def get_dbapi_type(self, dbapi): ...
    @property
    def python_type(self) -> type: ...
    def literal_processor(self, dialect: Dialect) -> Callable[[int], str]: ...

class SmallInteger(Integer):
    __visit_name__: str

class BigInteger(Integer):
    __visit_name__: str

class Numeric(_LookupExpressionAdapter, TypeEngine):
    __visit_name__: str
    precision: int | None
    scale: int | None
    decimal_return_scale: int | None
    asdecimal: bool
    def __init__(
        self,
        precision: int | None = None,
        scale: int | None = None,
        decimal_return_scale: int | None = None,
        asdecimal: bool = True,
    ) -> None: ...
    def get_dbapi_type(self, dbapi): ...
    def literal_processor(self, dialect: Dialect) -> Callable[[float | decimal.Decimal], str]: ...
    @property
    def python_type(self) -> type[float | decimal.Decimal]: ...
    def bind_processor(self, dialect: Dialect) -> Callable[[str | None], decimal.Decimal] | None: ...
    def result_processor(
        self, dialect: Dialect, coltype
    ) -> Callable[[Incomplete | None], float | decimal.Decimal | None] | None: ...

class Float(Numeric):
    __visit_name__: str
    scale: None
    precision: int | None
    asdecimal: bool
    decimal_return_scale: int | None
    def __init__(
        self, precision: int | None = None, asdecimal: bool = False, decimal_return_scale: int | None = None
    ) -> None: ...
    def result_processor(
        self, dialect: Dialect, coltype
    ) -> Callable[[Incomplete | None], float | decimal.Decimal | None] | None: ...

class DateTime(_LookupExpressionAdapter, TypeEngine):
    __visit_name__: str
    timezone: bool
    def __init__(self, timezone: bool = False) -> None: ...
    def get_dbapi_type(self, dbapi): ...
    @property
    def python_type(self) -> type[datetime]: ...

class Date(_LookupExpressionAdapter, TypeEngine):
    __visit_name__: str
    def get_dbapi_type(self, dbapi): ...
    @property
    def python_type(self) -> type[date]: ...

class Time(_LookupExpressionAdapter, TypeEngine):
    __visit_name__: str
    timezone: bool
    def __init__(self, timezone: bool = False) -> None: ...
    def get_dbapi_type(self, dbapi): ...
    @property
    def python_type(self) -> type[time]: ...

class _Binary(TypeEngine):
    length: int
    def __init__(self, length: int | None = None) -> None: ...
    def literal_processor(self, dialect: Dialect) -> Callable[[bytes], str]: ...
    @property
    def python_type(self) -> type[bytes]: ...
    def bind_processor(self, dialect: Dialect) -> Callable[[bytes], Incomplete] | None: ...
    def result_processor(self, dialect: Dialect, coltype) -> Callable[[Incomplete | None], bytes | None] | None: ...
    def coerce_compared_value(self, op, value) -> Self | TypeEngine: ...
    def get_dbapi_type(self, dbapi): ...

class LargeBinary(_Binary):
    __visit_name__: str
    def __init__(self, length: int | None = None) -> None: ...

class SchemaType(SchemaEventTarget):
    name: quoted_name | None
    schema: str | None
    metadata: MetaData | None
    inherit_schema: bool
    def __init__(
        self,
        name: str | None = None,
        schema: str | None = None,
        metadata: MetaData | None = None,
        inherit_schema: bool = False,
        quote: bool | None = None,
        _create_events: bool = True,
    ) -> None: ...
    def copy(self, **kw: Unused) -> Self: ...
    def adapt(self, impltype: type[_T], **kw) -> _T: ...
    @property
    def bind(self) -> Engine | Connection | None: ...
    def create(self, bind: Connectable | None = None, checkfirst: bool = False) -> None: ...
    def drop(self, bind: Connectable | None = None, checkfirst: bool = False) -> None: ...

class Enum(Emulated, String, SchemaType):
    __visit_name__: str
    native_enum: bool
    create_constraint: bool
    values_callable: Incomplete | None
    validate_strings: bool
    enums: list[str]
    enum_class: Incomplete | None
    def __init__(self, *enums, **kw) -> None: ...
    @property
    def sort_key_function(self): ...
    @property
    def native(self) -> bool: ...

    class Comparator(Concatenable.Comparator[_T]): ...
    comparator_factory: Callable[[Incomplete], Comparator[Incomplete]]
    def as_generic(self, allow_nulltype: bool = False): ...
    def adapt_to_emulated(self, impltype: type[_T], **kw) -> _T: ...
    def adapt(self, impltype: type[Incomplete], **kw): ...  # type: ignore[override]
    def literal_processor(self, dialect: Dialect): ...
    def bind_processor(self, dialect: Dialect): ...
    def result_processor(self, dialect: Dialect, coltype): ...
    def copy(self, **kw: Unused) -> Self: ...  # type: ignore[override]
    @property
    def python_type(self): ...

class PickleType(TypeDecorator):
    impl: type[LargeBinary] | Incomplete
    cache_ok: bool
    protocol: int
    pickler: Pickler
    comparator: Any
    def __init__(
        self,
        protocol: int = 5,
        pickler: Pickler | None = None,
        comparator: Callable[[Any, Any], bool] | None = None,
        impl: type[Incomplete] | Incomplete | None = None,
    ) -> None: ...
    def __reduce__(self): ...
    def bind_processor(self, dialect: Dialect) -> Callable[[Incomplete | None], str | None]: ...
    def result_processor(self, dialect: Dialect, coltype) -> Callable[[Incomplete | None], Incomplete]: ...
    def compare_values(self, x: object, y: object) -> bool: ...

class Boolean(Emulated, TypeEngine, SchemaType):  # type: ignore[misc]
    __visit_name__: str
    native: bool
    create_constraint: bool
    name: str | None  # type: ignore[assignment]
    def __init__(self, create_constraint: bool = False, name: str | None = None, _create_events: bool = True) -> None: ...
    @property
    def python_type(self) -> type[bool]: ...
    def literal_processor(self, dialect: Dialect) -> Callable[[bool | None], str]: ...
    def bind_processor(self, dialect: Dialect) -> Callable[[bool | None], bool | int | None]: ...
    def result_processor(self, dialect: Dialect, coltype) -> Callable[[int | None], bool] | None: ...

class _AbstractInterval(_LookupExpressionAdapter, TypeEngine):
    def coerce_compared_value(self, op, value) -> TypeEngine: ...

class Interval(Emulated, _AbstractInterval, TypeDecorator):  # type: ignore[misc]
    impl: Any  # impl is Type[TypeEngine[DateTime]] on the class, but TypeEngine[DateTime] on instances
    epoch: datetime
    cache_ok: bool
    native: bool
    second_precision: float | None
    day_precision: float | None
    def __init__(
        self, native: bool = True, second_precision: float | None = None, day_precision: float | None = None
    ) -> None: ...
    @property
    def python_type(self) -> type[timedelta]: ...
    def adapt_to_emulated(self, impltype: type[Incomplete], **kw): ...
    def bind_processor(self, dialect: Dialect) -> Callable[[timedelta | None], str]: ...
    def result_processor(self, dialect: Dialect, coltype) -> Callable[[str | None], timedelta | None]: ...

class JSON(Indexable, TypeEngine):
    __visit_name__: str
    hashable: bool
    NULL: Any
    none_as_null: bool
    def __init__(self, none_as_null: bool = False) -> None: ...

    class JSONElementType(TypeEngine):
        def string_bind_processor(self, dialect: Dialect): ...
        def string_literal_processor(self, dialect: Dialect): ...
        def bind_processor(self, dialect: Dialect): ...
        def literal_processor(self, dialect: Dialect): ...

    class JSONIndexType(JSONElementType): ...
    class JSONIntIndexType(JSONIndexType): ...
    class JSONStrIndexType(JSONIndexType): ...
    class JSONPathType(JSONElementType): ...

    class Comparator(Indexable.Comparator[_T], Concatenable.Comparator[_T]):
        def as_boolean(self) -> BinaryExpression: ...
        def as_string(self) -> BinaryExpression: ...
        def as_integer(self) -> BinaryExpression: ...
        def as_float(self) -> BinaryExpression: ...
        def as_numeric(self, precision, scale, asdecimal: bool = True) -> BinaryExpression: ...
        def as_json(self): ...
    comparator_factory: Callable[[Incomplete], Comparator[Incomplete]]
    @property
    def python_type(self) -> type: ...
    @property  # type: ignore[override]
    def should_evaluate_none(self) -> bool: ...
    @should_evaluate_none.setter
    def should_evaluate_none(self, value: bool) -> None: ...
    def bind_processor(self, dialect: Dialect) -> Callable[[Incomplete | None], str | None]: ...
    def result_processor(self, dialect: Dialect, coltype) -> Callable[[str | None], Incomplete | None] | None: ...

class ARRAY(SchemaEventTarget, Indexable, Concatenable, TypeEngine):
    __visit_name__: str
    zero_indexes: bool

    class Comparator(Indexable.Comparator[_T], Concatenable.Comparator[_T], Generic[_T]):
        def contains(self, other: str, **kwargs) -> BinaryExpression: ...
        def any(self, other, operator: Incomplete | None = None) -> BinaryExpression: ...
        def all(self, other, operator: Incomplete | None = None) -> BinaryExpression: ...

    comparator_factory: Callable[[Incomplete], Comparator[Incomplete]]
    item_type: TypeEngine
    as_tuple: bool
    dimensions: int | None
    def __init__(
        self,
        item_type: TypeEngine | type[TypeEngine],  # Not[ARRAY]
        as_tuple: bool = False,
        dimensions: int | None = None,
        zero_indexes: bool = False,
    ) -> None: ...
    @property
    def hashable(self) -> bool: ...  # type: ignore[override]  # supertype is attribute
    @property
    def python_type(self) -> type[list[Incomplete]]: ...
    def compare_values(self, x: object, y: object) -> bool: ...

class TupleType(TypeEngine):
    types: Any
    def __init__(self, *types) -> None: ...
    def result_processor(self, dialect: Dialect, coltype) -> None: ...

class REAL(Float):
    __visit_name__: str

class FLOAT(Float):
    __visit_name__: str

class NUMERIC(Numeric):
    __visit_name__: str

class DECIMAL(Numeric):
    __visit_name__: str

class INTEGER(Integer):
    __visit_name__: str

INT = INTEGER

class SMALLINT(SmallInteger):
    __visit_name__: str

class BIGINT(BigInteger):
    __visit_name__: str

class TIMESTAMP(DateTime):
    __visit_name__: str
    def __init__(self, timezone: bool = False) -> None: ...
    def get_dbapi_type(self, dbapi): ...

class DATETIME(DateTime):
    __visit_name__: str

class DATE(Date):
    __visit_name__: str

class TIME(Time):
    __visit_name__: str

class TEXT(Text):
    __visit_name__: str

class CLOB(Text):
    __visit_name__: str

class VARCHAR(String):
    __visit_name__: str

class NVARCHAR(Unicode):
    __visit_name__: str

class CHAR(String):
    __visit_name__: str

class NCHAR(Unicode):
    __visit_name__: str

class BLOB(LargeBinary):
    __visit_name__: str

class BINARY(_Binary):
    __visit_name__: str

class VARBINARY(_Binary):
    __visit_name__: str

class BOOLEAN(Boolean):
    __visit_name__: str

class NullType(TypeEngine):
    __visit_name__: str
    def literal_processor(self, dialect: Unused) -> None: ...

    class Comparator(TypeEngine.Comparator[_T]): ...
    comparator_factory: Callable[[Incomplete], Comparator[Incomplete]]

class TableValueType(HasCacheKey, TypeEngine):
    def __init__(self, *elements) -> None: ...

class MatchType(Boolean): ...

NULLTYPE: NullType
BOOLEANTYPE: Boolean
STRINGTYPE: String
INTEGERTYPE: Integer
NUMERICTYPE: Numeric
MATCHTYPE: MatchType
TABLEVALUE: TableValueType
DATETIME_TIMEZONE: DateTime
TIME_TIMEZONE: Time
