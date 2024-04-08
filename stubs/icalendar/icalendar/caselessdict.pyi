from _typeshed import Incomplete
from collections import OrderedDict

def canonsort_keys(keys, canonical_order: Incomplete | None = None): ...
def canonsort_items(dict1, canonical_order: Incomplete | None = None): ...

class CaselessDict(OrderedDict):
    def __init__(self, *args, **kwargs) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __contains__(self, key) -> bool: ...
    def get(self, key, default: Incomplete | None = None): ...
    def setdefault(self, key, value: Incomplete | None = None): ...
    def pop(self, key, default: Incomplete | None = None): ...
    def popitem(self): ...
    def has_key(self, key): ...
    def update(self, *args, **kwargs) -> None: ...
    def copy(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    canonical_order: Incomplete
    def sorted_keys(self): ...
    def sorted_items(self): ...
