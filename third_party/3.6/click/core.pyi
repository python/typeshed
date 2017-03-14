from contextlib import contextmanager
from typing import (
    Any,
    Callable,
    Dict,
    Generator,
    Iterable,
    List,
    Mapping,
    Optional,
    Sequence,
    Set,
    Tuple,
    TypeVar,
    Union,
)

from click.formatting import HelpFormatter
from click.parser import OptionParser


def invoke_param_callback(
    callback: Callable[['Context', 'Parameter', Optional[str]], Any],
    ctx: 'Context',
    param: 'Parameter',
    value: Optional[str]
) -> Any:
    ...


@contextmanager
def augment_usage_errors(
    ctx: 'Context', param: 'Parameter' = None
) -> Generator[None, None, None]:
    ...


def iter_params_for_processing(
    invocation_order: Sequence['Parameter'],
    declaration_order: Iterable['Parameter'],
) -> Iterable['Parameter']:
    ...


class Context:
    parent = ...  # type: Optional['Context']
    command = ...  # type: 'Command'
    info_name = ...  # type: Optional[str]
    params = ...  # type: Dict
    args = ...  # type: List[str]
    protected_args = ...  # type: List[str]
    obj = ...  # type: Any
    default_map = ...  # type: Mapping[str, Any]
    invoked_subcommand = ...  # type: Optional[str]
    terminal_width = ...  # type: Optional[int]
    max_content_width = ...  # type: Optional[int]
    allow_extra_args = ...  # type: bool
    allow_interspersed_args = ...  # type: bool
    ignore_unknown_options = ...  # type: bool
    help_option_names = ...  # type: List[str]
    token_normalize_func = ...  # type: Optional[Callable[[str], str]]
    resilient_parsing = ...  # type: bool
    auto_envvar_prefix = ...  # type: Optional[str]
    color = ...  # type: Optional[bool]
    _meta = ...  # type: Dict[str, Any]
    _close_callbacks = ...  # type: List
    _depth = ...  # type: int

    # properties
    meta = ...  # type: Dict[str, Any]
    command_path = ...  # type: str

    def __init__(
        self,
        command: 'Command',
        parent: 'Context' = None,
        info_name: str = None,
        obj: Any = None,
        auto_envvar_prefix: str = None,
        default_map: Mapping[str, Any] = None,
        terminal_width: int = None,
        max_content_width: int = None,
        resilient_parsing: bool = False,
        allow_extra_args: bool = None,
        allow_interspersed_args: bool = None,
        ignore_unknown_options: bool = None,
        help_option_names: List[str] = None,
        token_normalize_func: Callable[[str], str] = None,
        color: bool = None
    ) -> None:
        ...

    @contextmanager
    def scope(self, cleanup: bool = True) -> Generator['Context', None, None]:
        ...

    def make_formatter(self) -> HelpFormatter:
        ...

    def call_on_close(self, f: Callable) -> Callable:
        ...

    def close(self) -> None:
        ...

    def find_root(self) -> 'Context':
        ...

    def find_object(self, object_type: type) -> Any:
        ...

    def ensure_object(self, object_type: type) -> Any:
        ...

    def lookup_default(self, name: str) -> Any:
        ...

    def fail(self, message: str) -> None:
        ...

    def abort(self) -> None:
        ...

    def exit(self, code: Union[int, str] = 0) -> None:
        ...

    def get_usage(self) -> str:
        ...

    def get_help(self) -> str:
        ...

    def invoke(
        self, callback: Union['Command', Callable], *args, **kwargs
    ) -> Any:
        ...

    def forward(
        self, callback: Union['Command', Callable], *args, **kwargs
    ) -> Any:
        ...

class BaseCommand:
    allow_extra_args = ...  # type: bool
    allow_interspersed_args = ...  # type: bool
    ignore_unknown_options = ...  # type: bool
    name = ...  # type: str
    context_settings = ...  # type: Dict

    def __init__(self, name: str, context_settings: Dict = None) -> None:
        ...

    def get_usage(self, ctx: Context) -> str:
        ...

    def get_help(self, ctx: Context) -> str:
        ...

    def make_context(
        self, info_name: str, args: List[str], parent: Context = None, **extra
    ) -> Context:
        ...

    def parse_args(self, ctx: Context, args: List[str]) -> List[str]:
        ...

    def invoke(self, ctx: Context) -> Any:
        ...

    def main(
        self,
        args: List[str] = None,
        prog_name: str = None,
        complete_var: str = None,
        standalone_mode: bool = True,
        **extra
    ) -> Any:
        ...

    def __call__(self, *args, **kwargs) -> Any:
        ...


class Command(BaseCommand):
    callback = ...  # type: Optional[Callable]
    params = ...  # type: List['Parameter']
    help = ...  # type: Optional[str]
    epilog = ...  # type: Optional[str]
    short_help = ...  # type: Optional[str]
    options_metavar = ...  # type: str
    add_help_option = ...  # type: bool

    def __init__(
        self,
        name: str,
        context_settings: Dict = None,
        callback: Callable = None,
        params: List['Parameter'] = None,
        help: str = None,
        epilog: str = None,
        short_help: str = None,
        options_metavar: str = '[OPTIONS]',
        add_help_option: bool = True
    ) -> None:
        ...

    def get_params(self, ctx: Context) -> List['Parameter']:
        ...

    def format_usage(
        self,
        ctx: Context,
        formatter: HelpFormatter
    ) -> None:
        ...

    def collect_usage_pieces(self, ctx: Context) -> List[str]:
        ...

    def get_help_option_names(self, ctx: Context) -> Set[str]:
        ...

    def get_help_option(self, ctx: Context) -> Optional['Option']:
        ...

    def make_parser(self, ctx: Context) -> OptionParser:
        ...

    def format_help(self, ctx: Context, formatter: HelpFormatter) -> None:
        ...

    def format_help_text(self, ctx: Context, formatter: HelpFormatter) -> None:
        ...

    def format_options(self, ctx: Context, formatter: HelpFormatter) -> None:
        ...

    def format_epilog(self, ctx: Context, formatter: HelpFormatter) -> None:
        ...


_T = TypeVar('_T')
_Decorator = Callable[[_T], _T]


class MultiCommand(Command):
    no_args_is_help = ...  # type: bool
    invoke_without_command = ...  # type: bool
    subcommand_metavar = ...  # type: str
    chain = ...  # type: bool
    result_callback = ...  # type: Callable

    def __init__(
        self,
        name: str = None,
        invoke_without_command: bool = False,
        no_args_is_help: bool = None,
        subcommand_metavar: str = None,
        chain: bool = False,
        result_callback: Callable = None,
        **attrs
    ) -> None:
        ...

    def resultcallback(
        self, replace: bool = False
    ) -> _Decorator:
        ...

    def format_commands(self, ctx: Context, formatter: HelpFormatter) -> None:
        ...

    def resolve_command(
        self, ctx: Context, args: List[str]
    ) -> Tuple[str, Command, List[str]]:
        ...

    def get_command(self, ctx: Context, cmd_name: str) -> Optional[Command]:
        ...

    def list_commands(self, ctx: Context) -> Iterable[Command]:
        ...


class Group(MultiCommand):
    commands = ...  # type: Dict[str, Command]

    def __init__(
        self, name: str = None, commands: Dict[str, Command] = None, **attrs
    ) -> None:
        ...

    def add_command(self, cmd: Command, name: str = None):
        ...

    def command(self, *args, **kwargs) -> _Decorator:
        ...

    def group(self, *args, **kwargs) -> _Decorator:
        ...


class CommandCollection(MultiCommand):
    sources = ...  # type: List[MultiCommand]

    def __init__(
        self, name: str = None, sources: List[MultiCommand] = None, **attrs
    ) -> None:
        ...

    def add_source(self, multi_cmd: MultiCommand) -> None:
        ...


class Parameter:
    param_type_name = ...  # type: str
    name = ...  # type: str
    opts = ...  # type: List[str]
    secondary_opts = ...  # type: List[str]
    type = ...  # type: 'ParamType'
    required = ...  # type: bool
    callback = ...  # type: Optional[Callable[[Context, 'Parameter', str], Any]]
    nargs = ...  # type: int
    multiple = ...  # type: bool
    expose_value = ...  # type: bool
    default = ...  # type: Any
    is_eager = ...  # type: bool
    metavar = ...  # type: Optional[str]
    envvar = ...  # type: Union[str, List[str], None]
    # properties
    human_readable_name = ...  # type: str

    def __init__(
        self,
        param_decls: List[str] = None,
        type: Union[type, 'ParamType'] = None,
        required: bool = False,
        default: Any = None,
        callback: Callable[[Context, 'Parameter', str], Any] = None,
        nargs: int = None,
        metavar: str = None,
        expose_value: bool = True,
        is_eager: bool = False,
        envvar: Union[str, List[str]] = None
    ) -> None:
        ...

    def make_metavar(self) -> str:
        ...

    def get_default(self, ctx: Context) -> Any:
        ...

    def add_to_parser(self, parser: OptionParser, ctx: Context) -> None:
        ...

    def consume_value(self, ctx: Context, opts: Dict[str, Any]) -> Any:
        ...

    def type_cast_value(self, ctx: Context, value: Any) -> Any:
        ...

    def process_value(self, ctx: Context, value: Any) -> Any:
        ...

    def value_is_missing(self, value: Any) -> bool:
        ...

    def full_process_value(self, ctx: Context, value: Any) -> Any:
        ...

    def resolve_envvar_value(self, ctx: Context) -> str:
        ...

    def value_from_envvar(self, ctx: Context) -> Union[str, List[str]]:
        ...

    def handle_parse_result(
        self, ctx: Context, opts: Dict[str, Any], args: List[str]
    ) -> Tuple[Any, List[str]]:
        ...

    def get_help_record(self, ctx: Context) -> Tuple[str, str]:
        ...

    def get_usage_pieces(self, ctx: Context) -> List[str]:
        ...


class Option(Parameter):
    prompt = ...  # type: str  # sic
    confirmation_prompt = ...  # type: bool
    hide_input = ...  # type: bool
    is_flag = ...  # type: bool
    flag_value = ...  # type: Any
    is_bool_flag = ...  # type: bool
    count = ...  # type: bool
    multiple = ...  # type: bool
    allow_from_autoenv = ...  # type: bool
    help = ...  # type: Optional[str]
    show_default = ...  # type: bool

    def __init__(
        self,
        param_decls: List[str] = None,
        show_default: bool = False,
        prompt: Union[bool, str] = False,
        confirmation_prompt: bool = False,
        hide_input: bool = False,
        is_flag: bool = None,
        flag_value: Any = None,
        multiple: bool = False,
        count: bool = False,
        allow_from_autoenv: bool = True,
        type: Union[type, 'ParamType'] = None,
        help: str = None,
        **attrs
    ) -> None:
        ...

    def prompt_for_value(self, ctx: Context) -> Any:
        ...


class Argument(Parameter):
    def __init__(
        self,
        param_decls: List[str] = None,
        required: bool = None,
        **attrs
    ) -> None:
        ...

# cyclic dependency
from click.types import ParamType  # noqa: E402
