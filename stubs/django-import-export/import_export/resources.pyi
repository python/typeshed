from _typeshed import Incomplete
from collections.abc import Generator

from .fields import Field

logger: Incomplete

def get_related_model(field): ...
def has_natural_foreign_key(model): ...

class ResourceOptions:
    model: Incomplete
    fields: Incomplete
    exclude: Incomplete
    instance_loader_class: Incomplete
    import_id_fields: Incomplete
    export_order: Incomplete
    widgets: Incomplete
    use_transactions: Incomplete
    skip_unchanged: bool
    report_skipped: bool
    clean_model_instances: bool
    chunk_size: Incomplete
    skip_diff: bool
    skip_html_diff: bool
    use_bulk: bool
    batch_size: int
    force_init_instance: bool
    using_db: Incomplete
    store_row_values: bool
    store_instance: bool
    use_natural_foreign_keys: bool

class DeclarativeMetaclass(type):
    def __new__(cls, name, bases, attrs): ...

class Diff:
    left: Incomplete
    right: Incomplete
    new: Incomplete
    def __init__(self, resource, instance, new) -> None: ...
    def compare_with(self, resource, instance, dry_run: bool = False) -> None: ...
    def as_html(self): ...

class Resource(metaclass=DeclarativeMetaclass):
    fields: Incomplete
    create_instances: Incomplete
    update_instances: Incomplete
    delete_instances: Incomplete
    def __init__(self, **kwargs) -> None: ...
    @classmethod
    def get_result_class(self): ...
    @classmethod
    def get_row_result_class(self): ...
    @classmethod
    def get_error_result_class(self): ...
    @classmethod
    def get_diff_class(self): ...
    @classmethod
    def get_db_connection_name(self): ...
    def get_use_transactions(self): ...
    def get_chunk_size(self): ...
    def get_fields(self, **kwargs): ...
    def get_field_name(self, field): ...
    def init_instance(self, row: Incomplete | None = None) -> None: ...
    def get_instance(self, instance_loader, row): ...
    def get_or_init_instance(self, instance_loader, row): ...
    def get_import_id_fields(self): ...
    def get_bulk_update_fields(self): ...
    def bulk_create(
        self, using_transactions, dry_run, raise_errors, batch_size: Incomplete | None = None, result: Incomplete | None = None
    ) -> None: ...
    def bulk_update(
        self, using_transactions, dry_run, raise_errors, batch_size: Incomplete | None = None, result: Incomplete | None = None
    ) -> None: ...
    def bulk_delete(self, using_transactions, dry_run, raise_errors, result: Incomplete | None = None) -> None: ...
    def validate_instance(
        self, instance, import_validation_errors: Incomplete | None = None, validate_unique: bool = True
    ) -> None: ...
    def save_instance(self, instance, is_create, using_transactions: bool = True, dry_run: bool = False) -> None: ...
    def before_save_instance(self, instance, using_transactions, dry_run) -> None: ...
    def after_save_instance(self, instance, using_transactions, dry_run) -> None: ...
    def delete_instance(self, instance, using_transactions: bool = True, dry_run: bool = False) -> None: ...
    def before_delete_instance(self, instance, dry_run) -> None: ...
    def after_delete_instance(self, instance, dry_run) -> None: ...
    def import_field(self, field, obj, data, is_m2m: bool = False, **kwargs) -> None: ...
    def get_import_fields(self): ...
    def import_obj(self, obj, data, dry_run, **kwargs) -> None: ...
    def save_m2m(self, obj, data, using_transactions, dry_run) -> None: ...
    def for_delete(self, row, instance): ...
    def skip_row(self, instance, original, row, import_validation_errors: Incomplete | None = None): ...
    def get_diff_headers(self): ...
    def before_import(self, dataset, using_transactions, dry_run, **kwargs) -> None: ...
    def after_import(self, dataset, result, using_transactions, dry_run, **kwargs) -> None: ...
    def before_import_row(self, row, row_number: Incomplete | None = None, **kwargs) -> None: ...
    def after_import_row(self, row, row_result, row_number: Incomplete | None = None, **kwargs) -> None: ...
    def after_import_instance(self, instance, new, row_number: Incomplete | None = None, **kwargs) -> None: ...
    def handle_import_error(self, result, error, raise_errors: bool = False) -> None: ...
    def import_row(
        self,
        row,
        instance_loader,
        using_transactions: bool = True,
        dry_run: bool = False,
        raise_errors: Incomplete | None = None,
        **kwargs,
    ): ...
    def import_data(
        self,
        dataset,
        dry_run: bool = False,
        raise_errors: bool = False,
        use_transactions: Incomplete | None = None,
        collect_failed_rows: bool = False,
        rollback_on_validation_errors: bool = False,
        **kwargs,
    ): ...
    def import_data_inner(
        self,
        dataset,
        dry_run,
        raise_errors,
        using_transactions,
        collect_failed_rows,
        rollback_on_validation_errors: Incomplete | None = None,
        **kwargs,
    ): ...
    def get_export_order(self): ...
    def before_export(self, queryset, *args, **kwargs) -> None: ...
    def after_export(self, queryset, data, *args, **kwargs) -> None: ...
    def filter_export(self, queryset, *args, **kwargs): ...
    def export_field(self, field, obj): ...
    def get_export_fields(self): ...
    def export_resource(self, obj): ...
    def get_export_headers(self): ...
    def get_user_visible_headers(self): ...
    def get_user_visible_fields(self): ...
    def iter_queryset(self, queryset) -> Generator[Incomplete, Incomplete, None]: ...
    def export(self, *args, queryset: Incomplete | None = None, **kwargs): ...

class ModelDeclarativeMetaclass(DeclarativeMetaclass):
    def __new__(cls, name, bases, attrs): ...

class ModelResource(Resource, metaclass=ModelDeclarativeMetaclass):
    DEFAULT_RESOURCE_FIELD = Field
    WIDGETS_MAP: Incomplete
    @classmethod
    def get_m2m_widget(cls, field): ...
    @classmethod
    def get_fk_widget(cls, field): ...
    @classmethod
    def widget_from_django_field(cls, f, default=...): ...
    @classmethod
    def widget_kwargs_for_field(self, field_name): ...
    @classmethod
    def field_from_django_field(cls, field_name, django_field, readonly): ...
    def get_queryset(self): ...
    def init_instance(self, row: Incomplete | None = None): ...
    def after_import(self, dataset, result, using_transactions, dry_run, **kwargs) -> None: ...
    @classmethod
    def get_display_name(cls): ...

def modelresource_factory(model, resource_class=...): ...
