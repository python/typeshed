from _typeshed import FloatInt, Incomplete
from collections.abc import Mapping, Sequence
from typing import Any, Final, TypeAlias, overload
from typing_extensions import deprecated

from affine import Affine as Affine
from numpy.typing import ArrayLike, NDArray
from rasterio._typing import CRSInput, Geometry, _GDALOption
from rasterio.control import GroundControlPoint
from rasterio.enums import Resampling
from rasterio.rpc import RPC

_Resolution: TypeAlias = tuple[FloatInt, FloatInt] | FloatInt
_Gcps: TypeAlias = Sequence[GroundControlPoint]
_Rpcs: TypeAlias = RPC | Mapping[str, Any]

SUPPORTED_RESAMPLING: Final[list[Resampling]]

def transform(
    src_crs: CRSInput, dst_crs: CRSInput, xs: ArrayLike, ys: ArrayLike, zs: ArrayLike | None = None
) -> tuple[list[float], list[float]] | tuple[list[float], list[float], list[float]]: ...

@overload
def transform_geom(
    src_crs: CRSInput, dst_crs: CRSInput, geom: Geometry | Sequence[Geometry], *, precision: FloatInt = -1
) -> dict[str, Any] | list[dict[str, Any]]: ...
@overload
@deprecated(
    "`antimeridian_cutting` and `antimeridian_offset` are no-ops since GDAL 2.2 "
    "and will be removed in a future rasterio release. Call transform_geom "
    "without them."
)
def transform_geom(
    src_crs: CRSInput,
    dst_crs: CRSInput,
    geom: Geometry | Sequence[Geometry],
    antimeridian_cutting: bool | None = None,
    antimeridian_offset: FloatInt | None = None,
    precision: FloatInt = -1,
) -> dict[str, Any] | list[dict[str, Any]]: ...

def transform_bounds(
    src_crs: CRSInput, dst_crs: CRSInput, left: FloatInt, bottom: FloatInt, right: FloatInt, top: FloatInt, densify_pts: int = 21
) -> tuple[float, float, float, float]: ...
def reproject(
    source: ArrayLike | Incomplete,
    destination: ArrayLike | Incomplete | None = None,
    src_transform: Affine | None = None,
    gcps: _Gcps | None = None,
    rpcs: _Rpcs | None = None,
    src_crs: CRSInput | None = None,
    src_nodata: FloatInt | None = None,
    dst_transform: Affine | None = None,
    dst_crs: CRSInput | None = None,
    dst_nodata: FloatInt | None = None,
    dst_resolution: _Resolution | None = None,
    src_alpha: int = 0,
    dst_alpha: int = 0,
    masked: bool = False,
    resampling: Resampling = ...,
    num_threads: int = 1,
    init_dest_nodata: bool = True,
    tolerance: FloatInt = 0.125,
    warp_mem_limit: int = 0,
    src_geoloc_array: NDArray[Any] | None = None,
    **kwargs: _GDALOption,
) -> tuple[NDArray[Any], Affine]: ...
def aligned_target(transform: Affine, width: int, height: int, resolution: _Resolution) -> tuple[Affine, int, int]: ...
def calculate_default_transform(
    src_crs: CRSInput,
    dst_crs: CRSInput,
    width: int,
    height: int,
    left: FloatInt | None = None,
    bottom: FloatInt | None = None,
    right: FloatInt | None = None,
    top: FloatInt | None = None,
    gcps: _Gcps | None = None,
    rpcs: _Rpcs | None = None,
    resolution: _Resolution | None = None,
    dst_width: int | None = None,
    dst_height: int | None = None,
    src_geoloc_array: NDArray[Any] | None = None,
    **kwargs: _GDALOption,
) -> tuple[Affine, int, int]: ...
