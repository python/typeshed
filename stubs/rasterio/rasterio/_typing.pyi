from collections.abc import Sequence
from typing import BinaryIO, TypeAlias

from rasterio.crs import CRS
from rasterio.io import BufferedDatasetWriter, DatasetReader, DatasetWriter, MemoryFile
from rasterio.windows import Window

AnyDataset: TypeAlias = DatasetReader | DatasetWriter | BufferedDatasetWriter | MemoryFile
Colormap: TypeAlias = dict[int, tuple[int, int, int] | tuple[int, int, int, int]]
CRSInput: TypeAlias = str | dict[str, str] | CRS
FileOrBytes: TypeAlias = BinaryIO | bytes
Indexes: TypeAlias = int | Sequence[int]
NumType: TypeAlias = int | float
ShapeND: TypeAlias = Sequence[int]
WindowInput: TypeAlias = Window | tuple[tuple[int, int], tuple[int, int]]
