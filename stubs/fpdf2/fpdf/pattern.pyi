from _typeshed import Incomplete, Unused
from abc import ABC
from collections.abc import Iterable
from typing import Final, Literal
from typing_extensions import Never, Self, TypeAlias

from .drawing import BoundingBox, DeviceCMYK, DeviceGray, DeviceRGB, Transform
from .enums import GradientSpreadMethod
from .syntax import Name, PDFArray, PDFContentStream, PDFObject

Color: TypeAlias = DeviceRGB | DeviceGray | DeviceCMYK

TOLERANCE: Final = 1e-9

def lerp(a: float, b: float, t: float) -> float: ...
def lerp_tuple(a: tuple[float, ...], b: tuple[float, ...], t: float) -> tuple[float, ...]: ...
def pick_colorspace_and_promote(colors: list[Color]) -> tuple[str, list[Color]]: ...
def normalize_stops(
    stops: list[tuple[float, Color | str]], coerce_to_device: bool = True, *, return_raw: bool = False
) -> tuple[str, list[tuple[float, Color]]] | tuple[str, list[tuple[float, Color]], list[tuple[float, Color]]]: ...
def merge_near_duplicates(pairs: list[tuple[float, Color | str]]) -> list[tuple[float, Color | str]]: ...
def spread_map(u: float, method: GradientSpreadMethod) -> float: ...
def sample_stops(stops01: list[tuple[float, Color]], u: float) -> tuple[float, ...]: ...
def extract_alpha_stops(stops01: list[tuple[float, Color]]) -> list[tuple[float, float]]: ...

class Pattern(PDFObject):
    type: Name
    pattern_type: int
    def __init__(self, shading: Gradient) -> None: ...
    @property
    def shading(self) -> str: ...
    @property
    def matrix(self) -> str: ...
    def set_matrix(self, matrix) -> Self: ...
    def get_matrix(self) -> Transform: ...
    def set_apply_page_ctm(self, apply: bool) -> None: ...
    def get_apply_page_ctm(self) -> bool: ...

class Type2Function(PDFObject):
    function_type: Final = 2
    domain: str
    c0: str
    c1: str
    n: int
    def __init__(self, color_1, color_2) -> None: ...

class Type2FunctionGray(PDFObject):
    function_type: Final = 2
    domain: str
    c0: str
    c1: str
    n: int
    def __init__(self, g0: float, g1: float): ...

class Type3Function(PDFObject):
    function_type: Final = 3
    domain: str
    bounds: str
    encode: str
    n: int

    def __init__(self, functions: Iterable[Incomplete], bounds: Iterable[Incomplete]) -> None: ...
    @property
    def functions(self) -> str: ...

class Shading(PDFObject):
    shading_type: Literal[2, 3]
    background: str | None
    color_space: Name
    coords: list[int]
    extend: str
    anti_alias: bool

    def __init__(
        self,
        shading_type: Literal[2, 3],
        background: Color | None,
        color_space: str,
        coords: list[float],
        functions: list[Type2Function | Type3Function],
        extend_before: bool,
        extend_after: bool,
    ) -> None: ...
    @property
    def function(self) -> str: ...
    def get_functions(self) -> list[Type2Function | Type3Function]: ...
    def get_shading_object(self) -> Self: ...

class Gradient(ABC):
    color_space: str
    colors: list[Incomplete]
    background: Incomplete | None
    extend_before: Incomplete
    extend_after: Incomplete
    bounds: Incomplete
    functions: list[Type2Function | Type3Function]
    pattern: Pattern
    coords: Incomplete | None
    shading_type: int

    def __init__(self, colors, background, extend_before, extend_after, bounds): ...
    def get_functions(self) -> list[Type2Function | Type3Function]: ...
    def get_shading_object(self) -> Shading: ...
    def get_pattern(self) -> Pattern: ...
    def has_alpha(self) -> bool: ...
    def get_alpha_shading_object(self, _: Unused = None) -> Shading | None: ...

class LinearGradient(Gradient):
    coords: list[float]  # has four elements
    shading_type: int
    def __init__(
        self,
        from_x: float,
        from_y: float,
        to_x: float,
        to_y: float,
        colors: list[Incomplete],
        background=None,
        extend_before: bool = False,
        extend_after: bool = False,
        bounds: list[float] | None = None,
    ) -> None: ...

class RadialGradient(Gradient):
    coords: list[float]  # has six elements
    shading_type: int
    def __init__(
        self,
        start_circle_x: float,
        start_circle_y: float,
        start_circle_radius: float,
        end_circle_x: float,
        end_circle_y: float,
        end_circle_radius: float,
        colors: list[Incomplete],
        background=None,
        extend_before: bool = False,
        extend_after: bool = False,
        bounds: list[float] | None = None,
    ): ...

class MeshShading(PDFContentStream):
    type: Name
    shading_type: Final = 4
    color_space: Name
    background: str
    anti_alias: bool
    bits_per_coordinate: int
    bits_per_component: int
    bits_per_flag: int
    decode: PDFArray[str]

    def __init__(
        self,
        *,
        color_space: str,
        bbox: BoundingBox,
        comp_count: int,
        triangles: list[tuple[tuple[float, float], tuple[float, float], tuple[float, float]]],
        colors: list[tuple[tuple[float, ...], tuple[float, ...], tuple[float, ...]]],
        background: Color | None = None,
        anti_alias: bool = True,
    ) -> None: ...
    def get_shading_object(self) -> MeshShading: ...
    @classmethod
    def get_functions(cls) -> list[Never]: ...

class SweepGradient(PDFObject):
    __slots__ = (
        "cx",
        "cy",
        "start_angle",
        "end_angle",
        "stops",
        "spread_method",
        "segments",
        "inner_radius_factor",
        "_cached_key",
        "_shading",
        "_alpha_shading",
    )
    cx: float
    cy: float
    start_angle: float
    end_angle: float
    stops: list[tuple[float, Color | str]]
    spread_method: GradientSpreadMethod
    segments: int | None
    inner_radius_factor: float
    _cached_key: Incomplete | None
    _shading: Incomplete | None
    _alpha_shading: Incomplete | None

    def __init__(
        self,
        cx: float,
        cy: float,
        start_angle: float,
        end_angle: float,
        stops: list[tuple[float, Color | str]],
        spread_method: GradientSpreadMethod | str = GradientSpreadMethod.PAD,
        segments: int | None = None,
        inner_radius_factor: float = 0.002,
    ) -> None: ...
    def has_alpha(self) -> bool: ...
    def get_shading_object(self, bbox: BoundingBox) -> MeshShading: ...
    def get_alpha_shading_object(self, bbox: BoundingBox) -> MeshShading | None: ...

def shape_sweep_gradient_as_mesh(
    cx: float,
    cy: float,
    start_angle: float,
    end_angle: float,
    stops: list[tuple[float, Color | str]],
    *,
    spread_method: GradientSpreadMethod,
    bbox: BoundingBox,
    segments: int | None = None,
    inner_radius_factor: float = 0.002,
) -> MeshShading: ...
def shape_linear_gradient(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    stops: list[tuple[float, Color | str]],
    spread_method: GradientSpreadMethod | str = GradientSpreadMethod.PAD,
    bbox: BoundingBox | None = None,
) -> LinearGradient: ...
def shape_radial_gradient(
    cx: float,
    cy: float,
    r: float,
    stops: list[tuple[float, Color | str]],
    fx: float | None = None,
    fy: float | None = None,
    fr: float = 0.0,
    spread_method: GradientSpreadMethod | str = GradientSpreadMethod.PAD,
    bbox: BoundingBox | None = None,
) -> RadialGradient: ...
