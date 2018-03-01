# Stub for termcolor: https://pypi.python.org/pypi/termcolor
from typing import Any, AnyStr, Iterable, Optional


def colored(
    text: AnyStr,
    color: Optional[str] = ...,
    on_color: Optional[str] = ...,
    attrs: Optional[Iterable[str]] = ...,
) -> str:
    ...


def cprint(
    text: AnyStr,
    color: Optional[str] = ...,
    on_color: Optional[str] = ...,
    attrs: Optional[Iterable[str]] = ...,
    **kwargs: Any,
) -> None:
    ...
