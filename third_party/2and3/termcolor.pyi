# Stub for termcolor: https://pypi.python.org/pypi/termcolor
from typing import Any, Iterable, Optional, Text


def colored(
    text: Text,
    color: Optional[str] = ...,
    on_color: Optional[str] = ...,
    attrs: Optional[Iterable[str]] = ...,
) -> str:
    ...


def cprint(
    text: Text,
    color: Optional[str] = ...,
    on_color: Optional[str] = ...,
    attrs: Optional[Iterable[str]] = ...,
    **kwargs: Any,
) -> None:
    ...
