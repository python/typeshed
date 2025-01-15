from _typeshed import Incomplete
from collections import OrderedDict
from collections.abc import Iterator, Sequence
from functools import partial
from logging import Logger
from typing import Any, ClassVar, Generic, Literal, NoReturn, TypeVar, overload
from typing_extensions import TypeAlias, deprecated

import _typeshed

from django.db.models import Field as DjangoField, ForeignObjectRel, Model, QuerySet
from django.utils.safestring import SafeString

from .fields import Field
from .instance_loaders import BaseInstanceLoader
from .results import Error, Result, RowResult
from .widgets import ForeignKeyWidget, ManyToManyWidget, Widget

Dataset: TypeAlias = Incomplete  # tablib.Dataset
logger: Logger

@overload
def get_related_model(field: ForeignObjectRel) -> Model: ...
@overload
def get_related_model(field: DjangoField[Any, Any]) -> Model | None: ...
def has_natural_foreign_key(model: Model) -> bool: ...

class ResourceOptions(Generic[_ModelT]):
    model: _ModelT
    fields: Sequence[str] | None
    exclude: Sequence[str] | None
    instance_loader_class: type[BaseInstanceLoader] | None
    import_id_fields: Sequence[str]
    export_order: Sequence[str] | None
    widgets: dict[str, Any] | None
    use_transactions: bool | None
    skip_unchanged: bool
    report_skipped: bool
    clean_model_instances: bool
    chunk_size: int | None
    skip_diff: bool
    skip_html_diff: bool
    use_bulk: bool
    batch_size: int
    force_init_instance: bool
    using_db: str | None
    store_row_values: bool
    store_instance: bool
    use_natural_foreign_keys: bool

class DeclarativeMetaclass(type):
    def __new__(cls: type[_typeshed.Self], name: str, bases: tuple[type[Any], ...], attrs: dict[str, Any]) -> _typeshed.Self: ...

class Diff:
    left: list[str]
    right: list[str]
    new: bool
    def __init__(self, resource: Resource[_ModelT], instance: _ModelT, new: bool) -> None: ...
    def compare_with(self, resource: Resource[_ModelT], instance: _ModelT, dry_run: bool = False) -> None: ...
    def as_html(self) -> list[SafeString]: ...

_ModelT = TypeVar("_ModelT", bound=Model)

class Resource(Generic[_ModelT], metaclass=DeclarativeMetaclass):
    _meta: ResourceOptions[_ModelT]
    fields: OrderedDict[str, Field]
    create_instances: list[_ModelT]
    update_instances: list[_ModelT]
    delete_instances: list[_ModelT]
    def __init__(self, **kwargs: Any) -> None: ...
    @classmethod
    def get_result_class(self) -> type[Result]: ...
    @classmethod
    def get_row_result_class(self) -> type[RowResult]: ...
    @classmethod
    def get_error_result_class(self) -> type[Error]: ...
    @classmethod
    def get_diff_class(self) -> type[Diff]: ...
    @classmethod
    def get_db_connection_name(self) -> str: ...
    def get_use_transactions(self) -> bool: ...
    def get_chunk_size(self) -> int: ...
    def get_fields(self, **kwargs: Any) -> list[Field]: ...
    def get_field_name(self, field: Field) -> str: ...
    def init_instance(self, row: dict[str, Any] | None = None) -> _ModelT: ...
    def get_instance(self, instance_loader: BaseInstanceLoader, row: dict[str, Any]) -> _ModelT | None: ...
    def get_or_init_instance(self, instance_loader: BaseInstanceLoader, row: dict[str, Any]) -> tuple[_ModelT | None, bool]: ...
    def get_import_id_fields(self) -> Sequence[str]: ...
    def get_bulk_update_fields(self) -> list[str]: ...
    def bulk_create(
        self,
        using_transactions: bool,
        dry_run: bool,
        raise_errors: bool,
        batch_size: int | None = None,
        result: Result | None = None,
    ) -> None: ...
    def bulk_update(
        self,
        using_transactions: bool,
        dry_run: bool,
        raise_errors: bool,
        batch_size: int | None = None,
        result: Result | None = None,
    ) -> None: ...
    def bulk_delete(self, using_transactions: bool, dry_run: bool, raise_errors: bool, result: Result | None = None) -> None: ...
    def validate_instance(
        self, instance: _ModelT, import_validation_errors: dict[str, Any] | None = None, validate_unique: bool = True
    ) -> None: ...
    def save_instance(
        self, instance: _ModelT, is_create: bool, using_transactions: bool = True, dry_run: bool = False
    ) -> None: ...
    def before_save_instance(self, instance: _ModelT, using_transactions: bool, dry_run: bool) -> None: ...
    def after_save_instance(self, instance: _ModelT, using_transactions: bool, dry_run: bool) -> None: ...
    def delete_instance(self, instance: _ModelT, using_transactions: bool = True, dry_run: bool = False) -> None: ...
    def before_delete_instance(self, instance: _ModelT, dry_run: bool) -> None: ...
    def after_delete_instance(self, instance: _ModelT, dry_run: bool) -> None: ...
    def import_field(self, field: Field, obj: _ModelT, data: dict[str, Any], is_m2m: bool = False, **kwargs: Any) -> None: ...
    def get_import_fields(self) -> list[Field]: ...
    def import_obj(self, obj: _ModelT, data: dict[str, Any], dry_run: bool, **kwargs: Any) -> None: ...
    def save_m2m(self, obj: _ModelT, data: dict[str, Any], using_transactions: bool, dry_run: bool) -> None: ...
    def for_delete(self, row: dict[str, Any], instance: _ModelT) -> bool: ...
    def skip_row(
        self, instance: _ModelT, original: _ModelT, row: dict[str, Any], import_validation_errors: dict[str, Any] | None = None
    ) -> bool: ...
    def get_diff_headers(self) -> list[str]: ...
    def before_import(self, dataset: Dataset, using_transactions: bool, dry_run: bool, **kwargs: Any) -> None: ...
    def after_import(self, dataset: Dataset, result: Result, using_transactions: bool, dry_run: bool, **kwargs: Any) -> None: ...
    def before_import_row(self, row: dict[str, Any], row_number: int | None = None, **kwargs: Any) -> None: ...
    def after_import_row(
        self, row: dict[str, Any], row_result: RowResult, row_number: int | None = None, **kwargs: Any
    ) -> None: ...
    def after_import_instance(self, instance: _ModelT, new: bool, row_number: int | None = None, **kwargs: Any) -> None: ...
    @overload
    def handle_import_error(self, result: Result, error: Exception, raise_errors: Literal[True]) -> NoReturn: ...
    @overload
    def handle_import_error(self, result: Result, error: Exception, raise_errors: Literal[False] = ...) -> None: ...
    @overload
    @deprecated("raise_errors argument is deprecated and will be removed in a future release.")
    def import_row(
        self,
        row: dict[str, Any],
        instance_loader: BaseInstanceLoader,
        using_transactions: bool = True,
        dry_run: bool = False,
        *,
        raise_errors: bool,
        **kwargs: Any,
    ) -> RowResult: ...
    @overload
    def import_row(
        self,
        row: dict[str, Any],
        instance_loader: BaseInstanceLoader,
        using_transactions: bool = True,
        dry_run: bool = False,
        raise_errors: None = None,
        **kwargs: Any,
    ) -> RowResult: ...
    def import_data(
        self,
        dataset: Dataset,
        dry_run: bool = False,
        raise_errors: bool = False,
        use_transactions: bool | None = None,
        collect_failed_rows: bool = False,
        rollback_on_validation_errors: bool = False,
        **kwargs: Any,
    ) -> Result: ...
    @overload
    @deprecated("rollback_on_validation_errors argument is deprecated and will be removed in a future release.")
    def import_data_inner(
        self,
        dataset: Dataset,
        dry_run: bool,
        raise_errors: bool,
        using_transactions: bool,
        collect_failed_rows: bool,
        rollback_on_validation_errors: bool,
        **kwargs: Any,
    ) -> Result: ...
    @overload
    def import_data_inner(
        self,
        dataset: Dataset,
        dry_run: bool,
        raise_errors: bool,
        using_transactions: bool,
        collect_failed_rows: bool,
        rollback_on_validation_errors: None = None,
        **kwargs: Any,
    ) -> Result: ...
    def get_export_order(self) -> tuple[str, ...]: ...
    def before_export(self, queryset: QuerySet[_ModelT], *args: Any, **kwargs: Any) -> None: ...
    def after_export(self, queryset: QuerySet[_ModelT], data: Dataset, *args: Any, **kwargs: Any) -> None: ...
    def filter_export(self, queryset: QuerySet[_ModelT], *args: Any, **kwargs: Any) -> QuerySet[_ModelT]: ...
    def export_field(self, field: Field, obj: _ModelT) -> str: ...
    def get_export_fields(self) -> list[Field]: ...
    def export_resource(self, obj: _ModelT) -> list[str]: ...
    def get_export_headers(self) -> list[str]: ...
    def get_user_visible_headers(self) -> list[str]: ...
    def get_user_visible_fields(self) -> list[str]: ...
    def iter_queryset(self, queryset: QuerySet[_ModelT]) -> Iterator[_ModelT]: ...
    def export(self, *args: Any, queryset: QuerySet[_ModelT] | None = None, **kwargs: Any) -> Dataset: ...

class ModelDeclarativeMetaclass(DeclarativeMetaclass):
    def __new__(cls: type[_typeshed.Self], name: str, bases: tuple[type[Any], ...], attrs: dict[str, Any]) -> _typeshed.Self: ...

class ModelResource(Resource[_ModelT], metaclass=ModelDeclarativeMetaclass):
    DEFAULT_RESOURCE_FIELD: ClassVar[type[Field]] = ...
    WIDGETS_MAP: ClassVar[dict[str, type[Widget]]]
    @classmethod
    def get_m2m_widget(cls, field: DjangoField[Any, Any]) -> partial[ManyToManyWidget[Any]]: ...
    @classmethod
    def get_fk_widget(cls, field: DjangoField[Any, Any]) -> partial[ForeignKeyWidget[Any]]: ...
    @classmethod
    def widget_from_django_field(cls, f: DjangoField[Any, Any], default: type[Widget] = ...) -> type[Widget]: ...
    @classmethod
    def widget_kwargs_for_field(self, field_name: str) -> dict[str, Any]: ...
    @classmethod
    def field_from_django_field(cls, field_name: str, django_field: DjangoField[Any, Any], readonly: bool) -> Field: ...
    def get_queryset(self) -> QuerySet[_ModelT]: ...
    def init_instance(self, row: dict[str, Any] | None = None) -> _ModelT: ...
    def after_import(self, dataset: Dataset, result: Result, using_transactions: bool, dry_run: bool, **kwargs: Any) -> None: ...
    @classmethod
    def get_display_name(cls) -> str: ...

_ResourceT = TypeVar("_ResourceT", bound=Resource[Any])

# HK Type Vars could help type the first overload:
@overload
def modelresource_factory(model: Model, resource_class: type[_ResourceT]) -> _ResourceT: ...
@overload
def modelresource_factory(model: _ModelT) -> ModelResource[_ModelT]: ...
