from _typeshed import ConvertibleToInt
from collections.abc import Callable, Sequence
from typing import Any, Final, Literal, TypeAlias, overload
from typing_extensions import Self, TypeVar, deprecated

from affine import Affine as Affine
from numpy.typing import ArrayLike, NDArray
from rasterio._transform import GCPTransformerBase, RPCTransformerBase
from rasterio._typing import _GDALOption
from rasterio.control import GroundControlPoint
from rasterio.enums import TransformDirection as TransformDirection, TransformMethod as TransformMethod
from rasterio.errors import RasterioDeprecationWarning as RasterioDeprecationWarning
from rasterio.rpc import RPC

_Sextuple: TypeAlias = tuple[float, float, float, float, float, float]
_OffsetOptions: TypeAlias = Literal["center", "ul", "ur", "ll", "lr"]
_T = TypeVar("_T", default=int)
_RoundOperation: TypeAlias = Callable[[float], _T]

IDENTITY: Final[Affine]
GDAL_IDENTITY: Final[_Sextuple]

class TransformMethodsMixin:
    def xy(
        self,
        row: int | Sequence[int] | ArrayLike,
        col: int | Sequence[int] | ArrayLike,
        z: float | Sequence[float] | ArrayLike | None = None,
        offset: _OffsetOptions = "center",
        transform_method: TransformMethod = ...,
        **rpc_options: _GDALOption,
    ) -> tuple[float, float] | tuple[list[float], list[float]] | tuple[NDArray[Any], NDArray[Any]]: ...
    def index(
        self,
        x: float | Sequence[float] | ArrayLike,
        y: float | Sequence[float] | ArrayLike,
        z: float | Sequence[float] | ArrayLike | None = None,
        op: _RoundOperation[ConvertibleToInt] | None = None,
        precision: int | None = None,
        transform_method: TransformMethod = ...,
        **rpc_options: _GDALOption,
    ) -> tuple[int, int] | tuple[list[int], list[int]] | tuple[NDArray[Any], NDArray[Any]]: ...

def tastes_like_gdal(seq: Affine | _Sextuple) -> bool: ...
def guard_transform(transform: Affine | _Sextuple) -> Affine: ...
def from_origin(west: float, north: float, xsize: float, ysize: float) -> Affine: ...
def from_bounds(west: float, south: float, east: float, north: float, width: float, height: float) -> Affine: ...
def array_bounds(height: int, width: int, transform: Affine) -> tuple[float, float, float, float]: ...
def from_gcps(gcps: Sequence[GroundControlPoint]) -> Affine: ...
def xy(
    transform: Affine | Sequence[GroundControlPoint] | RPC,
    rows: int | Sequence[int] | ArrayLike,
    cols: int | Sequence[int] | ArrayLike,
    zs: float | Sequence[float] | ArrayLike | None = None,
    offset: _OffsetOptions = "center",
    **rpc_options: _GDALOption,
) -> tuple[float, float] | tuple[list[float], list[float]] | tuple[NDArray[Any], NDArray[Any]]: ...
def rowcol(
    transform: Affine | Sequence[GroundControlPoint] | RPC,
    xs: float | Sequence[float] | ArrayLike,
    ys: float | Sequence[float] | ArrayLike,
    zs: float | Sequence[float] | ArrayLike | None = None,
    op: _RoundOperation[_T] | None = None,
    precision: int | None = None,
    **rpc_options: _GDALOption,
) -> tuple[_T, _T] | tuple[list[_T], list[_T]] | tuple[NDArray[Any], NDArray[Any]]: ...
def get_transformer(
    transform: Affine | Sequence[GroundControlPoint] | RPC, **rpc_options: _GDALOption
) -> type[TransformerBase]: ...

class TransformerBase:
    def __init__(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: object) -> None: ...
    def xy(
        self,
        rows: int | Sequence[int] | ArrayLike,
        cols: int | Sequence[int] | ArrayLike,
        zs: float | Sequence[float] | ArrayLike | None = None,
        offset: _OffsetOptions = "center",
    ) -> tuple[float, float] | tuple[list[float], list[float]] | tuple[NDArray[Any], NDArray[Any]]: ...

    @overload
    def rowcol(
        self,
        xs: float | Sequence[float] | ArrayLike,
        ys: float | Sequence[float] | ArrayLike,
        zs: float | Sequence[float] | ArrayLike | None = None,
        op: _RoundOperation[_T] | None = None,
    ) -> tuple[_T, _T] | tuple[list[_T], list[_T]] | tuple[NDArray[Any], NDArray[Any]]: ...
    @overload
    @deprecated("The `precision` parameter is unused since rasterio 1.3 and will be removed in 2.0.0.")
    def rowcol(
        self,
        xs: float | Sequence[float] | ArrayLike,
        ys: float | Sequence[float] | ArrayLike,
        zs: float | Sequence[float] | ArrayLike | None = None,
        op: _RoundOperation[_T] | None = None,
        precision: int | None = None,
    ) -> tuple[_T, _T] | tuple[list[_T], list[_T]] | tuple[NDArray[Any], NDArray[Any]]: ...

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
