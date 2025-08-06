from typing import Any

from django.db.models import QuerySet
from django.http import HttpRequest
from django_filters.filterset import FilterSetMetaclass
from rest_framework.views import APIView

from . import filterset

class DjangoFilterBackend:
    filterset_base: FilterSetMetaclass = ...
    raise_exception: bool
    @property
    def template(self) -> str: ...

    # Works with any model type
    def get_filterset(self, request: HttpRequest, queryset: QuerySet[Any], view: APIView) -> filterset.FilterSet | None: ...

    # Any model queryset
    def get_filterset_class(self, view: APIView, queryset: QuerySet[Any] | None = None) -> type[filterset.FilterSet] | None: ...

    # Kwargs vary by filterset
    def get_filterset_kwargs(self, request: HttpRequest, queryset: QuerySet[Any], view: APIView) -> dict[str, Any]: ...

    # Filters any model type
    def filter_queryset(self, request: HttpRequest, queryset: QuerySet[Any], view: APIView) -> QuerySet[Any]: ...
    def to_html(self, request: HttpRequest, queryset: QuerySet[Any], view: APIView) -> str: ...  # Renders form for any model
