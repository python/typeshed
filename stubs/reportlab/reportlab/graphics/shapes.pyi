from _typeshed import FloatInt
from _typeshed import Incomplete, SupportsItems
from abc import abstractmethod
from collections.abc import Iterable, Sequence
from typing import Any, Final, Literal, TypeAlias, TypedDict, type_check_only
from typing_extensions import Never, Self, Unpack

from reportlab.lib.colors import Color
from reportlab.lib.validators import NoneOr, Validator
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Flowable
from reportlab.platypus.flowables import _HAlignment, _VAlignment

_IntBool: TypeAlias = Literal[0, 1]
_BoolLike: TypeAlias = _IntBool | bool
_PathOp: TypeAlias = (
    tuple[Literal["moveTo"], FloatInt, FloatInt]
    | tuple[Literal["lineTo"], FloatInt, FloatInt]
    | tuple[Literal["curveTo"], FloatInt, FloatInt, FloatInt, FloatInt, FloatInt, FloatInt]
    # close path may either be a tuple or just the string
    | Literal["closePath"]
    | tuple[Literal["closePath"]]
    # fallback for list that is not type safe
    | list[Any]
)

# NOTE: These are derived from _attrMap and can optionally be
#       verified at runtime
@type_check_only
class _GroupKwArgs(TypedDict, total=False):
    transform: tuple[FloatInt, FloatInt, FloatInt, FloatInt, FloatInt, FloatInt] | list[FloatInt] | list[int]
    # NOTE: This should be used with care, since it will replace elements
    #       it's mostly useful for circumventing validation logic and
    #       reusing the list, rather than populating a new list
    contents: list[Shape]
    strokeOverprint: _BoolLike
    fillOverprint: _BoolLike
    overprintMask: _BoolLike

@type_check_only
class _DrawingKwArgs(_GroupKwArgs, total=False):
    # TODO: Restrict to supported formats?
    formats: list[str] | tuple[str, ...]
    # NOTE: This looks like an implementation detail, so we may not
    #       want to include this in KwArgs
    canv: Canvas
    background: Shape | UserNode | None
    # NOTE: The runtime validation for alignments is incorrect, so
    #       we assume it is turned off and allow all valid values
    hAlign: _HAlignment
    vAlign: _VAlignment
    renderScale: FloatInt
    initialFontName: str | None
    initialFontSize: FloatInt | None

@type_check_only
class _LineShapeKwArgs(TypedDict, total=False):
    strokeColor: Color | None
    strokeWidth: FloatInt
    strokeLineCap: Literal[0, 1, 2]
    strokeLineJoin: Literal[0, 1, 2]
    strokeMiterLimit: FloatInt
    strokeDashArray: Sequence[FloatInt] | tuple[FloatInt, Sequence[FloatInt]]
    strokeOpacity: FloatInt | None
    strokeOverprint: _BoolLike
    overprintMask: _BoolLike

@type_check_only
class _PathKwArgs(_LineShapeKwArgs, total=False):
    fillColor: Color | None
    fillOpacity: FloatInt
    fillOverprint: _BoolLike

@type_check_only
class _AllPathKwArgs(_PathKwArgs, total=False):
    points: list[FloatInt] | None
    operators: list[FloatInt] | None
    isClipPath: _BoolLike
    autoclose: Literal["svg", "pdf"] | None
    fillMode: Literal[0, 1]

@type_check_only
class _SolidShapeKwArgs(_PathKwArgs, total=False):
    fillMode: Literal[0, 1]

@type_check_only
class _DefinePathKwArgs(_SolidShapeKwArgs, total=False):
    autoclose: Literal["svg", "pdf"] | None
    bbox: tuple[FloatInt, FloatInt, FloatInt, FloatInt] | None

@type_check_only
class _WedgeKwArgs(_SolidShapeKwArgs, total=False):
    radius1: FloatInt | None
    yradius1: FloatInt | None

@type_check_only
class _StringKwArgs(TypedDict, total=False):
    fontName: str
    fontSize: FloatInt
    fillColor: Color | None
    textAnchor: Literal["start", "middle", "end", "numeric"]
    encoding: str
    textRenderMode: Literal[0, 1, 2, 3, 4, 5, 6, 7]

__version__: Final[str]
isOpacity: NoneOr
NON_ZERO_WINDING: Final[str]
EVEN_ODD: Final[str]

class RL_STATE_DEFAULTS(dict[str, Any]):
    def get(self, x: str, default: Any = None) -> Any: ...  # type: ignore[override]
    def copy(self) -> dict[str, Any]: ...

STATE_DEFAULTS: Final[RL_STATE_DEFAULTS]

class _DrawTimeResizeable: ...

class _SetKeyWordArgs:
    def __init__(self, keywords: SupportsItems[str, Any] = {}) -> None: ...

def getRectsBounds(rectList): ...
def getPathBounds(points): ...
def getPointsBounds(pointList): ...

class Shape(_SetKeyWordArgs, _DrawTimeResizeable):
    @abstractmethod
    def copy(self) -> Self: ...
    def getProperties(self, recur: int = 1) -> dict[str, Any]: ...
    def setProperties(self, props) -> None: ...
    def dumpProperties(self, prefix: str = "") -> None: ...
    def verify(self) -> None: ...
    @abstractmethod
    def getBounds(self) -> tuple[float, float, float, float]: ...

class Group(Shape):
    contents: list[Shape]
    transform: tuple[FloatInt, FloatInt, FloatInt, FloatInt, FloatInt, FloatInt] | list[FloatInt] | list[int]
    def __init__(self, *elements: Shape | UserNode, **keywords: Unpack[_GroupKwArgs]) -> None: ...
    def add(self, node: Shape | UserNode, name: str | None = None) -> None: ...
    def insert(self, i: int, n: Shape | UserNode, name: str | None = None) -> None: ...
    def expandUserNodes(self) -> Group: ...
    def copy(self) -> Self: ...
    def rotate(self, theta: FloatInt, cx: FloatInt = 0, cy: FloatInt = 0) -> None: ...
    def translate(self, dx: FloatInt, dy: FloatInt = 0) -> None: ...
    def scale(self, sx: FloatInt, sy: FloatInt = 1) -> None: ...
    def skew(self, kx: FloatInt, ky: FloatInt = 0) -> None: ...
    def shift(self, x: FloatInt, y: FloatInt = 0) -> None: ...
    # NOTE: This changes the object to a Drawing, rather than returning
    #       a new one, which is not ideal...
    def asDrawing(self, width: FloatInt, height: FloatInt) -> None: ...
    def getContents(self) -> list[Shape | UserNode]: ...
    def getBounds(self) -> tuple[float, float, float, float]: ...

class Drawing(Group, Flowable):
    background: Shape | UserNode | None
    renderScale: FloatInt
    def __init__(
        self, width: FloatInt = 400, height: FloatInt = 200, *nodes: Shape | UserNode, **keywords: Unpack[_DrawingKwArgs]
    ) -> None: ...
    def draw(self, showBoundary=...) -> None: ...
    def expandUserNodes(self) -> Drawing: ...
    def asGroup(self, *args: Shape | UserNode, **kw: Unpack[_GroupKwArgs]) -> Group: ...
    def save(
        self,
        formats: Iterable[str] | None = None,
        verbose: bool | None = None,
        fnRoot: str | None = None,
        outDir: str | None = None,
        title: str = "",
        **kw,
    ): ...
    def asString(self, format: str, verbose: bool | None = None, preview: int = 0, **kw) -> str: ...
    def resized(
        self, kind: Literal["fit", "fitx", "fity"] = "fit", lpad: FloatInt = 0, rpad: FloatInt = 0, bpad: FloatInt = 0, tpad: FloatInt = 0
    ) -> Drawing: ...

class _DrawingEditorMixin: ...

@type_check_only
class _isStrokeDashArray(Validator):
    def test(self, x): ...

isStrokeDashArray: _isStrokeDashArray

class LineShape(Shape):
    strokeColor: Color | None
    strokeWidth: FloatInt
    strokeLineCap: Literal[0, 1, 2]
    strokeLineJoin: Literal[0, 1, 2]
    strokeMiterLimit: FloatInt
    strokeDashArray: Sequence[FloatInt] | tuple[FloatInt, Sequence[FloatInt]]
    strokeOpacity: FloatInt | None
    def __init__(self, kw: _LineShapeKwArgs) -> None: ...
    @abstractmethod
    def copy(self) -> Self: ...
    @abstractmethod
    def getBounds(self) -> tuple[float, float, float, float]: ...

class Line(LineShape):
    x1: FloatInt
    y1: FloatInt
    x2: FloatInt
    y2: FloatInt
    def __init__(self, x1: FloatInt, y1: FloatInt, x2: FloatInt, y2: FloatInt, **kw: Unpack[_LineShapeKwArgs]) -> None: ...
    # NOTE: For some reason Line doesn't implement copy
    def copy(self) -> Never: ...
    def getBounds(self) -> tuple[float, float, float, float]: ...

class SolidShape(LineShape):
    fillColor: Color | None
    fillOpacity: FloatInt | None
    def __init__(self, kw: _SolidShapeKwArgs) -> None: ...
    @abstractmethod
    def copy(self) -> Self: ...
    @abstractmethod
    def getBounds(self) -> tuple[float, float, float, float]: ...

class Path(SolidShape):
    points: list[FloatInt]
    operators: list[FloatInt]
    isClipPath: _BoolLike
    autoclose: Literal["svg", "pdf"] | None
    fillMode: Literal[0, 1]
    def __init__(
        self,
        points: list[FloatInt] | None = None,
        operators: list[FloatInt] | None = None,
        isClipPath: _BoolLike = 0,
        autoclose: Literal["svg", "pdf"] | None = None,
        fillMode: Literal[0, 1] = 0,
        **kw: Unpack[_PathKwArgs],
    ) -> None: ...
    def copy(self) -> Self: ...
    def moveTo(self, x: FloatInt, y: FloatInt) -> None: ...
    def lineTo(self, x: FloatInt, y: FloatInt) -> None: ...
    def curveTo(self, x1: FloatInt, y1: FloatInt, x2: FloatInt, y2: FloatInt, x3: FloatInt, y3: FloatInt) -> None: ...
    def closePath(self) -> None: ...
    def getBounds(self) -> tuple[float, float, float, float]: ...

EmptyClipPath: Final[Path]

def getArcPoints(
    centerx: FloatInt,
    centery: FloatInt,
    radius: FloatInt,
    startangledegrees: FloatInt,
    endangledegrees: FloatInt,
    yradius: FloatInt | None = None,
    degreedelta: FloatInt | None = None,
    reverse: _BoolLike | None = None,
) -> list[float]: ...

class ArcPath(Path):
    def addArc(
        self,
        centerx: FloatInt,
        centery: FloatInt,
        radius: FloatInt,
        startangledegrees: FloatInt,
        endangledegrees: FloatInt,
        yradius: FloatInt | None = None,
        degreedelta: FloatInt | None = None,
        moveTo: _BoolLike | None = None,
        reverse: _BoolLike | None = None,
    ) -> None: ...

def definePath(
    pathSegs: Iterable[_PathOp] = [], isClipPath: _BoolLike = 0, dx: FloatInt = 0, dy: FloatInt = 0, **kw: Unpack[_DefinePathKwArgs]
) -> Path: ...

class Rect(SolidShape):
    x: FloatInt
    y: FloatInt
    width: FloatInt
    height: FloatInt
    rx: FloatInt
    ry: FloatInt
    def __init__(
        self, x: FloatInt, y: FloatInt, width: FloatInt, height: FloatInt, rx: FloatInt = 0, ry: FloatInt = 0, **kw: _SolidShapeKwArgs
    ) -> None: ...
    def copy(self) -> Self: ...
    def getBounds(self) -> tuple[float, float, float, float]: ...

class Image(SolidShape):
    x: FloatInt
    y: FloatInt
    width: FloatInt
    height: FloatInt
    path: Incomplete
    def __init__(self, x: FloatInt, y: FloatInt, width: FloatInt, height: FloatInt, path, **kw: Unpack[_SolidShapeKwArgs]) -> None: ...
    def copy(self) -> Self: ...
    def getBounds(self) -> tuple[float, float, float, float]: ...

class Circle(SolidShape):
    cx: FloatInt
    cy: FloatInt
    r: FloatInt
    def __init__(self, cx: FloatInt, cy: FloatInt, r: FloatInt, **kw: Unpack[_SolidShapeKwArgs]) -> None: ...
    def copy(self) -> Self: ...
    def getBounds(self) -> tuple[float, float, float, float]: ...

class Ellipse(SolidShape):
    cx: FloatInt
    cy: FloatInt
    rx: FloatInt
    ry: FloatInt
    def __init__(self, cx: FloatInt, cy: FloatInt, rx: FloatInt, ry: FloatInt, **kw: Unpack[_SolidShapeKwArgs]) -> None: ...
    def copy(self) -> Self: ...
    def getBounds(self) -> tuple[float, float, float, float]: ...

class Wedge(SolidShape):
    centerx: FloatInt
    centery: FloatInt
    radius: FloatInt
    startangledegrees: FloatInt
    endangledegrees: FloatInt
    yradius: FloatInt | None
    annular: bool
    # NOTE: This one is not actually settable on the instance if runtime validation
    #       is turned on, but it seems bad to disallow it anyways
    degreedelta: FloatInt
    def __init__(
        self,
        centerx: FloatInt,
        centery: FloatInt,
        radius: FloatInt,
        startangledegrees: FloatInt,
        endangledegrees: FloatInt,
        yradius: FloatInt | None = None,
        annular: bool = False,
        **kw: Unpack[_WedgeKwArgs],
    ) -> None: ...
    def asPolygon(self) -> Path | Polygon: ...
    def copy(self) -> Self: ...
    def getBounds(self) -> tuple[float, float, float, float]: ...

class Polygon(SolidShape):
    points: list[FloatInt]
    def __init__(self, points: list[FloatInt] = [], **kw: Unpack[_SolidShapeKwArgs]) -> None: ...
    def copy(self) -> Self: ...
    def getBounds(self) -> tuple[float, float, float, float]: ...

class PolyLine(LineShape):
    points: list[FloatInt]
    def __init__(self, points: list[FloatInt] = [], **kw: Unpack[_SolidShapeKwArgs]) -> None: ...
    def copy(self) -> Self: ...
    def getBounds(self) -> tuple[float, float, float, float]: ...

class Hatching(Path):
    xyLists: Sequence[tuple[FloatInt, FloatInt]]
    angles: Sequence[FloatInt]
    spacings: Sequence[FloatInt]
    def __init__(
        self,
        spacings: FloatInt | Sequence[FloatInt] = 2,
        angles: FloatInt | Sequence[FloatInt] = 45,
        xyLists: Sequence[tuple[FloatInt, FloatInt] | list[FloatInt]] = [],
        **kwds: Unpack[_AllPathKwArgs],
    ) -> None: ...

def numericXShift(
    tA, text: str, w: FloatInt, fontName: str, fontSize: FloatInt, encoding: str | None = None, pivotCharacter: str = "."
) -> float: ...

class String(Shape):
    encoding: str
    x: FloatInt
    y: FloatInt
    text: str
    textAnchor: Literal["start", "middle", "end", "numeric"]
    fontName: str
    fontSize: FloatInt
    fillColor: Color | None
    def __init__(self, x: FloatInt, y: FloatInt, text: str, **kw: Unpack[_StringKwArgs]) -> None: ...
    def getEast(self): ...
    def copy(self) -> Self: ...
    def getBounds(self) -> tuple[float, float, float, float]: ...

class UserNode(_DrawTimeResizeable):
    @abstractmethod
    def provideNode(self) -> Shape: ...

class DirectDraw(Shape):
    @abstractmethod
    def drawDirectly(self, canvas: Canvas) -> None: ...

def test() -> None: ...
