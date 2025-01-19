from collections.abc import Sequence
from typing import Any

from django import forms

from .formats.base_formats import Format
from .resources import Resource

class ImportExportFormBase(forms.Form):
    resource: forms.ChoiceField
    format: forms.ChoiceField
    def __init__(
        self, formats: list[type[Format]], resources: list[type[Resource[Any]]] | None = None, *args: Any, **kwargs: Any
    ) -> None: ...

class ImportForm(ImportExportFormBase):
    import_file: forms.FileField
    field_order: Sequence[str]
    @property
    def media(self) -> forms.Media: ...

class ConfirmImportForm(forms.Form):
    import_file_name: forms.CharField
    original_file_name: forms.CharField
    resource: forms.CharField
    def clean_import_file_name(self) -> str: ...

class ExportForm(ImportExportFormBase):
    export_items: forms.MultipleChoiceField
