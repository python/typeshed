from collections.abc import Callable, Iterable
from typing import Any

from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.forms import BaseForm, BaseInlineFormSet, BaseModelFormSet, Media, ModelForm

class UnsupportedChildType(LookupError): ...

class PolymorphicFormSetChild:
    model: type[models.Model]
    fields: list[str] | None
    exclude: tuple[str, ...] | list[str]
    formfield_callback: Callable[..., Any] | None
    widgets: dict[str, Any] | None
    localized_fields: list[str] | None
    labels: dict[str, str] | None
    help_texts: dict[str, str] | None
    error_messages: dict[str, dict[str, str]] | None
    def __init__(
        self,
        model: type[models.Model],
        form: type[ModelForm[Any]] = ...,
        fields: list[str] | None = None,
        exclude: tuple[str, ...] | list[str] | None = None,
        formfield_callback: Callable[..., Any] | None = None,
        widgets: dict[str, Any] | None = None,
        localized_fields: list[str] | None = None,
        labels: dict[str, str] | None = None,
        help_texts: dict[str, str] | None = None,
        error_messages: dict[str, dict[str, str]] | None = None,
    ) -> None: ...
    @property
    def content_type(self) -> ContentType: ...
    def get_form(self, **kwargs: Any) -> type[ModelForm[Any]]: ...

def polymorphic_child_forms_factory(
    formset_children: Iterable[PolymorphicFormSetChild], **kwargs: Any
) -> dict[type[models.Model], type[ModelForm[Any]]]: ...

class BasePolymorphicModelFormSet(BaseModelFormSet[Any, Any]):
    child_forms: dict[type[models.Model], type[ModelForm[Any]]]
    queryset_data: Any
    @property
    def media(self) -> Media: ...
    @property
    def empty_forms(self) -> list[BaseForm]: ...
    @property
    def empty_form(self) -> BaseForm: ...
    def get_form_class(self, model: type[models.Model]) -> type[ModelForm[Any]]: ...
    def is_multipart(self) -> bool: ...

class BasePolymorphicInlineFormSet(BaseInlineFormSet[Any, Any, Any], BasePolymorphicModelFormSet): ...

def polymorphic_modelformset_factory(
    model: type[models.Model],
    formset_children: Iterable[PolymorphicFormSetChild],
    formset: type[BasePolymorphicModelFormSet] = ...,
    form: type[ModelForm[Any]] = ...,
    fields: list[str] | None = None,
    exclude: list[str] | None = None,
    extra: int = 1,
    can_order: bool = False,
    can_delete: bool = True,
    max_num: int | None = None,
    formfield_callback: Callable[..., Any] | None = None,
    widgets: dict[str, Any] | None = None,
    validate_max: bool = False,
    localized_fields: list[str] | None = None,
    labels: dict[str, str] | None = None,
    help_texts: dict[str, str] | None = None,
    error_messages: dict[str, dict[str, str]] | None = None,
    min_num: int | None = None,
    validate_min: bool = False,
    field_classes: dict[str, type[Any]] | None = None,
    child_form_kwargs: dict[str, Any] | None = None,
) -> type[BasePolymorphicModelFormSet]: ...
def polymorphic_inlineformset_factory(
    parent_model: type[models.Model],
    model: type[models.Model],
    formset_children: Iterable[PolymorphicFormSetChild],
    formset: type[BasePolymorphicInlineFormSet] = ...,
    fk_name: str | None = None,
    form: type[ModelForm[Any]] = ...,
    fields: list[str] | None = None,
    exclude: list[str] | None = None,
    extra: int = 1,
    can_order: bool = False,
    can_delete: bool = True,
    max_num: int | None = None,
    formfield_callback: Callable[..., Any] | None = None,
    widgets: dict[str, Any] | None = None,
    validate_max: bool = False,
    localized_fields: list[str] | None = None,
    labels: dict[str, str] | None = None,
    help_texts: dict[str, str] | None = None,
    error_messages: dict[str, dict[str, str]] | None = None,
    min_num: int | None = None,
    validate_min: bool = False,
    field_classes: dict[str, type[Any]] | None = None,
    child_form_kwargs: dict[str, Any] | None = None,
) -> type[BasePolymorphicInlineFormSet]: ...
