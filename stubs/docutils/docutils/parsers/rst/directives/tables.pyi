import csv
from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import ClassVar, Final, Literal, TypeAlias
from typing_extensions import deprecated

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.statemachine import StringList

__docformat__: Final = "reStructuredText"

# A table cell as expected by `docutils.parsers.rst.states.RSTState.build_table()` is a tuple representing:
# (morerows, morecols, offset, cell content)
_Cell: TypeAlias = tuple[int, int, int, StringList | list[str]]
_Row: TypeAlias = list[_Cell]

def align(argument: str) -> str: ...

class Table(Directive):
    option_spec: ClassVar[dict[str, Callable[[str], object]]]
    def make_title(self) -> tuple[nodes.title | None, list[nodes.system_message]]: ...
    def check_table_dimensions(self, rows: Sequence[object], header_rows: int, stub_columns: int) -> None: ...
    def set_table_width(self, table_node: nodes.table) -> None: ...
    @property
    def widths(self) -> list[int] | Literal["auto", "grid", ""]: ...
    def get_column_widths(self, n_cols: int) -> list[int]: ...
    def extend_short_rows_with_empty_cells(self, columns: int, parts: Iterable[list[_Row]]) -> None: ...

class RSTTable(Table):
    def run(self) -> Sequence[nodes.table | nodes.system_message]: ...

class CSVTable(Table):
    option_spec: ClassVar[dict[str, Callable[[str], object]]]

    class DocutilsDialect(csv.Dialect):
        delimiter: str
        quotechar: str
        doublequote: bool
        skipinitialspace: bool
        strict: bool
        lineterminator: str
        escapechar: str | None
        def __init__(self, options: Mapping[str, object]) -> None: ...

    @deprecated("Deprecated and will be removed in Docutils 1.0.")
    class HeaderDialect(csv.Dialect):
        delimiter: str
        quotechar: str
        escapechar: str
        doublequote: bool
        skipinitialspace: bool
        strict: bool
        lineterminator: str
        def __init__(self) -> None: ...

    def process_header_option(self) -> tuple[list[_Row], int]: ...
    def run(self) -> Sequence[nodes.table | nodes.system_message]: ...
    def get_csv_data(self) -> tuple[StringList | list[str], str]: ...
    def parse_csv_data_into_rows(
        self, csv_data: Iterable[str], dialect: csv.Dialect | type[csv.Dialect], source: str
    ) -> tuple[list[_Row], int]: ...

class ListTable(Table):
    option_spec: ClassVar[dict[str, Callable[[str], object]]]
    def run(self) -> Sequence[nodes.table | nodes.system_message]: ...
    def check_list_content(self, node: nodes.Element) -> tuple[int, list[int]]: ...
    def build_table_from_list(
        self, table_data: Sequence[Sequence[Sequence[nodes.Node]]], col_widths: Sequence[int], header_rows: int, stub_columns: int
    ) -> nodes.table: ...
