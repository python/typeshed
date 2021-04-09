import optparse
from configparser import RawConfigParser
from typing import Any, ClassVar, Optional

from docutils import SettingsSpec
from docutils.utils import DependencyList

__docformat__: str

def store_multiple(option, opt, value, parser, *args, **kwargs) -> None: ...
def read_config_file(option, opt, value, parser) -> None: ...
def validate_encoding(setting, value, option_parser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...): ...
def validate_encoding_error_handler(
    setting, value, option_parser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...
): ...
def validate_encoding_and_error_handler(
    setting, value, option_parser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...
): ...
def validate_boolean(
    setting, value, option_parser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...
) -> bool: ...
def validate_nonnegative_int(
    setting, value, option_parser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...
) -> int: ...
def validate_threshold(
    setting, value, option_parser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...
) -> int: ...
def validate_colon_separated_string_list(
    setting, value, option_parser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...
) -> list[str]: ...
def validate_comma_separated_list(
    setting, value, option_parser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...
) -> list[str]: ...
def validate_url_trailing_slash(
    setting, value, option_parser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...
) -> str: ...
def validate_dependency_file(
    setting, value, option_parser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...
) -> DependencyList: ...
def validate_strip_class(
    setting, value, option_parser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...
): ...
def validate_smartquotes_locales(
    setting, value, option_parser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...
) -> list[tuple[str, str]]: ...
def make_paths_absolute(pathdict, keys, base_path: Optional[Any] = ...) -> None: ...
def make_one_path_absolute(base_path, path) -> str: ...
def filter_settings_spec(settings_spec, *exclude, **replace) -> tuple[Any, ...]: ...

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
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class ConfigParser(RawConfigParser):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class ConfigDeprecationWarning(DeprecationWarning): ...
