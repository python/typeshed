from _typeshed import Incomplete

from docutils import writers

__docformat__: str

class Writer(writers.Writer):
    supported: Incomplete
    settings_spec: Incomplete
    config_section: str
    config_section_dependencies: Incomplete
    output: Incomplete
    def translate(self) -> None: ...
    def supports(self, format): ...
