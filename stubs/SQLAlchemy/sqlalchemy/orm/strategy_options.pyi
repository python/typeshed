from _typeshed import Incomplete, Self
from collections.abc import Callable
from typing import Any, Generic, Protocol, TypeVar

from ..sql.base import Generative
from .interfaces import LoaderOption

class Load(Generative, LoaderOption):
    path: Any
    context: Any
    local_opts: Any
    is_class_strategy: bool
    def __init__(self, entity) -> None: ...
    @classmethod
    def for_existing_path(cls, path): ...
    is_opts_only: bool
    strategy: Any
    propagate_to_loaders: bool
    def process_compile_state_replaced_entities(self, compile_state, mapper_entities) -> None: ...
    def process_compile_state(self, compile_state) -> None: ...
    def options(self: Self, *opts) -> Self: ...
    def set_relationship_strategy(self: Self, attr, strategy, propagate_to_loaders: bool = ...) -> Self: ...
    def set_column_strategy(self: Self, attrs, strategy, opts: Incomplete | None = ..., opts_only: bool = ...) -> Self: ...
    def set_generic_strategy(self: Self, attrs, strategy) -> Self: ...
    def set_class_strategy(self: Self, strategy, opts) -> Self: ...
    # added dynamically at runtime
    def contains_eager(loadopt, attr, alias: Incomplete | None = ...): ...
    def load_only(loadopt, *attrs): ...
    def joinedload(loadopt, attr, innerjoin: Incomplete | None = ...): ...
    def subqueryload(loadopt, attr): ...
    def selectinload(loadopt, attr): ...
    def lazyload(loadopt, attr): ...
    def immediateload(loadopt, attr): ...
    def noload(loadopt, attr): ...
    def raiseload(loadopt, attr, sql_only: bool = ...): ...
    def defaultload(loadopt, attr): ...
    def defer(loadopt, key, raiseload: bool = ...): ...
    def undefer(loadopt, key): ...
    def undefer_group(loadopt, name): ...
    def with_expression(loadopt, key, expression): ...
    def selectin_polymorphic(loadopt, classes): ...

class _UnboundLoad(Load):
    path: Any
    local_opts: Any
    def __init__(self) -> None: ...

###
# The methods below are decorated with the class loader_option
# They dynamically become instances of loader_option,
# wich is callable with their original parameters.
#
# While both mypy and pyright's validation work, Pylance is unable to
# show the parameters and return types.
#
# There is a workaround (define the method for Pylance, then reassign
# an instance of loader_option to it for mypy, and add pyright+Flake8
# suppressions), but it is too hacky and relies on some unsupported quirks.
#
# Asking Pylance to add support for these generic callables might be preferable.
###

_F = TypeVar("_F", bound=Callable[..., loader_option[Any]])

class loader_option(Generic[_F]):
    name: str
    _dynamic: _F
    fn: _F
    __call__: _F  # Cheesy "__call__" definition to use the dynamic methods instead

class _contains_eager(Protocol):
    def __call__(self, loadopt, attr, alias: Incomplete | None = ...) -> loader_option[_contains_eager]: ...

contains_eager: loader_option[_contains_eager]

class _load_only(Protocol):
    def __call__(self, loadopt, *attrs) -> loader_option[_load_only]: ...

load_only: loader_option[_load_only]

class _subqueryload(Protocol):
    def __call__(self, loadopt, attr) -> loader_option[_subqueryload]: ...

subqueryload: loader_option[_subqueryload]

class _selectinload(Protocol):
    def __call__(self, loadopt, attr) -> loader_option[_selectinload]: ...

selectinload: loader_option[_selectinload]

class _lazyload(Protocol):
    def __call__(self, loadopt, attr) -> loader_option[_lazyload]: ...

lazyload: loader_option[_lazyload]

class _immediateload(Protocol):
    def __call__(self, loadopt, attr) -> loader_option[_immediateload]: ...

immediateload: loader_option[_immediateload]

class _noload(Protocol):
    def __call__(self, loadopt, attr) -> loader_option[_noload]: ...

noload: loader_option[_noload]

class _raiseload(Protocol):
    def __call__(self, loadopt, attr, sql_only: bool = ...) -> loader_option[_raiseload]: ...

raiseload: loader_option[_raiseload]

class _defaultload(Protocol):
    def __call__(self, loadopt, attr) -> loader_option[_defaultload]: ...

defaultload: loader_option[_defaultload]

class _defer(Protocol):
    def __call__(self, loadopt, attr, sql_only: bool = ...) -> loader_option[_defer]: ...

defer: loader_option[_defer]

class _undefer(Protocol):
    def __call__(self, loadopt, key) -> loader_option[_undefer]: ...

undefer: loader_option[_undefer]

class _undefer_group(Protocol):
    def __call__(self, loadopt, name) -> loader_option[_undefer_group]: ...

undefer_group: loader_option[_undefer_group]

class _with_expression(Protocol):
    def __call__(self, loadopt, key, expression) -> loader_option[_with_expression]: ...

with_expression: loader_option[_with_expression]

class _selectin_polymorphic(Protocol):
    def __call__(self, loadopt, classes) -> loader_option[_selectin_polymorphic]: ...

selectin_polymorphic: loader_option[_selectin_polymorphic]
