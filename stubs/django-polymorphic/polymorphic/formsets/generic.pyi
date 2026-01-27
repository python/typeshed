from collections.abc import Callable, Iterable
from typing import Any

from django.contrib.contenttypes.forms import BaseGenericInlineFormSet
from django.db import models
from django.forms import ModelForm

from .models import BasePolymorphicModelFormSet, PolymorphicFormSetChild

class GenericPolymorphicFormSetChild(PolymorphicFormSetChild):
    ct_field: str
    fk_field: str
    def __init__(self, *args: Any, ct_field: str = "content_type", fk_field: str = "object_id", **kwargs: Any) -> None: ...
    def get_form(self, ct_field: str = "content_type", fk_field: str = "object_id", **kwargs: Any) -> type[ModelForm[Any]]: ...

class BaseGenericPolymorphicInlineFormSet(BaseGenericInlineFormSet[Any, Any], BasePolymorphicModelFormSet): ...

def generic_polymorphic_inlineformset_factory(
    model: type[models.Model],
    formset_children: Iterable[PolymorphicFormSetChild],
    form: type[ModelForm[Any]] = ...,
    formset: type[BaseGenericPolymorphicInlineFormSet] = ...,
    ct_field: str = "content_type",
    fk_field: str = "object_id",
    fields: list[str] | None = None,
    exclude: list[str] | None = None,
    extra: int = 1,
    can_order: bool = False,
    can_delete: bool = True,
    max_num: int | None = None,
    formfield_callback: Callable[..., Any] | None = None,
    validate_max: bool = False,
    for_concrete_model: bool = True,
    min_num: int | None = None,
    validate_min: bool = False,
    child_form_kwargs: dict[str, Any] | None = None,
) -> type[BaseGenericPolymorphicInlineFormSet]: ...
