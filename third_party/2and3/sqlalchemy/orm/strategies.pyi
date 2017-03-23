# Stubs for sqlalchemy.orm.strategies (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
import util
from .. import exc as sa_exc
from ..sql import visitors as visitors
from ..sql import util as sql_util
from . import exc as orm_exc, util as orm_util
from .state import InstanceState as InstanceState
from .util import _none_set as _none_set
from .interfaces import LoaderStrategy as LoaderStrategy, StrategizedProperty as StrategizedProperty
from .base import _SET_DEFERRED_EXPIRED as _SET_DEFERRED_EXPIRED, _DEFER_FOR_STATE as _DEFER_FOR_STATE
from .session import _state_session as _state_session

class UninstrumentedColumnLoader(LoaderStrategy):
    columns = ...  # type: Any
    def __init__(self, parent, strategy_key) -> None: ...
    def setup_query(self, context, entity, path, loadopt, adapter, column_collection: Optional[Any] = ..., **kwargs): ...
    def create_row_processor(self, context, path, loadopt, mapper, result, adapter, populators): ...

class ColumnLoader(LoaderStrategy):
    columns = ...  # type: Any
    is_composite = ...  # type: Any
    def __init__(self, parent, strategy_key) -> None: ...
    def setup_query(self, context, entity, path, loadopt, adapter, column_collection, memoized_populators, **kwargs): ...
    is_class_level = ...  # type: bool
    def init_class_attribute(self, mapper): ...
    def create_row_processor(self, context, path, loadopt, mapper, result, adapter, populators): ...

class DeferredColumnLoader(LoaderStrategy):
    columns = ...  # type: Any
    group = ...  # type: Any
    def __init__(self, parent, strategy_key) -> None: ...
    def create_row_processor(self, context, path, loadopt, mapper, result, adapter, populators): ...
    is_class_level = ...  # type: bool
    def init_class_attribute(self, mapper): ...
    def setup_query(self, context, entity, path, loadopt, adapter, column_collection, memoized_populators, only_load_props: Optional[Any] = ..., **kw): ...

class LoadDeferredColumns:
    key = ...  # type: Any
    def __init__(self, key) -> None: ...
    def __call__(self, state, passive: Any = ...): ...

class AbstractRelationshipLoader(LoaderStrategy):
    mapper = ...  # type: Any
    target = ...  # type: Any
    uselist = ...  # type: Any
    def __init__(self, parent, strategy_key) -> None: ...

class NoLoader(AbstractRelationshipLoader):
    is_class_level = ...  # type: bool
    def init_class_attribute(self, mapper): ...
    def create_row_processor(self, context, path, loadopt, mapper, result, adapter, populators): ...

class LazyLoader(AbstractRelationshipLoader, util.MemoizedSlots):
    use_get = ...  # type: Any
    def __init__(self, parent, strategy_key) -> None: ...
    is_class_level = ...  # type: bool
    def init_class_attribute(self, mapper): ...
    def create_row_processor(self, context, path, loadopt, mapper, result, adapter, populators): ...

class LoadLazyAttribute:
    key = ...  # type: Any
    strategy_key = ...  # type: Any
    def __init__(self, key, initiating_strategy) -> None: ...
    def __call__(self, state, passive: Any = ...): ...

class ImmediateLoader(AbstractRelationshipLoader):
    def init_class_attribute(self, mapper): ...
    def setup_query(self, context, entity, path, loadopt, adapter, column_collection: Optional[Any] = ..., parentmapper: Optional[Any] = ..., **kwargs): ...
    def create_row_processor(self, context, path, loadopt, mapper, result, adapter, populators): ...

class SubqueryLoader(AbstractRelationshipLoader):
    join_depth = ...  # type: Any
    def __init__(self, parent, strategy_key) -> None: ...
    def init_class_attribute(self, mapper): ...
    def setup_query(self, context, entity, path, loadopt, adapter, column_collection: Optional[Any] = ..., parentmapper: Optional[Any] = ..., **kwargs): ...
    class _SubqCollections:
        subq = ...  # type: Any
        def __init__(self, subq) -> None: ...
        def get(self, key, default): ...
        def loader(self, state, dict_, row): ...
    def create_row_processor(self, context, path, loadopt, mapper, result, adapter, populators): ...

class JoinedLoader(AbstractRelationshipLoader):
    join_depth = ...  # type: Any
    def __init__(self, parent, strategy_key) -> None: ...
    def init_class_attribute(self, mapper): ...
    def setup_query(self, context, entity, path, loadopt, adapter, column_collection: Optional[Any] = ..., parentmapper: Optional[Any] = ..., chained_from_outerjoin: bool = ..., **kwargs): ...
    def create_row_processor(self, context, path, loadopt, mapper, result, adapter, populators): ...

def single_parent_validator(desc, prop): ...
