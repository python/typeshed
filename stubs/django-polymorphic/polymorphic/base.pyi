from typing import Any

from django.db import models
from django.db.models.base import ModelBase

from .managers import PolymorphicManager as PolymorphicManager
from .query import PolymorphicQuerySet as PolymorphicQuerySet

POLYMORPHIC_SPECIAL_Q_KWORDS: set[str]
DUMPDATA_COMMAND: str

class ManagerInheritanceWarning(RuntimeWarning): ...

class PolymorphicModelBase(ModelBase):
    def __new__(cls, model_name: str, bases: tuple[type, ...], attrs: dict[str, Any], **kwargs: Any) -> type: ...
    @classmethod
    def validate_model_manager(cls, manager: models.Manager[Any], model_name: str, manager_name: str) -> models.Manager[Any]: ...
    @property
    def base_objects(self) -> models.Manager[Any]: ...
    @property
    def _base_objects(self) -> models.Manager[Any]: ...
    @property
    def _default_manager(self) -> PolymorphicManager[Any]: ...
