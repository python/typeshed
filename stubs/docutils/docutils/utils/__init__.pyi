import optparse
from _typeshed import Incomplete
from collections.abc import Callable, Iterable
from typing import IO, Any, Literal
from typing_extensions import TypeAlias

from docutils import ApplicationError, nodes
from docutils.io import ErrorOutput, FileOutput
from docutils.nodes import document

class DependencyList:
    list: list[str]
    file: FileOutput | None
    def __init__(self, output_file: str | None = None, dependencies: Iterable[str] = ()) -> None: ...
    def set_output(self, output_file: str | None) -> None: ...
    def add(self, *filenames: str) -> None: ...
    def close(self) -> None: ...

_SystemMessageLevel: TypeAlias = Literal[0, 1, 2, 3, 4]

class Reporter:
    levels: list[str]

    DEBUG_LEVEL: Literal[0]
    INFO_LEVEL: Literal[1]
    WARNING_LEVEL: Literal[2]
    ERROR_LEVEL: Literal[3]
    SEVERE_LEVEL: Literal[4]

    def __init__(
        self,
        source: str,
        report_level: int,
        halt_level: int,
        stream: IO[str] | str | bool | None = None,
        debug: bool = False,
        encoding: str | None = None,
        error_handler: str = "backslashreplace",
    ) -> None: ...

    source: str
    error_handler: str
    debug_flag: bool
    report_level: int
    halt_level: int
    stream: ErrorOutput
    encoding: str
    observers: list[Callable[[nodes.system_message], None]]
    max_level: int
    def set_conditions(
        self, category: Any, report_level: int, halt_level: int, stream: IO[str] | None = None, debug: bool = False
    ) -> None: ...
    def attach_observer(self, observer: Callable[[nodes.system_message], None]) -> None: ...
    def detach_observer(self, observer: Callable[[nodes.system_message], None]) -> None: ...
    def notify_observers(self, message: nodes.system_message) -> None: ...
    def system_message(self, level: int, message: str, *children: nodes.Node, **kwargs: Any) -> nodes.system_message: ...
    def debug(self, *args: Any, **kwargs: Any) -> nodes.system_message: ...
    def info(self, *args: Any, **kwargs: Any) -> nodes.system_message: ...
    def warning(self, *args: Any, **kwargs: Any) -> nodes.system_message: ...
    def error(self, *args: Any, **kwargs: Any) -> nodes.system_message: ...
    def severe(self, *args: Any, **kwargs: Any) -> nodes.system_message: ...

class SystemMessage(ApplicationError):
    level: _SystemMessageLevel
    def __init__(self, system_message: object, level: _SystemMessageLevel): ...

def new_reporter(source_path: str, settings: optparse.Values) -> Reporter: ...
def new_document(source_path: str, settings: optparse.Values | None = None) -> document: ...
def __getattr__(name: str) -> Incomplete: ...
