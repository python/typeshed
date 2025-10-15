from _typeshed import Incomplete

from .Exporter import Exporter

__all__ = ["CSVExporter"]

class CSVExporter(Exporter):
    Name: str
    windows: Incomplete
    params: Incomplete
    index_counter: Incomplete
    header: Incomplete
    data: Incomplete
    def __init__(self, item) -> None: ...
    def parameters(self): ...
    def export(self, fileName=None) -> None: ...
