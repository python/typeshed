from collections.abc import Iterable
from typing import ClassVar
from typing_extensions import Self

from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q
from django.db.models.base import ModelBase
from django.utils.functional import classproperty

from .base import PolymorphicModelBase as PolymorphicModelBase
from .managers import PolymorphicManager as PolymorphicManager

class PolymorphicTypeUndefined(LookupError): ...
class PolymorphicTypeInvalid(RuntimeError): ...

class PolymorphicModel(models.Model, metaclass=PolymorphicModelBase):
    _meta_skip: ClassVar[bool] = True
    polymorphic_model_marker: ClassVar[bool] = True
    polymorphic_query_multiline_output: ClassVar[bool] = False
    polymorphic_ctype: models.ForeignKey[ContentType | None, ContentType | None]
    polymorphic_internal_model_fields: ClassVar[list[str]] = ["polymorphic_ctype"]
    objects: ClassVar[PolymorphicManager[Self]]
    @classproperty
    def polymorphic_primary_key_name(cls) -> str: ...

    class Meta:
        abstract: ClassVar[bool] = True

    @classmethod
    def translate_polymorphic_Q_object(cls, q: Q) -> Q: ...
    def pre_save_polymorphic(self, using: str = ...) -> None: ...
    def save(
        self,
        force_insert: bool | tuple[ModelBase, ...] = False,
        force_update: bool = False,
        using: str | None = None,
        update_fields: Iterable[str] | None = None,
    ) -> None: ...
    def get_real_instance_class(self) -> type[Self] | None: ...
    def get_real_concrete_instance_class_id(self) -> int | None: ...
    def get_real_concrete_instance_class(self) -> type[Self] | None: ...
    def get_real_instance(self) -> Self: ...
    def delete(self, using: str | None = None, keep_parents: bool = False) -> tuple[int, dict[str, int]]: ...
