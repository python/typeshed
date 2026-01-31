from collections.abc import Sequence
from typing import Any, ClassVar

from django.contrib import admin
from django.db import models
from django.forms import Form, ModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

class ParentAdminNotRegistered(RuntimeError): ...

class PolymorphicChildModelAdmin(admin.ModelAdmin[Any]):
    base_model: type[models.Model] | None
    base_form: type[Form] | None
    base_fieldsets: Sequence[tuple[str | None, dict[str, Any]]] | None
    extra_fieldset_title: str
    show_in_index: bool
    change_form_template: ClassVar[list[str]]  # type: ignore[misc]
    delete_confirmation_template: ClassVar[list[str]]  # type: ignore[misc]
    object_history_template: ClassVar[list[str]]  # type: ignore[misc]
    def get_form(
        self, request: HttpRequest, obj: Any | None = None, change: bool = False, **kwargs: Any
    ) -> type[ModelForm[Any]]: ...
    def get_model_perms(self, request: HttpRequest) -> dict[str, bool]: ...
    def get_base_fieldsets(self, request: HttpRequest, obj: Any = None) -> list[tuple[str | None, dict[str, Any]]] | None: ...
    def get_fieldsets(self, request: HttpRequest, obj: Any = None) -> list[tuple[str | None, dict[str, Any]]]: ...  # type: ignore[override]
    def get_subclass_fields(self, request: HttpRequest, obj: Any = None) -> list[str]: ...
    def response_post_save_add(self, request: HttpRequest, obj: Any) -> HttpResponseRedirect: ...
    def response_post_save_change(self, request: HttpRequest, obj: Any) -> HttpResponseRedirect: ...
    def render_change_form(
        self,
        request: HttpRequest,
        context: dict[str, Any],
        add: bool = False,
        change: bool = False,
        form_url: str = "",
        obj: Any = None,
    ) -> HttpResponse: ...
    def delete_view(self, request: HttpRequest, object_id: str, context: dict[str, Any] | None = None) -> HttpResponse: ...
    def history_view(self, request: HttpRequest, object_id: str, extra_context: dict[str, Any] | None = None) -> HttpResponse: ...
