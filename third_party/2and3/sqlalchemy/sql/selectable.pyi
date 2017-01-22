from typing import Any

from .base import Immutable, Executable, \
    ColumnCollection, ColumnSet, Generative
from .elements import ClauseElement, TextClause, ClauseList, \
    Grouping, UnaryExpression, BindParameter
from .annotation import Annotated
from .visitors import Visitable
from .. import util

def subquery(alias, *args, **kwargs): ...
def alias(selectable, name=..., flat: bool=...): ...

class Selectable(ClauseElement):
    def selectable(self): ...

class HasPrefixes(object):
    def prefix_with(self, *expr, **kw): ...

class HasSuffixes(object):
    def suffix_with(self, *expr, **kw): ...

class FromClause(Selectable):
    def count(self, functions, whereclause=None, **params): ...
    def select(self, whereclause=None, **params): ...
    def join(self, right, onclause=None, isouter: bool=False): ...
    def outerjoin(self, right, onclause=None): ...
    def alias(self, name=None, flat: bool=False): ...
    def is_derived_from(self, fromclause): ...
    def _is_lexical_equivalent(self, other): ...
    def replace_selectable(self, sqlutil, old, alias): ...
    def correspond_on_equivalents(self, column, equivalents): ...
    def corresponding_column(self, column, require_embedded: bool=False): ...
    @property
    def description(self): ...
    def _reset_exported(self): ...
    @property
    def columns(self): ...
    @property
    def primary_key(self) -> Any: ...
    @property
    def foreign_keys(self) -> Any: ...
    def _init_collections(self): ...
    @property
    def _cols_populated(self): ...
    def _populate_column_collection(self): ...
    def _refresh_for_new_column(self, column): ...

class Join(FromClause): ...
class Alias(FromClause): ...
class CTE(Generative, HasSuffixes, Alias): ...
class FromGrouping(FromClause): ...

class TableClause(Immutable, FromClause):
    def __init__(self, name, *columns): ...
    def _export_columns(self): ...
    @util.memoized_property
    def description(self): ...
    def append_column(self, c): ...
    def get_children(self, **kwargs): ...
    def count(self, whereclause=None, **params): ...
    def insert(self, values=None, inline=False, **kwargs): ...
    def update(self, whereclause=None, values=None, inline=False, **kwargs): ...
    def delete(self, whereclause=None, **kwargs): ...
    @property
    def _from_objects(self): ...

class ForUpdateArg(ClauseElement): ...
class SelectBase(Executable, FromClause): ...
class GenerativeSelect(SelectBase): ...
class CompoundSelect(GenerativeSelect): ...
class Select(HasPrefixes, HasSuffixes, GenerativeSelect): ...
class ScalarSelect(Generative, Grouping): ...
class Exists(UnaryExpression): ...
class TextAsFrom(SelectBase): ...
class AnnotatedFromClause(Annotated): ...
