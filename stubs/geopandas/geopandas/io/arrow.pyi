import os
from _typeshed import SupportsGetItem, SupportsKeysAndGetItem
from collections.abc import Iterable
from typing import Any

from ..geodataframe import GeoDataFrame

METADATA_VERSION: str
SUPPORTED_VERSIONS: list[str]
GEOARROW_ENCODINGS: list[str]
SUPPORTED_ENCODINGS: list[str]

def _read_parquet(
    path: str | os.PathLike[str],
    columns: Iterable[str] | None = None,
    storage_options: SupportsKeysAndGetItem[str, Any] | None = None,
    bbox: SupportsGetItem[int, float] | None = None,
    **kwargs: Any,  # kwargs passed to pyarrow.parquet.read_table
) -> GeoDataFrame: ...
def _read_feather(
    path: str | os.PathLike[str],
    columns: Iterable[str] | None = None,
    **kwargs: Any,  # kwargs passed to pyarrow.feather.read_table
) -> GeoDataFrame: ...
