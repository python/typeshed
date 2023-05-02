from _typeshed import Incomplete, ReadableBuffer, SupportsTrunc, Unused
from collections.abc import Callable
from typing import SupportsInt, TypeVar, overload
from typing_extensions import SupportsIndex

from ..sql.coercions import _CoercibleElement
from ..sql.type_api import TypeEngine
from ..util.langhelpers import _DictLike, _symbol, symbol
from .base import PARSE_AUTOCOMMIT as PARSE_AUTOCOMMIT, ColumnCollection as ColumnCollection, Executable as Executable
from .dml import Delete as Delete, Insert as Insert, Update as Update, UpdateBase as UpdateBase, ValuesBase as ValuesBase
from .elements import (
    BinaryExpression as BinaryExpression,
    BindParameter as BindParameter,
    BooleanClauseList as BooleanClauseList,
    Case as Case,
    Cast as Cast,
    ClauseElement as ClauseElement,
    ClauseList as ClauseList,
    CollectionAggregate as CollectionAggregate,
    ColumnClause as ColumnClause,
    ColumnElement as ColumnElement,
    Extract as Extract,
    False_ as False_,
    FunctionFilter as FunctionFilter,
    Grouping as Grouping,
    Label as Label,
    Null as Null,
    Over as Over,
    ReleaseSavepointClause as ReleaseSavepointClause,
    RollbackToSavepointClause as RollbackToSavepointClause,
    SavepointClause as SavepointClause,
    TextClause as TextClause,
    True_ as True_,
    Tuple as Tuple,
    TypeClause as TypeClause,
    TypeCoerce as TypeCoerce,
    UnaryExpression as UnaryExpression,
    WithinGroup as WithinGroup,
    _anonymous_label,
    _truncated_label as _truncated_label,
    between as between,
    collate as collate,
    literal as literal,
    literal_column as literal_column,
    not_ as not_,
    outparam as outparam,
    quoted_name as quoted_name,
)
from .functions import Function as Function, FunctionElement as FunctionElement, func as func, modifier as modifier
from .lambdas import LambdaElement as LambdaElement, StatementLambdaElement as StatementLambdaElement, lambda_stmt as lambda_stmt
from .operators import ColumnOperators as ColumnOperators, Operators as Operators, custom_op as custom_op
from .selectable import (
    CTE as CTE,
    LABEL_STYLE_DEFAULT as LABEL_STYLE_DEFAULT,
    LABEL_STYLE_DISAMBIGUATE_ONLY as LABEL_STYLE_DISAMBIGUATE_ONLY,
    LABEL_STYLE_NONE as LABEL_STYLE_NONE,
    LABEL_STYLE_TABLENAME_PLUS_COL as LABEL_STYLE_TABLENAME_PLUS_COL,
    Alias as Alias,
    AliasedReturnsRows as AliasedReturnsRows,
    CompoundSelect as CompoundSelect,
    Exists as Exists,
    FromClause as FromClause,
    FromGrouping as FromGrouping,
    GenerativeSelect as GenerativeSelect,
    HasCTE as HasCTE,
    HasPrefixes as HasPrefixes,
    HasSuffixes as HasSuffixes,
    Join as Join,
    Lateral as Lateral,
    ReturnsRows as ReturnsRows,
    ScalarSelect as ScalarSelect,
    Select as Select,
    Selectable as Selectable,
    SelectBase as SelectBase,
    Subquery as Subquery,
    TableClause as TableClause,
    TableSample as TableSample,
    TableValuedAlias as TableValuedAlias,
    TextAsFrom as TextAsFrom,
    TextualSelect as TextualSelect,
    Values as Values,
    subquery as subquery,
)
from .traversals import CacheKey as CacheKey
from .visitors import Traversible, Visitable as Visitable

_T = TypeVar("_T")

__all__ = [
    "Alias",
    "AliasedReturnsRows",
    "any_",
    "all_",
    "CacheKey",
    "ClauseElement",
    "ColumnCollection",
    "ColumnElement",
    "CompoundSelect",
    "Delete",
    "FromClause",
    "Insert",
    "Join",
    "Lateral",
    "LambdaElement",
    "StatementLambdaElement",
    "Select",
    "Selectable",
    "TableClause",
    "TableValuedAlias",
    "Update",
    "Values",
    "alias",
    "and_",
    "asc",
    "between",
    "bindparam",
    "case",
    "cast",
    "column",
    "custom_op",
    "cte",
    "delete",
    "desc",
    "distinct",
    "except_",
    "except_all",
    "exists",
    "extract",
    "func",
    "modifier",
    "collate",
    "insert",
    "intersect",
    "intersect_all",
    "join",
    "label",
    "lateral",
    "lambda_stmt",
    "literal",
    "literal_column",
    "not_",
    "null",
    "nulls_first",
    "nulls_last",
    "or_",
    "outparam",
    "outerjoin",
    "over",
    "select",
    "table",
    "text",
    "tuple_",
    "type_coerce",
    "quoted_name",
    "union",
    "union_all",
    "update",
    "quoted_name",
    "within_group",
    "Subquery",
    "TableSample",
    "tablesample",
    "values",
]

def all_(expr) -> CollectionAggregate: ...
def any_(expr) -> CollectionAggregate: ...
@overload
def and_() -> BooleanClauseList: ...
@overload
def and_(__clause: _CoercibleElement) -> ClauseElement: ...
@overload
def and_(*clauses: _CoercibleElement) -> ClauseElement | BooleanClauseList: ...
def alias(selectable, name=None, flat=False) -> Alias: ...
def tablesample(selectable, sampling, name=None, seed=None) -> TableSample: ...
def lateral(selectable, name=None) -> Lateral: ...
@overload
def or_() -> BooleanClauseList: ...
@overload
def or_(__clause: _CoercibleElement) -> ClauseElement: ...
@overload
def or_(*clauses: _CoercibleElement) -> ClauseElement | BooleanClauseList: ...

# If the parameter quote is not None. The parameter key is strigified.
@overload
def bindparam(
    key: str,
    value: _T | _symbol | symbol | None = None,
    type_: TypeEngine | type[TypeEngine] | None = None,
    unique: bool = False,
    required: bool | _symbol | symbol = ...,
    quote: None = None,
    callable_: Callable[[], _T] | None = None,
    expanding: bool = False,
    isoutparam: bool = False,
    literal_execute: bool = False,
    _compared_to_operator: Incomplete | None = None,
    _compared_to_type: Incomplete | None = None,
    _is_crud: bool = False,
) -> BindParameter[Incomplete]: ...
@overload
def bindparam(
    key: object,
    *,
    value: _T | _symbol | symbol | None = None,
    type_: TypeEngine | type[TypeEngine] | None = None,
    unique: bool = False,
    required: bool | _symbol | symbol = ...,
    quote: bool,
    callable_: Callable[[], _T] | None = None,
    expanding: bool = False,
    isoutparam: bool = False,
    literal_execute: bool = False,
    _compared_to_operator: Incomplete | None = None,
    _compared_to_type: Incomplete | None = None,
    _is_crud: bool = False,
) -> BindParameter[Incomplete]: ...
def select(*args, **kw) -> Select: ...
def text(text, bind=None) -> TextClause: ...
def table(name: str, *columns: ColumnClause, **kw) -> TableClause: ...
def column(
    text, type_: TypeEngine | type[TypeEngine] | None = None, is_literal: bool = False, _selectable: Incomplete | None = None
) -> ColumnClause: ...
def over(
    element: FunctionElement | WithinGroup,
    partition_by: _CoercibleElement | None = None,
    order_by: _CoercibleElement | None = None,
    range_: tuple[
        str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc | None,
        str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc | None,
    ]
    | None = None,
    rows: tuple[
        str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc | None,
        str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc | None,
    ]
    | None = None,
) -> Over: ...
def within_group(element: FunctionElement, *order_by: _CoercibleElement) -> WithinGroup: ...
def label(
    name: str | _anonymous_label, element: ColumnElement[Incomplete], type_: TypeEngine | type[TypeEngine] | None = None
) -> Label: ...
def case(
    *whens: _DictLike[ClauseElement, Incomplete], value: Incomplete | None = None, else_: Incomplete | None = None
) -> Case: ...
def cast(expression, type_: TypeEngine | type[TypeEngine] | None) -> Cast: ...
def cte(selectable, name=None, recursive=False) -> CTE: ...
def values(*columns, **kw) -> Values: ...
def extract(field, expr: ClauseElement, **kwargs: Unused) -> Extract: ...
def tuple_(*clauses: ColumnElement[Incomplete], **kw) -> Tuple: ...
def except_(*selects, **kwargs) -> CompoundSelect: ...
def except_all(*selects, **kwargs) -> CompoundSelect: ...
def intersect(*selects, **kwargs) -> CompoundSelect: ...
def intersect_all(*selects, **kwargs) -> CompoundSelect: ...
def union(*selects, **kwargs) -> CompoundSelect: ...
def union_all(*selects, **kwargs) -> CompoundSelect: ...
def exists(*args, **kwargs) -> Exists: ...
def nulls_first(column) -> UnaryExpression: ...
def nulls_last(column) -> UnaryExpression: ...
def asc(column) -> UnaryExpression: ...
def desc(column) -> UnaryExpression: ...
def distinct(expr) -> UnaryExpression: ...
def type_coerce(expression: str | ColumnElement[Incomplete], type_: TypeEngine | type[TypeEngine] | None) -> TypeCoerce: ...
def true() -> True_: ...
def false() -> False_: ...
def null() -> Null: ...
def join(left, right, onclause=None, isouter=False, full=False) -> Join: ...
def outerjoin(left, right, onclause=None, full=False) -> Join: ...
def insert(
    table: _CoercibleElement,
    values: Incomplete | None = None,
    inline: bool = False,
    bind: Incomplete | None = None,
    prefixes: Incomplete | None = None,
    returning: Incomplete | None = None,
    return_defaults: bool = False,
    **dialect_kw,
) -> Insert: ...
def update(
    table: _CoercibleElement,
    whereclause: bool | str | Traversible | None = None,
    values: Incomplete | None = None,
    inline: bool = False,
    bind: Incomplete | None = None,
    prefixes: Incomplete | None = None,
    returning: Incomplete | None = None,
    return_defaults: bool = False,
    preserve_parameter_order: bool = False,
    **dialect_kw,
) -> Update: ...
def delete(
    table: _CoercibleElement,
    whereclause: bool | str | Traversible | None = None,
    bind: Incomplete | None = None,
    returning: Incomplete | None = None,
    prefixes: Incomplete | None = None,
    **dialect_kw,
) -> Delete: ...
def funcfilter(func: FunctionFilter, *criterion) -> FunctionFilter: ...
