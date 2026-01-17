from typing import Any

from django.contrib.admin.options import InlineModelAdmin
from django.contrib.admin.sites import AdminSite
from django.db import models
from django.forms import Media
from django.http import HttpRequest

from ..formsets import BasePolymorphicInlineFormSet, PolymorphicFormSetChild

class PolymorphicInlineModelAdmin(InlineModelAdmin[Any, Any]):
    formset: type[BasePolymorphicInlineFormSet]  # type: ignore[assignment]
    polymorphic_media: Media
    extra: int
    child_inlines: tuple[type[PolymorphicInlineModelAdmin.Child], ...]
    child_inline_instances: list[PolymorphicInlineModelAdmin.Child]
    def __init__(self, parent_model: type[models.Model], admin_site: AdminSite) -> None: ...
    def get_child_inlines(self) -> list[type[PolymorphicInlineModelAdmin.Child]]: ...
    def get_child_inline_instances(self) -> list[PolymorphicInlineModelAdmin.Child]: ...
    def get_child_inline_instance(self, model: type[models.Model]) -> PolymorphicInlineModelAdmin.Child: ...
    def get_formset_children(self, request: HttpRequest, obj: Any = None) -> list[PolymorphicFormSetChild]: ...
    def get_formset(self, request: HttpRequest, obj: Any = None, **kwargs: Any) -> type[BasePolymorphicInlineFormSet]: ...  # type: ignore[override]
    def get_fieldsets(self, request: HttpRequest, obj: Any = None) -> list[tuple[str | None, dict[str, Any]]]: ...  # type: ignore[override]
    def get_fields(self, request: HttpRequest, obj: Any = None) -> list[str]: ...  # type: ignore[override]

    class Child(InlineModelAdmin[Any, Any]):
        formset_child: type[PolymorphicFormSetChild]
        extra: int
        parent_inline: PolymorphicInlineModelAdmin
        def __init__(self, parent_inline: PolymorphicInlineModelAdmin) -> None: ...
        def get_formset(self, request: HttpRequest, obj: Any = None, **kwargs: Any) -> None: ...  # type: ignore[override]
        def get_fields(self, request: HttpRequest, obj: Any = None) -> list[str]: ...  # type: ignore[override]
        def get_formset_child(self, request: HttpRequest, obj: Any = None, **kwargs: Any) -> PolymorphicFormSetChild: ...

class StackedPolymorphicInline(PolymorphicInlineModelAdmin):
    template: str
