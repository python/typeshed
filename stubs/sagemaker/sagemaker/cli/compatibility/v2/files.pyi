import abc
from _typeshed import Incomplete
from abc import abstractmethod

LOGGER: Incomplete

class FileUpdater(metaclass=abc.ABCMeta):
    input_path: Incomplete
    output_path: Incomplete
    def __init__(self, input_path, output_path) -> None: ...
    @abstractmethod
    def update(self): ...

class PyFileUpdater(FileUpdater):
    def update(self) -> None: ...

class JupyterNotebookFileUpdater(FileUpdater):
    def update(self) -> None: ...
