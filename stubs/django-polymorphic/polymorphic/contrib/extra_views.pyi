from typing import Any

from django.forms import BaseFormSet

from ..formsets import (
    BasePolymorphicInlineFormSet as BasePolymorphicInlineFormSet,
    BasePolymorphicModelFormSet as BasePolymorphicModelFormSet,
    PolymorphicFormSetChild,
)

__all__ = ["PolymorphicFormSetView", "PolymorphicInlineFormSetView", "PolymorphicInlineFormSet"]

class PolymorphicFormSetMixin:
    formset_class: type[BaseFormSet[Any]]
    factory_kwargs: dict[str, Any]
    formset_children: list[PolymorphicFormSetChild] | None
    def get_formset_children(self) -> list[PolymorphicFormSetChild]: ...
    def get_formset_child_kwargs(self) -> dict[str, Any]: ...
    def get_formset(self) -> type[BaseFormSet[Any]]: ...

class PolymorphicFormSetView(PolymorphicFormSetMixin):
    formset_class: type[BasePolymorphicModelFormSet]

class PolymorphicInlineFormSetView(PolymorphicFormSetMixin):
    formset_class: type[BasePolymorphicInlineFormSet]

class PolymorphicInlineFormSet(PolymorphicFormSetMixin):
    formset_class: type[BasePolymorphicInlineFormSet]
