import typing as t
from _typeshed import Incomplete

import click

__version__: str

class DefaultGroup(click.Group):
    ignore_unknown_options: bool
    default_cmd_name: str
    default_if_no_args: bool
    def __init__(self, *args, **kwargs) -> None: ...
    def set_default_command(self, command: str) -> None: ...
    def parse_args(self, ctx: click.Context, args: list[str]) -> list[str]: ...
    def get_command(self, ctx: click.Context, cmd_name: str) -> click.Command | None: ...
    def resolve_command(self, ctx: click.Context, args: list[str]) -> tuple[str | None, click.Command | None, list[str]]: ...
    def format_commands(self, ctx: click.Context, formatter: click.HelpFormatter) -> None: ...
    def command(self, *args, **kwargs) -> click.Command: ...  # incomplete

class DefaultCommandFormatter:
    group: click.Group
    formatter: click.HelpFormatter
    mark: str
    def __init__(self, group: click.Group, formatter: click.HelpFormatter, mark: str = ...) -> None: ...
    def write_dl(self, rows: t.Sequence[tuple[str, str]], col_max: int = ..., col_spacing: int = ...) -> None: ...
    def __getattr__(self, attr: str) -> Incomplete: ...
    # __getattr__ used to ala-derive from click.HelpFormatter:
    # indent_increment: int
    # width: int | None
    # current_indent: int
    # buffer: t.List[str]
    # def write(self, string: str) -> None: ...
    # def indent(self) -> None: ...
    # def dedent(self) -> None: ...
    # def write_usage(self, prog: str, args: str = ..., prefix: str | None = ...) -> None: ...
    # def write_heading(self, heading: str) -> None: ...
    # def write_paragraph(self) -> None: ...
    # def write_text(self, text: str) -> None: ...
    # def section(self, name: str) -> t.Iterator[None]: ...
    # def indentation(self) -> t.Iterator[None]: ...
    # def getvalue(self) -> str: ...
