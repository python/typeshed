from _typeshed import Incomplete, SupportsGetItem
from logging import Logger
from typing import Any, Generic, TypeVar
from typing_extensions import TypeAlias, deprecated

from django.db.models import Model, QuerySet
from django.forms import BaseForm, Form
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.views.generic.edit import FormView

from .formats.base_formats import Format
from .resources import Resource

Dataset: TypeAlias = Incomplete  # tablib.Dataset

logger: Logger

_ModelT = TypeVar("_ModelT", bound=Model)

class BaseImportExportMixin(Generic[_ModelT]):
    resource_classes: SupportsGetItem[int, type[Resource[_ModelT]]]
    @property
    def formats(self) -> list[type[Format]]: ...
    @property
    def export_formats(self) -> list[type[Format]]: ...
    @property
    def import_formats(self) -> list[type[Format]]: ...
    def check_resource_classes(self, resource_classes: SupportsGetItem[int, type[Resource[_ModelT]]]) -> None: ...
    def get_resource_classes(self, request: HttpRequest) -> list[type[Resource[_ModelT]]]: ...
    def get_resource_kwargs(self, request: HttpRequest, *args: Any, **kwargs: Any) -> dict[str, Any]: ...
    def get_resource_index(self, form: Form) -> int: ...

class BaseImportMixin(BaseImportExportMixin[_ModelT]):
    skip_import_confirm: bool
    def get_import_resource_classes(self, request: HttpRequest) -> list[type[Resource[_ModelT]]]: ...
    def get_import_formats(self) -> list[Format]: ...
    def get_import_resource_kwargs(self, request: HttpRequest, **kwargs: Any) -> dict[str, Any]: ...
    def choose_import_resource_class(self, form: Form, request: HttpRequest) -> type[Resource[_ModelT]]: ...
    def is_skip_import_confirm_enabled(self) -> bool: ...

class BaseExportMixin(BaseImportExportMixin[_ModelT]):
    model: Model
    skip_export_form: bool
    skip_export_form_from_action: bool
    def get_export_formats(self) -> list[Format]: ...
    def get_export_resource_classes(self, request: HttpRequest) -> list[Resource[_ModelT]]: ...
    def choose_export_resource_class(self, form: Form, request: HttpRequest) -> Resource[_ModelT]: ...
    def get_export_resource_kwargs(self, request: HttpRequest, **kwargs: Any) -> dict[str, Any]: ...
    def get_data_for_export(self, request: HttpRequest, queryset: QuerySet[_ModelT], **kwargs: Any) -> Dataset: ...
    def get_export_filename(self, file_format: Format) -> str: ...
    def is_skip_export_form_enabled(self) -> bool: ...
    def is_skip_export_form_from_action_enabled(self) -> bool: ...

class ExportViewMixin(BaseExportMixin[_ModelT]):
    form_class: type[BaseForm] = ...
    def get_export_data(self, file_format: Format, queryset: QuerySet[_ModelT], **kwargs: Any) -> str | bytes: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
    def get_form_kwargs(self) -> dict[str, Any]: ...

_FormT = TypeVar("_FormT", bound=BaseForm)

@deprecated("ExportViewFormMixin is deprecated and will be removed in a future release.")
class ExportViewFormMixin(ExportViewMixin[_ModelT], FormView[_FormT]):  # type: ignore[misc]
    def form_valid(self, form: _FormT) -> HttpResponse: ...
