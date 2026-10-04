import optparse
from _typeshed import StrPath, SupportsWrite
from collections.abc import Iterable, Mapping, MutableMapping, Sequence
from configparser import RawConfigParser
from typing import Any, ClassVar, Final, Literal, Protocol, overload, type_check_only
from typing_extensions import Unpack, deprecated

from docutils import SettingsSpec, _OptionKwargs, _OptionTuple, _SettingsSpecTuple
from docutils.utils import DependencyList

__docformat__: Final = "reStructuredText"

@type_check_only
class _OptionValidator(Protocol):
    def __call__(
        self,
        setting: str,
        value: str | None,
        option_parser: OptionParser,
        /,
        config_parser: ConfigParser | None = None,
        config_section: str | None = None,
    ) -> object: ...

@deprecated("Deprecated and will be removed with the switch from optparse to argparse in Docutils 2.0.")
def store_multiple(
    option: optparse.Option, opt: str, value: object, parser: OptionParser, *args: str, **kwargs: object
) -> None: ...
@deprecated("Deprecated and will be removed with the switch from optparse to argparse in Docutils 2.0.")
def read_config_file(option: optparse.Option, opt: str, value: str, parser: OptionParser) -> None: ...
def validate_encoding(
    setting: str,
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> str | None: ...  # `None` for the deprecated empty value
def validate_encoding_error_handler(
    setting: str,
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> str: ...
def validate_encoding_and_error_handler(
    setting: str,
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> str: ...
def validate_boolean(
    setting: str | bool,
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> bool: ...
def validate_ternary(
    setting: str | bool,
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> str | bool | None: ...
def validate_nonnegative_int(
    setting: str | int,
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> int: ...
def validate_threshold(
    setting: str | int,
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> int: ...
def validate_colon_separated_string_list(
    setting: str | list[str],
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> list[str]: ...
def validate_comma_separated_list(
    setting: str | list[str],
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> list[str]: ...
def validate_math_output(
    setting: str,
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> tuple[()] | tuple[str, str]: ...
def validate_url_trailing_slash(
    setting: str,
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> str: ...
def validate_dependency_file(
    setting: str | None,
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> DependencyList: ...
def validate_strip_class(
    setting: str,
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> list[str]: ...
def validate_smartquotes_locales(
    setting: str | list[str | tuple[str, str]],
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> list[tuple[str, Sequence[str]]]: ...
def make_paths_absolute(pathdict: MutableMapping[str, Any], keys: Iterable[str], base_path: StrPath | None = None) -> None: ...
@deprecated("The `frontend.make_one_path_absolute` will be removed in Docutils 2.0 or later.")
def make_one_path_absolute(base_path: StrPath, path: StrPath) -> str: ...
def filter_settings_spec(settings_spec: _SettingsSpecTuple, *exclude: str, **replace: _OptionTuple) -> _SettingsSpecTuple: ...

# Storage for setting values; one attribute per setting.
# The attributes below are the settings of the core `OptionParser` (always present),
# and of the reStructuredText parser (present when it is used).
# Settings of other components are available via `optparse.Values.__getattr__()`.
class Values(optparse.Values):
    # Settings from `OptionParser.settings_spec` and `OptionParser.settings_defaults`
    _config_files: list[str]
    _destination: StrPath | None
    _disable_config: bool | None
    _source: StrPath | None
    auto_id_prefix: str
    config: str | None
    datestamp: str | None
    debug: bool | None
    dump_internals: bool | None
    dump_pseudo_xml: bool | None
    dump_settings: bool | None
    dump_transforms: bool | None
    error_encoding: str
    error_encoding_error_handler: str
    exit_status_level: int
    expose_internals: list[str] | None
    footnote_backlinks: bool
    generator: bool | None
    halt_level: int
    id_prefix: str
    input_encoding: str | None
    input_encoding_error_handler: str
    language_code: str
    output_encoding: str
    output_encoding_error_handler: str
    output_path: StrPath | None
    record_dependencies: DependencyList
    report_level: int
    root_prefix: str
    sectnum_xform: bool
    source_link: bool | None
    source_url: str | None
    strict_visitor: bool | None
    strip_classes: list[str] | None
    strip_comments: bool | None
    strip_elements_with_classes: list[str] | None
    title: str | None
    toc_backlinks: Literal["entry", "top", False]
    traceback: bool | None
    warning_stream: str | SupportsWrite[str] | None
    # Settings for the reStructuredText parser (`docutils.parsers.rst.Parser.settings_spec`)
    character_level_inline_markup: bool
    file_insertion_enabled: bool
    legacy_ids: bool
    line_length_limit: int
    pep_base_url: str
    pep_file_url_template: str
    pep_references: bool | None
    raw_enabled: bool
    rfc_base_url: str
    rfc_references: bool | None
    # Any string starting with "alt" (as in "alternative") are meaningful.
    # `apply()` catches AttributeError and sets it to False.
    smart_quotes: bool | str
    smartquotes_locales: list[tuple[str, Sequence[str]]] | None
    syntax_highlight: Literal["long", "short", "none"]
    tab_width: int
    trim_footnote_reference_space: bool | None
    validate: bool | None

    @deprecated("The `frontend.Values` class will be removed in Docutils 2.0 or later.")
    def __init__(self, defaults: Mapping[str, object] | None = None) -> None: ...
    def update(self, other_dict: Values | Mapping[str, object], option_parser: OptionParser) -> None: ...
    def copy(self) -> Values: ...
    # Returns the current or new value of an arbitrary setting.
    def setdefault(self, name: str, default: object) -> Any: ...

class Option(optparse.Option):
    ATTRS: list[str]
    validator: _OptionValidator
    overrides: str | None

    @deprecated("The `frontend.Option` class will be removed in Docutils 2.0 or later.")
    def __init__(self, *args: str | None, **kwargs: Unpack[_OptionKwargs]) -> None: ...

class OptionParser(optparse.OptionParser, SettingsSpec):
    standard_config_files: ClassVar[list[str]]
    threshold_choices: ClassVar[tuple[str, ...]]
    thresholds: ClassVar[dict[str, int]]
    booleans: ClassVar[dict[str, bool]]
    default_error_encoding: ClassVar[str]
    default_error_encoding_error_handler: ClassVar[str]
    config_section: ClassVar[str]
    version_template: ClassVar[str]
    details: str
    lists: dict[str, Literal[True]]
    config_files: list[str]
    relative_path_settings: ClassVar[tuple[str, ...]]
    version: str
    components: tuple[SettingsSpec, ...]

    @deprecated(
        "The `frontend.OptionParser` class will be replaced by a subclass of `argparse.ArgumentParser` in Docutils 2.0 or later."
    )
    def __init__(
        self,
        components: Iterable[SettingsSpec | type[SettingsSpec]] = (),
        defaults: Mapping[str, object] | None = None,
        read_config_files: bool | None = False,
        *args: Any,  # passed on to `optparse.OptionParser.__init__()`
        **kwargs: Any,
    ) -> None: ...
    def populate_from_components(self, components: Iterable[SettingsSpec]) -> None: ...
    @classmethod
    def get_standard_config_files(cls) -> Sequence[StrPath]: ...
    def get_standard_config_settings(self) -> Values: ...
    # `Any` for values of arbitrary settings
    def get_config_file_settings(self, config_file: str) -> dict[str, Any]: ...
    # Docutils itself commits this violation; not fixable in a stub.
    def check_values(self, values: Values, args: list[str]) -> Values: ...  # type: ignore[override]
    def check_args(self, args: list[str]) -> tuple[str | None, str | None]: ...
    def get_default_values(self) -> Values: ...
    def get_option_by_dest(self, dest: str) -> Option: ...

class ConfigParser(RawConfigParser):
    old_settings: ClassVar[dict[str, tuple[str, str]]]
    old_warning: ClassVar[str]
    not_utf8_error: ClassVar[str]

    @overload  # type: ignore[override]
    def read(self, filenames: str | Sequence[str]) -> list[str]: ...
    @overload
    @deprecated("The `option_parser` parameter is deprecated and will be removed in Docutils 0.24.")
    def read(self, filenames: str | Sequence[str], option_parser: OptionParser | None) -> list[str]: ...

    def handle_old_config(self, filename: str) -> None: ...
    def validate_settings(self, filename: str, option_parser: OptionParser) -> None: ...
    def optionxform(self, optionstr: str) -> str: ...

class ConfigDeprecationWarning(FutureWarning): ...

def get_default_settings(*components: SettingsSpec | type[SettingsSpec]) -> Values: ...
