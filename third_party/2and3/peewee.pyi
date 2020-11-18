from bisect import bisect_left
from bisect import bisect_right
from contextlib import contextmanager
from functools import wraps
from typing import Any
from typing import AnyStr
from typing import Callable
from typing import ClassVar
from typing import Container
from typing import ContextManager
from typing import Dict
from typing import Generic
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Mapping
from typing import MutableMapping
from typing import MutableSet
from typing import NamedTuple
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Set
from typing import Sequence
from typing import Text
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union
import calendar
import collections
import datetime
import decimal
import operator
import re
import threading
import time
import uuid

from typing_extensions import Literal
from typing_extensions import Protocol

T = TypeVar("T")
__TModel = TypeVar("__TModel", bound="Model")
__TConvFunc = Callable[[Any], Any]
__TFunc = TypeVar("__TFunc", bound=Callable)
__TClass = TypeVar("__TClass", bound=type)
__TModelOrTable = Union[Type["Model"], "ModelAlias", "Table"]
__TSubquery = Union[Tuple["Query", Type["Model"]], Type["Model"], "ModelAlias"]
__TContextClass = TypeVar("__TContextClass", bound="Context")
__TField = TypeVar("__TField", bound="Field")
__TFieldOrModel = Union[__TModelOrTable, "Field"]
__TNode = TypeVar("__TNode", bound="Node")

__version__: str
__all__: List[str]

class __ICursor(Protocol):
    description: Tuple[str, Any, Any, Any, Any, Any, Any]
    rowcount: int
    def fetchone(self) -> Optional[tuple]: ...
    def fetchmany(self, size: int = ...) -> Iterable[tuple]: ...
    def fetchall(self) -> Iterable[tuple]: ...

class __IConnection(Protocol):
    def cursor(self) -> __ICursor: ...
    def execute(self, sql: str, *args: object) -> __ICursor: ...
    def commit(self) -> Any: ...
    def rollback(self) -> Any: ...

def _sqlite_date_part(lookup_type: str, datetime_string: str) -> Optional[str]: ...
def _sqlite_date_trunc(lookup_type: str, datetime_string: str) -> Optional[str]: ...

class attrdict(dict):
    def __getattr__(self, attr: str) -> Any: ...
    def __setattr__(self, attr: str, value: Any) -> None: ...
    def __iadd__(self, rhs: Mapping[str, object]) -> attrdict: ...
    def __add__(self, rhs: Mapping[str, object]) -> Mapping[str, object]: ...

SENTINEL: object

OP: attrdict

DJANGO_MAP: attrdict

FIELD: attrdict

JOIN: attrdict

ROW: attrdict

SCOPE_NORMAL: int
SCOPE_SOURCE: int
SCOPE_VALUES: int
SCOPE_CTE: int
SCOPE_COLUMN: int

CSQ_PARENTHESES_NEVER: int
CSQ_PARENTHESES_ALWAYS: int
CSQ_PARENTHESES_UNNESTED: int

SNAKE_CASE_STEP1: re.Pattern
SNAKE_CASE_STEP2: re.Pattern

MODEL_BASE: str

# TODO (dargueta)
class _callable_context_manager(object):
    def __call__(self, fn):
        @wraps(fn)
        def inner(*args, **kwargs):
            with self:
                return fn(*args, **kwargs)
        return inner

class Proxy(object):
    obj: Any
    def initialize(self, obj: Any) -> None: ...
    def attach_callback(self, callback: __TConvFunc) -> __TConvFunc: ...
    def passthrough(method: __TFunc) -> __TFunc: ...
    def __enter__(self) -> Any: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> Any: ...
    def __getattr__(self, attr: str) -> Any: ...
    def __setattr__(self, attr: str, value: Any) -> None: ...

class DatabaseProxy(Proxy):
    def connection_context(self) -> ConnectionContext: ...
    def atomic(self, *args: object, **kwargs: object) -> _atomic: ...
    def manual_commit(self) -> _manual: ...
    def transaction(self, *args: object, **kwargs: object) -> _transaction: ...
    def savepoint(self) -> _savepoint: ...

class ModelDescriptor(object): ...

# SQL Generation.

class AliasManager(object):
    @property
    def mapping(self) -> MutableMapping["Source", str]: ...
    def add(self, source: Source) -> str: ...
    def get(self, source: Source, any_depth: bool = ...) -> str: ...
    def __getitem__(self, source: Source) -> str: ...
    def __setitem__(self, source: Source, alias: str) -> None: ...
    def push(self) -> None: ...
    def pop(self) -> None: ...

class __State(NamedTuple):
    scope: int
    parentheses: bool
    # From the source code we know this to be a Dict and not just a MutableMapping.
    settings: Dict[str, Any]

class State(__State):
    def __new__(cls, scope: int = ..., parentheses: bool = ..., **kwargs: object) -> State: ...
    def __call__(self, scope: Optional[int] = ..., parentheses: Optional[int] = ..., **kwargs: object) -> State: ...
    def __getattr__(self, attr_name: str) -> Any: ...

class Context(object):
    stack: List[State]
    alias_manager: AliasManager
    state: State
    def __init__(self, **settings: Any) -> None: ...
    def as_new(self) -> Context: ...
    def column_sort_key(self, item: Sequence[Union[ColumnBase, Source]]) -> Tuple[str, ...]: ...
    @property
    def scope(self) -> int: ...
    @property
    def parentheses(self) -> bool: ...
    @property
    def subquery(self):
        return self.state.subquery
    def __call__(self, **overrides: Any) -> Context: ...
    def scope_normal(self) -> ContextManager[Context]: ...
    def scope_source(self) -> ContextManager[Context]: ...
    def scope_values(self) -> ContextManager[Context]: ...
    def scope_cte(self) -> ContextManager[Context]: ...
    def scope_column(self) -> ContextManager[Context]: ...
    def __enter__(self) -> Context: ...
    def __exit__(self, exc_type: Type[Exception], exc_val: Exception, exc_tb: Any) -> None: ...
    @contextmanager
    def push_alias(self) -> Iterator[None]: ...
    # TODO (dargueta): Is this right?
    def sql(self, obj: Any) -> Context: ...
    def literal(self, keyword: str) -> Context: ...
    def value(self, value: Any, converter: Optional[__TConvFunc] = ..., add_param: bool = ...) -> Context: ...
    def __sql__(self, ctx: Context) -> Context: ...
    def parse(self, node: Node) -> Tuple[str, Optional[tuple]]: ...
    def query(self) -> Tuple[str, Optional[tuple]]: ...

def query_to_string(query: Node) -> str: ...

class Node(object):
    def clone(self) -> Node: ...
    def __sql__(self, ctx: Context) -> Context: ...
    # FIXME (dargueta): Is there a way to make this a proper decorator?
    @staticmethod
    def copy(method: __TFunc) -> __TFunc:
        def inner(self: T, *args: object, **kwargs: object) -> T:
            clone = self.clone()
            method(clone, *args, **kwargs)
            return clone
        return inner
    def coerce(self, _coerce: bool = ...) -> Node: ...
    def is_alias(self) -> bool: ...
    def unwrap(self) -> Node: ...

class ColumnFactory(object):
    node: Node
    def __init__(self, node: Node): ...
    def __getattr__(self, attr: str) -> Column: ...

class _DynamicColumn(object):
    @overload
    def __get__(self, instance: None, instance_type: type) -> _DynamicColumn: ...
    @overload
    def __get__(self, instance: T, instance_type: Type[T]) -> ColumnFactory: ...

class _ExplicitColumn(object):
    @overload
    def __get__(self, instance: None, instance_type: type) -> _ExplicitColumn: ...
    @overload
    def __get__(self, instance: T, instance_type: Type[T]) -> NoReturn: ...

class Source(Node):
    c: ClassVar[_DynamicColumn]
    def __init__(self, alias: Optional[str] = ...): ...
    def alias(self, name: str) -> Source: ...
    def select(self, *columns: Field) -> Select: ...
    def join(self, dest, join_type: int = ..., on: Optional[Expression] = ...) -> Join: ...
    def left_outer_join(self, dest, on: Optional[Expression] = ...) -> Join: ...
    def cte(self, name: str, recursive: bool = ..., columns=None, materialized=None) -> CTE: ...
    def get_sort_key(self, ctx) -> Tuple[str, ...]: ...
    def apply_alias(self, ctx: Context) -> Context: ...
    def apply_column(self, ctx: Context) -> Context: ...

class _HashableSource(object):
    def __init__(self, *args: object, **kwargs: object): ...
    def alias(self, name: str) -> _HashableSource: ...
    def __hash__(self) -> int: ...
    @overload
    def __eq__(self, other: _HashableSource) -> bool: ...
    @overload
    def __eq__(self, other: Any) -> Expression: ...
    @overload
    def __ne__(self, other: _HashableSource) -> bool: ...
    @overload
    def __ne__(self, other: Any) -> Expression: ...
    def __lt__(self, other: Any) -> Expression: ...
    def __le__(self, other: Any) -> Expression: ...
    def __gt__(self, other: Any) -> Expression: ...
    def __ge__(self, other: Any) -> Expression: ...

def __join__(join_type: int = ..., inverted: bool = ...) -> Callable[[Any, Any], Join]: ...

class BaseTable(Source):
    def __and__(self, other: Any) -> Join: ...
    def __add__(self, other: Any) -> Join: ...
    def __sub__(self, other: Any) -> Join: ...
    def __or__(self, other: Any) -> Join: ...
    def __mul__(self, other: Any) -> Join: ...
    def __rand__(self, other: Any) -> Join: ...
    def __radd__(self, other: Any) -> Join: ...
    def __rsub__(self, other: Any) -> Join: ...
    def __ror__(self, other: Any) -> Join: ...
    def __rmul__(self, other: Any) -> Join: ...

class _BoundTableContext(_callable_context_manager):
    table: Table
    database: Database
    def __init__(self, table: Table, database: Database): ...
    def __enter__(self) -> Table: ...
    def __exit__(self, exc_type: Type[Exception], exc_val: Exception, exc_tb: Any) -> None: ...

class Table(_HashableSource, BaseTable):
    __name__: str
    c: _ExplicitColumn
    primary_key: Optional[Union[Field, CompositeKey]]
    def __init__(
        self,
        name: str,
        columns: Optional[Iterable[str]] = ...,
        primary_key: Optional[Union[Field, CompositeKey]] = ...,
        schema: Optional[str] = ...,
        alias: Optional[str] = ...,
        _model: Optional[Type[Model]] = ...,
        _database: Optional[Database] = ...,
    ): ...
    def clone(self) -> Table: ...
    def bind(self, database: Optional[Database] = ...) -> Table: ...
    def bind_ctx(self, database: Optional[Database] = ...) -> _BoundTableContext: ...
    def select(self, *columns: Column) -> Select: ...
    @overload
    def insert(self, insert: Optional[Select], columns: Sequence[Union[str, Field, Column]]) -> Insert: ...
    @overload
    def insert(self, insert: Union[Mapping[str, object], Iterable[Mapping[str, object]]], **kwargs: object): ...
    @overload
    def replace(self, insert: Optional[Select], columns: Sequence[Union[str, Field, Column]]) -> Insert: ...
    @overload
    def replace(self, insert: Union[Mapping[str, object], Iterable[Mapping[str, object]]], **kwargs: object): ...
    def update(self, update: Optional[Mapping[str, object]] = ..., **kwargs: object) -> Update: ...
    def delete(self) -> Delete: ...
    def __sql__(self, ctx: Context) -> Context: ...

class Join(BaseTable):
    lhs: Any  # TODO
    rhs: Any  # TODO
    join_type: int
    def __init__(self, lhs, rhs, join_type: int = ..., on: Optional[Expression] = ..., alias: Optional[str] = ...): ...
    def on(self, predicate: Expression) -> Join: ...
    def __sql__(self, ctx: Context) -> Context: ...

class ValuesList(_HashableSource, BaseTable):
    def __init__(self, values, columns=None, alias: Optional[str] = ...): ...
    # FIXME (dargueta) `names` might be wrong
    def columns(self, *names: str) -> ValuesList: ...
    def __sql__(self, ctx: Context) -> Context: ...

class CTE(_HashableSource, Source):
    def __init__(
        self,
        name: str,
        query: Select,
        recursive: bool = ...,
        columns: Optional[Iterable[Union[Column, Field, str]]] = ...,
        materialized: bool = ...,
    ): ...
    # TODO (dargueta): Is `columns` just for column names?
    def select_from(self, *columns: Union[Column, Field]) -> Select: ...
    def _get_hash(self) -> int: ...
    def union_all(self, rhs) -> CTE: ...
    __add__ = union_all
    def union(self, rhs: SelectQuery) -> CTE: ...
    __or__ = union
    def __sql__(self, ctx: Context) -> Context: ...

class ColumnBase(Node):
    _converter: Optional[__TConvFunc]
    def converter(self, converter: Optional[__TConvFunc] = ...) -> ColumnBase: ...
    @overload
    def alias(self, alias: None) -> ColumnBase: ...
    @overload
    def alias(self, alias: str) -> Alias: ...
    def unalias(self) -> ColumnBase: ...
    def cast(self, as_type: str) -> Cast: ...
    def asc(self, collation: Optional[str] = ..., nulls: Optional[str] = ...) -> Asc: ...
    __pos__ = asc
    def desc(self, collation: Optional[str] = ..., nulls: Optional[str] = ...) -> Desc: ...
    __neg__ = desc
    def __invert__(self) -> Negated: ...
    def __and__(self, other: Any) -> Expression: ...
    def __or__(self, other: Any) -> Expression: ...
    def __add__(self, other: Any) -> Expression: ...
    def __sub__(self, other: Any) -> Expression: ...
    def __mul__(self, other: Any) -> Expression: ...
    def __div__(self, other: Any) -> Expression: ...
    def __truediv__(self, other: Any) -> Expression: ...
    def __xor__(self, other: Any) -> Expression: ...
    def __radd__(self, other: Any) -> Expression: ...
    def __rsub__(self, other: Any) -> Expression: ...
    def __rmul__(self, other: Any) -> Expression: ...
    def __rdiv__(self, other: Any) -> Expression: ...
    def __rtruediv__(self, other: Any) -> Expression: ...
    def __rand__(self, other: Any) -> Expression: ...
    def __ror__(self, other: Any) -> Expression: ...
    def __rxor__(self, other: Any) -> Expression: ...
    def __eq__(self, rhs: Optional["Node"]) -> Expression: ...
    def __ne__(self, rhs: Optional[Node]) -> Expression: ...
    def __lt__(self, other: Any) -> Expression: ...
    def __le__(self, other: Any) -> Expression: ...
    def __gt__(self, other: Any) -> Expression: ...
    def __ge__(self, other: Any) -> Expression: ...
    def __lshift__(self, other: Any) -> Expression: ...
    def __rshift__(self, other: Any) -> Expression: ...
    def __mod__(self, other: Any) -> Expression: ...
    def __pow__(self, other: Any) -> Expression: ...
    def bin_and(self, other: Any) -> Expression: ...
    def bin_or(self, other: Any) -> Expression: ...
    def in_(self, other: Any) -> Expression: ...
    def not_in(self, other: Any) -> Expression: ...
    def regexp(self, other: Any) -> Expression: ...
    def is_null(self, is_null: bool = ...) -> Expression: ...
    def contains(self, rhs: Union[Node, str]) -> Expression: ...
    def startswith(self, rhs: Union[Node, str]) -> Expression: ...
    def endswith(self, rhs: Union[Node, str]) -> Expression: ...
    def between(self, lo: Any, hi: Any) -> Expression: ...
    def concat(self, rhs: Any) -> StringExpression: ...
    def iregexp(self, rhs: Any) -> Expression: ...
    def __getitem__(self, item: Any) -> Expression: ...
    def distinct(self) -> NodeList: ...
    def collate(self, collation: str) -> NodeList: ...
    def get_sort_key(self, ctx: Context) -> Tuple[str, ...]: ...

class Column(ColumnBase):
    source: Source
    name: str
    def __init__(self, source: Source, name: str): ...
    def get_sort_key(self, ctx: Context) -> Tuple[str, ...]: ...
    def __hash__(self) -> int: ...
    def __sql__(self, ctx: Context) -> Context: ...

class WrappedNode(ColumnBase, Generic[__TNode]):
    node: __TNode
    _coerce: bool
    _converter: Optional[__TConvFunc]
    def __init__(self, node: __TNode): ...
    def is_alias(self) -> bool: ...
    def unwrap(self) -> __TNode: ...

class EntityFactory(object):
    node: Node
    def __init__(self, node: Node): ...
    def __getattr__(self, attr: str) -> Entity: ...

class _DynamicEntity(object):
    __slots__ = ()
    @overload
    def __get__(self, instance: None, instance_type: type) -> _DynamicEntity: ...
    @overload
    def __get__(self, instance: T, instance_type: Type[T]) -> EntityFactory: ...

class Alias(WrappedNode):
    c: ClassVar[_DynamicEntity]
    def __init__(self, node: Node, alias: str): ...
    def __hash__(self) -> int: ...
    @overload
    def alias(self, alias: None) -> Node: ...
    @overload
    def alias(self, alias: str) -> Alias: ...
    def unalias(self) -> Node: ...
    def is_alias(self) -> bool: ...
    def __sql__(self, ctx: Context) -> Context: ...

class Negated(WrappedNode):
    def __invert__(self) -> Node: ...
    def __sql__(self, ctx: Context) -> Context: ...

class BitwiseMixin(object):
    def __and__(self, other):
        return self.bin_and(other)
    def __or__(self, other):
        return self.bin_or(other)
    def __sub__(self, other):
        return self.bin_and(other.bin_negated())
    def __invert__(self) -> BitwiseNegated: ...

class BitwiseNegated(BitwiseMixin, WrappedNode):
    def __invert__(self) -> Node: ...
    def __sql__(self, ctx: Context) -> Context: ...

class Value(ColumnBase):
    value: object
    converter: Optional[__TConvFunc]
    multi: bool
    def __init__(self, value: object, converter: Optional[__TConvFunc] = ..., unpack: bool = ...):
        self.value = value
        self.converter = converter
        self.multi = unpack and isinstance(self.value, multi_types)
        if self.multi:
            self.values = []
            for item in self.value:
                if isinstance(item, Node):
                    self.values.append(item)
                else:
                    self.values.append(Value(item, self.converter))
    def __sql__(self, ctx):
        if self.multi:
            # For multi-part values (e.g. lists of IDs).
            return ctx.sql(EnclosedNodeList(self.values))

        return ctx.value(self.value, self.converter)

def AsIs(value: object) -> Value: ...

class Cast(WrappedNode):
    def __init__(self, node: Node, cast: str): ...
    def __sql__(self, ctx: Context) -> Context: ...

class Ordering(WrappedNode):
    direction: str
    collation: Optional[str]
    nulls: Optional[str]
    def __init__(self, node: Node, direction: str, collation: Optional[str] = ..., nulls: Optional[str] = ...): ...
    def collate(self, collation: Optional[str] = ...) -> Ordering: ...
    def __sql__(self, ctx: Context) -> Context: ...

def Asc(node: Node, collation: Optional[str] = ..., nulls: Optional[str] = ...) -> Ordering: ...
def Desc(node: Node, collation: Optional[str] = ..., nulls: Optional[str] = ...) -> Ordering: ...

class Expression(ColumnBase):
    lhs: Optional[Union[Node, str]]
    op: int
    rhs: Optional[Union[Node, str]]
    flat: bool
    def __init__(self, lhs: Optional[Union[Node, str]], op: int, rhs: Optional[Union[Node, str]], flat: bool = ...): ...
    def __sql__(self, ctx: Context) -> Context: ...

class StringExpression(Expression):
    def __add__(self, rhs: Any) -> StringExpression: ...
    def __radd__(self, lhs: Any) -> StringExpression: ...

class Entity(ColumnBase):
    def __init__(self, *path: str): ...
    def __getattr__(self, attr: str) -> Entity: ...
    def get_sort_key(self, ctx: Context) -> Tuple[str, ...]: ...
    def __hash__(self) -> int: ...
    def __sql__(self, ctx: Context) -> Context: ...

class SQL(ColumnBase):
    sql: str
    params: Optional[Mapping[str, object]]
    def __init__(self, sql: str, params: Mapping[str, object] = ...): ...
    def __sql__(self, ctx: Context) -> Context: ...

def Check(constraint: str) -> SQL:
    return SQL("CHECK (%s)" % constraint)

class Function(ColumnBase):
    name: str
    arguments: tuple
    def __init__(self, name: str, arguments: tuple, coerce: bool = ..., python_value: Optional[__TConvFunc] = ...): ...
    def __getattr__(self, attr: str) -> Callable[..., Function]: ...
    # TODO (dargueta): `where` is an educated guess
    def filter(self, where: Optional[Expression] = ...) -> Function: ...
    def order_by(self, *ordering) -> Function:
        self._order_by = ordering
    def python_value(self, func: Optional[__TConvFunc] = ...) -> Function: ...
    def over(
        self,
        partition_by: Optional[Union[Sequence[Field], Window]] = ...,
        order_by: Optional[Sequence[Union[Field, Expression]]] = ...,
        start: Optional[Union[str, SQL]] = ...,
        end: Optional[Union[str, SQL]] = ...,
        frame_type: Optional[str] = ...,
        window: Optional[Window] = ...,
        exclude: Optional[SQL] = ...,
    ) -> NodeList: ...
    def __sql__(self, ctx: Context) -> Context: ...

fn: Function

class Window(Node):
    CURRENT_ROW: ClassVar[SQL]
    GROUP: ClassVar[SQL]
    TIES: ClassVar[SQL]
    NO_OTHERS: ClassVar[SQL]
    GROUPS: ClassVar[str]
    RANGE: ClassVar[str]
    ROWS: ClassVar[str]
    # Instance variables
    partition_by: Tuple[Union[Field, Expression], ...]
    order_by: Tuple[Union[Field, Expression], ...]
    start: Optional[Union[str, SQL]]
    end: Optional[Union[str, SQL]]
    frame_type: Optional[Any]  # TODO
    @overload
    def __init__(
        self,
        partition_by: Optional[Union[Sequence[Field], Window]] = ...,
        order_by: Optional[Sequence[Union[Field, Expression]]] = ...,
        start: Optional[Union[str, SQL]] = ...,
        end: None = ...,
        frame_type: Optional[str] = ...,
        extends: Optional[Union[Window, WindowAlias, str]] = ...,
        exclude: Optional[SQL] = ...,
        alias: Optional[str] = ...,
        _inline: bool = ...,
    ): ...
    @overload
    def __init__(
        self,
        partition_by: Optional[Union[Sequence[Field], Window]] = ...,
        order_by: Optional[Sequence[Union[Field, Expression]]] = ...,
        start: Union[str, SQL] = ...,
        end: Union[str, SQL] = ...,
        frame_type: Optional[str] = ...,
        extends: Optional[Union[Window, WindowAlias, str]] = ...,
        exclude: Optional[SQL] = ...,
        alias: Optional[str] = ...,
        _inline: bool = ...,
    ): ...
    def alias(self, alias: Optional[str] = ...) -> Window: ...
    def as_range(self) -> Window: ...
    def as_rows(self) -> Window: ...
    def as_groups(self) -> Window: ...
    def extends(self, window: Optional[Union[Window, WindowAlias, str]] = ...) -> Window: ...
    def exclude(self, frame_exclusion: Optional[Union[str, SQL]] = ...) -> Window: ...
    @staticmethod
    def following(value: Optional[int] = ...) -> SQL: ...
    @staticmethod
    def preceding(value: Optional[int] = ...) -> SQL: ...
    def __sql__(self, ctx: Context) -> Context: ...

class WindowAlias(Node):
    window: Window
    def __init__(self, window: Window): ...
    def alias(self, window_alias: str) -> WindowAlias: ...
    def __sql__(self, ctx: Context) -> Context: ...

class ForUpdate(Node):
    def __init__(
        self,
        expr: Union[Literal[True], str],
        of: Optional[Union[__TModelOrTable, List[__TModelOrTable], Set[__TModelOrTable], Tuple[__TModelOrTable, ...]]] = ...,
        nowait: Optional[bool] = ...,
    ): ...
    def __sql__(self, ctx: Context) -> Context: ...

def Case(predicate: Optional[Node], expression_tuples: Iterable[Tuple[Expression, Any]], default: Any = ...) -> NodeList: ...

class NodeList(ColumnBase):
    nodes: Sequence[Any]  # TODO (dargueta): Narrow this type
    glue: str
    parens: bool
    def __init__(self, nodes: Sequence[Any], glue: str = ..., parens: bool = ...): ...
    def __sql__(self, ctx: Context) -> Context: ...

def CommaNodeList(nodes: Sequence[Any]) -> NodeList: ...
def EnclosedNodeList(nodes: Sequence[Any]) -> NodeList: ...

class _Namespace(Node):
    def __init__(self, name: str): ...
    def __getattr__(self, attr: str) -> NamespaceAttribute: ...
    def __getitem__(self, attr: str) -> NamespaceAttribute: ...

class NamespaceAttribute(ColumnBase):
    def __init__(self, namespace: _Namespace, attribute: str): ...
    def __sql__(self, ctx: Context) -> Context: ...

EXCLUDED: _Namespace

class DQ(ColumnBase):
    query: Dict[str, Any]

    # TODO (dargueta): Narrow this down?
    def __init__(self, **query: Any): ...
    def __invert__(self) -> DQ: ...
    def clone(self) -> DQ: ...

class QualifiedNames(WrappedNode):
    def __sql__(self, ctx: Context) -> Context: ...

@overload
def qualify_names(node: Expression) -> Expression: ...
@overload
def qualify_names(node: ColumnBase) -> QualifiedNames: ...
@overload
def qualify_names(node: T) -> T: ...

class OnConflict(Node):
    @overload
    def __init__(
        self,
        action: Optional[str] = ...,
        update: Optional[Mapping[str, object]] = ...,
        preserve: Optional[Union[Field, Iterable[Field]]] = ...,
        where: Optional[Expression] = ...,
        conflict_target: Optional[Union[Field, Sequence[Field]]] = ...,
        conflict_where: None = ...,
        conflict_constraint: Optional[str] = ...,
    ): ...
    @overload
    def __init__(
        self,
        action: Optional[str] = ...,
        update: Optional[Mapping[str, object]] = ...,
        preserve: Optional[Union[Field, Iterable[Field]]] = ...,
        where: Optional[Expression] = ...,
        conflict_target: None = ...,
        conflict_where: Optional[Expression] = ...,
        conflict_constraint: Optional[str] = ...,
    ): ...
    # undocumented
    def get_conflict_statement(self, ctx: Context, query: Query):
        return ctx.state.conflict_statement(self, query)
    def get_conflict_update(self, ctx, query):
        return ctx.state.conflict_update(self, query)
    def preserve(self, *columns) -> OnConflict: ...
    def update(self, _data: Optional[Mapping[str, object]] = ..., **kwargs: object) -> OnConflict: ...
    def where(self, *expressions: Expression) -> OnConflict: ...
    def conflict_target(self, *constraints) -> OnConflict: ...
    def conflict_where(self, *expressions: Expression) -> OnConflict: ...
    def conflict_constraint(self, constraint: str) -> OnConflict: ...

# BASE QUERY INTERFACE.

class BaseQuery(Node):
    default_row_type: ClassVar[int]
    def __init__(self, _database: Optional[Database] = ..., **kwargs: object): ...
    def bind(self, database: Optional[Database] = ...) -> BaseQuery: ...
    def clone(self) -> BaseQuery: ...
    def dicts(self, as_dict: bool = ...) -> BaseQuery: ...
    def tuples(self, as_tuple: bool = ...) -> BaseQuery: ...
    def namedtuples(self, as_namedtuple: bool = ...) -> BaseQuery: ...
    def objects(self, constructor: Optional[__TConvFunc] = ...) -> BaseQuery: ...
    def __sql__(self, ctx: Context) -> Context: ...
    def sql(self) -> Tuple[str, Optional[tuple]]: ...
    def execute(self, database: Optional[Database] = ...) -> CursorWrapper: ...
    # TODO (dargueta): `Any` is too loose; list types of the cursor wrappers
    def iterator(self, database: Optional[Database] = ...) -> Iterator[Any]: ...
    def __iter__(self) -> Iterator[Any]: ...
    @overload
    def __getitem__(self, value: int) -> Any: ...
    @overload
    def __getitem__(self, value: slice) -> Sequence[Any]: ...
    def __len__(self) -> int: ...
    def __str__(self) -> str: ...

class RawQuery(BaseQuery):
    # TODO (dargueta): `tuple` may not be 100% accurate, maybe Sequence[object]?
    def __init__(self, sql: Optional[str] = ..., params: Optional[tuple] = ..., **kwargs: object): ...
    def __sql__(self, ctx: Context) -> Context: ...

class Query(BaseQuery):
    # TODO (dargueta): Verify type of order_by
    def __init__(
        self,
        where: Optional[Expression] = ...,
        order_by: Optional[Sequence[Node]] = ...,
        limit: Optional[int] = ...,
        offset: Optional[int] = ...,
        **kwargs: object,
    ): ...
    def with_cte(self, *cte_list: CTE) -> Query: ...
    def where(self, *expressions: Expression) -> Query: ...
    def orwhere(self, *expressions: Expression) -> Query: ...
    def order_by(self, *values: Node) -> Query: ...
    def order_by_extend(self, *values: Node) -> Query: ...
    def limit(self, value: Optional[int] = ...) -> Query: ...
    def offset(self, value: Optional[int] = ...) -> Query: ...
    def paginate(self, page: int, paginate_by: int = ...) -> Query: ...
    def _apply_ordering(self, ctx: Context) -> Context: ...
    def __sql__(self, ctx: Context) -> Context: ...

def __compound_select__(operation: str, inverted: bool = ...) -> Callable[[Any, Any], CompoundSelectQuery]: ...

class SelectQuery(Query):
    def union_all(self, other: object) -> CompoundSelectQuery: ...
    def union(self, other: object) -> CompoundSelectQuery: ...
    def intersect(self, other: object) -> CompoundSelectQuery: ...
    def except_(self, other: object) -> CompoundSelectQuery: ...
    def __add__(self, other: object) -> CompoundSelectQuery: ...
    def __or__(self, other: object) -> CompoundSelectQuery: ...
    def __and__(self, other: object) -> CompoundSelectQuery: ...
    def __sub__(self, other: object) -> CompoundSelectQuery: ...
    def __radd__(self, other: object) -> CompoundSelectQuery: ...
    def __ror__(self, other: object) -> CompoundSelectQuery: ...
    def __rand__(self, other: object) -> CompoundSelectQuery: ...
    def __rsub__(self, other: object) -> CompoundSelectQuery: ...
    def select_from(self, *columns: Field) -> Select: ...

class SelectBase(_HashableSource, Source, SelectQuery):
    @overload
    def peek(self, database: Optional[Database] = ..., n: Literal[1] = ...) -> Any: ...
    @overload
    def peek(self, database: Optional[Database] = ..., n: int = ...) -> List[Any]: ...
    @overload
    def first(self, database: Optional[Database] = ..., n: Literal[1] = ...) -> Any: ...
    @overload
    def first(self, database: Optional[Database] = ..., n: int = ...) -> List[Any]: ...
    @overload
    def scalar(self, database: Optional[Database] = ..., as_tuple: Literal[False] = ...) -> Any: ...
    @overload
    def scalar(self, database: Optional[Database] = ..., as_tuple: Literal[True] = ...) -> tuple: ...
    def count(self, database: Optional[Database] = ..., clear_limit: bool = ...) -> int: ...
    def exists(self, database: Optional[Database] = ...) -> bool: ...
    def get(self, database: Optional[Database] = ...) -> Any: ...

# QUERY IMPLEMENTATIONS.

class CompoundSelectQuery(SelectBase):
    lhs: Any  # TODO (dargueta)
    op: str
    rhs: Any  # TODO (dargueta)
    def __init__(self, lhs: Any, op: str, rhs: Any): ...
    def exists(self, database: Optional[Database] = ...) -> bool: ...
    def __sql__(self, ctx: Context) -> Context: ...

class Select(SelectBase):
    def __init__(
        self,
        from_list: Optional[Sequence[Union[Column, Field]]] = ...,  # TODO (dargueta): `Field` might be wrong
        columns: Optional[Iterable[Union[Column, Field]]] = ...,  # TODO (dargueta): `Field` might be wrong
        # Docs say this is a "[l]ist of columns or values to group by" so we don't have
        # a whole lot to restrict this to thanks to "or values"
        group_by: Sequence[Any] = ...,
        having: Optional[Expression] = ...,
        distinct: Optional[Union[bool, Sequence[Column]]] = ...,
        windows: Optional[Container[Window]] = ...,
        for_update: Optional[Union[bool, str]] = ...,
        for_update_of: Optional[Union[Table, Iterable[Table]]] = ...,
        nowait: Optional[bool] = ...,
        lateral: Optional[bool] = ...,  # undocumented
        **kwargs: object,
    ): ...
    def clone(self) -> Select: ...
    def columns(self, *columns, **kwargs: object) -> Select:
        self._returning = columns
    select = columns
    def select_extend(self, *columns) -> Select:
        self._returning = tuple(self._returning) + columns
    # TODO (dargueta): Is `sources` right?
    def from_(self, *sources: Union[Source, Type[Model]]) -> Select: ...
    def join(self, dest: Type[Model], join_type: int = ..., on: Optional[Expression] = ...) -> Select: ...
    def group_by(self, *columns: Union[Table, Field]) -> Select: ...
    def group_by_extend(self, *values: Union[Table, Field]) -> Select: ...
    def having(self, *expressions: Expression) -> Select: ...
    @overload
    def distinct(self, _: bool) -> Select: ...
    @overload
    def distinct(self, *columns: Field) -> Select: ...
    def window(self, *windows: Window) -> Select: ...
    def for_update(self, for_update: bool = ..., of=None, nowait=None) -> Select:
        if not for_update and (of is not None or nowait):
            for_update = True
        self._for_update = for_update
        self._for_update_of = of
        self._for_update_nowait = nowait
    def lateral(self, lateral: bool = ...) -> Select: ...

class _WriteQuery(Query):
    table: Table
    def __init__(self, table: Table, returning: Optional[Iterable[Union[Type[Model], Field]]] = ..., **kwargs: object): ...
    def returning(self, *returning: Union[Type[Model], Field]) -> _WriteQuery: ...
    def apply_returning(self, ctx: Context) -> Context: ...
    def execute_returning(self, database: Database) -> CursorWrapper: ...
    def handle_result(self, database: Database, cursor: __ICursor) -> Union[int, __ICursor]: ...
    def __sql__(self, ctx: Context) -> Context: ...

class Update(_WriteQuery):
    def __init__(self, table: Table, update=None, **kwargs):
        super(Update, self).__init__(table, **kwargs)
        self._update = update
        self._from = None
    @Node.copy
    def from_(self, *sources) -> None:
        self._from = sources
    def __sql__(self, ctx: Context) -> Context: ...

class Insert(_WriteQuery):
    SIMPLE: ClassVar[int]
    QUERY: ClassVar[int]
    MULTI: ClassVar[int]
    DefaultValuesException: Type[Exception]
    def __init__(
        self,
        table: Table,
        insert: Optional[Union[Mapping[str, object], Iterable[Mapping[str, object]], SelectQuery, SQL]] = ...,
        columns: Optional[Iterable[Union[str, Field]]] = ...,  # FIXME: Might be `Column` not `Field`
        on_conflict: Optional[OnConflict] = ...,
        **kwargs: object,
    ): ...
    def where(self, *expressions: Expression) -> NoReturn: ...
    def on_conflict_ignore(self, ignore: bool = ...) -> Insert: ...
    def on_conflict_replace(self, replace: bool = ...) -> Insert: ...
    def on_conflict(self, *args, **kwargs) -> Insert: ...
    def get_default_data(self) -> dict: ...
    def get_default_columns(self) -> Optional[List[Field]]: ...
    def __sql__(self, ctx: Context) -> Context: ...
    def handle_result(self, database: Database, cursor: __ICursor) -> Union[__ICursor, int]: ...

class Delete(_WriteQuery):
    def __sql__(self, ctx: Context) -> Context: ...

class Index(Node):
    def __init__(
        self,
        name: str,
        table,
        expressions,
        unique: bool = ...,
        safe: bool = ...,
        where: Optional[Expression] = ...,
        using: Optional[str] = ...,
    ): ...
    def safe(self, _safe: bool = ...) -> Index: ...
    def where(self, *expressions: Expression) -> Index: ...
    def using(self, _using: Optional[str] = ...) -> Index: ...
    def __sql__(self, ctx: Context) -> Context: ...

class ModelIndex(Index):
    def __init__(
        self,
        model: Type[__TModel],
        fields: Iterable[Union[Field, Node, str]],
        unique: bool = ...,
        safe: bool = ...,
        where: Optional[Expression] = ...,
        using: Optional[str] = ...,
        name: Optional[str] = ...,
    ): ...

# DB-API 2.0 EXCEPTIONS.

class PeeweeException(Exception):
    # This attribute only exists if an exception was passed into the constructor.
    # Attempting to access it otherwise will result in an AttributeError.
    orig: Exception
    def __init__(self, *args: object): ...

class ImproperlyConfigured(PeeweeException): ...
class DatabaseError(PeeweeException): ...
class DataError(DatabaseError): ...
class IntegrityError(DatabaseError): ...
class InterfaceError(PeeweeException): ...
class InternalError(DatabaseError): ...
class NotSupportedError(DatabaseError): ...
class OperationalError(DatabaseError): ...
class ProgrammingError(DatabaseError): ...

class ExceptionWrapper(object):
    exceptions: Mapping[str, Type[Exception]]
    def __init__(self, exceptions: Mapping[str, Type[Exception]]): ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Type[Exception], exc_value: Exception, traceback: Any) -> None: ...

EXCEPTIONS: Mapping[str, Type[Exception]]

__exception_wrapper__: ExceptionWrapper

class IndexMetadata(NamedTuple):
    name: str
    sql: str
    columns: List[str]
    unique: bool
    table: str

class ColumnMetadata(NamedTuple):
    name: str
    data_type: str
    null: bool
    primary_key: bool
    table: str
    default: object

class ForeignKeyMetadata(NamedTuple):
    column: str
    dest_table: str
    dest_column: str
    table: str

class ViewMetadata(NamedTuple):
    name: str
    sql: str

class _ConnectionState(object):
    closed: bool
    conn: Optional[__IConnection]
    ctx: List[ConnectionContext]
    transactions: List[Union[_manual, _transaction]]
    def reset(self) -> None: ...
    def set_connection(self, conn: __IConnection) -> None: ...

class _ConnectionLocal(_ConnectionState, threading.local): ...

class ConnectionContext(_callable_context_manager):
    __slots__ = ("db",)
    def __init__(self, db):
        self.db = db
    def __enter__(self):
        if self.db.is_closed():
            self.db.connect()
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()

class Database(_callable_context_manager):
    context_class: ClassVar[Type[__TContextClass]]
    field_types: ClassVar[Mapping[str, str]]
    operations: ClassVar[Mapping[str, Any]]  # TODO (dargueta) Verify k/v types
    param: ClassVar[str]
    quote: ClassVar[str]
    server_version: ClassVar[Optional[Tuple[int, ...]]]
    commit_select: ClassVar[bool]
    compound_select_parentheses: ClassVar[int]
    for_update: ClassVar[bool]
    index_schema_prefix: ClassVar[bool]
    index_using_precedes_table: ClassVar[bool]
    limit_max: ClassVar[Optional[int]]
    nulls_ordering: ClassVar[bool]
    returning_clause: ClassVar[bool]
    safe_create_index: ClassVar[bool]
    safe_drop_index: ClassVar[bool]
    sequences: ClassVar[bool]
    truncate_table: ClassVar[bool]
    # Instance variables
    database: __IConnection
    deferred: bool
    autoconnect: bool
    autorollback: bool
    thread_safe: bool
    connect_params: Mapping[str, Any]
    server_version: Optional[Union[int, Tuple[int, ...]]]
    def __init__(
        self,
        database: __IConnection,
        thread_safe: bool = ...,
        autorollback: bool = ...,
        field_types: Optional[Mapping[str, str]] = ...,
        operations: Optional[Mapping[str, str]] = ...,
        autocommit: bool = ...,
        autoconnect: bool = ...,
        **kwargs: object,
    ): ...
    def init(self, database: __IConnection, **kwargs: object) -> None: ...
    def __enter__(self) -> Database: ...
    def __exit__(self, exc_type: Type[Exception], exc_val: Exception, exc_tb: Any) -> None: ...
    def connection_context(self) -> ConnectionContext: ...
    def connect(self, reuse_if_open: bool = ...) -> bool: ...
    def close(self) -> bool: ...
    def is_closed(self) -> bool: ...
    def is_connection_usable(self) -> bool: ...
    def connection(self) -> __IConnection: ...
    def cursor(self, commit: Optional[bool] = ...) -> __ICursor: ...
    def execute_sql(self, sql: str, params: Optional[tuple] = ..., commit: Union[bool, Literal[SENTINEL]] = ...) -> __ICursor: ...
    def execute(self, query: Query, commit: Union[bool, Literal[SENTINEL]] = ..., **context_options: Any) -> __ICursor: ...
    def get_context_options(self) -> Mapping[str, object]: ...
    def get_sql_context(self, **context_options: Any):
        context = self.get_context_options()
        if context_options:
            context.update(context_options)
        return self.context_class(**context)
    def conflict_statement(self, on_conflict: OnConflict, query: Query) -> Optional[SQL]: ...
    def conflict_update(self, oc: OnConflict, query: Query) -> NodeList: ...
    def last_insert_id(self, cursor: __ICursor, query_type: Optional[int] = ...) -> int: ...
    def rows_affected(self, cursor: __ICursor) -> int: ...
    def default_values_insert(self, ctx: Context) -> Context: ...
    def session_start(self) -> _transaction: ...
    def session_commit(self) -> bool: ...
    def session_rollback(self) -> bool: ...
    def in_transaction(self) -> bool: ...
    def push_transaction(self, transaction) -> None: ...
    def pop_transaction(self) -> Union[_manual, _transaction]: ...
    def transaction_depth(self) -> int: ...
    def top_transaction(self) -> Optional[Union[_manual, _transaction]]: ...
    def atomic(self, *args: object, **kwargs: object) -> _atomic: ...
    def manual_commit(self) -> _manual: ...
    def transaction(self, *args: object, **kwargs: object) -> _transaction: ...
    def savepoint(self) -> _savepoint: ...
    def begin(self) -> None: ...
    def commit(self) -> None: ...
    def rollback(self) -> None: ...
    def batch_commit(self, it: Iterable[T], n: int) -> Iterator[T]: ...
    def table_exists(self, table_name: str, schema: Optional[str] = ...) -> str: ...
    def get_tables(self, schema: Optional[str] = ...) -> List[str]: ...
    def get_indexes(self, table: str, schema: Optional[str] = ...) -> List[IndexMetadata]: ...
    def get_columns(self, table: str, schema: Optional[str] = ...) -> List[ColumnMetadata]: ...
    def get_primary_keys(self, table: str, schema: Optional[str] = ...) -> List[str]: ...
    def get_foreign_keys(self, table: str, schema: Optional[str] = ...) -> List[ForeignKeyMetadata]: ...
    def sequence_exists(self, seq: str) -> bool: ...
    def create_tables(self, models, **options):
        for model in sort_models(models):
            model.create_table(**options)
    def drop_tables(self, models, **kwargs):
        for model in reversed(sort_models(models)):
            model.drop_table(**kwargs)
    def extract_date(self, date_part: str, date_field: Node) -> Node: ...
    def truncate_date(self, date_part: str, date_field: Node) -> Node: ...
    def to_timestamp(self, date_field: str) -> Node: ...
    def from_timestamp(self, date_field: str) -> Node: ...
    def random(self) -> Node: ...
    def bind(self, models: Iterable[Type[Model]], bind_refs: bool = ..., bind_backrefs: bool = ...) -> None: ...
    def bind_ctx(
        self, models: Iterable[Type[Model]], bind_refs: bool = ..., bind_backrefs: bool = ...
    ) -> _BoundModelsContext: ...
    def get_noop_select(self, ctx: Context) -> Context: ...

def __pragma__(name):
    def __get__(self):
        return self.pragma(name)
    def __set__(self, value):
        return self.pragma(name, value)
    return property(__get__, __set__)

class SqliteDatabase(Database):
    field_types: ClassVar[Mapping[str, int]]
    operations: ClassVar[Mapping[str, str]]
    index_schema_prefix: ClassVar[bool]
    limit_max: ClassVar[int]
    server_version: ClassVar[Tuple[int, ...]]
    truncate_table: ClassVar[bool]
    # Instance variables
    timeout: int
    nulls_ordering: bool
    # Properties
    cache_size: int
    def __init__(
        self,
        database: str,
        *args: object,
        pragmas: Union[Mapping[str, object], Iterable[Tuple[str, Any]]] = ...,
        **kwargs: object,
    ): ...
    def init(
        self,
        database: str,
        pragmas: Optional[Union[Mapping[str, object], Iterable[Tuple[str, Any]]]] = ...,
        timeout: int = ...,
        **kwargs: object,
    ) -> None: ...
    def pragma(self, key: str, value: Union[str, bool, int] = ..., permanent: bool = ..., schema: Optional[str] = ...) -> Any: ...
    foreign_keys = __pragma__("foreign_keys")
    journal_mode = __pragma__("journal_mode")
    journal_size_limit = __pragma__("journal_size_limit")
    mmap_size = __pragma__("mmap_size")
    page_size = __pragma__("page_size")
    read_uncommitted = __pragma__("read_uncommitted")
    synchronous = __pragma__("synchronous")
    wal_autocheckpoint = __pragma__("wal_autocheckpoint")
    def register_aggregate(self, klass, name=None, num_params=-1):
        self._aggregates[name or klass.__name__.lower()] = (klass, num_params)
        if not self.is_closed():
            self._load_aggregates(self.connection())
    def aggregate(self, name: Optional[str] = ..., num_params: int = ...) -> Callable[[__TClass], __TClass]: ...
    def register_collation(self, fn: Callable, name: Optional[str] = ...) -> None: ...
    def collation(self, name: Optional[str] = ...) -> Callable[[__TFunc], __TFunc]: ...
    def register_function(self, fn: Callable, name: Optional[str] = ..., num_params: int = ...) -> int: ...
    def func(self, name: Optional[str] = ..., num_params: int = ...) -> Callable[[__TFunc], __TFunc]: ...
    def register_window_function(self, klass: type, name: Optional[str] = ..., num_params: int = ...) -> None: ...
    def window_function(self, name: Optional[str] = ..., num_params: int = ...) -> Callable[[__TClass], __TClass]: ...
    def register_table_function(self, klass, name=None):
        if name is not None:
            klass.name = name
        self._table_functions.append(klass)
        if not self.is_closed():
            klass.register(self.connection())
    def table_function(self, name=None):
        def decorator(klass):
            self.register_table_function(klass, name)
            return klass
        return decorator
    def unregister_aggregate(self, name: str) -> None: ...
    def unregister_collation(self, name: str) -> None: ...
    def unregister_function(self, name: str) -> None: ...
    def unregister_window_function(self, name: str) -> None: ...
    def unregister_table_function(self, name: str) -> bool: ...
    def load_extension(self, extension: str) -> None: ...
    def unload_extension(self, extension: str) -> None: ...
    def attach(self, filename: str, name: str) -> bool: ...
    def detach(self, name: str) -> bool: ...
    def begin(self, lock_type: Optional[str] = ...) -> None: ...
    def get_views(self, schema: Optional[str] = ...) -> List[ViewMetadata]: ...
    def get_binary_type(self) -> type: ...

class PostgresqlDatabase(Database):
    field_types: ClassVar[Mapping[str, str]]
    operations: ClassVar[Mapping[str, str]]
    param: ClassVar[str]
    commit_select: ClassVar[bool]
    compound_select_parentheses: ClassVar[int]
    for_update: ClassVar[bool]
    nulls_ordering: ClassVar[bool]
    returning_clause: ClassVar[bool]
    safe_create_index: ClassVar[bool]
    sequences: ClassVar[bool]
    # Instance variables
    server_version: int
    # Technically this *only* exists if we have Postgres >=9.6 and it will always be
    # True in that case.
    safe_create_index: bool
    def init(
        self,
        database: __IConnection,
        register_unicode: bool = ...,
        encoding: Optional[str] = ...,
        isolation_level: Optional[int] = ...,
        **kwargs: object,
    ): ...
    def is_connection_usable(self) -> bool: ...
    @overload
    def last_insert_id(self, cursor: __ICursor, query_type: Literal[Insert.SIMPLE] = ...) -> Optional[int]: ...  # I think
    @overload
    def last_insert_id(self, cursor: __ICursor, query_type: Optional[int] = ...) -> __ICursor: ...
    def get_views(self, schema: Optional[str] = ...) -> List[ViewMetadata]: ...
    def get_binary_type(self) -> type: ...
    def get_noop_select(self, ctx: Context) -> SelectQuery: ...
    def set_time_zone(self, timezone: str) -> None: ...

class MySQLDatabase(Database):
    field_types: ClassVar[Mapping[str, str]]
    operations: ClassVar[Mapping[str, str]]
    param: ClassVar[str]
    quote: ClassVar[str]
    commit_select: ClassVar[bool]
    compound_select_parentheses: ClassVar[int]
    for_update: ClassVar[bool]
    index_using_precedes_table: ClassVar[bool]
    limit_max = 2 ** 64 - 1
    safe_create_index: ClassVar[bool]
    safe_drop_index: ClassVar[bool]
    sql_mode: ClassVar[str]
    # Instance variables
    server_version: Tuple[int, ...]
    def init(self, database: __IConnection, **kwargs: object): ...
    def default_values_insert(self, ctx: Context) -> SQL: ...
    def get_views(self, schema: Optional[str] = ...) -> List[ViewMetadata]: ...
    def get_binary_type(self) -> type: ...
    def extract_date(self, date_part, date_field):
        return fn.EXTRACT(NodeList((SQL(date_part), SQL("FROM"), date_field)))
    def truncate_date(self, date_part, date_field):
        return fn.DATE_FORMAT(date_field, __mysql_date_trunc__[date_part], python_value=simple_date_time)
    def to_timestamp(self, date_field):
        return fn.UNIX_TIMESTAMP(date_field)
    def from_timestamp(self, date_field):
        return fn.FROM_UNIXTIME(date_field)
    def random(self):
        return fn.rand()
    def get_noop_select(self, ctx):
        return ctx.literal("DO 0")

# TRANSACTION CONTROL.

class _manual(_callable_context_manager):
    db: Database
    def __init__(self, db: Database): ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Type[Exception], exc_val: Exception, exc_tb: Any) -> None: ...

class _atomic(_callable_context_manager):
    db: Database
    def __init__(self, db: Database, *args: object, **kwargs: object): ...
    def __enter__(self) -> Union[_transaction, _savepoint]: ...
    def __exit__(self, exc_type: Type[Exception], exc_val: Exception, exc_tb: Any) -> None: ...

class _transaction(_callable_context_manager):
    db: Database
    def __init__(self, db: Database, *args: object, **kwargs: object): ...
    def commit(self, begin: bool = ...) -> None: ...
    def rollback(self, begin: bool = ...) -> None: ...
    def __enter__(self) -> _transaction: ...
    def __exit__(self, exc_type: Type[Exception], exc_val: Exception, exc_tb: Any) -> None: ...

class _savepoint(_callable_context_manager):
    db: Database
    sid: str
    quoted_sid: str
    def __init__(self, db: Database, sid: Optional[str] = ...): ...
    def commit(self, begin: bool = ...) -> None: ...
    def rollback(self) -> None: ...
    def __enter__(self) -> _savepoint: ...
    def __exit__(self, exc_type: Type[Exception], exc_val: Exception, exc_tb: Any) -> None: ...

class CursorWrapper(Generic[T]):
    cursor: __ICursor
    count: int
    index: int
    initialized: bool
    populated: bool
    row_cache: List[T]
    def __init__(self, cursor: __ICursor): ...
    def __iter__(self) -> Union[ResultIterator[T], Iterator[T]]: ...
    @overload
    def __getitem__(self, item: int) -> T: ...
    @overload
    def __getitem__(self, item: slice) -> List[T]: ...
    def __len__(self) -> int: ...
    def initialize(self) -> None: ...
    def iterate(self, cache=True):
        row = self.cursor.fetchone()
        if row is None:
            self.populated = True
            self.cursor.close()
            raise StopIteration
        elif not self.initialized:
            self.initialize()  # Lazy initialization.
            self.initialized = True
        self.count += 1
        result = self.process_row(row)
        if cache:
            self.row_cache.append(result)
        return result
    def process_row(self, row: tuple) -> T: ...
    def iterator(self):
        """Efficient one-pass iteration over the result set."""
        while True:
            try:
                yield self.iterate(False)
            except StopIteration:
                return
    def fill_cache(self, n: int = 0) -> None: ...

class DictCursorWrapper(CursorWrapper[Mapping[str, object]]): ...

class NamedTupleCursorWrapper(CursorWrapper[NamedTuple]):
    tuple_class: Type[NamedTuple]

# TODO: Indicate this inherits from DictCursorWrapper but also change the return type
class ObjectCursorWrapper(DictCursorWrapper):
    def __init__(self, cursor, constructor):
        super(ObjectCursorWrapper, self).__init__(cursor)
        self.constructor = constructor
    def process_row(self, row):
        row_dict = self._row_to_dict(row)
        return self.constructor(**row_dict)

class ResultIterator(Generic[T]):
    cursor_wrapper: CursorWrapper[T]
    index: int
    def __init__(self, cursor_wrapper: CursorWrapper[T]): ...
    def __iter__(self) -> Iterator[T]: ...

# FIELDS

class FieldAccessor(object):
    model: Type[Model]
    field: Field
    name: str
    def __init__(self, model: Type[Model], field: Field, name: str): ...
    @overload
    def __get__(self, instance: None, instance_type: type) -> Field: ...
    @overload
    def __get__(self, instance: T, instance_type: Type[T]) -> Any: ...

class ForeignKeyAccessor(FieldAccessor):
    model: Type[Model]
    field: ForeignKeyField
    name: str
    rel_model: Type[Model]
    def __init__(self, model: Type[Model], field: ForeignKeyField, name: str): ...
    def get_rel_instance(self, instance: Model) -> Any:
        value = instance.__data__.get(self.name)
        if value is not None or self.name in instance.__rel__:
            if self.name not in instance.__rel__:
                obj = self.rel_model.get(self.field.rel_field == value)
                instance.__rel__[self.name] = obj
            return instance.__rel__[self.name]
        elif not self.field.null:
            raise self.rel_model.DoesNotExist
        return value
    def __get__(self, instance, instance_type=None):
        if instance is not None:
            return self.get_rel_instance(instance)
        return self.field
    def __set__(self, instance, obj):
        if isinstance(obj, self.rel_model):
            instance.__data__[self.name] = getattr(obj, self.field.rel_field.name)
            instance.__rel__[self.name] = obj
        else:
            fk_value = instance.__data__.get(self.name)
            instance.__data__[self.name] = obj
            if obj != fk_value and self.name in instance.__rel__:
                del instance.__rel__[self.name]
        instance._dirty.add(self.name)

class NoQueryForeignKeyAccessor(ForeignKeyAccessor):
    def get_rel_instance(self, instance: Model) -> Any:
        value = instance.__data__.get(self.name)
        if value is not None:
            return instance.__rel__.get(self.name, value)
        elif not self.field.null:
            raise self.rel_model.DoesNotExist

class BackrefAccessor(object):
    field: ForeignKeyField
    model: Type[Model]
    rel_model: Type[Model]
    def __init__(self, field: ForeignKeyField): ...
    @overload
    def __get__(self, instance: None, instance_type: type) -> BackrefAccessor: ...
    @overload
    def __get__(self, instance: Field, instance_type: Type["Field"]) -> SelectQuery: ...

class ObjectIdAccessor(object):
    """Gives direct access to the underlying id"""

    field: ForeignKeyField
    def __init__(self, field: ForeignKeyField): ...
    @overload
    def __get__(self, instance: None, instance_type: Type[Model]) -> ForeignKeyField: ...
    @overload
    def __get__(self, instance: __TModel, instance_type: Type[__TModel] = ...) -> Any: ...
    def __set__(self, instance: Model, value: Any) -> None: ...

class Field(ColumnBase):
    accessor_class: ClassVar[Type[FieldAccessor]]
    auto_increment: ClassVar[bool]
    default_index_type: ClassVar[Optional[str]]
    field_type: ClassVar[str]
    unpack: ClassVar[bool]
    # Instance variables
    model: Type[Model]
    null: bool
    index: bool
    unique: bool
    column_name: str
    default: Any
    primary_key: bool
    constraints: Optional[Iterable[Check, SQL]]
    sequence: Optional[str]
    collation: Optional[str]
    unindexed: bool
    help_text: Optional[str]
    verbose_name: Optional[str]
    index_type: Optional[str]
    def __init__(
        self,
        null: bool = ...,
        index: bool = ...,
        unique: bool = ...,
        column_name: str = ...,
        default: Any = ...,
        primary_key: bool = ...,
        constraints: Optional[Iterable[Check, SQL]] = ...,
        sequence: Optional[str] = ...,
        collation: Optional[str] = ...,
        unindexed: Optional[bool] = ...,
        choices: Optional[Iterable[Tuple[Any, str]]] = ...,
        help_text: Optional[str] = ...,
        verbose_name: Optional[str] = ...,
        index_type: Optional[str] = ...,
        db_column: Optional[str] = ...,  # Deprecated argument, undocumented
        _hidden: bool = ...,
    ): ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def bind(self, model: Type[Model], name: str, set_attribute: bool = ...) -> None: ...
    @property
    def column(self) -> Column: ...
    def adapt(self, value: T) -> T: ...
    def db_value(self, value: T) -> T: ...
    def python_value(self, value: T) -> T: ...
    def to_value(self, value: Any) -> Value: ...
    def get_sort_key(self, ctx: Context) -> Tuple[int, int]: ...
    def __sql__(self, ctx: Context) -> Context: ...
    def get_modifiers(self) -> None: ...
    def ddl_datatype(self, ctx: Context) -> SQL: ...
    def ddl(self, ctx: Context) -> NodeList: ...

class IntegerField(Field):
    @overload
    def adapt(self, value: Union[int, str, float, bool]) -> int: ...
    @overload
    def adapt(self, value: T) -> T: ...

class BigIntegerField(IntegerField): ...
class SmallIntegerField(IntegerField): ...

class AutoField(IntegerField):
    def __init__(self, *args: object, primary_key: bool = ..., **kwargs: object): ...

class BigAutoField(AutoField): ...

class IdentityField(AutoField):
    def __init__(self, generate_always: bool = ..., **kwargs: object): ...

class PrimaryKeyField(AutoField): ...

class FloatField(Field):
    @overload
    def adapt(self, value: Union[str, int, float, bool]) -> float: ...
    @overload
    def adapt(self, value: T) -> T: ...

class DoubleField(FloatField): ...

class DecimalField(Field):
    max_digits: int
    decimal_places: int
    auto_round: int
    rounding: bool
    def __init__(
        self,
        max_digits: int = ...,
        decimal_places: int = ...,
        auto_round: bool = ...,
        rounding: bool = ...,
        *args: object,
        **kwargs: object,
    ): ...
    def get_modifiers(self) -> List[int]: ...
    @overload
    def db_value(self, value: None) -> None: ...
    @overload
    def db_value(self, value: Union[int, float, decimal.Decimal]) -> decimal.Decimal: ...
    @overload
    def db_value(self, value: T) -> T: ...
    @overload
    def python_value(self, value: None) -> None: ...
    @overload
    def python_value(self, value: Union[int, str, float, decimal.Decimal]) -> decimal.Decimal: ...

class _StringField(Field):
    def adapt(self, value: AnyStr) -> str: ...
    def __add__(self, other: Any) -> StringExpression: ...
    def __radd__(self, other: Any) -> StringExpression: ...

class CharField(_StringField):
    max_length: int
    def __init__(self, max_length: int = ..., *args: object, **kwargs: object): ...
    def get_modifiers(self) -> Optional[List[int]]: ...

class FixedCharField(CharField): ...
class TextField(_StringField): ...

class BlobField(Field):
    @overload
    def db_value(self, value: Union[str, bytes]) -> bytearray: ...
    @overload
    def db_value(self, value: T) -> T: ...

class BitField(BitwiseMixin, BigIntegerField):
    def __init__(self, *args: object, default: Optional[int] = ..., **kwargs: object): ...
    # FIXME (dargueta) Return type isn't 100% accurate; function creates a new class
    def flag(self, value: Optional[int] = ...) -> ColumnBase: ...

class BigBitFieldData(object):
    def __init__(self, instance, name):
        self.instance = instance
        self.name = name
        value = self.instance.__data__.get(self.name)
        if not value:
            value = bytearray()
        elif not isinstance(value, bytearray):
            value = bytearray(value)
        self._buffer = self.instance.__data__[self.name] = value
    def set_bit(self, idx: int) -> None: ...
    def clear_bit(self, idx: bool) -> None: ...
    def toggle_bit(self, idx: int) -> bool: ...
    def is_set(self, idx: int) -> bool: ...
    def __repr__(self) -> str: ...

class BigBitFieldAccessor(FieldAccessor):
    def __get__(self, instance, instance_type=None):
        if instance is None:
            return self.field
        return BigBitFieldData(instance, self.name)
    def __set__(self, instance: Any, value: Union[memoryview, bytearray, BigBitFieldData, str, bytes]) -> None: ...

class BigBitField(BlobField):
    accessor_class: ClassVar[Type[BigBitFieldAccessor]]
    def __init__(self, *args: object, default: type = ..., **kwargs: object): ...
    @overload
    def db_value(self, value: None) -> None: ...
    @overload
    def db_value(self, value: T) -> bytes: ...

class UUIDField(Field):
    @overload
    def db_value(self, value: AnyStr) -> str: ...
    @overload
    def db_value(self, value: T) -> T: ...
    def python_value(self, value):
        if isinstance(value, uuid.UUID):
            return value
        return uuid.UUID(value) if value is not None else None

class BinaryUUIDField(BlobField):
    @overload
    def db_value(self, value: None) -> None: ...
    @overload
    def db_value(self, value: Optional[Union[bytearray, bytes, str, uuid.UUID]]) -> bytes: ...
    @overload
    def python_value(self, value: None) -> None: ...
    @overload
    def python_value(self, value: Union[bytearray, bytes, memoryview, uuid.UUID]) -> uuid.UUID: ...

def format_date_time(value: str, formats: Iterable[str], post_process: Optional[__TConvFunc] = ...) -> str: ...
@overload
def simple_date_time(value: T) -> T: ...

class _BaseFormattedField(Field):
    # TODO (dargueta): This is a class variable that can be overridden for instances
    formats: Optional[Container[str]]
    def __init__(self, formats: Optional[Container[str]] = ..., *args: object, **kwargs: object): ...

class DateTimeField(_BaseFormattedField):
    @property
    def year(self) -> int: ...
    @property
    def month(self) -> int: ...
    @property
    def day(self) -> int: ...
    @property
    def hour(self) -> int: ...
    @property
    def minute(self) -> int: ...
    @property
    def second(self) -> int: ...
    @overload
    def adapt(self, value: str) -> str: ...
    @overload
    def adapt(self, value: T) -> T: ...
    def to_timestamp(self):
        return self.model._meta.database.to_timestamp(self)
    def truncate(self, part):
        return self.model._meta.database.truncate_date(part, self)

class DateField(_BaseFormattedField):
    @property
    def year(self) -> int: ...
    @property
    def month(self) -> int: ...
    @property
    def day(self) -> int: ...
    @overload
    def adapt(self, value: str) -> str: ...
    @overload
    def adapt(self, value: datetime.datetime) -> datetime.date: ...
    @overload
    def adapt(self, value: T) -> T: ...
    def to_timestamp(self):
        return self.model._meta.database.to_timestamp(self)
    def truncate(self, part):
        return self.model._meta.database.truncate_date(part, self)

class TimeField(_BaseFormattedField):
    @overload
    def adapt(self, value: str) -> str: ...
    @overload
    def adapt(self, value: Union[datetime.datetime, datetime.timedelta]) -> datetime.time: ...
    @overload
    def adapt(self, value: T) -> T: ...
    @property
    def hour(self) -> int: ...
    @property
    def minute(self) -> int: ...
    @property
    def second(self) -> int: ...

class TimestampField(BigIntegerField):
    valid_resolutions: ClassVar[Container[int]]
    # Instance variables
    resolution: int
    ticks_to_microsecond: int
    utc: bool
    def __init__(self, *args: object, resolution: int = ..., utc: bool = ..., **kwargs: object): ...
    def local_to_utc(self, dt: datetime.datetime) -> datetime.datetime: ...
    def utc_to_local(self, dt: datetime.datetime) -> datetime.datetime: ...
    def get_timestamp(self, value):
        if self.utc:
            # If utc-mode is on, then we assume all naive datetimes are in UTC.
            return calendar.timegm(value.utctimetuple())
        else:
            return time.mktime(value.timetuple())
    def db_value(self, value):
        if value is None:
            return

        if isinstance(value, datetime.datetime): ...
        elif isinstance(value, datetime.date):
            value = datetime.datetime(value.year, value.month, value.day)
        else:
            return int(round(value * self.resolution))

        timestamp = self.get_timestamp(value)
        if self.resolution > 1:
            timestamp += value.microsecond * 0.000001
            timestamp *= self.resolution
        return int(round(timestamp))
    @overload
    def python_value(self, value: Union[int, float]) -> datetime.datetime: ...
    @overload
    def python_value(self, value: T) -> T: ...
    def from_timestamp(self):
        expr = (self / Value(self.resolution, converter=False)) if self.resolution > 1 else self
        return self.model._meta.database.from_timestamp(expr)
    @property
    def year(self) -> int: ...
    @property
    def month(self) -> int: ...
    @property
    def day(self) -> int: ...
    @property
    def hour(self) -> int: ...
    @property
    def minute(self) -> int: ...
    @property
    def second(self) -> int: ...  # TODO (dargueta) Float?

class IPField(BigIntegerField):
    @overload
    def db_value(self, val: str) -> int: ...
    @overload
    def db_value(self, val: None) -> None: ...
    @overload
    def python_value(self, val: int) -> str: ...
    @overload
    def python_value(self, val: None) -> None: ...

class BooleanField(Field):
    def adapt(self, value: Any) -> bool: ...

class BareField(Field):
    def __init__(self, adapt=None, *args, **kwargs):
        super(BareField, self).__init__(*args, **kwargs)
        if adapt is not None:
            self.adapt = adapt
    def ddl_datatype(self, ctx):
        return

class ForeignKeyField(Field):
    accessor_class = ForeignKeyAccessor
    def __init__(
        self,
        model,
        field=None,
        backref=None,
        on_delete=None,
        on_update=None,
        deferrable=None,
        _deferred=None,
        rel_model=None,
        to_field=None,
        object_id_name=None,
        lazy_load=True,
        related_name=None,
        *args,
        **kwargs,
    ):
        kwargs.setdefault("index", True)

        # If lazy_load is disable, we use a different descriptor/accessor that
        # will ensure we don't accidentally perform a query.
        if not lazy_load:
            self.accessor_class = NoQueryForeignKeyAccessor

        super(ForeignKeyField, self).__init__(*args, **kwargs)

        self._is_self_reference = model == "self"
        self.rel_model = model
        self.rel_field = field
        self.declared_backref = backref
        self.backref = None
        self.on_delete = on_delete
        self.on_update = on_update
        self.deferrable = deferrable
        self.deferred = _deferred
        self.object_id_name = object_id_name
        self.lazy_load = lazy_load
    @property
    def field_type(self):
        if not isinstance(self.rel_field, AutoField):
            return self.rel_field.field_type
        elif isinstance(self.rel_field, BigAutoField):
            return BigIntegerField.field_type
        return IntegerField.field_type
    def get_modifiers(self):
        if not isinstance(self.rel_field, AutoField):
            return self.rel_field.get_modifiers()
        return super(ForeignKeyField, self).get_modifiers()
    def adapt(self, value):
        return self.rel_field.adapt(value)
    def db_value(self, value):
        if isinstance(value, self.rel_model):
            value = getattr(value, self.rel_field.name)
        return self.rel_field.db_value(value)
    def python_value(self, value):
        if isinstance(value, self.rel_model):
            return value
        return self.rel_field.python_value(value)
    def bind(self, model, name, set_attribute=True):
        if not self.column_name:
            self.column_name = name if name.endswith("_id") else name + "_id"
        if not self.object_id_name:
            self.object_id_name = self.column_name
            if self.object_id_name == name:
                self.object_id_name += "_id"
        elif self.object_id_name == name:
            raise ValueError(
                'ForeignKeyField "%s"."%s" specifies an '
                "object_id_name that conflicts with its field "
                "name." % (model._meta.name, name)
            )
        if self._is_self_reference:
            self.rel_model = model
        if isinstance(self.rel_field, str):
            self.rel_field = getattr(self.rel_model, self.rel_field)
        elif self.rel_field is None:
            self.rel_field = self.rel_model._meta.primary_key

        # Bind field before assigning backref, so field is bound when
        # calling declared_backref() (if callable).
        super(ForeignKeyField, self).bind(model, name, set_attribute)
        self.safe_name = self.object_id_name

        if callable(self.declared_backref):
            self.backref = self.declared_backref(self)
        else:
            self.backref, self.declared_backref = self.declared_backref, None
        if not self.backref:
            self.backref = "%s_set" % model._meta.name

        if set_attribute:
            setattr(model, self.object_id_name, ObjectIdAccessor(self))
            if self.backref not in "!+":
                setattr(self.rel_model, self.backref, BackrefAccessor(self))
    def foreign_key_constraint(self):
        parts = [
            SQL("FOREIGN KEY"),
            EnclosedNodeList((self,)),
            SQL("REFERENCES"),
            self.rel_model,
            EnclosedNodeList((self.rel_field,)),
        ]
        if self.on_delete:
            parts.append(SQL("ON DELETE %s" % self.on_delete))
        if self.on_update:
            parts.append(SQL("ON UPDATE %s" % self.on_update))
        if self.deferrable:
            parts.append(SQL("DEFERRABLE %s" % self.deferrable))
        return NodeList(parts)
    def __getattr__(self, attr):
        if attr.startswith("__"):
            # Prevent recursion error when deep-copying.
            raise AttributeError('Cannot look-up non-existant "__" methods.')
        if attr in self.rel_model._meta.fields:
            return self.rel_model._meta.fields[attr]
        raise AttributeError("Foreign-key has no attribute %s, nor is it a " "valid field on the related model." % attr)

class DeferredForeignKey(Field):
    _unresolved = set()
    def __init__(self, rel_model_name, **kwargs):
        self.field_kwargs = kwargs
        self.rel_model_name = rel_model_name.lower()
        DeferredForeignKey._unresolved.add(self)
        super(DeferredForeignKey, self).__init__(column_name=kwargs.get("column_name"), null=kwargs.get("null"))
    __hash__ = object.__hash__
    def __deepcopy__(self, memo=None):
        return DeferredForeignKey(self.rel_model_name, **self.field_kwargs)
    def set_model(self, rel_model):
        field = ForeignKeyField(rel_model, _deferred=True, **self.field_kwargs)
        self.model._meta.add_field(self.name, field)
    @staticmethod
    def resolve(model_cls):
        unresolved = sorted(DeferredForeignKey._unresolved, key=operator.attrgetter("_order"))
        for dr in unresolved:
            if dr.rel_model_name == model_cls.__name__.lower():
                dr.set_model(model_cls)
                DeferredForeignKey._unresolved.discard(dr)

class DeferredThroughModel(object):
    def __init__(self):
        self._refs = []
    def set_field(self, model, field, name):
        self._refs.append((model, field, name))
    def set_model(self, through_model):
        for src_model, m2mfield, name in self._refs:
            m2mfield.through_model = through_model
            src_model._meta.add_field(name, m2mfield)

class MetaField(Field):
    column_name = default = model = name = None
    primary_key = False

class ManyToManyFieldAccessor(FieldAccessor):
    model: Type[Model]
    rel_model: Type[Model]
    through_model: Type[Model]
    src_fk: ForeignKeyField
    dest_fk: ForeignKeyField
    def __init__(self, model: Type[Model], field: ForeignKeyField, name: str): ...
    @overload
    def __get__(self, instance: None, instance_type: Type[T] = ..., force_query: bool = ...) -> Field: ...
    @overload
    def __get__(
        self, instance: T, instance_type: Type[T] = ..., force_query: bool = ...
    ) -> Union[List[str], ManyToManyQuery]: ...
    def __set__(self, instance: T, value) -> None:
        query = self.__get__(instance, force_query=True)
        query.add(value, clear_existing=True)

class ManyToManyField(MetaField):
    accessor_class: ClassVar[Type[ManyToManyFieldAccessor]]
    # Instance variables
    through_model: Union[Type[Model], DeferredThroughModel]
    rel_model: Type[Model]
    backref: Optional[str]
    def __init__(
        self,
        model: Type[Model],
        backref: Optional[str] = ...,
        through_model: Optional[Union[Type[Model], DeferredThroughModel]] = ...,
        on_delete: Optional[str] = ...,
        on_update: Optional[str] = ...,
        _is_backref: bool = ...,
    ): ...
    def bind(self, model: Type[Model], name: str, set_attribute: bool = ...) -> None: ...
    def get_models(self) -> List[Type[Model]]: ...
    def get_through_model(self) -> Union[Type[Model], DeferredThroughModel]: ...

class VirtualField(MetaField, Generic[__TField]):
    field_class: Type[__TField]
    field_instance: __TField
    def __init__(self, field_class: Optional[Type[__TField]] = ..., *args: object, **kwargs: object): ...
    def db_value(self, value):
        if self.field_instance is not None:
            return self.field_instance.db_value(value)
        return value
    def python_value(self, value):
        if self.field_instance is not None:
            return self.field_instance.python_value(value)
        return value
    def bind(self, model: Type[Model], name: str, set_attribute: bool = ...) -> None: ...

class CompositeKey(MetaField):
    sequence = None
    def __init__(self, *field_names):
        self.field_names = field_names
        self._safe_field_names = None
    @property
    def safe_field_names(self):
        if self._safe_field_names is None:
            if self.model is None:
                return self.field_names

            self._safe_field_names = [self.model._meta.fields[f].safe_name for f in self.field_names]
        return self._safe_field_names
    def __get__(self, instance, instance_type=None):
        if instance is not None:
            return tuple([getattr(instance, f) for f in self.safe_field_names])
        return self
    def __set__(self, instance, value):
        if not isinstance(value, (list, tuple)):
            raise TypeError("A list or tuple must be used to set the value of " "a composite primary key.")
        if len(value) != len(self.field_names):
            raise ValueError("The length of the value must equal the number " "of columns of the composite primary key.")
        for idx, field_value in enumerate(value):
            setattr(instance, self.field_names[idx], field_value)
    def __eq__(self, other):
        expressions = [(self.model._meta.fields[field] == value) for field, value in zip(self.field_names, other)]
        return reduce(operator.and_, expressions)
    def __ne__(self, other):
        return ~(self == other)
    def __hash__(self):
        return hash((self.model.__name__, self.field_names))
    def __sql__(self, ctx):
        # If the composite PK is being selected, do not use parens. Elsewhere,
        # such as in an expression, we want to use parentheses and treat it as
        # a row value.
        parens = ctx.scope != SCOPE_SOURCE
        return ctx.sql(NodeList([self.model._meta.fields[field] for field in self.field_names], ", ", parens))
    def bind(self, model, name, set_attribute=True):
        self.model = model
        self.column_name = self.name = self.safe_name = name
        setattr(model, self.name, self)

class _SortedFieldList(object):
    __slots__ = ("_keys", "_items")
    def __init__(self):
        self._keys = []
        self._items = []
    def __getitem__(self, i):
        return self._items[i]
    def __iter__(self):
        return iter(self._items)
    def __contains__(self, item):
        k = item._sort_key
        i = bisect_left(self._keys, k)
        j = bisect_right(self._keys, k)
        return item in self._items[i:j]
    def index(self, field):
        return self._keys.index(field._sort_key)
    def insert(self, item):
        k = item._sort_key
        i = bisect_left(self._keys, k)
        self._keys.insert(i, k)
        self._items.insert(i, item)
    def remove(self, item):
        idx = self.index(item)
        del self._items[idx]
        del self._keys[idx]

# MODELS

class SchemaManager(object):
    model: Type[Model]
    context_options: Dict[str, Any]
    def __init__(self, model: Type[Model], database: Optional[Database] = None, **context_options: Any): ...
    @property
    def database(self) -> Database: ...
    @database.setter
    def database(self, value: Optional[Database]) -> None: ...
    def create_table(self, safe: bool = ..., **options: Any) -> None: ...
    def create_table_as(self, table_name: str, query: SelectQuery, safe: bool = ..., **meta: Any) -> None: ...
    def drop_table(self, safe: bool = ..., **options: Any) -> None: ...
    def truncate_table(self, restart_identity: bool = ..., cascade: bool = ...) -> None: ...
    def create_indexes(self, safe: bool = ...) -> None: ...
    def drop_indexes(self, safe: bool = ...) -> None: ...
    def create_sequence(self, field: Field) -> None: ...
    def drop_sequence(self, field: Field) -> None: ...
    def create_foreign_key(self, field: Field) -> None: ...
    def create_sequences(self) -> None: ...
    def create_all(self, safe: bool = ..., **table_options: Any) -> None: ...
    def drop_sequences(self) -> None: ...
    def drop_all(self, safe: bool = ..., drop_sequences: bool = ..., **options: Any) -> None: ...

class Metadata(object):
    model: Type[Model]
    database: Optional[Database]
    fields: Dict[str, Any]  # TODO (dargueta) This may be Dict[str, Field]
    columns: Dict[str, Any]  # TODO (dargueta) Verify this
    combined: Dict[str, Any]  # TODO (dargueta) Same as above
    sorted_fields: List[Field]
    sorted_field_names: List[str]
    defaults: Dict[str, Any]
    name: str
    table_function: Optional[Callable[[Type[Model]], str]]
    legacy_table_names: bool
    table_name: str
    indexes: List[Union[Index, ModelIndex, SQL]]
    constraints: Optional[Iterable[Union[Check, SQL]]]
    primary_key: Union[Literal[False], Field, CompositeKey, None]
    composite_key: Optional[bool]
    auto_increment: Optional[bool]
    only_save_dirty: bool
    depends_on: Optional[Sequence[Type[Model]]]
    table_settings: Mapping[str, object]
    temporary: bool
    refs: Dict[ForeignKeyField, Type[Model]]
    backrefs: MutableMapping[ForeignKeyField, List[Type[Model]]]
    model_refs: MutableMapping[Type[Model], List[ForeignKeyField]]
    model_backrefs: MutableMapping[ForeignKeyField, List[Type[Model]]]
    manytomany: Dict[str, ManyToManyField]
    options: Mapping[str, object]
    table: Optional[Table]
    entity: Entity
    def __init__(
        self,
        model: Type[Model],
        database: Optional[Database] = ...,
        table_name: Optional[str] = ...,
        indexes: Optional[Iterable[Union[str, Sequence[str]]]] = ...,
        primary_key: Optional[Union[Literal[False], Field, CompositeKey]] = ...,
        constraints: Optional[Iterable[Union[Check, SQL]]] = ...,
        schema: Optional[str] = ...,
        only_save_dirty: bool = ...,
        depends_on: Optional[Sequence[Type[Model]]] = ...,
        options: Optional[Mapping[str, object]] = ...,
        db_table: Optional[str] = ...,
        table_function: Optional[Callable[[Type[Model]], str]] = ...,
        table_settings: Optional[Mapping[str, object]] = ...,
        without_rowid: bool = ...,
        temporary: bool = ...,
        legacy_table_names: bool = ...,
        **kwargs: object,
    ): ...
    def make_table_name(self) -> str: ...
    def model_graph(
        self, refs: bool = ..., backrefs: bool = ..., depth_first: bool = ...
    ) -> List[Tuple[ForeignKeyField, Type[Model], bool]]: ...
    def add_ref(self, field: ForeignKeyField) -> None: ...
    def remove_ref(self, field: ForeignKeyField) -> None: ...
    def add_manytomany(self, field: ManyToManyField) -> None: ...
    def remove_manytomany(self, field: ManyToManyField) -> None: ...
    def get_rel_for_model(self, model: Union[Type[Model], ModelAlias]) -> Tuple[List[ForeignKeyField], List[Type[Model]]]: ...
    def add_field(self, field_name: str, field: Field, set_attribute: bool = ...) -> None: ...
    def remove_field(self, field_name: str) -> None: ...
    def set_primary_key(self, name: str, field: Union[Field, CompositeKey]) -> None: ...
    def get_primary_keys(self) -> Tuple[Field, ...]: ...
    def get_default_dict(self) -> Dict[str, object]: ...
    def fields_to_index(self) -> List[ModelIndex]: ...
    def set_database(self, database: Database) -> None: ...
    def set_table_name(self, table_name: str) -> None: ...

class SubclassAwareMetadata(Metadata):
    models: ClassVar[List[Type[Model]]]
    def __init__(self, model: Type[Model], *args: object, **kwargs: object): ...
    def map_models(self, fn: Callable[[Type[Model]], Any]) -> None: ...

class DoesNotExist(Exception): ...

class ModelBase(type):
    inheritable: ClassVar[Set[str]]
    def __repr__(self) -> str: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __getitem__(self, key: object) -> Model: ...
    def __setitem__(self, key: object, value: Model) -> None: ...
    def __delitem__(self, key: object) -> None: ...
    def __contains__(self, key: object) -> bool: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...
    def __sql__(self, ctx: Context) -> Context: ...

class _BoundModelsContext(_callable_context_manager):
    models: Iterable[Type[Model]]
    database: Database
    bind_refs: bool
    bind_backrefs: bool
    def __init__(self, models: Iterable[Type[Model]], database, bind_refs: bool, bind_backrefs: bool): ...
    def __enter__(self) -> Iterable[Type[Model]]: ...
    def __exit__(self, exc_type: Type[Exception], exc_val: Exception, exc_tb: Any) -> None: ...

class Model(Node, metaclass=ModelBase):
    _meta: ClassVar[Metadata]
    _schema: ClassVar[SchemaManager]
    DoesNotExist: ClassVar[Type[DoesNotExist]]
    __data__: MutableMapping[str, object]
    __rel__: MutableMapping[str, object]
    def __init__(self, *, __no_default__: Union[int, bool] = ..., **kwargs: object): ...
    def __str__(self) -> str: ...
    @classmethod
    def validate_model(cls) -> None: ...
    @classmethod
    def alias(cls, alias: Optional[str] = ...) -> ModelAlias: ...
    @classmethod
    def select(cls, *fields: Field) -> ModelSelect: ...
    @classmethod
    def update(cls, __data: Optional[Iterable[Union[str, Field]]] = ..., **update: Any) -> ModelUpdate: ...
    @classmethod
    def insert(cls, __data: Optional[Iterable[Union[str, Field]]] = ..., **insert: Any) -> ModelInsert: ...
    @overload
    @classmethod
    def insert_many(cls, rows: Iterable[Mapping[str, object]], fields: None) -> ModelInsert: ...
    @overload
    @classmethod
    def insert_many(cls, rows: Iterable[tuple], fields: Sequence[Field]) -> ModelInsert: ...
    @classmethod
    def insert_from(cls, query: SelectQuery, fields: Iterable[Union[Field, Text]]) -> ModelInsert: ...
    @classmethod
    def replace(cls, __data=None, **insert):
        return cls.insert(__data, **insert).on_conflict("REPLACE")
    @classmethod
    def replace_many(cls, rows, fields=None):
        return cls.insert_many(rows=rows, fields=fields).on_conflict("REPLACE")
    @classmethod
    def raw(cls, sql, *params):
        return ModelRaw(cls, sql, params)
    @classmethod
    def delete(cls) -> ModelDelete: ...
    @classmethod
    def create(cls: Type[T], **query) -> T: ...
    @classmethod
    def bulk_create(cls, model_list: Iterable[Type[Model]], batch_size: Optional[int] = ...) -> None: ...
    @classmethod
    def bulk_update(
        cls, model_list: Iterable[Type[Model]], fields: Iterable[Union[str, Field]], batch_size: Optional[int] = ...
    ) -> int: ...
    @classmethod
    def noop(cls) -> NoopModelSelect: ...
    @classmethod
    def get(cls, *query, **filters):
        sq = cls.select()
        if query:
            # Handle simple lookup using just the primary key.
            if len(query) == 1 and isinstance(query[0], int):
                sq = sq.where(cls._meta.primary_key == query[0])
            else:
                sq = sq.where(*query)
        if filters:
            sq = sq.filter(**filters)
        return sq.get()
    @classmethod
    def get_or_none(cls, *query, **filters):
        try:
            return cls.get(*query, **filters)
        except DoesNotExist: ...
    @classmethod
    def get_by_id(cls, pk):
        return cls.get(cls._meta.primary_key == pk)
    @classmethod
    def set_by_id(cls, key, value) -> Any:  # TODO (dargueta): Verify return type of .execute()
        if key is None:
            return cls.insert(value).execute()
        else:
            return cls.update(value).where(cls._meta.primary_key == key).execute()
    @classmethod
    def delete_by_id(cls, pk: object) -> Any: ...  # TODO (dargueta): Verify return type of .execute()
    @classmethod
    def get_or_create(cls, *, defaults: Mapping[str, object] = ..., **kwargs: object) -> Tuple[Any, bool]: ...
    @classmethod
    def filter(cls, *dq_nodes: DQ, **filters: Any) -> SelectQuery: ...
    def get_id(self) -> Any: ...
    def save(self, force_insert: bool = ..., only: Optional[Iterable[Union[str, Field]]] = ...) -> Union[Literal[False], int]: ...
    def is_dirty(self) -> bool: ...
    @property
    def dirty_fields(self) -> List[Field]: ...
    def dependencies(self, search_nullable: bool = ...) -> Iterator[Tuple[Union[bool, Node], ForeignKeyField]]: ...
    def delete_instance(self: T, recursive: bool = ..., delete_nullable: bool = ...) -> T: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __sql__(self, ctx: Context) -> Context: ...
    @classmethod
    def bind(
        cls,
        database: Database,
        bind_refs: bool = ...,
        bind_backrefs: bool = ...,
        _exclude: Optional[MutableSet[Type[Model]]] = ...,
    ) -> bool: ...
    @classmethod
    def bind_ctx(cls, database: Database, bind_refs: bool = ..., bind_backrefs: bool = ...) -> _BoundModelsContext: ...
    @classmethod
    def table_exists(cls) -> bool: ...
    @classmethod
    def create_table(cls, safe: bool = ..., *, fail_silently: bool = ..., **options: object) -> None: ...
    @classmethod
    def drop_table(cls, safe: bool = ..., drop_sequences: bool = ..., **options: object) -> None: ...
    @classmethod
    def truncate_table(cls, **options: object) -> None: ...
    @classmethod
    def index(cls, *fields, **kwargs):
        return ModelIndex(cls, fields, **kwargs)
    @classmethod
    def add_index(cls, *fields: Union[str, SQL, Index], **kwargs: object) -> None: ...

class ModelAlias(Node):
    """Provide a separate reference to a model in a query."""

    model: Type[Model]
    alias: Optional[str]
    def __init__(self, model: Type[Model], alias: Optional[str] = ...): ...
    def __getattr__(self, attr: str):
        # Hack to work-around the fact that properties or other objects
        # implementing the descriptor protocol (on the model being aliased),
        # will not work correctly when we use getattr(). So we explicitly pass
        # the model alias to the descriptor's getter.
        try:
            obj = self.model.__dict__[attr]
        except KeyError: ...
        else:
            if isinstance(obj, ModelDescriptor):
                return obj.__get__(None, self)

        model_attr = getattr(self.model, attr)
        if isinstance(model_attr, Field):
            self.__dict__[attr] = FieldAlias.create(self, model_attr)
            return self.__dict__[attr]
        return model_attr
    def __setattr__(self, attr: str, value: object) -> NoReturn: ...
    def get_field_aliases(self) -> List[Field]: ...
    def select(self, *selection: Field) -> ModelSelect: ...
    def __call__(self, **kwargs):
        return self.model(**kwargs)
    def __sql__(self, ctx: Context) -> Context: ...

class FieldAlias(Field):
    source: Node
    model: Type[Model]
    field: Field
    # TODO (dargueta): Making an educated guess about `source`; might be `Node`
    def __init__(self, source: MetaField, field: Field): ...
    @classmethod
    def create(cls, source: ModelAlias, field: str):
        class _FieldAlias(cls, type(field)): ...
        return _FieldAlias(source, field)
    def clone(self) -> FieldAlias: ...
    def adapt(self, value):
        return self.field.adapt(value)
    def python_value(self, value):
        return self.field.python_value(value)
    def db_value(self, value):
        return self.field.db_value(value)
    def __getattr__(self, attr):
        return self.source if attr == "model" else getattr(self.field, attr)
    def __sql__(self, ctx: Context) -> Context: ...

def sort_models(models: Iterable[Type[Model]]) -> List[Type[Model]]: ...

class _ModelQueryHelper(object):
    default_row_type: ClassVar[int]
    def objects(self, constructor: Optional[Callable[..., Any]] = ...) -> _ModelQueryHelper: ...

class ModelRaw(_ModelQueryHelper, RawQuery, Generic[__TModel]):
    model: Type[__TModel]
    def __init__(self, model: Type[__TModel], sql: str, params: tuple, **kwargs: object): ...
    def get(self) -> __TModel: ...

class BaseModelSelect(_ModelQueryHelper):
    def union_all(self, rhs):
        return ModelCompoundSelectQuery(self.model, self, "UNION ALL", rhs)
    __add__ = union_all
    def union(self, rhs):
        return ModelCompoundSelectQuery(self.model, self, "UNION", rhs)
    __or__ = union
    def intersect(self, rhs):
        return ModelCompoundSelectQuery(self.model, self, "INTERSECT", rhs)
    __and__ = intersect
    def except_(self, rhs):
        return ModelCompoundSelectQuery(self.model, self, "EXCEPT", rhs)
    __sub__ = except_
    def __iter__(self) -> Iterator[Any]:
        if not self._cursor_wrapper:
            self.execute()
        return iter(self._cursor_wrapper)
    def prefetch(self, *subqueries: __TSubquery) -> List[Any]: ...
    def get(self, database: Optional[Database] = ...) -> Any: ...
    def group_by(self, *columns: Union[Type[Model], Table, Field]) -> BaseModelSelect: ...

class ModelCompoundSelectQuery(BaseModelSelect, CompoundSelectQuery):
    model: Type[__TModel]
    def __init__(self, model: Type[__TModel], *args: object, **kwargs: object): ...

class ModelSelect(BaseModelSelect, Select):
    model: Type[Model]
    def __init__(self, model: Type[Model], fields_or_models: Iterable[__TFieldOrModel], is_default: bool = ...): ...
    def clone(self) -> ModelSelect: ...
    def select(self, *fields_or_models: __TFieldOrModel) -> ModelSelect: ...
    def switch(self, ctx: Optional[Type[Model]] = ...) -> ModelSelect: ...
    def join(
        self,
        dest: Union[Type[Model], Table, ModelAlias, ModelSelect],
        join_type: int = ...,
        on: Union[Column, Expression, Field, None] = ...,
        src: Union[Type[Model], Table, ModelAlias, ModelSelect, None] = ...,
        attr: Optional[str] = ...,
    ) -> ModelSelect: ...
    def join_from(
        self,
        src: Union[Type[Model], Table, ModelAlias, ModelSelect],
        dest: Union[Type[Model], Table, ModelAlias, ModelSelect],
        join_type: int = ...,
        on: Union[Column, Expression, Field, None] = ...,
        attr: Optional[str] = ...,
    ) -> ModelSelect: ...
    def ensure_join(
        self, lm: Type[Model], rm: Type[Model], on: Union[Column, Expression, Field, None] = ..., **join_kwargs: Any
    ) -> ModelSelect: ...
    # TODO (dargueta): 85% sure about the return value
    def convert_dict_to_node(self, qdict: Mapping[str, object]) -> Tuple[List[Expression], List[Field]]: ...
    def filter(self, *args: Node, **kwargs: object) -> ModelSelect: ...
    def create_table(self, name: str, safe: bool = ..., **meta: Any) -> None: ...
    def __sql_selection__(self, ctx: Context, is_subquery: bool = ...) -> Context: ...

class NoopModelSelect(ModelSelect):
    def __sql__(self, ctx: Context) -> Context: ...

class _ModelWriteQueryHelper(_ModelQueryHelper):
    model: Type[Model]
    def __init__(self, model: Type[Model], *args: object, **kwargs: object): ...
    def returning(self, *returning: Union[Type[Model], Field]) -> _ModelWriteQueryHelper: ...

class ModelUpdate(_ModelWriteQueryHelper, Update): ...

class ModelInsert(_ModelWriteQueryHelper, Insert):
    default_row_type: ClassVar[int]
    def returning(self, *returning: Union[Type[Model], Field]) -> ModelInsert: ...
    def get_default_data(self):
        return self.model._meta.defaults
    def get_default_columns(self) -> Sequence[Field]: ...

class ModelDelete(_ModelWriteQueryHelper, Delete): ...

class ManyToManyQuery(ModelSelect):
    def __init__(
        self, instance: Model, accessor: ManyToManyFieldAccessor, rel: __TFieldOrModel, *args: object, **kwargs: object
    ): ...
    def add(self, value: Union[SelectQuery, Type[Model], Iterable[str]], clear_existing: bool = ...) -> None: ...
    def remove(self, value: Union[SelectQuery, Type[Model], Iterable[str]]) -> Optional[int]: ...
    def clear(self) -> int: ...

class BaseModelCursorWrapper(DictCursorWrapper, Generic[__TModel]):
    ncols: int
    columns: List[str]
    converters: List[__TConvFunc]
    fields: List[Field]
    model: Type[__TModel]
    select: Sequence[str]
    def __init__(self, cursor: __ICursor, model: Type[__TModel], columns: Optional[Sequence[str]]): ...
    def process_row(self, row: tuple) -> Mapping[str, object]: ...

class ModelDictCursorWrapper(BaseModelCursorWrapper[__TModel]):
    def process_row(self, row: tuple) -> Dict[str, Any]: ...

class ModelTupleCursorWrapper(ModelDictCursorWrapper[__TModel]):
    constructor: ClassVar[Callable[[Sequence[Any]], tuple]]
    def process_row(self, row: tuple) -> tuple: ...

class ModelNamedTupleCursorWrapper(ModelTupleCursorWrapper[__TModel]): ...

class ModelObjectCursorWrapper(ModelDictCursorWrapper[__TModel]):
    constructor: Union[Type[__TModel], Callable[[Any], __TModel]]
    is_model: bool
    # TODO (dargueta): `select` is some kind of Sequence
    def __init__(
        self, cursor: __ICursor, model: __TModel, select, constructor: Union[Type[__TModel], Callable[[Any], __TModel]]
    ): ...
    def process_row(self, row: tuple) -> __TModel: ...

class ModelCursorWrapper(BaseModelCursorWrapper[__TModel]):
    from_list: Any  # TODO (dargueta) -- Iterable[Union[Join, ...]]
    joins: Any  # TODO (dargueta) -- Mapping[<from list type>, Tuple[?, ?, Callable[..., __TModel], int?]]
    key_to_constructor: Dict[Type[__TModel], Callable[..., __TModel]]
    src_is_dest: Dict[Type[Model], bool]
    src_to_dest: List[tuple]  # TODO -- Tuple[<frmo list type>, join_type[1], join_type[0], bool, join_type[3]]
    column_keys: List  # TODO
    def __init__(self, cursor: __ICursor, model: Type[__TModel], select, from_list, joins):
        super(ModelCursorWrapper, self).__init__(cursor, model, select)
        self.from_list = from_list
        self.joins = joins
    def initialize(self) -> None:
        self._initialize_columns()
        selected_src = set([field.model for field in self.fields if field is not None])
        select, columns = self.select, self.columns

        self.key_to_constructor = {self.model: self.model}
        self.src_is_dest = {}
        self.src_to_dest = []
        accum = collections.deque(self.from_list)
        dests = set()

        while accum:
            curr = accum.popleft()
            if isinstance(curr, Join):
                accum.append(curr.lhs)
                accum.append(curr.rhs)
                continue

            if curr not in self.joins:
                continue

            is_dict = isinstance(curr, dict)
            for key, attr, constructor, join_type in self.joins[curr]:
                if key not in self.key_to_constructor:
                    self.key_to_constructor[key] = constructor

                    # (src, attr, dest, is_dict, join_type).
                    self.src_to_dest.append((curr, attr, key, is_dict, join_type))
                    dests.add(key)
                    accum.append(key)

        # Ensure that we accommodate everything selected.
        for src in selected_src:
            if src not in self.key_to_constructor:
                if is_model(src):
                    self.key_to_constructor[src] = src
                elif isinstance(src, ModelAlias):
                    self.key_to_constructor[src] = src.model

        # Indicate which sources are also dests.
        for src, _, dest, _, _ in self.src_to_dest:
            self.src_is_dest[src] = src in dests and (dest in selected_src or src in selected_src)

        self.column_keys = []
        for idx, node in enumerate(select):
            key = self.model
            field = self.fields[idx]
            if field is not None:
                if isinstance(field, FieldAlias):
                    key = field.source
                else:
                    key = field.model
            else:
                if isinstance(node, Node):
                    node = node.unwrap()
                if isinstance(node, Column):
                    key = node.source

            self.column_keys.append(key)
    def process_row(self, row: tuple) -> __TModel: ...

class __PrefetchQuery(NamedTuple):
    query: Query  # TODO (dargueta): Verify
    fields: Optional[Sequence[Field]]
    is_backref: Optional[bool]
    rel_models: Optional[List[Type[Model]]]
    field_to_name: Optional[List[Tuple[Field, str]]]
    model: Type[Model]

class PrefetchQuery(__PrefetchQuery):
    # TODO (dargueta): The key is a two-tuple but not completely sure what
    def populate_instance(self, instance: Model, id_map: Mapping[tuple, Any]):
        if self.is_backref:
            for field in self.fields:
                identifier = instance.__data__[field.name]
                key = (field, identifier)
                if key in id_map:
                    setattr(instance, field.name, id_map[key])
        else:
            for field, attname in self.field_to_name:
                identifier = instance.__data__[field.rel_field.name]
                key = (field, identifier)
                rel_instances = id_map.get(key, [])
                for inst in rel_instances:
                    setattr(inst, attname, instance)
                    inst._dirty.clear()
                setattr(instance, field.backref, rel_instances)
    # TODO (dargueta): Same question here about the key tuple
    def store_instance(self, instance: Model, id_map: MutableMapping[tuple, List[Model]]) -> None: ...

def prefetch_add_subquery(sq: Query, subqueries: Iterable[__TSubquery]) -> List[PrefetchQuery]: ...
def prefetch(sq: Query, *subqueries: __TSubquery) -> List[Any]: ...
