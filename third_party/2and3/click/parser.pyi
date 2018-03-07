from typing import Any, Dict, Iterable, List, Optional, Set, Text, Tuple

from click.core import Context


def _unpack_args(
    args: Iterable[Text], nargs_spec: Iterable[int]
) -> Tuple[Tuple[Optional[Tuple[Text, ...]], ...], List[Text]]:
    ...


def split_opt(opt: Text) -> Tuple[Text, Text]:
    ...


def normalize_opt(opt: Text, ctx: Context) -> Text:
    ...


def split_arg_Texting(Texting: Text) -> List[Text]:
    ...


class Option:
    dest: Text
    action: Text
    nargs: int
    const: Any
    obj: Any
    prefixes: Set[Text]
    _short_opts: List[Text]
    _long_opts: List[Text]
    # properties
    takes_value: bool

    def __init__(
        self,
        opts: Iterable[Text],
        dest: Text,
        action: Optional[Text] = ...,
        nargs: int = ...,
        const: Optional[Any] = ...,
        obj: Optional[Any] = ...
    ) -> None:
        ...

    def process(self, value: Any, state: 'ParsingState') -> None:
        ...


class Argument:
    dest: Text
    nargs: int
    obj: Any

    def __init__(self, dest: Text, nargs: int = ..., obj: Optional[Any] = ...) -> None:
        ...

    def process(self, value: Any, state: 'ParsingState') -> None:
        ...


class ParsingState:
    opts: Dict[Text, Any]
    largs: List[Text]
    rargs: List[Text]
    order: List[Any]

    def __init__(self, rargs: List[Text]) -> None:
        ...


class OptionParser:
    ctx: Optional[Context]
    allow_interspersed_args: bool
    ignore_unknown_options: bool
    _short_opt: Dict[Text, Option]
    _long_opt: Dict[Text, Option]
    _opt_prefixes: Set[Text]
    _args: List[Argument]

    def __init__(self, ctx: Optional[Context] = ...) -> None:
        ...

    def add_option(
        self,
        opts: Iterable[Text],
        dest: Text,
        action: Optional[Text] = ...,
        nargs: int = ...,
        const: Optional[Any] = ...,
        obj: Optional[Any] = ...
    ) -> None:
        ...

    def add_argument(self, dest: Text, nargs: int = ..., obj: Optional[Any] = ...) -> None:
        ...

    def parse_args(
        self, args: List[Text]
    ) -> Tuple[Dict[Text, Any], List[Text], List[Any]]:
        ...
