from _typeshed import Incomplete
from typing import Generic, TypeVar

from ..cimmutabledict import immutabledict
from ..schema import Table
from .compiler import _CompileLabel
from .crud import _multiparam_column
from .elements import (
    AnnotatedColumnElement as _ElementsAnnotatedColumnElement,
    AsBoolean,
    BinaryExpression,
    BindParameter,
    BooleanClauseList,
    Case,
    Cast,
    ClauseList,
    CollationClause,
    CollectionAggregate,
    ColumnClause,
    ColumnElement,
    Extract,
    False_,
    FunctionFilter,
    Grouping,
    IndexExpression,
    Label,
    NamedColumn,
    Null,
    Over,
    Slice,
    TableValuedColumn,
    True_,
    Tuple,
    TypeCoerce,
    UnaryExpression,
    WithinGroup,
    _label_reference,
    _textual_label_reference,
)
from .functions import (
    AnsiFunction,
    Function,
    FunctionAsBinary,
    FunctionElement,
    GenericFunction,
    OrderedSetAgg,
    ReturnTypeFromArgs,
    ScalarFunctionColumn,
    array_agg,
    char_length,
    coalesce,
    concat,
    count,
    cube,
    cume_dist,
    current_date,
    current_time,
    current_timestamp,
    current_user,
    dense_rank,
    grouping_sets,
    localtime,
    localtimestamp,
    max,
    min,
    mode,
    next_value,
    now,
    percent_rank,
    percentile_cont,
    percentile_disc,
    random,
    rank,
    rollup,
    session_user,
    sum,
    sysdate,
    user,
)
from .schema import Column
from .selectable import (
    CTE,
    Alias,
    AliasedReturnsRows,
    AnnotatedFromClause as _SelectableAnnotatedFromClause,
    Exists,
    FromClause,
    FromGrouping,
    Join,
    Lateral,
    ScalarSelect,
    Subquery,
    TableClause,
    TableSample,
    TableValuedAlias,
    Values,
    _OffsetLimitParam,
)

_T = TypeVar("_T")

class _SupportsDict(Generic[_T]):
    __dict__: dict[str, _T]

EMPTY_ANNOTATIONS: immutabledict[Incomplete, Incomplete]

class SupportsAnnotations: ...
class SupportsCloneAnnotations(SupportsAnnotations): ...
class SupportsWrappingAnnotations(SupportsAnnotations): ...

class Annotated(Generic[_T]):
    __dict__: dict[str, _T]
    __element: _SupportsDict[_T]
    def __init__(self, element: _SupportsDict[_T], values) -> None: ...
    def __reduce__(self): ...
    def __hash__(self) -> int: ...
    def __eq__(self, other) -> bool: ...
    @property
    def entity_namespace(self): ...

annotated_classes: dict[type[Incomplete], type[Annotated]] = ...  # pyright: ignore[reportMissingTypeArgument]  # pytype issue

# Everything below is dynamically generated at runtime

class AnnotatedAlias(AnnotatedAliasedReturnsRows, Alias): ...
class AnnotatedAliasedReturnsRows(AnnotatedFromClause, AliasedReturnsRows): ...
class AnnotatedAnsiFunction(AnnotatedGenericFunction[_T], AnsiFunction): ...  # type: ignore[misc]
class AnnotatedAsBoolean(AnnotatedUnaryExpression[_T], AsBoolean): ...  # type: ignore[misc]
class AnnotatedBinaryExpression(AnnotatedColumnElement[_T], BinaryExpression): ...  # type: ignore[misc]
class AnnotatedBindParameter(AnnotatedColumnElement[_T], BindParameter[_T]): ...  # type: ignore[misc]
class AnnotatedBooleanClauseList(AnnotatedColumnElement[_T], BooleanClauseList): ...  # type: ignore[misc]
class AnnotatedCTE(AnnotatedAliasedReturnsRows, CTE): ...
class AnnotatedCase(AnnotatedColumnElement[_T], Case): ...  # type: ignore[misc]
class AnnotatedCast(AnnotatedColumnElement[_T], Cast): ...  # type: ignore[misc]
class AnnotatedClauseList(Annotated[_T], ClauseList): ...
class AnnotatedCollationClause(AnnotatedColumnElement[_T], CollationClause): ...  # type: ignore[misc]
class AnnotatedCollectionAggregate(AnnotatedUnaryExpression[_T], CollectionAggregate): ...  # type: ignore[misc]
class AnnotatedColumn(AnnotatedColumnClause[_T], Column): ...  # type: ignore[misc]
class AnnotatedColumnClause(AnnotatedNamedColumn[_T], ColumnClause): ...  # type: ignore[misc]
class AnnotatedColumnElement(_ElementsAnnotatedColumnElement, ColumnElement[_T]): ...  # type: ignore[misc]
class AnnotatedExists(AnnotatedUnaryExpression[_T], Exists): ...  # type: ignore[misc]
class AnnotatedExtract(AnnotatedColumnElement[_T], Extract): ...  # type: ignore[misc]
class AnnotatedFalse_(AnnotatedColumnElement[_T], False_): ...  # type: ignore[misc]
class AnnotatedFromClause(_SelectableAnnotatedFromClause, FromClause): ...
class AnnotatedFromGrouping(AnnotatedFromClause, FromGrouping): ...
class AnnotatedFunction(AnnotatedFunctionElement[_T], Function): ...  # type: ignore[misc]
class AnnotatedFunctionAsBinary(AnnotatedBinaryExpression[_T], FunctionAsBinary): ...  # type: ignore[misc]
class AnnotatedFunctionElement(AnnotatedColumnElement[_T], FunctionElement): ...  # type: ignore[misc]
class AnnotatedFunctionFilter(AnnotatedColumnElement[_T], FunctionFilter): ...  # type: ignore[misc]
class AnnotatedGenericFunction(AnnotatedFunction[_T], GenericFunction): ...  # type: ignore[misc]
class AnnotatedGrouping(AnnotatedColumnElement[_T], Grouping): ...  # type: ignore[misc]
class AnnotatedIndexExpression(AnnotatedBinaryExpression[_T], IndexExpression): ...  # type: ignore[misc]
class AnnotatedJoin(AnnotatedFromClause, Join): ...
class AnnotatedLabel(AnnotatedColumnElement[_T], Label): ...  # type: ignore[misc]
class AnnotatedLateral(AnnotatedAliasedReturnsRows, Lateral): ...
class AnnotatedNamedColumn(AnnotatedColumnElement[_T], NamedColumn): ...  # type: ignore[misc]
class AnnotatedNull(AnnotatedColumnElement[_T], Null): ...  # type: ignore[misc]
class AnnotatedOrderedSetAgg(AnnotatedGenericFunction[_T], OrderedSetAgg): ...  # type: ignore[misc]
class AnnotatedOver(AnnotatedColumnElement[_T], Over): ...  # type: ignore[misc]
class AnnotatedReturnTypeFromArgs(AnnotatedGenericFunction[_T], ReturnTypeFromArgs): ...  # type: ignore[misc]
class AnnotatedScalarFunctionColumn(AnnotatedNamedColumn[_T], ScalarFunctionColumn): ...  # type: ignore[misc]
class AnnotatedScalarSelect(AnnotatedGrouping[_T], ScalarSelect): ...  # type: ignore[misc]
class AnnotatedSlice(AnnotatedColumnElement[_T], Slice): ...  # type: ignore[misc]
class AnnotatedSubquery(AnnotatedAliasedReturnsRows, Subquery): ...
class AnnotatedTable(AnnotatedTableClause, Table): ...
class AnnotatedTableClause(AnnotatedFromClause, TableClause): ...
class AnnotatedTableSample(AnnotatedAliasedReturnsRows, TableSample): ...
class AnnotatedTableValuedAlias(AnnotatedAlias, TableValuedAlias): ...
class AnnotatedTableValuedColumn(AnnotatedNamedColumn[_T], TableValuedColumn): ...  # type: ignore[misc]
class AnnotatedTrue_(AnnotatedColumnElement[_T], True_): ...  # type: ignore[misc]
class AnnotatedTuple(AnnotatedColumnElement[_T], Tuple): ...  # type: ignore[misc]
class AnnotatedTypeCoerce(AnnotatedColumnElement[_T], TypeCoerce): ...  # type: ignore[misc]
class AnnotatedUnaryExpression(AnnotatedColumnElement[_T], UnaryExpression): ...  # type: ignore[misc]
class AnnotatedValues(AnnotatedFromClause, Values): ...
class AnnotatedWithinGroup(AnnotatedColumnElement[_T], WithinGroup): ...  # type: ignore[misc]
class Annotated_CompileLabel(AnnotatedColumnElement[_T], _CompileLabel): ...  # type: ignore[misc]
class Annotated_OffsetLimitParam(AnnotatedBindParameter[_T], _OffsetLimitParam): ...  # type: ignore[misc]
class Annotated_label_reference(AnnotatedColumnElement[_T], _label_reference): ...  # type: ignore[misc]
class Annotated_multiparam_column(AnnotatedColumnElement[_T], _multiparam_column[_T]): ...  # type: ignore[misc]
class Annotated_textual_label_reference(AnnotatedColumnElement[_T], _textual_label_reference): ...  # type: ignore[misc]
class Annotatedarray_agg(AnnotatedGenericFunction[_T], array_agg): ...  # type: ignore[misc]
class Annotatedchar_length(AnnotatedGenericFunction[_T], char_length): ...  # type: ignore[misc]
class Annotatedcoalesce(AnnotatedReturnTypeFromArgs[_T], coalesce): ...  # type: ignore[misc]
class Annotatedconcat(AnnotatedGenericFunction[_T], concat): ...  # type: ignore[misc]
class Annotatedcount(AnnotatedGenericFunction[_T], count): ...  # type: ignore[misc]
class Annotatedcube(AnnotatedGenericFunction[_T], cube): ...  # type: ignore[misc]
class Annotatedcume_dist(AnnotatedGenericFunction[_T], cume_dist): ...  # type: ignore[misc]
class Annotatedcurrent_date(AnnotatedAnsiFunction[_T], current_date): ...  # type: ignore[misc]
class Annotatedcurrent_time(AnnotatedAnsiFunction[_T], current_time): ...  # type: ignore[misc]
class Annotatedcurrent_timestamp(AnnotatedAnsiFunction[_T], current_timestamp): ...  # type: ignore[misc]
class Annotatedcurrent_user(AnnotatedAnsiFunction[_T], current_user): ...  # type: ignore[misc]
class Annotateddense_rank(AnnotatedGenericFunction[_T], dense_rank): ...  # type: ignore[misc]
class Annotatedgrouping_sets(AnnotatedGenericFunction[_T], grouping_sets): ...  # type: ignore[misc]
class Annotatedlocaltime(AnnotatedAnsiFunction[_T], localtime): ...  # type: ignore[misc]
class Annotatedlocaltimestamp(AnnotatedAnsiFunction[_T], localtimestamp): ...  # type: ignore[misc]
class Annotatedmax(AnnotatedReturnTypeFromArgs[_T], max): ...  # type: ignore[misc]
class Annotatedmin(AnnotatedReturnTypeFromArgs[_T], min): ...  # type: ignore[misc]
class Annotatedmode(AnnotatedOrderedSetAgg[_T], mode): ...  # type: ignore[misc]
class Annotatednext_value(AnnotatedGenericFunction[_T], next_value): ...  # type: ignore[misc]
class Annotatednow(AnnotatedGenericFunction[_T], now): ...  # type: ignore[misc]
class Annotatedpercent_rank(AnnotatedGenericFunction[_T], percent_rank): ...  # type: ignore[misc]
class Annotatedpercentile_cont(AnnotatedOrderedSetAgg[_T], percentile_cont): ...  # type: ignore[misc]
class Annotatedpercentile_disc(AnnotatedOrderedSetAgg[_T], percentile_disc): ...  # type: ignore[misc]
class Annotatedrandom(AnnotatedGenericFunction[_T], random): ...  # type: ignore[misc]
class Annotatedrank(AnnotatedGenericFunction[_T], rank): ...  # type: ignore[misc]
class Annotatedrollup(AnnotatedGenericFunction[_T], rollup): ...  # type: ignore[misc]
class Annotatedsession_user(AnnotatedAnsiFunction[_T], session_user): ...  # type: ignore[misc]
class Annotatedsum(AnnotatedReturnTypeFromArgs[_T], sum): ...  # type: ignore[misc]
class Annotatedsysdate(AnnotatedAnsiFunction[_T], sysdate): ...  # type: ignore[misc]
class Annotateduser(AnnotatedAnsiFunction[_T], user): ...  # type: ignore[misc]
