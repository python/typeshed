from typing import Any, Optional

from google.cloud.ndb import model

class _BaseMetadata(model.Model):
    KIND_NAME: str = ...
    def __new__(cls, *args: Any, **kwargs: Any): ...

class Namespace(_BaseMetadata):
    KIND_NAME: str = ...
    EMPTY_NAMESPACE_ID: int = ...
    @property
    def namespace_name(self): ...
    @classmethod
    def key_for_namespace(cls, namespace: Any): ...
    @classmethod
    def key_to_namespace(cls, key: Any): ...

class Kind(_BaseMetadata):
    KIND_NAME: str = ...
    @property
    def kind_name(self): ...
    @classmethod
    def key_for_kind(cls, kind: Any): ...
    @classmethod
    def key_to_kind(cls, key: Any): ...

class Property(_BaseMetadata):
    KIND_NAME: str = ...
    @property
    def property_name(self): ...
    @property
    def kind_name(self): ...
    property_representation: Any = ...
    @classmethod
    def key_for_kind(cls, kind: Any): ...
    @classmethod
    def key_for_property(cls, kind: Any, property: Any): ...
    @classmethod
    def key_to_kind(cls, key: Any): ...
    @classmethod
    def key_to_property(cls, key: Any): ...

class EntityGroup:
    def __new__(cls, *args: Any, **kwargs: Any): ...

def get_entity_group_version(*args: Any, **kwargs: Any) -> None: ...
def get_kinds(start: Optional[Any] = ..., end: Optional[Any] = ...): ...
def get_namespaces(start: Optional[Any] = ..., end: Optional[Any] = ...): ...
def get_properties_of_kind(kind: Any, start: Optional[Any] = ..., end: Optional[Any] = ...): ...
def get_representations_of_kind(kind: Any, start: Optional[Any] = ..., end: Optional[Any] = ...): ...
