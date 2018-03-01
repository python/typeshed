# Stub for termcolor: https://pypi.python.org/pypi/termcolor
from typing import Any, AnyStr, Iterable, Optional


def colored(
    text: AnyStr,
    color: Optional[str] = None,
    on_color: Optional[str] = None,
    attrs: Optional[Iterable[str]] = None,
) -> str:
    ...


def cprint(
    text: AnyStr,
    color: Optional[str] = None,
    on_color: Optional[str] = None,
    attrs: Optional[Iterable[str]] = None,
    **kwargs: Any,
) -> None:
    ...
