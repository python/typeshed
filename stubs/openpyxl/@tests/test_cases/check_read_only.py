from collections.abc import Generator
from typing_extensions import assert_type

from openpyxl.cell import _CellGetValue
from openpyxl.cell.read_only import EmptyCell, ReadOnlyCell
from openpyxl.worksheet._read_only import ReadOnlyWorksheet


def check_read_only_methods(sheet: ReadOnlyWorksheet, values_only: bool) -> None:
    # These methods alias Worksheet methods at runtime; their self and cell types differ.
    assert_type(sheet.cell(1, 1), ReadOnlyCell | EmptyCell)
    assert_type(next(sheet.iter_rows()), tuple[ReadOnlyCell | EmptyCell, ...])
    assert_type(next(sheet.iter_rows(values_only=True)), tuple[_CellGetValue, ...])
    assert_type(next(sheet.iter_rows(1, 2, 1, 3, True)), tuple[_CellGetValue, ...])
    assert_type(
        sheet.iter_rows(values_only=values_only),
        Generator[tuple[ReadOnlyCell | EmptyCell, ...]] | Generator[tuple[_CellGetValue, ...]],
    )
    assert_type(next(iter(sheet)), tuple[ReadOnlyCell | EmptyCell, ...])
    assert_type(sheet[1], tuple[ReadOnlyCell | EmptyCell, ...])
