import builtins
from _typeshed import Incomplete, MaybeNone, SupportsWrite
from abc import abstractmethod
from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import Any, ClassVar, Literal, NoReturn, overload
from typing_extensions import Self

__all__ = [
    "Option",
    "make_option",
    "SUPPRESS_HELP",
    "SUPPRESS_USAGE",
    "Values",
    "OptionContainer",
    "OptionGroup",
    "OptionParser",
    "HelpFormatter",
    "IndentedHelpFormatter",
    "TitledHelpFormatter",
    "OptParseError",
    "OptionError",
    "OptionConflictError",
    "OptionValueError",
    "BadOptionError",
    "check_choice",
]

NO_DEFAULT: tuple[str, ...]
SUPPRESS_HELP: str
SUPPRESS_USAGE: str

# Can return complex, float, or int depending on the option's type
def check_builtin(option: Option, opt: str, value: str) -> complex: ...
def check_choice(option: Option, opt: str, value: str) -> str: ...

class OptParseError(Exception):
    msg: str
    def __init__(self, msg: str) -> None: ...

class BadOptionError(OptParseError):
    opt_str: str
    def __init__(self, opt_str: str) -> None: ...

class AmbiguousOptionError(BadOptionError):
    possibilities: Iterable[str]
    def __init__(self, opt_str: str, possibilities: Sequence[str]) -> None: ...

class OptionError(OptParseError):
    option_id: str
    def __init__(self, msg: str, option: Option) -> None: ...

class OptionConflictError(OptionError): ...
class OptionValueError(OptParseError): ...

class HelpFormatter:
    NO_DEFAULT_VALUE: str
    _long_opt_fmt: str
    _short_opt_fmt: str
    current_indent: int
    default_tag: str
    help_position: int
    help_width: int | MaybeNone  # initialized as None and computed later as int when storing option strings
    indent_increment: int
    level: int
    max_help_position: int
    option_strings: dict[Option, str]
    parser: OptionParser
    short_first: bool | Literal[0, 1]
    width: int
    def __init__(
        self, indent_increment: int, max_help_position: int, width: int | None, short_first: bool | Literal[0, 1]
    ) -> None: ...
    def dedent(self) -> None: ...
    def expand_default(self, option: Option) -> str: ...
    def format_description(self, description: str | None) -> str: ...
    def format_epilog(self, epilog: str | None) -> str: ...
    @abstractmethod
    def format_heading(self, heading: str) -> str: ...
    def format_option(self, option: Option) -> str: ...
    def format_option_strings(self, option: Option) -> str: ...
    @abstractmethod
    def format_usage(self, usage: str) -> str: ...
    def indent(self) -> None: ...
    def set_long_opt_delimiter(self, delim: str) -> None: ...
    def set_parser(self, parser: OptionParser) -> None: ...
    def set_short_opt_delimiter(self, delim: str) -> None: ...
    def store_option_strings(self, parser: OptionParser) -> None: ...

class IndentedHelpFormatter(HelpFormatter):
    def __init__(
        self,
        indent_increment: int = 2,
        max_help_position: int = 24,
        width: int | None = None,
        short_first: bool | Literal[0, 1] = 1,
    ) -> None: ...
    def format_heading(self, heading: str) -> str: ...
    def format_usage(self, usage: str) -> str: ...

class TitledHelpFormatter(HelpFormatter):
    def __init__(
        self,
        indent_increment: int = 0,
        max_help_position: int = 24,
        width: int | None = None,
        short_first: bool | Literal[0, 1] = 0,
    ) -> None: ...
    def format_heading(self, heading: str) -> str: ...
    def format_usage(self, usage: str) -> str: ...

class Option:
    ACTIONS: tuple[str, ...]
    ALWAYS_TYPED_ACTIONS: tuple[str, ...]
    ATTRS: list[str]
    CHECK_METHODS: list[Callable[[Self], object]] | None
    CONST_ACTIONS: tuple[str, ...]
    STORE_ACTIONS: tuple[str, ...]
    TYPED_ACTIONS: tuple[str, ...]
    TYPES: tuple[str, ...]
    TYPE_CHECKER: dict[str, Callable[[Option, str, str], Any]]
    _long_opts: list[str]
    _short_opts: list[str]
    action: str
    type: str | None
    dest: str | None
    default: Any
    nargs: int
    const: Any | None
    choices: list[str] | tuple[str, ...] | None
    callback: Callable[..., Incomplete] | None
    callback_args: tuple[Incomplete, ...] | None
    callback_kwargs: dict[str, Incomplete] | None
    help: str | None
    metavar: str | None
    def __init__(
        self,
        *opts: str | None,
        # The following keywords are handled by the _set_attrs method. All default to
        # `None` except for `default`, which defaults to `NO_DEFAULT`.
        action: str | None = None,
        type: str | builtins.type | None = None,
        dest: str | None = None,
        default: Any = ...,  # = NO_DEFAULT
        nargs: int | None = None,
        const: Any | None = None,
        choices: list[str] | tuple[str, ...] | None = None,
        # TODO: callback, callback_args, callback_kwargs must be all supplied or all omitted. Add overloads.
        # Revisit if ParamSpec is ever changed to support non-unpacked args and kwargs.
        callback: Callable[..., Incomplete] | None = None,
        callback_args: tuple[Incomplete, ...] | None = None,
        callback_kwargs: dict[str, Incomplete] | None = None,
        help: str | None = None,
        metavar: str | None = None,
    ) -> None: ...
    def _check_action(self) -> None: ...
    def _check_callback(self) -> None: ...
    def _check_choice(self) -> None: ...
    def _check_const(self) -> None: ...
    def _check_dest(self) -> None: ...
    def _check_nargs(self) -> None: ...
    def _check_opt_strings(self, opts: Iterable[str | None]) -> list[str]: ...
    def _check_type(self) -> None: ...
    def _set_attrs(self, attrs: dict[str, Incomplete]) -> None: ...
    def _set_opt_strings(self, opts: Iterable[str]) -> None: ...
    def check_value(self, opt: str, value: str) -> Any: ...
    def convert_value(self, opt: str, value: str | tuple[str, ...] | None) -> Any: ...
    def get_opt_string(self) -> str: ...
    def process(self, opt: str, value: str | tuple[str, ...] | None, values: Values, parser: OptionParser) -> int: ...
    def take_action(self, action: str, dest: str, opt: str, value: Any, values: Values, parser: OptionParser) -> int: ...
    def takes_value(self) -> bool: ...

make_option = Option

class OptionContainer:
    _long_opt: dict[str, Option]
    _short_opt: dict[str, Option]
    conflict_handler: str
    defaults: dict[str, Incomplete]
    description: str | None
    option_class: type[Option]
    def __init__(
        self, option_class: type[Option], conflict_handler: Literal["error", "resolve"], description: str | None
    ) -> None: ...
    def _check_conflict(self, option: Option) -> None: ...
    def _create_option_mappings(self) -> None: ...
    def _share_option_mappings(self, parser: OptionParser) -> None: ...
    @overload
    def add_option(self, opt: Option, /) -> Option: ...
    @overload
    def add_option(self, arg: str, /, *args: str | None, **kwargs) -> Option: ...
    def add_options(self, option_list: Iterable[Option]) -> None: ...
    def destroy(self) -> None: ...
    def format_option_help(self, formatter: HelpFormatter) -> str: ...
    def format_description(self, formatter: HelpFormatter) -> str: ...
    def format_help(self, formatter: HelpFormatter) -> str: ...
    def get_description(self) -> str | None: ...
    def get_option(self, opt_str: str) -> Option | None: ...
    def has_option(self, opt_str: str) -> bool: ...
    def remove_option(self, opt_str: str) -> None: ...
    def set_conflict_handler(self, handler: Literal["error", "resolve"]) -> None: ...
    def set_description(self, description: str | None) -> None: ...

class OptionGroup(OptionContainer):
    option_list: list[Option]
    parser: OptionParser
    title: str
    def __init__(self, parser: OptionParser, title: str, description: str | None = None) -> None: ...
    def _create_option_list(self) -> None: ...
    def set_title(self, title: str) -> None: ...

class Values:
    def __init__(self, defaults: Mapping[str, Incomplete] | None = None) -> None: ...
    def _update(self, dict: Mapping[str, Incomplete], mode) -> None: ...
    def _update_careful(self, dict: Mapping[str, Incomplete]) -> None: ...
    def _update_loose(self, dict: Mapping[str, Incomplete]) -> None: ...
    def ensure_value(self, attr: str, value): ...
    def read_file(self, filename: str, mode: str = "careful") -> None: ...
    def read_module(self, modname: str, mode: str = "careful") -> None: ...
    __hash__: ClassVar[None]  # type: ignore[assignment]
    # __getattr__ doesn't exist, but anything passed as a default to __init__
    # is set on the instance.
    def __getattr__(self, name: str): ...
    def __setattr__(self, name: str, value, /) -> None: ...
    def __eq__(self, other: object) -> bool: ...

class OptionParser(OptionContainer):
    allow_interspersed_args: bool
    epilog: str | None
    formatter: HelpFormatter
    largs: list[str] | None
    option_groups: list[OptionGroup]
    option_list: list[Option]
    process_default_values: bool
    prog: str | None
    rargs: list[str] | None
    standard_option_list: list[Option]
    usage: str | None
    values: Values | None
    version: str
    def __init__(
        self,
        usage: str | None = None,
        option_list: Iterable[Option] | None = None,
        option_class: type[Option] = ...,
        version: str | None = None,
        conflict_handler: str = "error",
        description: str | None = None,
        formatter: HelpFormatter | None = None,
        add_help_option: bool = True,
        prog: str | None = None,
        epilog: str | None = None,
    ) -> None: ...
    def _add_help_option(self) -> None: ...
    def _add_version_option(self) -> None: ...
    def _create_option_list(self) -> None: ...
    def _get_all_options(self) -> list[Option]: ...
    def _get_args(self, args: list[str] | None) -> list[str]: ...
    def _init_parsing_state(self) -> None: ...
    def _match_long_opt(self, opt: str) -> str: ...
    def _populate_option_list(self, option_list: Iterable[Option] | None, add_help: bool = True) -> None: ...
    def _process_args(self, largs: list[str], rargs: list[str], values: Values) -> None: ...
    def _process_long_opt(self, rargs: list[str], values: Values) -> None: ...
    def _process_short_opts(self, rargs: list[str], values: Values) -> None: ...
    @overload
    def add_option_group(self, opt_group: OptionGroup, /) -> OptionGroup: ...
    @overload
    def add_option_group(self, title: str, /, description: str | None = None) -> OptionGroup: ...
    def check_values(self, values: Values, args: list[str]) -> tuple[Values, list[str]]: ...
    def disable_interspersed_args(self) -> None: ...
    def enable_interspersed_args(self) -> None: ...
    def error(self, msg: str) -> NoReturn: ...
    def exit(self, status: int = 0, msg: str | None = None) -> NoReturn: ...
    def expand_prog_name(self, s: str) -> str: ...
    def format_epilog(self, formatter: HelpFormatter) -> str: ...
    def format_help(self, formatter: HelpFormatter | None = None) -> str: ...
    def format_option_help(self, formatter: HelpFormatter | None = None) -> str: ...
    def get_default_values(self) -> Values: ...
    def get_option_group(self, opt_str: str) -> OptionGroup | None: ...
    def get_prog_name(self) -> str: ...
    def get_usage(self) -> str: ...
    def get_version(self) -> str: ...
    def parse_args(self, args: list[str] | None = None, values: Values | None = None) -> tuple[Values, list[str]]: ...
    def print_usage(self, file: SupportsWrite[str] | None = None) -> None: ...
    def print_help(self, file: SupportsWrite[str] | None = None) -> None: ...
    def print_version(self, file: SupportsWrite[str] | None = None) -> None: ...
    def set_default(self, dest: str, value: Any) -> None: ...  # default value can be "any" type
    def set_defaults(self, **kwargs: Any) -> None: ...  # default values can be "any" type
    def set_process_default_values(self, process: bool) -> None: ...
    def set_usage(self, usage: str | None) -> None: ...
