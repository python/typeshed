from contextlib import contextmanager
from typing import (
    Any,
    Callable,
    Generator,
    Iterable,
    IO,
    List,
    Optional,
    Text,
    Tuple,
    TypeVar,
)


def hidden_prompt_func(prompt: Text) -> Text:
    ...


def _build_prompt(
    text: Text,
    suffix: Text,
    show_default: bool = ...,
    default: Optional[Text] = ...,
) -> Text:
    ...


def prompt(
    text: Text,
    default: Optional[Text] = ...,
    hide_input: bool = ...,
    confirmation_prompt: bool = ...,
    type: Optional[Any] = ...,
    value_proc: Optional[Callable[[Optional[Text]], Any]] = ...,
    prompt_suffix: Text = ...,
    show_default: bool = ...,
    err: bool = ...,
) -> Any:
    ...


def confirm(
    text: Text,
    default: bool = ...,
    abort: bool = ...,
    prompt_suffix: Text = ...,
    show_default: bool = ...,
    err: bool = ...,
) -> bool:
    ...


def get_terminal_size() -> Tuple[int, int]:
    ...


def echo_via_pager(text: Text, color: Optional[bool] = ...) -> None:
    ...


_T = TypeVar('_T')


@contextmanager
def progressbar(
    iterable: Optional[Iterable[_T]] = ...,
    length: Optional[int] = ...,
    label: Optional[Text] = ...,
    show_eta: bool = ...,
    show_percent: Optional[bool] = ...,
    show_pos: bool = ...,
    item_show_func: Optional[Callable[[_T], Text]] = ...,
    fill_char: Text = ...,
    empty_char: Text = ...,
    bar_template: Text = ...,
    info_sep: Text = ...,
    width: int = ...,
    file: Optional[IO] = ...,
    color: Optional[bool] = ...,
) -> Generator[_T, None, None]:
    ...


def clear() -> None:
    ...


def style(
    text: Text,
    fg: Optional[Text] = ...,
    bg: Optional[Text] = ...,
    bold: Optional[bool] = ...,
    dim: Optional[bool] = ...,
    underline: Optional[bool] = ...,
    blink: Optional[bool] = ...,
    reverse: Optional[bool] = ...,
    reset: bool = ...,
):
    ...


def unstyle(text: Text) -> Text:
    ...


# Styling options copied from style() for nicer type checking.
def secho(
    text: Text,
    file: Optional[IO] = ...,
    nl: bool = ...,
    err: bool = ...,
    color: Optional[bool] = ...,
    fg: Optional[Text] = ...,
    bg: Optional[Text] = ...,
    bold: Optional[bool] = ...,
    dim: Optional[bool] = ...,
    underline: Optional[bool] = ...,
    blink: Optional[bool] = ...,
    reverse: Optional[bool] = ...,
    reset: bool = ...,
):
    ...


def edit(
    text: Optional[Text] = ...,
    editor: Optional[Text] = ...,
    env: Optional[Text] = ...,
    require_save: bool = ...,
    extension: Text = ...,
    filename: Optional[Text] = ...,
) -> Text:
    ...


def launch(url: Text, wait: bool = ..., locate: bool = ...) -> int:
    ...


def getchar(echo: bool = ...) -> Text:
    ...


def pause(
    info: Text = ..., err: bool = ...
) -> None:
    ...
