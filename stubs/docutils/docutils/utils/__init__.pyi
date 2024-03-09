import optparse
from _typeshed import Incomplete, StrPath, SupportsWrite, Unused
from collections.abc import Callable, Iterable, Mapping
from re import Pattern
from typing import Any, Literal, TypeVar
from typing_extensions import TypeAlias

from docutils import ApplicationError, DataError, nodes
from docutils.frontend import Values
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

    stream: ErrorOutput
    encoding: str
    observers: list[Callable[[nodes.system_message], None]]
    max_level: int
    def __init__(
        self,
        source: str,
        report_level: int,
        halt_level: int,
        stream: SupportsWrite[str] | SupportsWrite[bytes] | str | bool | None = None,
        debug: bool = False,
        encoding: str | None = None,
        error_handler: str = "backslashreplace",
    ) -> None: ...

    source: str
    error_handler: str
    debug_flag: bool
    report_level: _SystemMessageLevel
    halt_level: int
    def set_conditions(
        self,
        category: Unused,
        report_level: int,
        halt_level: int,
        stream: SupportsWrite[str] | SupportsWrite[bytes] | None = None,
        debug: bool = False,
    ) -> None: ...
    def attach_observer(self, observer: Callable[[nodes.system_message], None]) -> None: ...
    def detach_observer(self, observer: Callable[[nodes.system_message], None]) -> None: ...
    def notify_observers(self, message: nodes.system_message) -> None: ...
    def system_message(
        self,
        level: int,
        message: str | Exception,
        *children: nodes.Node,
        base_node: nodes.Node,
        source: str,
        **kwargs: Incomplete,
    ) -> nodes.system_message: ...
    def debug(self, *args: nodes.Node, **kwargs: Any) -> nodes.system_message: ...
    def info(self, *args: nodes.Node, **kwargs: Any) -> nodes.system_message: ...
    def warning(self, *args: nodes.Node, **kwargs: Any) -> nodes.system_message: ...
    def error(self, *args: nodes.Node, **kwargs: Any) -> nodes.system_message: ...
    def severe(self, *args: nodes.Node, **kwargs: Any) -> nodes.system_message: ...

class SystemMessage(ApplicationError):
    level: _SystemMessageLevel
    def __init__(self, system_message: object, level: _SystemMessageLevel): ...

def new_reporter(source_path: str, settings: optparse.Values) -> Reporter: ...
def new_document(source_path: str, settings: optparse.Values | None = None) -> document: ...

class ExtensionOptionError(DataError): ...
class BadOptionError(ExtensionOptionError): ...
class BadOptionDataError(ExtensionOptionError): ...
class DuplicateOptionError(ExtensionOptionError): ...

def extract_extension_options(
    field_list: nodes.field_list, options_spec: Mapping[str, Callable[[str], Any]]
) -> dict[str, Any]: ...
def extract_options(field_list: nodes.field_list) -> list[tuple[str, str]]: ...
def assemble_option_dict(
    option_list: Iterable[tuple[str, str]], options_spec: Mapping[str, Callable[[str], Any]]
) -> dict[str, Any]: ...

class NameValueError(DataError): ...

def decode_path(path: str) -> str: ...
def extract_name_value(line: str) -> list[tuple[str, str]]: ...
def clean_rcs_keywords(paragraph: nodes.paragraph, keyword_substitutions: Iterable[tuple[Pattern[str], str]]) -> None: ...
def relative_path(source: StrPath | None, target: StrPath) -> str: ...
def get_stylesheet_reference(settings: Values, relative_to: str | None = None) -> str: ...
def get_stylesheet_list(settings: Values) -> list[str]: ...
def find_file_in_dirs(path: StrPath, dirs: Iterable[StrPath]) -> str: ...
def get_trim_footnote_ref_space(settings: Values) -> bool: ...
def get_source_line(node: nodes.Node) -> tuple[str, int]: ...
def escape2null(text: str) -> str: ...
def split_escaped_whitespace(text: str) -> list[str]: ...
def strip_combining_chars(text: str) -> str: ...
def find_combining_chars(text: str) -> list[int]: ...
def column_indices(text: str) -> list[int]: ...

east_asian_widths: dict[str, int]

def column_width(text: str) -> int: ...

_T = TypeVar("_T")

def uniq(L: list[_T]) -> list[_T]: ...
def normalize_language_tag(tag: str) -> list[str]: ...

release_level_abbreviations: dict[str, str]

def version_identifier(version_info: tuple[int, int, int, str, int, bool] | None = None) -> str: ...
def unescape(text: str, restore_backslashes: bool = False, respect_whitespace: bool = False) -> str: ...
