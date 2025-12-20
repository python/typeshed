from typing import Any

from django.db import models

from .base import PolymorphicModelBase as PolymorphicModelBase
from .models import PolymorphicModel as PolymorphicModel

def reset_polymorphic_ctype(*models: type[PolymorphicModel], **filters: Any) -> None: ...
def sort_by_subclass(*classes: type[models.Model]) -> list[type[models.Model]]: ...
def get_base_polymorphic_model(
    ChildModel: type[PolymorphicModel], allow_abstract: bool = False
) -> type[PolymorphicModel] | None: ...
