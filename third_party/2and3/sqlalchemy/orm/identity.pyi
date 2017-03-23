# Stubs for sqlalchemy.orm.identity (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .. import exc as sa_exc
from . import util as orm_util

class IdentityMap:
    def __init__(self) -> None: ...
    def keys(self): ...
    def replace(self, state): ...
    def add(self, state): ...
    def update(self, dict): ...
    def clear(self): ...
    def check_modified(self): ...
    def has_key(self, key): ...
    def popitem(self): ...
    def pop(self, key, *args): ...
    def setdefault(self, key, default: Optional[Any] = ...): ...
    def __len__(self): ...
    def copy(self): ...
    def __setitem__(self, key, value): ...
    def __delitem__(self, key): ...

class WeakInstanceDict(IdentityMap):
    def __getitem__(self, key): ...
    def __contains__(self, key): ...
    def contains_state(self, state): ...
    def replace(self, state): ...
    def add(self, state): ...
    def get(self, key, default: Optional[Any] = ...): ...
    def items(self): ...
    def values(self): ...
    def __iter__(self): ...
    def iteritems(self): ...
    def itervalues(self): ...
    def all_states(self): ...
    def discard(self, state): ...
    def safe_discard(self, state): ...
    def prune(self): ...

class StrongInstanceDict(IdentityMap):
    def itervalues(self): ...
    def iteritems(self): ...
    def __iter__(self): ...
    def __getitem__(self, key): ...
    def __contains__(self, key): ...
    def get(self, key, default: Optional[Any] = ...): ...
    def values(self): ...
    def items(self): ...
    def all_states(self): ...
    def contains_state(self, state): ...
    def replace(self, state): ...
    def add(self, state): ...
    def discard(self, state): ...
    def safe_discard(self, state): ...
    modified = ...  # type: Any
    def prune(self): ...
