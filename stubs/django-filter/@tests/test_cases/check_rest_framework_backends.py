from typing import Any, TypedDict
from typing_extensions import assert_type

from django.db.models import Model, QuerySet
from django.http import HttpRequest
from django_filters.rest_framework import DjangoFilterBackend


class Product(Model): ...


class Customer(Model): ...


class ProductRow(TypedDict):
    name: str


def check_filter_queryset(
    request: HttpRequest,
    view: object,
    models: QuerySet[Product],
    values: QuerySet[Product, ProductRow],
    tuples: QuerySet[Product, tuple[int, str]],
    dynamic_rows: QuerySet[Product, Any],
) -> None:
    backend = DjangoFilterBackend()
    assert_type(backend.filter_queryset(request, models, view), QuerySet[Product])
    assert_type(backend.filter_queryset(request, values, view), QuerySet[Product, ProductRow])
    assert_type(backend.filter_queryset(request, tuples, view), QuerySet[Product, tuple[int, str]])

    assert_type(backend.filter_queryset(request, dynamic_rows, view), QuerySet[Product, Any])

    filtered = backend.filter_queryset(request, values, view)
    _wrong_model: QuerySet[Customer, ProductRow] = filtered  # type: ignore[assignment]
    _wrong_row: QuerySet[Product, str] = filtered  # type: ignore[assignment]
