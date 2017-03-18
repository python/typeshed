from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

from click.core import Context


def _unpack_args(
    args: Iterable[str], nargs_spec: Iterable[int]
) -> Tuple[Tuple[Optional[Tuple[str, ...]], ...], List[str]]:
    ...


def split_opt(opt: str) -> Tuple[str, str]:
    ...


def normalize_opt(opt: str, ctx: Context) -> str:
    ...


def split_arg_string(string: str) -> List[str]:
    ...


class Option:
    dest = ...  # type: str
    action = ...  # type: str
    nargs = ...  # type: int
    const = ...  # type: Any
    obj = ...  # type: Any
    prefixes = ...  # type: Set[str]
    _short_opts = ...  # type: List[str]
    _long_opts = ...  # type: List[str]
    # properties
    takes_value = ...  # type: bool

    def __init__(
        self,
        opts: Iterable[str],
        dest: str,
        action: str = None,
        nargs: int = 1,
        const: Any = None,
        obj: Any = None
    ) -> None:
        ...

    def process(self, value: Any, state: 'ParsingState') -> None:
        ...


class Argument:
    dest = ...  # type: str
    nargs = ...  # type: int
    obj = ...  # type: Any

    def __init__(self, dest: str, nargs: int = 1, obj: Any = None) -> None:
        ...

    def process(self, value: Any, state: 'ParsingState') -> None:
        ...


class ParsingState:
    opts = ...  # type: Dict[str, Any]
    largs = ...  # type: List[str]
    rargs = ...  # type: List[str]
    order = ...  # type: List[Any]

    def __init__(self, rargs: List[str]) -> None:
        ...


class OptionParser:
    ctx = ...  # type: Optional[Context]
    allow_interspersed_args = ...  # type: bool
    ignore_unknown_options = ...  # type: bool
    _short_opt = ...  # type: Dict[str, Option]
    _long_opt = ...  # type: Dict[str, Option]
    _opt_prefixes = ...  # type: Set[str]
    _args = ...  # type: List[Argument]

    def __init__(self, ctx: Context = None) -> None:
        ...

    def add_option(
        self,
        opts: Iterable[str],
        dest: str,
        action: str = None,
        nargs: int = 1,
        const: Any = None,
        obj: Any = None
    ) -> None:
        ...

    def add_argument(self, dest: str, nargs: int = 1, obj: Any = None) -> None:
        ...

    def parse_args(
        self, args: List[str]
    ) -> Tuple[Dict[str, Any], List[str], List[Any]]:
        ...
