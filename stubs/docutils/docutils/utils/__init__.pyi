from _typeshed import StrPath, SupportsWrite
from collections.abc import Callable, Iterable, Mapping, Sequence
from re import Pattern
from typing import Any, Final, Literal, Protocol, TypeAlias, TypeVar, type_check_only
from typing_extensions import deprecated

from docutils import ApplicationError, DataError, nodes
from docutils.frontend import Values
from docutils.io import ErrorOutput, FileOutput
from docutils.nodes import document, unescape as unescape

_T = TypeVar("_T")
_Observer: TypeAlias = Callable[[nodes.system_message], object]

__docformat__: Final = "reStructuredText"

class DependencyList:
    list: list[str]
    file: FileOutput | None
    # `output_file` "-" means stdout.
    def __init__(self, output_file: StrPath | None = None, dependencies: Iterable[StrPath] = ()) -> None: ...
    def set_output(self, output_file: StrPath | None) -> None: ...
    def add(self, *paths: StrPath) -> None: ...
    def close(self) -> None: ...

class SystemMessagePropagation(ApplicationError): ...

class Reporter:
    get_source_and_line: Callable[[int | None], tuple[StrPath | None, int | None]]
    levels: Final[Sequence[str]]

    DEBUG_LEVEL: Final = 0
    INFO_LEVEL: Final = 1
    WARNING_LEVEL: Final = 2
    ERROR_LEVEL: Final = 3
    SEVERE_LEVEL: Final = 4

    stream: ErrorOutput
    encoding: str
    observers: list[_Observer]
    max_level: int
    def __init__(
        self,
        source: StrPath,
        report_level: int,
        halt_level: int,
        stream: ErrorOutput | SupportsWrite[str] | SupportsWrite[bytes] | str | Literal[False] | None = None,
        debug: bool = False,
        encoding: str | None = None,
        error_handler: str = "backslashreplace",
    ) -> None: ...

    source: StrPath
    error_handler: str
    debug_flag: bool
    report_level: int
    halt_level: int
    def attach_observer(self, observer: _Observer) -> None: ...
    def detach_observer(self, observer: _Observer) -> None: ...
    def notify_observers(self, message: nodes.system_message) -> None: ...
    def system_message(
        self,
        level: int,
        message: str | Exception,
        *children: nodes.Node,
        base_node: nodes.Node | None = ...,
        source: StrPath | None = ...,
        line: int | None = ...,
        **kwargs: object,  # additional attributes of the system_message node
    ) -> nodes.system_message: ...
    def debug(
        self,
        message: str | Exception,
        *children: nodes.Node,
        base_node: nodes.Node | None = ...,
        source: StrPath | None = ...,
        line: int | None = ...,
        **kwargs: object,  # additional attributes of the system_message node
    ) -> nodes.system_message: ...
    def info(
        self,
        message: str | Exception,
        *children: nodes.Node,
        base_node: nodes.Node | None = ...,
        source: StrPath | None = ...,
        line: int | None = ...,
        **kwargs: object,  # additional attributes of the system_message node
    ) -> nodes.system_message: ...
    def warning(
        self,
        message: str | Exception,
        *children: nodes.Node,
        base_node: nodes.Node | None = ...,
        source: StrPath | None = ...,
        line: int | None = ...,
        **kwargs: object,  # additional attributes of the system_message node
    ) -> nodes.system_message: ...
    def error(
        self,
        message: str | Exception,
        *children: nodes.Node,
        base_node: nodes.Node | None = ...,
        source: StrPath | None = ...,
        line: int | None = ...,
        **kwargs: object,  # additional attributes of the system_message node
    ) -> nodes.system_message: ...
    def severe(
        self,
        message: str | Exception,
        *children: nodes.Node,
        base_node: nodes.Node | None = ...,
        source: StrPath | None = ...,
        line: int | None = ...,
        **kwargs: object,  # additional attributes of the system_message node
    ) -> nodes.system_message: ...

# The signature of `Reporter.debug()`, ..., `Reporter.severe()`,
# which are e.g. stored as `warn` and `error` attributes by some translators.
@type_check_only
class _ReporterMessageMethod(Protocol):  # noqa: Y046  # used by writers
    def __call__(
        self,
        message: str | Exception,
        *children: nodes.Node,
        base_node: nodes.Node | None = ...,
        source: StrPath | None = ...,
        line: int | None = ...,
        **kwargs: object,
    ) -> nodes.system_message: ...

class SystemMessage(ApplicationError):
    level: int
    def __init__(self, system_message: nodes.system_message, level: int) -> None: ...

def new_reporter(source_path: StrPath, settings: Values) -> Reporter: ...
def new_document(source_path: StrPath, settings: Values | None = None) -> document: ...

class ExtensionOptionError(DataError): ...
class BadOptionError(ExtensionOptionError): ...
class BadOptionDataError(ExtensionOptionError): ...
class DuplicateOptionError(ExtensionOptionError): ...

# Option conversion functions are called with `None` for options without argument.
def extract_extension_options(
    field_list: nodes.field_list, options_spec: Mapping[str, Callable[[str], object]]
) -> dict[str, Any]: ...  # values of arbitrary options, as returned by the conversion functions
def extract_options(field_list: nodes.field_list) -> list[tuple[str, str | None]]: ...
def assemble_option_dict(
    option_list: Iterable[tuple[str, str | None]], options_spec: Mapping[str, Callable[[str], object]]
) -> dict[str, Any]: ...  # values of arbitrary options, as returned by the conversion functions

class NameValueError(DataError): ...

@deprecated("Deprecated and will be removed in Docutils 1.0.")
def decode_path(path: str) -> str: ...
def extract_name_value(line: str) -> list[tuple[str, str]]: ...
def clean_rcs_keywords(paragraph: nodes.paragraph, keyword_substitutions: Iterable[tuple[Pattern[str], str]]) -> None: ...
def relative_path(source: StrPath | None, target: StrPath) -> str: ...
@deprecated("Deprecated and will be removed in Docutils 1.0. Use `get_stylesheet_list()` instead.")
def get_stylesheet_reference(settings: Values, relative_to: StrPath | None = None) -> str: ...
def get_stylesheet_list(settings: Values) -> list[str]: ...
def find_file_in_dirs(path: StrPath, dirs: Iterable[StrPath]) -> str: ...
def get_trim_footnote_ref_space(settings: Values) -> bool: ...
def get_source_line(node: nodes.Node | None) -> tuple[str | None, int | None]: ...
def escape2null(text: str) -> str: ...
def split_escaped_whitespace(text: str) -> list[str]: ...
def strip_combining_chars(text: str) -> str: ...
def find_combining_chars(text: str) -> list[int]: ...
def column_indices(text: str) -> list[int]: ...

east_asian_widths: dict[str, int]

def column_width(text: str) -> int: ...
def uniq(L: list[_T]) -> list[_T]: ...
def normalize_language_tag(tag: str) -> list[str]: ...
def xml_declaration(encoding: str | None = None) -> str: ...  # encoding may be "unicode"
