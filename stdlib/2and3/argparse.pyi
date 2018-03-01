# Stubs for argparse (Python 2.7 and 3.4)

from typing import (
    Any, Callable, Dict, Iterable, List, IO, NoReturn, Optional, Pattern,
    Sequence, Tuple, Type, Union, TypeVar, overload
)
import sys

_T = TypeVar('_T')
_ActionVar = TypeVar('_ActionVar', bound='Action')

if sys.version_info >= (3,):
    _Text = str
else:
    _Text = Union[str, unicode]

ONE_OR_MORE: str
OPTIONAL: str
PARSER: str
REMAINDER: str
SUPPRESS: str
ZERO_OR_MORE: str
_UNRECOGNIZED_ARGS_ATTR: str

class ArgumentError(Exception): ...

class _AttributeHolder:
    def _get_kwargs(self) -> List[Tuple[str, Any]]: ...
    def _get_args(self) -> List[Any]: ...

class _ActionsContainer:
    description: Optional[_Text]
    prefix_chars: _Text
    argument_default: Optional[_Text]
    conflict_handler: _Text

    _registries: Dict[_Text, Dict[Any, Any]]
    _actions: List[Action]
    _option_string_actions: Dict[_Text, Action]
    _action_groups: List[_ArgumentGroup]
    _mutually_exclusive_groups: List[_MutuallyExclusiveGroup]
    _defaults: Dict[str, Any]
    _negative_number_matcher: Pattern[str]
    _has_negative_number_optionals: List[bool]

    def __init__(self, description: Optional[_Text], prefix_chars: _Text,
                 argument_default: Optional[_Text], conflict_handler: _Text) -> None: ...
    def register(self, registry_name: _Text, value: Any, object: Any) -> None: ...
    def _registry_get(self, registry_name: _Text, value: Any, default: Any = ...) -> Any: ...
    def set_defaults(self, **kwargs: Any) -> None: ...
    def get_default(self, dest: _Text) -> Any: ...
    def add_argument(self, *args: Any, **kwargs: Any) -> Action: ...
    def add_argument_group(self, *args: Any, **kwargs: Any) -> _ArgumentGroup: ...
    def add_mutually_exclusive_group(self, **kwargs: Any) -> _MutuallyExclusiveGroup: ...
    def _add_action(self, action: _ActionVar) -> _ActionVar: ...
    def _remove_action(self, action: Action) -> None: ...
    def _add_container_actions(self, container: _ActionsContainer) -> None: ...
    def _get_positional_kwargs(self, dest: _Text, **kwargs: Any) -> Dict[str, Any]: ...
    def _get_optional_kwargs(self, *args: Any, **kwargs: Any) -> Dict[str, Any]: ...
    def _pop_action_class(self, kwargs: Any, default: Optional[Type[Action]] = ...) -> Type[Action]: ...
    def _get_handler(self) -> Callable[[Action, Iterable[Tuple[_Text, Action]]], Any]: ...
    def _check_conflict(self, action: Action) -> None: ...
    def _handle_conflict_error(self, action: Action, conflicting_actions: Iterable[Tuple[_Text, Action]]) -> NoReturn: ...
    def _handle_conflict_resolve(self, action: Action, conflicting_actions: Iterable[Tuple[_Text, Action]]) -> None: ...

class ArgumentParser(_AttributeHolder, _ActionsContainer):
    prog: _Text
    usage: Optional[_Text]
    epilog: Optional[_Text]
    formatter_class: Type[HelpFormatter]
    fromfile_prefix_chars: Optional[_Text]
    add_help: bool

    if sys.version_info >= (3, 5):
        allow_abbrev: bool

    if sys.version_info >= (3, 5):
        def __init__(self,
                     prog: Optional[str] = ...,
                     usage: Optional[str] = ...,
                     description: Optional[str] = ...,
                     epilog: Optional[str] = ...,
                     parents: Sequence[ArgumentParser] = ...,
                     formatter_class: Type[HelpFormatter] = ...,
                     prefix_chars: _Text = ...,
                     fromfile_prefix_chars: Optional[str] = ...,
                     argument_default: Optional[str] = ...,
                     conflict_handler: _Text = ...,
                     add_help: bool = ...,
                     allow_abbrev: bool = ...) -> None: ...
    else:
        def __init__(self,
                     prog: Optional[_Text] = ...,
                     usage: Optional[_Text] = ...,
                     description: Optional[_Text] = ...,
                     epilog: Optional[_Text] = ...,
                     parents: Sequence[ArgumentParser] = ...,
                     formatter_class: Type[HelpFormatter] = ...,
                     prefix_chars: _Text = ...,
                     fromfile_prefix_chars: Optional[_Text] = ...,
                     argument_default: Optional[_Text] = ...,
                     conflict_handler: _Text = ...,
                     add_help: bool = ...) -> None: ...
    def parse_args(self, args: Optional[Sequence[_Text]] = ...,
                   namespace: Optional[Namespace] = ...) -> Namespace: ...
    def add_subparsers(self, title: _Text = ...,
                       description: Optional[_Text] = ...,
                       prog: _Text = ...,
                       parser_class: Type[ArgumentParser] = ...,
                       action: Type[Action] = ...,
                       option_string: _Text = ...,
                       dest: Optional[_Text] = ...,
                       help: Optional[_Text] = ...,
                       metavar: Optional[_Text] = ...) -> _SubParsersAction: ...
    def print_usage(self, file: Optional[IO[str]] = ...) -> None: ...
    def print_help(self, file: Optional[IO[str]] = ...) -> None: ...
    def format_usage(self) -> str: ...
    def format_help(self) -> str: ...
    def parse_known_args(self, args: Optional[Sequence[_Text]] = ...,
                         namespace: Optional[Namespace] = ...) -> Tuple[Namespace, List[str]]: ...
    def convert_arg_line_to_args(self, arg_line: _Text) -> List[str]: ...
    def exit(self, status: int = ..., message: Optional[_Text] = ...) -> None: ...
    def error(self, message: _Text) -> None: ...

class HelpFormatter:
    # not documented
    def __init__(self, prog: _Text, indent_increment: int = ...,
                 max_help_position: int = ...,
                 width: Optional[int] = ...) -> None: ...
class RawDescriptionHelpFormatter(HelpFormatter): ...
class RawTextHelpFormatter(HelpFormatter): ...
class ArgumentDefaultsHelpFormatter(HelpFormatter): ...
if sys.version_info >= (3,):
    class MetavarTypeHelpFormatter(HelpFormatter): ...

class Action(_AttributeHolder):
    option_strings: Sequence[_Text]
    dest: _Text
    nargs: Optional[Union[int, _Text]]
    const: Any
    default: Any
    type: Optional[Union[Callable[[str], Any], FileType]]
    choices: Optional[Iterable[Any]]
    required: bool
    help: Optional[_Text]
    metavar: Optional[Union[_Text, Tuple[_Text, ...]]]
    def __init__(self,
                 option_strings: Sequence[_Text],
                 dest: _Text,
                 nargs: Optional[Union[int, _Text]] = ...,
                 const: Any = ...,
                 default: Any = ...,
                 type: Optional[Union[Callable[[str], _T], FileType]] = ...,
                 choices: Optional[Iterable[_T]] = ...,
                 required: bool = ...,
                 help: Optional[_Text] = ...,
                 metavar: Optional[Union[_Text, Tuple[_Text, ...]]] = ...) -> None: ...
    def __call__(self, parser: ArgumentParser, namespace: Namespace,
                 values: Union[_Text, Sequence[Any], None],
                 option_string: Optional[_Text] = ...) -> None: ...

class Namespace(_AttributeHolder):
    def __init__(self, **kwargs: Any) -> None: ...
    def __getattr__(self, name: _Text) -> Any: ...
    def __setattr__(self, name: _Text, value: Any) -> None: ...
    def __contains__(self, key: str) -> bool: ...

class FileType:
    if sys.version_info >= (3, 4):
        def __init__(self, mode: _Text = ..., bufsize: int = ...,
                     encoding: Optional[_Text] = ...,
                     errors: Optional[_Text] = ...) -> None: ...
    elif sys.version_info >= (3,):
        def __init__(self,
                     mode: _Text = ..., bufsize: int = ...) -> None: ...
    else:
        def __init__(self,
                     mode: _Text = ..., bufsize: Optional[int] = ...) -> None: ...
    def __call__(self, string: _Text) -> IO[Any]: ...

class _ArgumentGroup(_ActionsContainer):
    def __init__(self, container: _ActionsContainer,
                 title: Optional[_Text] = ...,
                 description: Optional[_Text] = ..., **kwargs: Any) -> None: ...

class _MutuallyExclusiveGroup(_ArgumentGroup): ...

class _StoreAction(Action): ...

class _StoreConstAction(Action):
    def __init__(self,
                 option_strings: Sequence[_Text],
                 dest: _Text,
                 const: Any,
                 default: Any = ...,
                 required: bool = ...,
                 help: Optional[_Text] = ...,
                 metavar: Optional[Union[_Text, Tuple[_Text, ...]]] = ...) -> None: ...

class _StoreTrueAction(_StoreConstAction):
    def __init__(self,
                 option_strings: Sequence[_Text],
                 dest: _Text,
                 default: bool = ...,
                 required: bool = ...,
                 help: Optional[_Text] = ...) -> None: ...

class _StoreFalseAction(_StoreConstAction):
    def __init__(self,
                 option_strings: Sequence[_Text],
                 dest: _Text,
                 default: bool = ...,
                 required: bool = ...,
                 help: Optional[_Text] = ...) -> None: ...

class _AppendAction(Action): ...

class _AppendConstAction(Action):
    def __init__(self,
                 option_strings: Sequence[_Text],
                 dest: _Text,
                 const: Any,
                 default: Any = ...,
                 required: bool = ...,
                 help: Optional[_Text] = ...,
                 metavar: Optional[Union[_Text, Tuple[_Text, ...]]] = ...) -> None: ...

class _CountAction(Action):
    def __init__(self,
                 option_strings: Sequence[_Text],
                 dest: _Text,
                 default: Any = ...,
                 required: bool = ...,
                 help: Optional[_Text] = ...) -> None: ...

class _HelpAction(Action):
    def __init__(self,
                 option_strings: Sequence[_Text],
                 dest: _Text = ...,
                 default: _Text = ...,
                 help: Optional[_Text] = ...) -> None: ...

class _VersionAction(Action):
    def __init__(self,
                 option_strings: Sequence[_Text],
                 version: Optional[_Text] = ...,
                 dest: _Text = ...,
                 default: _Text = ...,
                 help: _Text = ...) -> None: ...

class _SubParsersAction(Action):
    # TODO: Type keyword args properly.
    def add_parser(self, name: _Text, **kwargs: Any) -> ArgumentParser: ...

# not documented
class ArgumentTypeError(Exception): ...

if sys.version_info <= (3, 6):
    def _ensure_value(namespace: Namespace, name: _Text, value: Any) -> Any: ...

def _get_action_name(argument: Optional[Action]) -> Optional[str]: ...
