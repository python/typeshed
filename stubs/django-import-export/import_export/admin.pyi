from _typeshed import Incomplete
from collections.abc import Callable, Sequence
from logging import Logger
from typing import Any, Literal, TypeVar
from typing_extensions import TypeAlias

from django.contrib import admin
from django.contrib.admin.helpers import ActionForm
from django.core.files import File
from django.db.models import Model, QuerySet
from django.forms import Form
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.template.response import TemplateResponse
from django.urls import URLPattern

from .formats.base_formats import Format
from .mixins import BaseExportMixin, BaseImportMixin
from .results import Result
from .tmp_storages import BaseStorage

Dataset: TypeAlias = Incomplete  # tablib.Dataset
logger: Logger

_ModelT = TypeVar("_ModelT", bound=Model)

class ImportExportMixinBase:
    base_change_list_template: str
    change_list_template: str
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def init_change_list_template(self) -> None: ...
    def get_model_info(self) -> tuple[str, str]: ...
    def changelist_view(self, request: HttpRequest, extra_context: dict[str, Any] | None = None) -> HttpResponse: ...

class ImportMixin(BaseImportMixin[_ModelT], ImportExportMixinBase):
    import_export_change_list_template: str
    import_template_name: str
    import_form_class: type[Form] = ...
    confirm_form_class: type[Form] = ...
    from_encoding: str
    import_error_display: Sequence[Literal["message", "row", "traceback"]]
    skip_admin_log: bool | None
    tmp_storage_class: str | type[BaseStorage]
    def get_skip_admin_log(self) -> bool: ...
    def get_tmp_storage_class(self) -> type[BaseStorage]: ...
    def get_tmp_storage_class_kwargs(self) -> dict[str, Any]: ...
    def has_import_permission(self, request: HttpRequest) -> bool: ...
    def get_urls(self) -> list[URLPattern]: ...
    def process_import(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def process_dataset(
        self, dataset: Dataset, confirm_form: Form, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> Result: ...
    def process_result(self, result: Result, request: HttpRequest) -> HttpResponse: ...
    def generate_log_entries(self, result: Result, request: HttpRequest) -> None: ...
    def add_success_message(self, result: Result, request: HttpRequest) -> None: ...
    def get_import_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
    def create_import_form(self, request: HttpRequest) -> Form: ...
    def get_import_form_class(self, request: HttpRequest) -> type[Form]: ...
    def get_import_form_kwargs(self, request: HttpRequest) -> dict[str, Any]: ...
    def get_import_form_initial(self, request: HttpRequest) -> dict[str, Any]: ...
    def create_confirm_form(self, request: HttpRequest, import_form: Form | None = None) -> Form: ...
    def get_confirm_form_class(self, request: HttpRequest) -> type[Form]: ...
    def get_confirm_form_kwargs(self, request: HttpRequest, import_form: Form | None = None) -> dict[str, Any]: ...
    def get_confirm_form_initial(self, request: HttpRequest, import_form: Form | None) -> dict[str, Any]: ...
    def get_import_data_kwargs(self, request: HttpRequest, *args: Any, **kwargs: Any) -> dict[str, Any]: ...
    def write_to_tmp_storage(self, import_file: File[bytes], input_format: Format) -> BaseStorage: ...
    def add_data_read_fail_error_to_form(self, form: Form, e: Exception) -> None: ...
    def import_action(self, request: HttpRequest, *args: Any, **kwargs: Any) -> TemplateResponse: ...
    def changelist_view(self, request: HttpRequest, extra_context: dict[str, Any] | None = None) -> HttpResponse: ...

class ExportMixin(BaseExportMixin[_ModelT], ImportExportMixinBase):
    import_export_change_list_template: str
    export_template_name: str
    to_encoding: str | None
    export_form_class: type[Form] = ...
    def get_urls(self) -> list[URLPattern]: ...
    def has_export_permission(self, request: HttpRequest) -> bool: ...
    def get_export_queryset(self, request: HttpRequest) -> QuerySet[_ModelT]: ...
    def get_export_data(self, file_format: Format, queryset: QuerySet[_ModelT], *args: Any, **kwargs: Any) -> str | bytes: ...
    def get_export_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
    def get_export_form_class(self) -> type[Form]: ...
    def export_action(self, request: HttpRequest) -> TemplateResponse: ...
    def changelist_view(self, request: HttpRequest, extra_context: dict[str, Any] | None = None) -> HttpResponse: ...
    def get_export_filename(self, request: HttpRequest, queryset: QuerySet[_ModelT], file_format: Format) -> str: ...  # type: ignore[override]
    def init_request_context_data(self, request: HttpRequest, form: Form) -> dict[str, Any]: ...

class ImportExportMixin(ImportMixin[_ModelT], ExportMixin[_ModelT]): ...
class ImportExportModelAdmin(ImportExportMixin[_ModelT], admin.ModelAdmin[_ModelT]): ...  # type: ignore[misc]

class ExportActionMixin(ExportMixin[_ModelT]):
    change_form_template: str
    show_change_form_export: bool
    action_form: type[ActionForm]
    def change_view(
        self, request: HttpRequest, object_id: str, form_url: str = "", extra_context: dict[str, Any] | None = None
    ) -> HttpResponse: ...
    def response_change(self, request: HttpRequest, obj: _ModelT) -> HttpResponse: ...
    def export_admin_action(self, request: HttpRequest, queryset: QuerySet[_ModelT]) -> HttpResponse: ...
    def get_actions(self, request: HttpRequest) -> dict[str, tuple[Callable[..., str], str, str] | None]: ...

class ExportActionModelAdmin(ExportActionMixin[_ModelT], admin.ModelAdmin[_ModelT]): ...  # type: ignore[misc]
class ImportExportActionModelAdmin(ImportMixin[_ModelT], ExportActionModelAdmin[_ModelT]): ...  # type: ignore[misc]
