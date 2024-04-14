from typing import Any

from django.db.models import Model, QuerySet
from tablib import Dataset  # type: ignore[import-untyped]

from .fields import Field
from .resources import Resource

class BaseInstanceLoader:
    resource: Resource[Any]
    dataset: Dataset | None
    def __init__(self, resource: Resource[Any], dataset: Dataset | None = None) -> None: ...
    def get_instance(self, row: dict[str, Any]) -> Model | None: ...

class ModelInstanceLoader(BaseInstanceLoader):
    def get_queryset(self) -> QuerySet[Any]: ...

class CachedInstanceLoader(ModelInstanceLoader):
    pk_field: Field
    all_instances: dict[Any, Model]
