from _typeshed import Incomplete
from typing import Any

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
    def options(self, *opts) -> None: ...
    def set_relationship_strategy(self, attr, strategy, propagate_to_loaders: bool = True) -> None: ...
    def set_column_strategy(self, attrs, strategy, opts: Incomplete | None = None, opts_only: bool = False) -> None: ...
    def set_generic_strategy(self, attrs, strategy) -> None: ...
    def set_class_strategy(self, strategy, opts) -> None: ...
    # added dynamically at runtime
    def contains_eager(self, attr, alias: Incomplete | None = None): ...
    def load_only(self, *attrs): ...
    def joinedload(self, attr, innerjoin: Incomplete | None = None): ...
    def subqueryload(self, attr): ...
    def selectinload(self, attr): ...
    def lazyload(self, attr): ...
    def immediateload(self, attr): ...
    def noload(self, attr): ...
    def raiseload(self, attr, sql_only: bool = False): ...
    def defaultload(self, attr): ...
    def defer(self, key, raiseload: bool = False): ...
    def undefer(self, key): ...
    def undefer_group(self, name): ...
    def with_expression(self, key, expression): ...
    def selectin_polymorphic(self, classes): ...

class _UnboundLoad(Load):
    path: Any
    local_opts: Any
    def __init__(self) -> None: ...

class loader_option:
    name: Any
    fn: Any
    def __call__(self, fn): ...

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
