from typing import Any

from ..sql.traversals import HasCacheKey
from . import base as orm_base
from ..util import memoized_property

log: Any

class PathRegistry(HasCacheKey):
    is_token: bool
    is_root: bool
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def set(self, attributes, key, value) -> None: ...
    def setdefault(self, attributes, key, value) -> None: ...
    def get(self, attributes, key, value: Any | None = ...): ...
    def __len__(self): ...
    def __hash__(self): ...
    @property
    def length(self): ...
    def pairs(self) -> None: ...
    def contains_mapper(self, mapper): ...
    def contains(self, attributes, key): ...
    def __reduce__(self): ...
    @classmethod
    def serialize_context_dict(cls, dict_, tokens): ...
    @classmethod
    def deserialize_context_dict(cls, serialized): ...
    def serialize(self): ...
    @classmethod
    def deserialize(cls, path): ...
    @classmethod
    def per_mapper(cls, mapper): ...
    @classmethod
    def coerce(cls, raw): ...
    def token(self, token): ...
    def __add__(self, other): ...

class RootRegistry(PathRegistry):
    inherit_cache: bool
    path: Any
    natural_path: Any
    has_entity: bool
    is_aliased_class: bool
    is_root: bool
    def __getitem__(self, entity): ...

class PathToken(orm_base.InspectionAttr, HasCacheKey, str):
    @classmethod
    def intern(cls, strvalue): ...

class TokenRegistry(PathRegistry):
    inherit_cache: bool
    token: Any
    parent: Any
    path: Any
    natural_path: Any
    def __init__(self, parent, token) -> None: ...
    has_entity: bool
    is_token: bool
    def generate_for_superclasses(self) -> None: ...
    def __getitem__(self, entity) -> None: ...

class PropRegistry(PathRegistry):
    is_unnatural: bool
    inherit_cache: bool
    prop: Any
    parent: Any
    path: Any
    natural_path: Any
    def __init__(self, parent, prop) -> None: ...
    @memoized_property
    def has_entity(self): ...
    @memoized_property
    def entity(self): ...
    @property
    def mapper(self): ...
    @property
    def entity_path(self): ...
    def __getitem__(self, entity): ...

class AbstractEntityRegistry(PathRegistry):
    has_entity: bool
    key: Any
    parent: Any
    is_aliased_class: Any
    entity: Any
    path: Any
    natural_path: Any
    def __init__(self, parent, entity) -> None: ...
    @property
    def entity_path(self): ...
    @property
    def mapper(self): ...
    def __bool__(self): ...
    __nonzero__: Any
    def __getitem__(self, entity): ...

class SlotsEntityRegistry(AbstractEntityRegistry):
    inherit_cache: bool

class CachingEntityRegistry(AbstractEntityRegistry, dict):  # type: ignore[misc]
    inherit_cache: bool
    def __getitem__(self, entity): ...
    def __missing__(self, key): ...
