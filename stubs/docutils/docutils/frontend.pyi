import optparse
from configparser import RawConfigParser
from typing import Any, ClassVar, Tuple, Type
from collections.abc import Iterable, Mapping

from docutils import SettingsSpec
from docutils.parsers import Parser
from docutils.utils import DependencyList

__docformat__: str

def store_multiple(option, opt, value, parser, *args, **kwargs) -> None: ...
def read_config_file(option, opt, value, parser) -> None: ...
def validate_encoding(setting, value, option_parser, config_parser: Any | None = ..., config_section: Any | None = ...): ...
def validate_encoding_error_handler(
    setting, value, option_parser, config_parser: Any | None = ..., config_section: Any | None = ...
): ...
def validate_encoding_and_error_handler(
    setting, value, option_parser, config_parser: Any | None = ..., config_section: Any | None = ...
): ...
def validate_boolean(
    setting, value, option_parser, config_parser: Any | None = ..., config_section: Any | None = ...
) -> bool: ...
def validate_nonnegative_int(
    setting, value, option_parser, config_parser: Any | None = ..., config_section: Any | None = ...
) -> int: ...
def validate_threshold(
    setting, value, option_parser, config_parser: Any | None = ..., config_section: Any | None = ...
) -> int: ...
def validate_colon_separated_string_list(
    setting, value, option_parser, config_parser: Any | None = ..., config_section: Any | None = ...
) -> list[str]: ...
def validate_comma_separated_list(
    setting, value, option_parser, config_parser: Any | None = ..., config_section: Any | None = ...
) -> list[str]: ...
def validate_url_trailing_slash(
    setting, value, option_parser, config_parser: Any | None = ..., config_section: Any | None = ...
) -> str: ...
def validate_dependency_file(
    setting, value, option_parser, config_parser: Any | None = ..., config_section: Any | None = ...
) -> DependencyList: ...
def validate_strip_class(setting, value, option_parser, config_parser: Any | None = ..., config_section: Any | None = ...): ...
def validate_smartquotes_locales(
    setting, value, option_parser, config_parser: Any | None = ..., config_section: Any | None = ...
) -> list[tuple[str, str]]: ...
def make_paths_absolute(pathdict, keys, base_path: Any | None = ...) -> None: ...
def make_one_path_absolute(base_path, path) -> str: ...
def filter_settings_spec(settings_spec, *exclude, **replace) -> Tuple[Any, ...]: ...

class Values(optparse.Values):
    def update(self, other_dict, option_parser) -> None: ...
    def copy(self) -> Values: ...

class Option(optparse.Option): ...

class OptionParser(optparse.OptionParser, SettingsSpec):
    standard_config_files: ClassVar[list[str]]
    threshold_choices: ClassVar[list[str]]
    thresholds: ClassVar[dict[str, int]]
    booleans: ClassVar[dict[str, bool]]
    default_error_encoding: ClassVar[str]
    default_error_encoding_error_handler: ClassVar[str]
    config_section: ClassVar[str]
    version_template: ClassVar[str]
    def __init__(
        self,
        components: Iterable[Type[Parser]] = ...,
        defaults: Mapping[str, object] = ...,
        read_config_files: bool | None = ...,
        *args,
        **kwargs,
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class ConfigParser(RawConfigParser):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class ConfigDeprecationWarning(DeprecationWarning): ...
