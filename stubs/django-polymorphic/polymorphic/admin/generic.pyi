from typing import Any

from django.contrib.contenttypes.admin import GenericInlineModelAdmin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpRequest

from ..formsets import BaseGenericPolymorphicInlineFormSet, GenericPolymorphicFormSetChild
from .inlines import PolymorphicInlineModelAdmin

class GenericPolymorphicInlineModelAdmin(PolymorphicInlineModelAdmin, GenericInlineModelAdmin):
    formset: type[BaseGenericPolymorphicInlineFormSet]  # type: ignore[assignment]
    def get_formset(self, request: HttpRequest, obj: Any = None, **kwargs: Any) -> type[BaseGenericPolymorphicInlineFormSet]: ...  # type: ignore[override]

    class Child(PolymorphicInlineModelAdmin.Child):
        formset_child: type[GenericPolymorphicFormSetChild]  # type: ignore[assignment]
        ct_field: str
        ct_fk_field: str
        @property
        def content_type(self) -> ContentType: ...
        def get_formset_child(
            self, request: HttpRequest, obj: Any = None, **kwargs: Any
        ) -> GenericPolymorphicFormSetChild: ...  # type: ignore[override]

class GenericStackedPolymorphicInline(GenericPolymorphicInlineModelAdmin):
    template: str
