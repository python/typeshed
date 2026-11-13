from _typeshed import ConvertibleToInt, FloatInt
from collections.abc import Callable, Sequence
from typing import Final, Literal, TypeAlias, overload
from typing_extensions import Self, TypeVar, deprecated

from affine import Affine as Affine
from rasterio._transform import GCPTransformerBase, RPCTransformerBase
from rasterio._typing import _GDALOption
from rasterio.control import GroundControlPoint
from rasterio.enums import TransformDirection as TransformDirection, TransformMethod as TransformMethod
from rasterio.errors import RasterioDeprecationWarning as RasterioDeprecationWarning
from rasterio.rpc import RPC

_Sextuple: TypeAlias = tuple[FloatInt, FloatInt, FloatInt, FloatInt, FloatInt, FloatInt]
_OffsetOptions: TypeAlias = Literal["center", "ul", "ur", "ll", "lr"]
_T = TypeVar("_T", default=int)
_RoundOperation: TypeAlias = Callable[[FloatInt], _T]

IDENTITY: Final[Affine]
GDAL_IDENTITY: Final[_Sextuple]

class TransformMethodsMixin:
    def xy(
        self,
        row: int | Sequence[int],
        col: int | Sequence[int],
        z: FloatInt | Sequence[FloatInt] | None = None,
        offset: _OffsetOptions = "center",
        transform_method: TransformMethod = ...,
        **rpc_options: _GDALOption,
    ) -> tuple[float, float] | tuple[list[float], list[float]]: ...
    def index(
        self,
        x: FloatInt | Sequence[FloatInt],
        y: FloatInt | Sequence[FloatInt],
        z: FloatInt | Sequence[FloatInt] | None = None,
        op: _RoundOperation[ConvertibleToInt] | None = None,
        precision: int | None = None,
        transform_method: TransformMethod = ...,
        **rpc_options: _GDALOption,
    ) -> tuple[int, int] | tuple[list[int], list[int]]: ...

def tastes_like_gdal(seq: Affine | _Sextuple) -> bool: ...
def guard_transform(transform: Affine | _Sextuple) -> Affine: ...
def from_origin(west: FloatInt, north: FloatInt, xsize: FloatInt, ysize: FloatInt) -> Affine: ...
def from_bounds(
    west: FloatInt, south: FloatInt, east: FloatInt, north: FloatInt, width: FloatInt, height: FloatInt
) -> Affine: ...
def array_bounds(height: int, width: int, transform: Affine) -> tuple[float, float, float, float]: ...
def from_gcps(gcps: Sequence[GroundControlPoint]) -> Affine: ...
def xy(
    transform: Affine | Sequence[GroundControlPoint] | RPC,
    rows: int | Sequence[int],
    cols: int | Sequence[int],
    zs: FloatInt | Sequence[FloatInt] | None = None,
    offset: _OffsetOptions = "center",
    **rpc_options: _GDALOption,
) -> tuple[float, float] | tuple[list[float], list[float]]: ...
def rowcol(
    transform: Affine | Sequence[GroundControlPoint] | RPC,
    xs: FloatInt | Sequence[FloatInt],
    ys: FloatInt | Sequence[FloatInt],
    zs: FloatInt | Sequence[FloatInt] | None = None,
    op: _RoundOperation[_T] | None = None,
    precision: int | None = None,
    **rpc_options: _GDALOption,
) -> tuple[_T, _T] | tuple[list[_T], list[_T]]: ...
def get_transformer(
    transform: Affine | Sequence[GroundControlPoint] | RPC, **rpc_options: _GDALOption
) -> type[TransformerBase]: ...

class TransformerBase:
    def __init__(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: object) -> None: ...
    def xy(
        self,
        rows: int | Sequence[int],
        cols: int | Sequence[int],
        zs: FloatInt | Sequence[FloatInt] | None = None,
        offset: _OffsetOptions = "center",
    ) -> tuple[float, float] | tuple[list[float], list[float]]: ...

    @overload
    def rowcol(
        self,
        xs: FloatInt | Sequence[FloatInt],
        ys: FloatInt | Sequence[FloatInt],
        zs: FloatInt | Sequence[FloatInt] | None = None,
        op: _RoundOperation[_T] | None = None,
    ) -> tuple[_T, _T] | tuple[list[_T], list[_T]]: ...
    @overload
    @deprecated("The `precision` parameter is unused since rasterio 1.3 and will be removed in 2.0.0.")
    def rowcol(
        self,
        xs: FloatInt | Sequence[FloatInt],
        ys: FloatInt | Sequence[FloatInt],
        zs: FloatInt | Sequence[FloatInt] | None = None,
        op: _RoundOperation[_T] | None = None,
        precision: int | None = None,
    ) -> tuple[_T, _T] | tuple[list[_T], list[_T]]: ...

class GDALTransformerBase(TransformerBase):
    def __init__(self) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: object) -> None: ...

class AffineTransformer(TransformerBase):
    def __init__(self, affine_transform: Affine | _Sextuple) -> None: ...

class GCPTransformer(GCPTransformerBase, GDALTransformerBase):
    def __init__(self, gcps: Sequence[GroundControlPoint], tps: bool = False) -> None: ...

class RPCTransformer(RPCTransformerBase, GDALTransformerBase):
    def __init__(self, rpcs: RPC, **rpc_options: _GDALOption) -> None: ...
