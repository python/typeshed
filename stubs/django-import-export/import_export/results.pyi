from collections import OrderedDict
from collections.abc import Mapping
from typing import Any, ClassVar, Iterator, Literal, TypeAlias

from django.core.exceptions import ValidationError
from django.db.models import Model
from tablib import Dataset

class Error:
    error: Exception
    traceback: str
    row: Mapping[str, Any]
    def __init__(self, error: Exception, traceback: str | None = None, row: Mapping[str, Any] | None = None) -> None: ...

_ImportType: TypeAlias = Literal["update", "new", "delete", "skip", "error", "invalid"]

class RowResult:
    IMPORT_TYPE_UPDATE: ClassVar[Literal["update"]]
    IMPORT_TYPE_NEW: ClassVar[Literal["new"]]
    IMPORT_TYPE_DELETE: ClassVar[Literal["delete"]]
    IMPORT_TYPE_SKIP: ClassVar[Literal["skip"]]
    IMPORT_TYPE_ERROR: ClassVar[Literal["error"]]
    IMPORT_TYPE_INVALID: ClassVar[Literal["invalid"]]
    valid_import_types: frozenset[_ImportType]
    errors: list[Error]
    validation_error: ValidationError | None
    diff: list[str] | None
    import_type: _ImportType
    row_values: dict[str, Any]
    object_id: Any | None
    object_repr: str | None
    instance: Model
    original: Model
    new_record: bool | None
    def __init__(self) -> None: ...
    def add_instance_info(self, instance: Model) -> None: ...

class InvalidRow:
    number: int
    error: ValidationError
    values: tuple[Any, ...]
    error_dict: dict[str, list[str]]
    def __init__(self, number: int, validation_error: ValidationError, values: tuple[Any, ...]) -> None: ...
    @property
    def field_specific_errors(self) -> dict[str, list[str]]: ...
    @property
    def non_field_specific_errors(self) -> list[str]: ...
    @property
    def error_count(self) -> int: ...

class Result:
    base_errors: list[Error]
    diff_headers: list[str]
    rows: list[RowResult]
    invalid_rows: list[InvalidRow]
    failed_dataset: Dataset
    totals: OrderedDict[_ImportType, int]
    total_rows: int
    def __init__(self) -> None: ...
    def valid_rows(self) -> list[RowResult]: ...
    def append_row_result(self, row_result: RowResult) -> None: ...
    def append_base_error(self, error: Error) -> None: ...
    def add_dataset_headers(self, headers: list[str] | None) -> None: ...
    def append_failed_row(self, row: Mapping[str, Any], error) -> None: ...
    def append_invalid_row(self, number: int, row: Mapping[str, Any], validation_error: ValidationError) -> None: ...
    def increment_row_result_total(self, row_result: RowResult) -> None: ...
    def row_errors(self) -> list[tuple[int, Any]]: ...
    def has_errors(self) -> bool: ...
    def has_validation_errors(self) -> bool: ...
    def __iter__(self) -> Iterator[RowResult]: ...
