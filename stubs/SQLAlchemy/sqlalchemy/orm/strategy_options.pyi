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
    def set_relationship_strategy(self, attr, strategy, propagate_to_loaders: bool = ...) -> None: ...
    def set_column_strategy(self, attrs, strategy, opts: Any | None = ..., opts_only: bool = ...) -> None: ...
    def set_generic_strategy(self, attrs, strategy) -> None: ...
    def set_class_strategy(self, strategy, opts) -> None: ...

class _UnboundLoad(Load):
    path: Any
    local_opts: Any
    def __init__(self) -> None: ...

class loader_option:
    def __init__(self) -> None: ...
    name: Any
    fn: Any
    def __call__(self, fn): ...
