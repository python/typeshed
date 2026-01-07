from typing import Any

from django.contrib.contenttypes.admin import GenericInlineModelAdmin
from django.http import HttpRequest

from ..formsets import BaseGenericPolymorphicInlineFormSet
from .inlines import PolymorphicInlineModelAdmin

class GenericPolymorphicInlineModelAdmin(PolymorphicInlineModelAdmin, GenericInlineModelAdmin):
    formset: type[BaseGenericPolymorphicInlineFormSet]  # type: ignore[assignment]
    def get_formset(self, request: HttpRequest, obj: Any = None, **kwargs: Any) -> type[BaseGenericPolymorphicInlineFormSet]: ...  # type: ignore[override]

class GenericStackedPolymorphicInline(GenericPolymorphicInlineModelAdmin):
    template: str
