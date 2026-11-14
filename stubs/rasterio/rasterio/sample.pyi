from _typeshed import FloatInt
from collections.abc import Iterable, Iterator, Sequence
from typing import Any

from numpy.typing import NDArray
from rasterio.io import DatasetReaderBase

def sample_gen(
    dataset: DatasetReaderBase,
    xy: Iterable[tuple[FloatInt, FloatInt]],
    indexes: int | Sequence[int] | None = None,
    masked: bool = False,
) -> Iterator[NDArray[Any]]: ...
def sort_xy(xy: Iterable[tuple[FloatInt, FloatInt]]) -> list[tuple[float, float]]: ...
