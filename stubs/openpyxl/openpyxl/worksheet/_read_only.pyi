from _typeshed import SupportsGetItem
from collections.abc import Generator, Iterator
from typing import Any, Literal, TypeAlias, overload

from openpyxl import _VisibilityType
from openpyxl.cell import _CellGetValue
from openpyxl.cell.read_only import EmptyCell, ReadOnlyCell
from openpyxl.utils.cell import _RangeBoundariesTuple
from openpyxl.workbook.workbook import Workbook

_ReadOnlyCell: TypeAlias = ReadOnlyCell | EmptyCell

def read_dimension(source) -> _RangeBoundariesTuple | None: ...

class ReadOnlyWorksheet:
    # Worksheet methods are reused at runtime, but create read-only or empty cells here.
    def cell(self, row: int, column: int, value: None = None) -> _ReadOnlyCell: ...

    @overload
    def iter_rows(
        self, min_row: int | None, max_row: int | None, min_col: int | None, max_col: int | None, values_only: Literal[True]
    ) -> Generator[tuple[_CellGetValue, ...]]: ...
    @overload
    def iter_rows(
        self,
        min_row: int | None = None,
        max_row: int | None = None,
        min_col: int | None = None,
        max_col: int | None = None,
        *,
        values_only: Literal[True],
    ) -> Generator[tuple[_CellGetValue, ...]]: ...
    @overload
    def iter_rows(
        self,
        min_row: int | None = None,
        max_row: int | None = None,
        min_col: int | None = None,
        max_col: int | None = None,
        values_only: Literal[False] = False,
    ) -> Generator[tuple[_ReadOnlyCell, ...]]: ...
    @overload
    def iter_rows(
        self, min_row: int | None, max_row: int | None, min_col: int | None, max_col: int | None, values_only: bool
    ) -> Generator[tuple[_ReadOnlyCell, ...]] | Generator[tuple[_CellGetValue, ...]]: ...
    @overload
    def iter_rows(
        self,
        min_row: int | None = None,
        max_row: int | None = None,
        min_col: int | None = None,
        max_col: int | None = None,
        *,
        values_only: bool,
    ) -> Generator[tuple[_ReadOnlyCell, ...]] | Generator[tuple[_CellGetValue, ...]]: ...

    @property
    def values(self) -> Generator[tuple[_CellGetValue, ...]]: ...
    @property
    def rows(self) -> Generator[tuple[_ReadOnlyCell, ...]]: ...

    # An int is necessarily a row selection
    @overload
    def __getitem__(self, key: int) -> tuple[_ReadOnlyCell, ...]: ...
    # A slice is necessarily a row or rows, even if targetting a single cell
    @overload
    def __getitem__(self, key: slice) -> tuple[Any, ...]: ...  # tuple[AnyOf[_ReadOnlyCell, tuple[_ReadOnlyCell, ...]]]
    # A str could be an individual cell, row or full range
    @overload
    def __getitem__(
        self, key: str
    ) -> Any: ...  # AnyOf[_ReadOnlyCell, tuple[_ReadOnlyCell, ...], tuple[tuple[_ReadOnlyCell, ...], ...]]

    def __iter__(self) -> Iterator[tuple[_ReadOnlyCell, ...]]: ...
    parent: Workbook
    title: str
    sheet_state: _VisibilityType
    def __init__(
        self, parent_workbook: Workbook, title: str, worksheet_path, shared_strings: SupportsGetItem[int, str]
    ) -> None: ...
    def calculate_dimension(self, force: bool = False): ...
    def reset_dimensions(self) -> None: ...
    @property
    def min_row(self) -> int: ...
    @property
    def max_row(self) -> int | None: ...
    @property
    def min_column(self) -> int: ...
    @property
    def max_column(self) -> int | None: ...
