from contextlib import contextmanager
from typing import Generator, Iterable, List, Optional, Text, Tuple


FORCED_WIDTH: Optional[int]


def measure_table(rows: Iterable[Iterable[Text]]) -> Tuple[int, ...]:
    ...


def iter_rows(
    rows: Iterable[Iterable[Text]], col_count: int
) -> Generator[Tuple[Text, ...], None, None]:
    ...


def wrap_text(
    text: Text,
    width: int = ...,
    initial_indent: Text = ...,
    subsequent_indent: Text = ...,
    preserve_paragraphs: bool = ...
) -> Text:
    ...


class HelpFormatter:
    indent_increment: int
    width: Optional[int]
    current_indent: int
    buffer: List[Text]

    def __init__(
        self,
        indent_increment: int = ...,
        width: Optional[int] = ...,
        max_width: Optional[int] = ...,
    ) -> None:
        ...

    def write(self, string: Text) -> None:
        ...

    def indent(self) -> None:
        ...

    def dedent(self) -> None:
        ...

    def write_usage(
        self,
        prog: Text,
        args: Text = ...,
        prefix: Text = ...,
    ):
        ...

    def write_heading(self, heading: Text) -> None:
        ...

    def write_paragraph(self) -> None:
        ...

    def write_text(self, text: Text) -> None:
        ...

    def write_dl(
        self,
        rows: Iterable[Iterable[Text]],
        col_max: int = ...,
        col_spacing: int = ...,
    ) -> None:
        ...

    @contextmanager
    def section(self, name) -> Generator[None, None, None]:
        ...

    @contextmanager
    def indentation(self) -> Generator[None, None, None]:
        ...

    def getvalue(self) -> Text:
        ...


def join_options(options: List[Text]) -> Tuple[Text, bool]:
    ...
