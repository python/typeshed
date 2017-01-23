from typing import Any, Iterable

from .visitors import ClauseVisitor
from .. import util

class Immutable(object):
    def unique_params(self, *optionaldict, **kwargs): ...
    def params(self, *optionaldict, **kwargs): ...
    def _clone(self) -> Immutable: ...

class DialectKWArgs(object):
    def argument_for(cls, dialect_name, argument_name, default): ...
    def kwargs(self): ...
    def dialect_options(self): ...

class Generative(object): ...

class Executable(Generative):
    def execution_options(self, **kw): ...
    def execute(self, *multiparams, **params): ...
    def scalar(self, *multiparams, **params): ...

    @property
    def bind(self): ...

class SchemaEventTarget(object): ...
class SchemaVisitor(ClauseVisitor): ...
class ColumnCollection(util.OrderedProperties):
    def replace(self, column): ...
    def add(self, column): ...
    def clear(self): ...
    def remove(self, column): ...
    def update(self, iter: Iterable[Any]): ...
    def extend(self, iter: Iterable[Any]): ...
    def contains_column(self, col): ...
    def as_immutable(self): ...

class ImmutableColumnCollection(util.ImmutableProperties, ColumnCollection): ...

class ColumnSet(util.ordered_column_set): ...

def _bind_or_error(schemaitem, msg): ...
