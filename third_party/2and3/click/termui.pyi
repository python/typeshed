from contextlib import contextmanager
from typing import (
    Any,
    Callable,
    Generator,
    Iterable,
    IO,
    List,
    Optional,
    Tuple,
    TypeVar,
)


def hidden_prompt_func(prompt: str) -> str:
    ...


def _build_prompt(
    text: str,
    suffix: str,
    show_default: bool = ...,
    default: Optional[str] = None,
) -> str:
    ...


def prompt(
    text: str,
    default: Optional[str] = None,
    hide_input: bool = ...,
    confirmation_prompt: bool = ...,
    type: Optional[Any] = None,
    value_proc: Optional[Callable[[Optional[str]], Any]] = None,
    prompt_suffix: str = ...,
    show_default: bool = ...,
    err: bool = ...,
) -> Any:
    ...


def confirm(
    text: str,
    default: bool = ...,
    abort: bool = ...,
    prompt_suffix: str = ...,
    show_default: bool = ...,
    err: bool = ...,
) -> bool:
    ...


def get_terminal_size() -> Tuple[int, int]:
    ...


def echo_via_pager(text: str, color: Optional[bool] = None) -> None:
    ...


_T = TypeVar('_T')


@contextmanager
def progressbar(
    iterable: Optional[Iterable[_T]] = None,
    length: Optional[int] = None,
    label: Optional[str] = None,
    show_eta: bool = ...,
    show_percent: Optional[bool] = None,
    show_pos: bool = ...,
    item_show_func: Optional[Callable[[_T], str]] = None,
    fill_char: str = ...,
    empty_char: str = ...,
    bar_template: str = ...,
    info_sep: str = ...,
    width: int = ...,
    file: Optional[IO] = None,
    color: Optional[bool] = None,
) -> Generator[_T, None, None]:
    ...


def clear() -> None:
    ...


def style(
    text: str,
    fg: Optional[str] = None,
    bg: Optional[str] = None,
    bold: Optional[bool] = None,
    dim: Optional[bool] = None,
    underline: Optional[bool] = None,
    blink: Optional[bool] = None,
    reverse: Optional[bool] = None,
    reset: bool = ...,
):
    ...


def unstyle(text: str) -> str:
    ...


# Styling options copied from style() for nicer type checking.
def secho(
    text: str,
    file: Optional[IO] = None,
    nl: bool =True,
    err: bool = ...,
    color: Optional[bool] = None,
    fg: Optional[str] = None,
    bg: Optional[str] = None,
    bold: Optional[bool] = None,
    dim: Optional[bool] = None,
    underline: Optional[bool] = None,
    blink: Optional[bool] = None,
    reverse: Optional[bool] = None,
    reset: bool = ...,
):
    ...


def edit(
    text: Optional[str] = None,
    editor: Optional[str] = None,
    env: Optional[str] = None,
    require_save: bool = ...,
    extension: str = ...,
    filename: Optional[str] = None,
) -> str:
    ...


def launch(url: str, wait: bool = ..., locate: bool = ...) -> int:
    ...


def getchar(echo: bool = ...) -> str:
    ...


def pause(
    info: str ='Press any key to continue ...', err: bool = ...
) -> None:
    ...
