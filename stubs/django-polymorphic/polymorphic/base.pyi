from typing import Any

from django.db import models
from django.db.models.base import ModelBase

from .managers import PolymorphicManager as PolymorphicManager

POLYMORPHIC_SPECIAL_Q_KWORDS: set[str]

check_dump: bool

class ManagerInheritanceWarning(RuntimeWarning): ...

class PolymorphicModelBase(ModelBase):
    def __new__(cls, model_name: str, bases: tuple[type, ...], attrs: dict[str, Any], **kwargs: Any) -> type: ...
    @property
    def base_objects(self) -> models.Manager[Any]: ...
    @property
    def _base_objects(self) -> models.Manager[Any]: ...
    @property
    def _default_manager(self) -> PolymorphicManager[Any]: ...
    @property
    def _base_manager(self) -> PolymorphicManager[Any]: ...
