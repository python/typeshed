# Stubs for sqlalchemy.orm.persistence (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from .. import exc as sa_exc
from . import exc as orm_exc
from .base import state_str as state_str, _attr_as_key as _attr_as_key, _entity_descriptor as _entity_descriptor
from ..sql import expression as expression
from ..sql.base import _from_objects as _from_objects

def save_obj(base_mapper, states, uowtransaction, single: bool = ...): ...
def post_update(base_mapper, states, uowtransaction, post_update_cols): ...
def delete_obj(base_mapper, states, uowtransaction): ...

class BulkUD:
    query = ...  # type: Any
    mapper = ...  # type: Any
    def __init__(self, query) -> None: ...
    @property
    def session(self): ...
    def exec_(self): ...

class BulkEvaluate(BulkUD): ...
class BulkFetch(BulkUD): ...

class BulkUpdate(BulkUD):
    values = ...  # type: Any
    update_kwargs = ...  # type: Any
    def __init__(self, query, values, update_kwargs) -> None: ...
    @classmethod
    def factory(cls, query, synchronize_session, values, update_kwargs): ...

class BulkDelete(BulkUD):
    def __init__(self, query) -> None: ...
    @classmethod
    def factory(cls, query, synchronize_session): ...

class BulkUpdateEvaluate(BulkEvaluate, BulkUpdate): ...
class BulkDeleteEvaluate(BulkEvaluate, BulkDelete): ...
class BulkUpdateFetch(BulkFetch, BulkUpdate): ...
class BulkDeleteFetch(BulkFetch, BulkDelete): ...
