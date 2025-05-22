from _typeshed import Incomplete

from docutils.writers import html4css1

__docformat__: str

class Writer(html4css1.Writer):
    default_stylesheet: str
    default_stylesheet_path: Incomplete
    default_template: str
    default_template_path: Incomplete
    settings_spec: Incomplete
    settings_default_overrides: Incomplete
    relative_path_settings: Incomplete
    config_section: str
    config_section_dependencies: Incomplete
    translator_class: Incomplete
    def __init__(self) -> None: ...
    pepnum: Incomplete
    title: Incomplete
    def interpolation_dict(self): ...
    def assemble_parts(self) -> None: ...

class HTMLTranslator(html4css1.HTMLTranslator):
    def depart_field_list(self, node) -> None: ...
