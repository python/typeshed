from _typeshed import Incomplete

class IdentityMap:
    def keys(self): ...
    def replace(self, state) -> None: ...
    def add(self, state) -> None: ...
    def update(self, dict_) -> None: ...
    def clear(self) -> None: ...
    def check_modified(self): ...
    def has_key(self, key): ...
    def popitem(self) -> None: ...
    def pop(self, key, *args) -> None: ...
    def setdefault(self, key, default: Incomplete | None = ...) -> None: ...
    def __len__(self) -> int: ...
    def copy(self) -> None: ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...

class WeakInstanceDict(IdentityMap):
    def __getitem__(self, key): ...
    def __contains__(self, key): ...
    def contains_state(self, state): ...
    def replace(self, state): ...
    def add(self, state): ...
    def get(self, key, default: Incomplete | None = ...): ...
    def items(self): ...
    def values(self): ...
    def __iter__(self): ...
    def all_states(self): ...
    def discard(self, state) -> None: ...
    def safe_discard(self, state) -> None: ...
