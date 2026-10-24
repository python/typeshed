from _typeshed import StrPath, SupportsKeysAndGetItem
from typing import IO, Any, Final, Literal, Protocol, TypeAlias, overload, type_check_only
from typing_extensions import deprecated

from docutils import SettingsSpec, nodes
from docutils.frontend import Values
from docutils.io import Input, Output
from docutils.parsers import Parser
from docutils.readers import Reader
from docutils.utils import SystemMessage
from docutils.writers import Writer, _html_base, _HTMLWriterParts, _LaTeXWriterParts, _WriterParts, latex2e

__docformat__: Final = "reStructuredText"

# Components may be given as instances, by name, or by alias.
_ReaderArg: TypeAlias = Reader[Any] | str | None
_ParserArg: TypeAlias = Parser | str | None
_WriterArg: TypeAlias = Writer[Any] | str | None
_HTMLWriterName: TypeAlias = Literal[
    "html", "html4", "xhtml10", "html4css1", "html5", "xhtml", "html5_polyglot", "s5", "s5_html", "pep_html"
]
_LaTeXWriterName: TypeAlias = Literal["latex", "latex2e", "xetex", "xelatex", "luatex", "lualatex"]

# A mapping of setting names to values which is copied with `.copy()` and unpacked with `**`.
# This would typically be a `dict`.
#
# See: <https://docutils.sourceforge.io/docs/user/config.html>.
@type_check_only
class _SettingsOverrides(SupportsKeysAndGetItem[str, object], Protocol):
    def copy(self) -> SupportsKeysAndGetItem[str, object]: ...

_FileSource: TypeAlias = IO[str] | IO[bytes]
_FileDestination: TypeAlias = IO[str] | IO[bytes]

class Publisher:
    document: nodes.document | None
    reader: Reader[Any]
    parser: Parser | None
    writer: Writer[Any]
    source: Input[Any] | None
    source_class: type[Input[Any]]
    destination: Output | None
    destination_class: type[Output]
    settings: Values | None
    def __init__(
        self,
        reader: _ReaderArg = None,
        parser: _ParserArg = None,
        writer: _WriterArg = None,
        source: Input[Any] | None = None,
        source_class: type[Input[Any]] = ...,
        destination: Output | None = None,
        destination_class: type[Output] = ...,
        settings: Values | None = None,
    ) -> None: ...
    def set_reader(self, reader: str, parser: Parser | str | None = None, parser_name: str | None = None) -> None: ...
    def set_writer(self, writer_name: str) -> None: ...
    @deprecated("The `Publisher.set_components()` will be removed in Docutils 2.0.")
    def set_components(self, reader_name: str, parser_name: str, writer_name: str) -> None: ...
    def get_settings(
        self,
        usage: str | None = None,
        description: str | None = None,
        settings_spec: SettingsSpec | None = None,
        config_section: str | None = None,
        **defaults: object,
    ) -> Values: ...
    def process_programmatic_settings(
        self, settings_spec: SettingsSpec | None, settings_overrides: _SettingsOverrides | None, config_section: str | None
    ) -> None: ...
    def process_command_line(
        self,
        argv: list[str] | None = None,
        usage: str | None = None,
        description: str | None = None,
        settings_spec: SettingsSpec | None = None,
        config_section: str | None = None,
        **defaults: object,
    ) -> None: ...
    def set_io(self, source_path: StrPath | None = None, destination_path: StrPath | None = None) -> None: ...
    def set_source(self, source: object = None, source_path: StrPath | None = None) -> None: ...
    def set_destination(self, destination: _FileDestination | None = None, destination_path: StrPath | None = None) -> None: ...
    def apply_transforms(self) -> None: ...
    def publish(
        self,
        argv: list[str] | None = None,
        usage: str | None = None,
        description: str | None = None,
        settings_spec: SettingsSpec | None = None,
        settings_overrides: _SettingsOverrides | None = None,
        config_section: str | None = None,
        enable_exit_status: bool = False,
    ) -> str | bytes | None: ...
    def debugging_dumps(self) -> None: ...
    def prompt(self) -> None: ...
    def report_Exception(self, error: BaseException) -> None: ...
    def report_SystemMessage(self, error: SystemMessage) -> None: ...
    def report_UnicodeError(self, error: UnicodeEncodeError) -> None: ...

default_usage: Final[str]
default_description: Final[str]

def publish_cmdline(
    reader: _ReaderArg = None,
    reader_name: str | None = None,
    parser: _ParserArg = None,
    parser_name: str | None = None,
    writer: _WriterArg = None,
    writer_name: str | None = None,
    settings: Values | None = None,
    settings_spec: SettingsSpec | None = None,
    settings_overrides: _SettingsOverrides | None = None,
    config_section: str | None = None,
    enable_exit_status: bool = True,
    argv: list[str] | None = None,
    usage: str = ...,
    description: str = ...,
) -> str | bytes | None: ...
def publish_file(
    source: _FileSource | None = None,
    source_path: StrPath | None = None,
    destination: _FileDestination | None = None,
    destination_path: StrPath | None = None,
    reader: _ReaderArg = None,
    reader_name: str | None = None,
    parser: _ParserArg = None,
    parser_name: str | None = None,
    writer: _WriterArg = None,
    writer_name: str | None = None,
    settings: Values | None = None,
    settings_spec: SettingsSpec | None = None,
    settings_overrides: _SettingsOverrides | None = None,
    config_section: str | None = None,
    enable_exit_status: bool = False,
) -> str | bytes: ...

# Returns `bytes` unless the "output_encoding" setting is "unicode". This is not type encodable.
def publish_string(
    source: str | bytes,
    source_path: StrPath | None = None,
    destination_path: StrPath | None = None,
    reader: _ReaderArg = None,
    reader_name: str | None = None,
    parser: _ParserArg = None,
    parser_name: str | None = None,
    writer: _WriterArg = None,
    writer_name: str | None = None,
    settings: Values | None = None,
    settings_spec: SettingsSpec | None = None,
    settings_overrides: _SettingsOverrides | None = None,
    config_section: str | None = None,
    enable_exit_status: bool = False,
) -> str | bytes: ...

@overload
def publish_parts(  # type: ignore[overload-overlap]
    source: str | bytes | nodes.document | IO[str] | IO[bytes],  # depends on `source_class`
    source_path: StrPath | None = None,
    source_class: type[Input[Any]] = ...,
    destination_path: StrPath | None = None,
    reader: _ReaderArg = None,
    reader_name: str | None = None,
    parser: _ParserArg = None,
    parser_name: str | None = None,
    *,
    writer: _HTMLWriterName | _html_base.Writer,
    writer_name: str | None = None,
    settings: Values | None = None,
    settings_spec: SettingsSpec | None = None,
    settings_overrides: _SettingsOverrides | None = None,
    config_section: str | None = None,
    enable_exit_status: bool = False,
) -> _HTMLWriterParts: ...
@overload
def publish_parts(  # type: ignore[overload-overlap]
    source: str | bytes | nodes.document | IO[str] | IO[bytes],  # depends on `source_class`
    source_path: StrPath | None = None,
    source_class: type[Input[Any]] = ...,
    destination_path: StrPath | None = None,
    reader: _ReaderArg = None,
    reader_name: str | None = None,
    parser: _ParserArg = None,
    parser_name: str | None = None,
    *,
    writer: _LaTeXWriterName | latex2e.Writer,
    writer_name: str | None = None,
    settings: Values | None = None,
    settings_spec: SettingsSpec | None = None,
    settings_overrides: _SettingsOverrides | None = None,
    config_section: str | None = None,
    enable_exit_status: bool = False,
) -> _LaTeXWriterParts: ...
@overload
def publish_parts(
    source: str | bytes | nodes.document | IO[str] | IO[bytes],  # depends on `source_class`
    source_path: StrPath | None = None,
    source_class: type[Input[Any]] = ...,
    destination_path: StrPath | None = None,
    reader: _ReaderArg = None,
    reader_name: str | None = None,
    parser: _ParserArg = None,
    parser_name: str | None = None,
    writer: _WriterArg = None,
    writer_name: str | None = None,
    settings: Values | None = None,
    settings_spec: SettingsSpec | None = None,
    settings_overrides: _SettingsOverrides | None = None,
    config_section: str | None = None,
    enable_exit_status: bool = False,
) -> _WriterParts: ...

def publish_doctree(
    source: str | bytes | IO[str] | IO[bytes] | None,
    source_path: StrPath | None = None,
    source_class: type[Input[Any]] = ...,
    reader: _ReaderArg = None,
    reader_name: str | None = None,
    parser: _ParserArg = None,
    parser_name: str | None = None,
    settings: Values | None = None,
    settings_spec: SettingsSpec | None = None,
    settings_overrides: _SettingsOverrides | None = None,
    config_section: str | None = None,
    enable_exit_status: bool = False,
) -> nodes.document: ...
def publish_from_doctree(
    document: nodes.document,
    destination_path: StrPath | None = None,
    writer: _WriterArg = None,
    writer_name: str | None = None,
    settings: Values | None = None,
    settings_spec: SettingsSpec | None = None,
    settings_overrides: _SettingsOverrides | None = None,
    config_section: str | None = None,
    enable_exit_status: bool = False,
) -> str | bytes: ...
@deprecated("The `publish_cmdline_to_binary()` is deprecated by `publish_cmdline()` and will be removed in Docutils 0.24.")
def publish_cmdline_to_binary(
    reader: _ReaderArg = None,
    reader_name: str = "standalone",
    parser: _ParserArg = None,
    parser_name: str = "restructuredtext",
    writer: _WriterArg = None,
    writer_name: str = "pseudoxml",
    settings: Values | None = None,
    settings_spec: SettingsSpec | None = None,
    settings_overrides: _SettingsOverrides | None = None,
    config_section: str | None = None,
    enable_exit_status: bool = True,
    argv: list[str] | None = None,
    usage: str = ...,
    description: str = ...,
    destination: _FileDestination | None = None,
    destination_class: type[Output] = ...,
) -> str | bytes | None: ...
def publish_programmatically(
    source_class: type[Input[Any]],
    source: object,
    source_path: StrPath | None,
    destination_class: type[Output],
    destination: _FileDestination | None,
    destination_path: StrPath | None,
    reader: _ReaderArg,
    reader_name: str | None,
    parser: _ParserArg,
    parser_name: str | None,
    writer: _WriterArg,
    writer_name: str | None,
    settings: Values | None,
    settings_spec: SettingsSpec | None,
    settings_overrides: _SettingsOverrides | None,
    config_section: str | None,
    enable_exit_status: bool,
) -> tuple[str | bytes | None, Publisher]: ...
def rst2something(writer: str, documenttype: str, doc_path: str = "") -> None: ...
def rst2html() -> None: ...
def rst2html4() -> None: ...
def rst2html5() -> None: ...
def rst2latex() -> None: ...
def rst2man() -> None: ...
def rst2odt() -> None: ...
def rst2pseudoxml() -> None: ...
def rst2s5() -> None: ...
def rst2xetex() -> None: ...
def rst2xml() -> None: ...
