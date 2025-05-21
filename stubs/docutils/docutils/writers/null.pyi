from _typeshed import Incomplete

from docutils import writers

class Writer(writers.UnfilteredWriter):
    supported: Incomplete
    config_section: str
    config_section_dependencies: Incomplete
    def translate(self) -> None: ...
