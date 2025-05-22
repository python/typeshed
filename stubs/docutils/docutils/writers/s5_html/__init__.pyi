from _typeshed import Incomplete

from docutils.writers import html4css1

__docformat__: str
themes_dir_path: Incomplete

def find_theme(name): ...

class Writer(html4css1.Writer):
    settings_spec: Incomplete
    settings_default_overrides: Incomplete
    config_section: str
    config_section_dependencies: Incomplete
    translator_class: Incomplete
    def __init__(self) -> None: ...

class S5HTMLTranslator(html4css1.HTMLTranslator):
    s5_stylesheet_template: str
    disable_current_slide: str
    layout_template: str
    default_theme: str
    base_theme_file: str
    direct_theme_files: Incomplete
    indirect_theme_files: Incomplete
    required_theme_files: Incomplete
    theme_file_path: Incomplete
    s5_footer: Incomplete
    s5_header: Incomplete
    section_count: int
    theme_files_copied: Incomplete
    def __init__(self, *args) -> None: ...
    def setup_theme(self) -> None: ...
    def copy_theme(self) -> None: ...
    files_to_skip_pattern: Incomplete
    def copy_file(self, name, source_dir, dest_dir): ...
    head: Incomplete
    def depart_document(self, node) -> None: ...
    def depart_footer(self, node) -> None: ...
    def depart_header(self, node) -> None: ...
    def visit_section(self, node) -> None: ...
    def visit_subtitle(self, node) -> None: ...
    def visit_title(self, node) -> None: ...
