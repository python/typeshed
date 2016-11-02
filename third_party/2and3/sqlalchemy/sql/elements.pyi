
from .visitors import Visitable
from .annotation import Annotated
from .base import Executable, Immutable
from .operators import ColumnOperators
from .. import util

class ClauseElement(Visitable): ...

class ColumnElement(ColumnOperators, ClauseElement): ...

class BindParameter(ColumnElement): ...
class BinaryExpression(ColumnElement): ...

class TypeClause(ClauseElement): ...
class TextClause(Executable, ClauseElement): ...

class Null(ColumnElement): ...
class False_(ColumnElement): ...
class True_(ColumnElement): ...

class ClauseList(ClauseElement): ...
class BooleanClauseList(ClauseList, ColumnElement): ...
class Tuple(ClauseList, ColumnElement): ...
class Case(ColumnElement): ...
class Cast(ColumnElement): ...
class Extract(ColumnElement): ...
class _label_reference(ColumnElement): ...

class _textual_label_reference(ColumnElement): ...
class UnaryExpression(ColumnElement): ...
class AsBoolean(UnaryExpression): ...
class Grouping(ColumnElement): ...
class Over(ColumnElement): ...
class FunctionFilter(ColumnElement): ...
class Label(ColumnElement): ...
class ColumnClause(Immutable, ColumnElement): ...
class _IdentifiedClause(Executable, ClauseElement): ...
class SavepointClause(_IdentifiedClause): ...
class RollbackToSavepointClause(_IdentifiedClause): ...
class ReleaseSavepointClause(_IdentifiedClause): ...
class quoted_name(util.MemoizedSlots, util.text_type): ...
class _truncated_label(quoted_name): ...
class conv(_truncated_label): ...
class _defer_name(_truncated_label): ...
class _defer_none_name(_defer_name): ...
class _anonymous_label(_truncated_label): ...
class AnnotatedColumnElement(Annotated): ...

def _clone(element, **kw): ...
def _type_from_args(args): ...
def _literal_as_binds(element, name, type_=None): ...

def collate(expression, collation) -> BinaryExpression: ...
def between(expr, lower_bound, upper_bound, symmetric: bool=...): ...
def literal(value, type_=None) -> BindParameter: ...
def outparam(key, type_=None) -> BindParameter: ...
def type_coerce(expression, type_): ...
def not_(clause): ...
def literal_column(text, type_=None): ...
