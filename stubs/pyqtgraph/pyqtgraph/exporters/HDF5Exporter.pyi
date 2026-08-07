from _typeshed import Incomplete

from .Exporter import Exporter

__all__ = ["HDF5Exporter"]

class HDF5Exporter(Exporter):
    Name: str
    windows: Incomplete
    allowCopy: bool
    params: Incomplete
    def __init__(self, item) -> None: ...
    def parameters(self): ...
    def export(self, fileName=None) -> None: ...
