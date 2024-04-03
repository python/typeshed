from _typeshed import Incomplete

from django import forms

class ImportExportFormBase(forms.Form):
    resource: Incomplete
    def __init__(self, *args, resources: Incomplete | None = None, **kwargs) -> None: ...

class ImportForm(ImportExportFormBase):
    import_file: Incomplete
    input_format: Incomplete
    def __init__(self, import_formats, *args, **kwargs) -> None: ...
    @property
    def media(self): ...

class ConfirmImportForm(forms.Form):
    import_file_name: Incomplete
    original_file_name: Incomplete
    input_format: Incomplete
    resource: Incomplete
    def clean_import_file_name(self): ...

class ExportForm(ImportExportFormBase):
    file_format: Incomplete
    def __init__(self, formats, *args, **kwargs) -> None: ...

def export_action_form_factory(formats): ...
