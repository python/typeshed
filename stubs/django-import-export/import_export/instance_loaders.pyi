from collections.abc import Mapping
from typing import Any

from django.db.models import Model, QuerySet
from tablib import Dataset

from .fields import Field
from .resources import Resource

class BaseInstanceLoader:
    resource: Resource
    dataset: Dataset | None
    def __init__(self, resource: Resource, dataset: Dataset | None = None) -> None: ...
    def get_instance(self, row: Mapping[str, Any]) -> Model | None: ...

class ModelInstanceLoader(BaseInstanceLoader):
    def get_queryset(self) -> QuerySet: ...

class CachedInstanceLoader(ModelInstanceLoader):
    pk_field: Field
    all_instances: dict[Any, Model]
