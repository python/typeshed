from optparse import Values
from typing import IO, Any, Generic, TypeVar

from docutils import SettingsSpec, io, nodes
from docutils.frontend import OptionParser
from docutils.io import Input, Output
from docutils.parsers import Parser
from docutils.readers import Reader
from docutils.writers import Writer

__docformat__: str

_S = TypeVar("_S")

class Publisher(Generic[_S]):
    document: nodes.document | None
    reader: Reader[_S] | None
    parser: Parser | None
    writer: Writer | None
    source: Input[_S] | None
    source_class: type[Input[_S]]
    destination: Output | None
    destination_class: type[Output]
    settings: Values | None
    def __init__(
        self,
        reader: Reader[_S] | None = None,
        parser: Parser | None = None,
        writer: Writer | None = None,
        source: Input[_S] | None = None,
        source_class: type[Input[_S]] = io.FileInput,
        destination: Output | None = None,
        destination_class: type[Output] = io.FileOutput,
        settings: Values | None = None,
    ) -> None: ...
    def set_reader(self, reader_name: str, parser: Parser, parser_name: str) -> None: ...
    def set_writer(self, writer_name: str) -> None: ...
    def set_components(self, reader_name: str, parser_name: str, writer_name: str) -> None: ...
    def setup_option_parser(
        self,
        usage: str | None = None,
        description: str | None = None,
        settings_spec: SettingsSpec | None = None,
        config_section: str | None = None,
        **defaults,
    ) -> OptionParser: ...
    def get_settings(
        self,
        usage: str | None = None,
        description: str | None = None,
        settings_spec: SettingsSpec | None = None,
        config_section: str | None = None,
        **defaults,
    ) -> Values: ...
    def process_programmatic_settings(self, settings_spec: SettingsSpec, settings_overrides, config_section: str) -> None: ...
    def process_command_line(
        self,
        argv: list[str] | None = None,
        usage: str | None = None,
        description: str | None = None,
        settings_spec: SettingsSpec | None = None,
        config_section: str | None = None,
        **defaults,
    ) -> None: ...
    def set_io(self, source_path: str | None = None, destination_path: str | None = None) -> None: ...
    def set_source(self, source: Any | None = None, source_path: str | None = None) -> None: ...
    def set_destination(self, destination: Any | None = None, destination_path: str | None = None) -> None: ...
    def apply_transforms(self) -> None: ...
    def publish(
        self,
        argv: list[str] | None = None,
        usage: Any | None = None,
        description: Any | None = None,
        settings_spec: SettingsSpec | None = None,
        settings_overrides: Any | None = None,
        config_section: str | None = None,
        enable_exit_status: bool = False,
    ) -> Any: ...
    def debugging_dumps(self) -> None: ...
    def report_Exception(self, error: Exception) -> None: ...
    def report_SystemMessage(self, error: Exception) -> None: ...
    def report_UnicodeError(self, error: Exception) -> None: ...

default_usage: str
default_description: str

def publish_cmdline(
    reader: Reader[_S] | None = None,
    reader_name: str = "standalone",
    parser: Parser | None = None,
    parser_name: str = "restructuredtext",
    writer: Writer | None = None,
    writer_name: str = "pseudoxml",
    settings: Values | None = None,
    settings_spec: SettingsSpec | None = None,
    settings_overrides: Any | None = None,
    config_section: str | None = None,
    enable_exit_status: bool = True,
    argv: list[str] | None = None,
    usage: str = default_usage,
    description: str = default_description,
) -> Any: ...
def publish_file(
    source: IO[str] | None = None,
    source_path: str | None = None,
    destination: Output | None = None,
    destination_path: str | None = None,
    reader: Reader[_S] | None = None,
    reader_name: str = "standalone",
    parser: Parser | None = None,
    parser_name: str = "restructuredtext",
    writer: Writer | None = None,
    writer_name: str = "pseudoxml",
    settings: Values | None = None,
    settings_spec: SettingsSpec | None = None,
    settings_overrides: Any | None = None,
    config_section: str | None = None,
    enable_exit_status: bool = False,
) -> Any: ...
def publish_string(
    source: str,
    source_path: str | None = None,
    destination_path: str | None = None,
    reader: Reader[_S] | None = None,
    reader_name: str = "standalone",
    parser: Parser | None = None,
    parser_name: str = "restructuredtext",
    writer: Writer | None = None,
    writer_name: str = "pseudoxml",
    settings: Values | None = None,
    settings_spec: SettingsSpec | None = None,
    settings_overrides: Any | None = None,
    config_section: str | None = None,
    enable_exit_status: bool = False,
) -> Any: ...
def publish_parts(
    source: Any,
    source_path: str | None = None,
    source_class: type[Input[_S]] = io.StringInput,
    destination_path: str | None = None,
    reader: Reader[_S] | None = None,
    reader_name: str = "standalone",
    parser: Parser | None = None,
    parser_name: str = "restructuredtext",
    writer: Writer | None = None,
    writer_name: str = "pseudoxml",
    settings: Values | None = None,
    settings_spec: SettingsSpec | None = None,
    settings_overrides: Any | None = None,
    config_section: str | None = None,
    enable_exit_status: bool = False,
) -> dict[str, Any]: ...
def publish_doctree(
    source: Any,
    source_path: str | None = None,
    source_class: type[Input[_S]] = io.StringInput,
    reader: Reader[_S] | None = None,
    reader_name: str = "standalone",
    parser: Parser | None = None,
    parser_name: str = "restructuredtext",
    settings: Values | None = None,
    settings_spec: SettingsSpec | None = None,
    settings_overrides: Any | None = None,
    config_section: str | None = None,
    enable_exit_status: bool = False,
) -> nodes.document: ...
def publish_from_doctree(
    document: nodes.document,
    destination_path: str | None = None,
    writer: Writer | None = None,
    writer_name: str = "pseudoxml",
    settings: Values | None = None,
    settings_spec: SettingsSpec | None = None,
    settings_overrides: Any | None = None,
    config_section: str | None = None,
    enable_exit_status: bool = False,
) -> Any: ...
def publish_cmdline_to_binary(
    reader=None,
    reader_name="standalone",
    parser=None,
    parser_name="restructuredtext",
    writer=None,
    writer_name="pseudoxml",
    settings: Values | None = None,
    settings_spec: SettingsSpec | None = None,
    settings_overrides: Any | None = None,
    config_section: str | None = None,
    enable_exit_status: bool = True,
    argv: list[str] | None = None,
    usage: str = default_usage,
    description: str = default_description,
    destination: Output | None = None,
    destination_class: type[Output] = io.BinaryFileOutput,
) -> Any: ...
def publish_programmatically(
    source_class: type[Input[_S]],
    source: Any,
    source_path: str,
    destination_class: type[Output],
    destination: Any,
    destination_path: str,
    reader: Reader[_S],
    reader_name: str,
    parser: Parser,
    parser_name: str,
    writer: Writer,
    writer_name: str,
    settings: Values,
    settings_spec: SettingsSpec,
    settings_overrides: Any,
    config_section: str,
    enable_exit_status: bool,
) -> tuple[Any, Publisher[_S]]: ...
