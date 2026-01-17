from collections.abc import Iterable
from typing import Any

from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.db.models import QuerySet
from django.http import HttpRequest

class PolymorphicChildModelFilter(SimpleListFilter):
    title: str
    parameter_name: str
    def lookups(self, request: HttpRequest, model_admin: ModelAdmin[Any]) -> Iterable[tuple[str, str]]: ...
    def queryset(self, request: HttpRequest, queryset: QuerySet[Any]) -> QuerySet[Any]: ...
