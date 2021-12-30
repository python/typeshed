from tkinter import Canvas, Frame, PhotoImage, Misc
from typing import Any, Callable, ClassVar, Sequence, TypeVar, Union, overload, Scrollbar

# Note: '_Color' is the alias we use for arguments and _AnyColor is the
# alias we use for return types. Really, these two aliases should be the
# same, but as per the "no union returns" typeshed policy, we'll return
# Any instead.
_Color = Union[str, tuple[float, float, float]]
_AnyColor = Any

# TODO: Replace this with a TypedDict once it becomes standardized.
_PenState = dict[str, Any]

_Speed = Union[str, float]
_PolygonCoords = Sequence[tuple[float, float]]

# TODO: Type this more accurately
# Vec2D is actually a custom subclass of 'tuple'.
Vec2D = tuple[float, float]

# Does not actually inherit from Canvas, but dynamically gets all methods of Canvas
class ScrolledCanvas(Canvas):
    bg: str
    hscroll: Scrollbar
    vscroll: Scrollbar
    def __init__(self, master: Misc | None, width: int = ..., height: int = ..., canvwidth: int = ..., canvheight: int = ...) -> None: ...
    canvwidth: int
    canvheight: int
    def reset(self, canvwidth: int | None = ..., canvheight: int | None = ..., bg: str | None = ...) -> None: ...

class TurtleScreenBase(object):
    cv: Canvas
    canvwidth: int
    canvheight: int
    xscale: float
    yscale: float
    def __init__(self, cv: Canvas) -> None: ...
    def mainloop(self) -> None: ...
    def textinput(self, title: str, prompt: str) -> str | None: ...
    def numinput(
        self, title: str, prompt: str, default: float | None = ..., minval: float | None = ..., maxval: float | None = ...
    ) -> float | None: ...

class Terminator(Exception): ...
class TurtleGraphicsError(Exception): ...

class Shape(object):
    def __init__(self, type_: str, data: _PolygonCoords | PhotoImage | None = ...) -> None: ...
    def addcomponent(self, poly: _PolygonCoords, fill: _Color, outline: _Color | None = ...) -> None: ...

class TurtleScreen(TurtleScreenBase):
    def __init__(self, cv: Canvas, mode: str = ..., colormode: float = ..., delay: int = ...) -> None: ...
    def clear(self) -> None: ...
    @overload
    def mode(self, mode: None = ...) -> str: ...
    @overload
    def mode(self, mode: str) -> None: ...
    def setworldcoordinates(self, llx: float, lly: float, urx: float, ury: float) -> None: ...
    def register_shape(self, name: str, shape: _PolygonCoords | Shape | None = ...) -> None: ...
    @overload
    def colormode(self, cmode: None = ...) -> float: ...
    @overload
    def colormode(self, cmode: float) -> None: ...
    def reset(self) -> None: ...
    def turtles(self) -> list[Turtle]: ...
    @overload
    def bgcolor(self) -> _AnyColor: ...
    @overload
    def bgcolor(self, color: _Color) -> None: ...
    @overload
    def bgcolor(self, r: float, g: float, b: float) -> None: ...
    @overload
    def tracer(self, n: None = ...) -> int: ...
    @overload
    def tracer(self, n: int, delay: int | None = ...) -> None: ...
    @overload
    def delay(self, delay: None = ...) -> int: ...
    @overload
    def delay(self, delay: int) -> None: ...
    def update(self) -> None: ...
    def window_width(self) -> int: ...
    def window_height(self) -> int: ...
    def getcanvas(self) -> Canvas: ...
    def getshapes(self) -> list[str]: ...
    def onclick(self, fun: Callable[[float, float], Any], btn: int = ..., add: Any | None = ...) -> None: ...
    def onkey(self, fun: Callable[[], Any], key: str) -> None: ...
    def listen(self, xdummy: float | None = ..., ydummy: float | None = ...) -> None: ...
    def ontimer(self, fun: Callable[[], Any], t: int = ...) -> None: ...
    @overload
    def bgpic(self, picname: None = ...) -> str: ...
    @overload
    def bgpic(self, picname: str) -> None: ...
    @overload
    def screensize(self, canvwidth: None = ..., canvheight: None = ..., bg: None = ...) -> tuple[int, int]: ...
    # Looks like if self.cv is not a ScrolledCanvas, this could return a tuple as well
    @overload
    def screensize(self, canvwidth: int, canvheight: int, bg: _Color | None = ...) -> None: ...
    onscreenclick = onclick
    resetscreen = reset
    clearscreen = clear
    addshape = register_shape
    def onkeypress(self, fun: Callable[[], Any], key: str | None = ...) -> None: ...
    onkeyrelease = onkey

class TNavigator(object):
    START_ORIENTATION: dict[str, Vec2D]
    DEFAULT_MODE: str
    DEFAULT_ANGLEOFFSET: int
    DEFAULT_ANGLEORIENT: int
    def __init__(self, mode: str = ...) -> None: ...
    def reset(self) -> None: ...
    def degrees(self, fullcircle: float = ...) -> None: ...
    def radians(self) -> None: ...
    def forward(self, distance: float) -> None: ...
    def back(self, distance: float) -> None: ...
    def right(self, angle: float) -> None: ...
    def left(self, angle: float) -> None: ...
    def pos(self) -> Vec2D: ...
    def xcor(self) -> float: ...
    def ycor(self) -> float: ...
    @overload
    def goto(self, x: tuple[float, float], y: None = ...) -> None: ...
    @overload
    def goto(self, x: float, y: float) -> None: ...
    def home(self) -> None: ...
    def setx(self, x: float) -> None: ...
    def sety(self, y: float) -> None: ...
    @overload
    def distance(self, x: TNavigator | tuple[float, float], y: None = ...) -> float: ...
    @overload
    def distance(self, x: float, y: float) -> float: ...
    @overload
    def towards(self, x: TNavigator | tuple[float, float], y: None = ...) -> float: ...
    @overload
    def towards(self, x: float, y: float) -> float: ...
    def heading(self) -> float: ...
    def setheading(self, to_angle: float) -> None: ...
    def circle(self, radius: float, extent: float | None = ..., steps: int | None = ...) -> None: ...
    fd = forward
    bk = back
    backward = back
    rt = right
    lt = left
    position = pos
    setpos = goto
    setposition = goto
    seth = setheading

class TPen(object):
    def __init__(self, resizemode: str = ...) -> None: ...
    @overload
    def resizemode(self, rmode: None = ...) -> str: ...
    @overload
    def resizemode(self, rmode: str) -> None: ...
    @overload
    def pensize(self, width: None = ...) -> int: ...
    @overload
    def pensize(self, width: int) -> None: ...
    def penup(self) -> None: ...
    def pendown(self) -> None: ...
    def isdown(self) -> bool: ...
    @overload
    def speed(self, speed: None = ...) -> int: ...
    @overload
    def speed(self, speed: _Speed) -> None: ...
    @overload
    def pencolor(self) -> _AnyColor: ...
    @overload
    def pencolor(self, color: _Color) -> None: ...
    @overload
    def pencolor(self, r: float, g: float, b: float) -> None: ...
    @overload
    def fillcolor(self) -> _AnyColor: ...
    @overload
    def fillcolor(self, color: _Color) -> None: ...
    @overload
    def fillcolor(self, r: float, g: float, b: float) -> None: ...
    @overload
    def color(self) -> tuple[_AnyColor, _AnyColor]: ...
    @overload
    def color(self, color: _Color) -> None: ...
    @overload
    def color(self, r: float, g: float, b: float) -> None: ...
    @overload
    def color(self, color1: _Color, color2: _Color) -> None: ...
    def showturtle(self) -> None: ...
    def hideturtle(self) -> None: ...
    def isvisible(self) -> bool: ...
    # Note: signatures 1 and 2 overlap unsafely when no arguments are provided
    @overload
    def pen(self) -> _PenState: ...  # type: ignore[misc]
    @overload
    def pen(
        self,
        pen: _PenState | None = ...,
        *,
        shown: bool = ...,
        pendown: bool = ...,
        pencolor: _Color = ...,
        fillcolor: _Color = ...,
        pensize: int = ...,
        speed: int = ...,
        resizemode: str = ...,
        stretchfactor: tuple[float, float] = ...,
        outline: int = ...,
        tilt: float = ...,
    ) -> None: ...
    width = pensize
    up = penup
    pu = penup
    pd = pendown
    down = pendown
    st = showturtle
    ht = hideturtle

_T = TypeVar("_T")

class RawTurtle(TPen, TNavigator):
    screen: TurtleScreen
    screens: ClassVar[list[TurtleScreen]]
    def __init__(
        self, canvas: Canvas | TurtleScreen | None = ..., shape: str = ..., undobuffersize: int = ..., visible: bool = ...
    ) -> None: ...
    def reset(self) -> None: ...
    def setundobuffer(self, size: int | None) -> None: ...
    def undobufferentries(self) -> int: ...
    def clear(self) -> None: ...
    def clone(self: _T) -> _T: ...
    @overload
    def shape(self, name: None = ...) -> str: ...
    @overload
    def shape(self, name: str) -> None: ...
    # Unsafely overlaps when no arguments are provided
    @overload
    def shapesize(self) -> tuple[float, float, float]: ...  # type: ignore[misc]
    @overload
    def shapesize(
        self, stretch_wid: float | None = ..., stretch_len: float | None = ..., outline: float | None = ...
    ) -> None: ...
    @overload
    def shearfactor(self, shear: None = ...) -> float: ...
    @overload
    def shearfactor(self, shear: float) -> None: ...
    # Unsafely overlaps when no arguments are provided
    @overload
    def shapetransform(self) -> tuple[float, float, float, float]: ...  # type: ignore[misc]
    @overload
    def shapetransform(
        self, t11: float | None = ..., t12: float | None = ..., t21: float | None = ..., t22: float | None = ...
    ) -> None: ...
    def get_shapepoly(self) -> _PolygonCoords | None: ...
    def settiltangle(self, angle: float) -> None: ...
    @overload
    def tiltangle(self, angle: None = ...) -> float: ...
    @overload
    def tiltangle(self, angle: float) -> None: ...
    def tilt(self, angle: float) -> None: ...
    # Can return either 'int' or Tuple[int, ...] based on if the stamp is
    # a compound stamp or not. So, as per the "no Union return" policy,
    # we return Any.
    def stamp(self) -> Any: ...
    def clearstamp(self, stampid: int | tuple[int, ...]) -> None: ...
    def clearstamps(self, n: int | None = ...) -> None: ...
    def filling(self) -> bool: ...
    def begin_fill(self) -> None: ...
    def end_fill(self) -> None: ...
    def dot(self, size: int | None = ..., *color: _Color) -> None: ...
    def write(self, arg: object, move: bool = ..., align: str = ..., font: tuple[str, int, str] = ...) -> None: ...
    def begin_poly(self) -> None: ...
    def end_poly(self) -> None: ...
    def get_poly(self) -> _PolygonCoords | None: ...
    def getscreen(self) -> TurtleScreen: ...
    def getturtle(self: _T) -> _T: ...
    getpen = getturtle
    def onclick(self, fun: Callable[[float, float], Any], btn: int = ..., add: bool | None = ...) -> None: ...
    def onrelease(self, fun: Callable[[float, float], Any], btn: int = ..., add: bool | None = ...) -> None: ...
    def ondrag(self, fun: Callable[[float, float], Any], btn: int = ..., add: bool | None = ...) -> None: ...
    def undo(self) -> None: ...
    turtlesize = shapesize

class _Screen(TurtleScreen):
    def __init__(self) -> None: ...
    # Note int and float are interpreted differently, hence the Union instead of just float
    def setup(
        self, width: int | float = ..., height: int | float = ..., startx: int | None = ..., starty: int | None = ...
    ) -> None: ...
    def title(self, titlestring: str) -> None: ...
    def bye(self) -> None: ...
    def exitonclick(self) -> None: ...

class Turtle(RawTurtle):
    def __init__(self, shape: str = ..., undobuffersize: int = ..., visible: bool = ...) -> None: ...

RawPen = RawTurtle
Pen = Turtle

def write_docstringdict(filename: str = ...) -> None: ...

# Note: it's somewhat unfortunate that we have to copy the function signatures.
# It would be nice if we could partially reduce the redundancy by doing something
# like the following:
#
#     _screen: Screen
#     clear = _screen.clear
#
# However, it seems pytype does not support this type of syntax in pyi files.

# Functions copied from TurtleScreenBase:

# Note: mainloop() was always present in the global scope, but was added to
# TurtleScreenBase in Python 3.0
def mainloop() -> None: ...
def textinput(title: str, prompt: str) -> str | None: ...
def numinput(
    title: str, prompt: str, default: float | None = ..., minval: float | None = ..., maxval: float | None = ...
) -> float | None: ...

# Functions copied from TurtleScreen:

def clear() -> None: ...
@overload
def mode(mode: None = ...) -> str: ...
@overload
def mode(mode: str) -> None: ...
def setworldcoordinates(llx: float, lly: float, urx: float, ury: float) -> None: ...
def register_shape(name: str, shape: _PolygonCoords | Shape | None = ...) -> None: ...
@overload
def colormode(cmode: None = ...) -> float: ...
@overload
def colormode(cmode: float) -> None: ...
def reset() -> None: ...
def turtles() -> list[Turtle]: ...
@overload
def bgcolor() -> _AnyColor: ...
@overload
def bgcolor(color: _Color) -> None: ...
@overload
def bgcolor(r: float, g: float, b: float) -> None: ...
@overload
def tracer(n: None = ...) -> int: ...
@overload
def tracer(n: int, delay: int | None = ...) -> None: ...
@overload
def delay(delay: None = ...) -> int: ...
@overload
def delay(delay: int) -> None: ...
def update() -> None: ...
def window_width() -> int: ...
def window_height() -> int: ...
def getcanvas() -> Canvas: ...
def getshapes() -> list[str]: ...
def onclick(fun: Callable[[float, float], Any], btn: int = ..., add: Any | None = ...) -> None: ...
def onkey(fun: Callable[[], Any], key: str) -> None: ...
def listen(xdummy: float | None = ..., ydummy: float | None = ...) -> None: ...
def ontimer(fun: Callable[[], Any], t: int = ...) -> None: ...
@overload
def bgpic(picname: None = ...) -> str: ...
@overload
def bgpic(picname: str) -> None: ...
@overload
def screensize(canvwidth: None = ..., canvheight: None = ..., bg: None = ...) -> tuple[int, int]: ...
@overload
def screensize(canvwidth: int, canvheight: int, bg: _Color | None = ...) -> None: ...

onscreenclick = onclick
resetscreen = reset
clearscreen = clear
addshape = register_shape

def onkeypress(fun: Callable[[], Any], key: str | None = ...) -> None: ...

onkeyrelease = onkey

# Functions copied from _Screen:

def setup(width: float = ..., height: float = ..., startx: int | None = ..., starty: int | None = ...) -> None: ...
def title(titlestring: str) -> None: ...
def bye() -> None: ...
def exitonclick() -> None: ...
def Screen() -> _Screen: ...

# Functions copied from TNavigator:

def degrees(fullcircle: float = ...) -> None: ...
def radians() -> None: ...
def forward(distance: float) -> None: ...
def back(distance: float) -> None: ...
def right(angle: float) -> None: ...
def left(angle: float) -> None: ...
def pos() -> Vec2D: ...
def xcor() -> float: ...
def ycor() -> float: ...
@overload
def goto(x: tuple[float, float], y: None = ...) -> None: ...
@overload
def goto(x: float, y: float) -> None: ...
def home() -> None: ...
def setx(x: float) -> None: ...
def sety(y: float) -> None: ...
@overload
def distance(x: TNavigator | tuple[float, float], y: None = ...) -> float: ...
@overload
def distance(x: float, y: float) -> float: ...
@overload
def towards(x: TNavigator | tuple[float, float], y: None = ...) -> float: ...
@overload
def towards(x: float, y: float) -> float: ...
def heading() -> float: ...
def setheading(to_angle: float) -> None: ...
def circle(radius: float, extent: float | None = ..., steps: int | None = ...) -> None: ...

fd = forward
bk = back
backward = back
rt = right
lt = left
position = pos
setpos = goto
setposition = goto
seth = setheading

# Functions copied from TPen:
@overload
def resizemode(rmode: None = ...) -> str: ...
@overload
def resizemode(rmode: str) -> None: ...
@overload
def pensize(width: None = ...) -> int: ...
@overload
def pensize(width: int) -> None: ...
def penup() -> None: ...
def pendown() -> None: ...
def isdown() -> bool: ...
@overload
def speed(speed: None = ...) -> int: ...
@overload
def speed(speed: _Speed) -> None: ...
@overload
def pencolor() -> _AnyColor: ...
@overload
def pencolor(color: _Color) -> None: ...
@overload
def pencolor(r: float, g: float, b: float) -> None: ...
@overload
def fillcolor() -> _AnyColor: ...
@overload
def fillcolor(color: _Color) -> None: ...
@overload
def fillcolor(r: float, g: float, b: float) -> None: ...
@overload
def color() -> tuple[_AnyColor, _AnyColor]: ...
@overload
def color(color: _Color) -> None: ...
@overload
def color(r: float, g: float, b: float) -> None: ...
@overload
def color(color1: _Color, color2: _Color) -> None: ...
def showturtle() -> None: ...
def hideturtle() -> None: ...
def isvisible() -> bool: ...

# Note: signatures 1 and 2 overlap unsafely when no arguments are provided
@overload
def pen() -> _PenState: ...  # type: ignore[misc]
@overload
def pen(
    pen: _PenState | None = ...,
    *,
    shown: bool = ...,
    pendown: bool = ...,
    pencolor: _Color = ...,
    fillcolor: _Color = ...,
    pensize: int = ...,
    speed: int = ...,
    resizemode: str = ...,
    stretchfactor: tuple[float, float] = ...,
    outline: int = ...,
    tilt: float = ...,
) -> None: ...

width = pensize
up = penup
pu = penup
pd = pendown
down = pendown
st = showturtle
ht = hideturtle

# Functions copied from RawTurtle:

def setundobuffer(size: int | None) -> None: ...
def undobufferentries() -> int: ...
@overload
def shape(name: None = ...) -> str: ...
@overload
def shape(name: str) -> None: ...

# Unsafely overlaps when no arguments are provided
@overload
def shapesize() -> tuple[float, float, float]: ...  # type: ignore[misc]
@overload
def shapesize(stretch_wid: float | None = ..., stretch_len: float | None = ..., outline: float | None = ...) -> None: ...
@overload
def shearfactor(shear: None = ...) -> float: ...
@overload
def shearfactor(shear: float) -> None: ...

# Unsafely overlaps when no arguments are provided
@overload
def shapetransform() -> tuple[float, float, float, float]: ...  # type: ignore[misc]
@overload
def shapetransform(
    t11: float | None = ..., t12: float | None = ..., t21: float | None = ..., t22: float | None = ...
) -> None: ...
def get_shapepoly() -> _PolygonCoords | None: ...
def settiltangle(angle: float) -> None: ...
@overload
def tiltangle(angle: None = ...) -> float: ...
@overload
def tiltangle(angle: float) -> None: ...
def tilt(angle: float) -> None: ...

# Can return either 'int' or Tuple[int, ...] based on if the stamp is
# a compound stamp or not. So, as per the "no Union return" policy,
# we return Any.
def stamp() -> Any: ...
def clearstamp(stampid: int | tuple[int, ...]) -> None: ...
def clearstamps(n: int | None = ...) -> None: ...
def filling() -> bool: ...
def begin_fill() -> None: ...
def end_fill() -> None: ...
def dot(size: int | None = ..., *color: _Color) -> None: ...
def write(arg: object, move: bool = ..., align: str = ..., font: tuple[str, int, str] = ...) -> None: ...
def begin_poly() -> None: ...
def end_poly() -> None: ...
def get_poly() -> _PolygonCoords | None: ...
def getscreen() -> TurtleScreen: ...
def getturtle() -> Turtle: ...

getpen = getturtle

def onrelease(fun: Callable[[float, float], Any], btn: int = ..., add: Any | None = ...) -> None: ...
def ondrag(fun: Callable[[float, float], Any], btn: int = ..., add: Any | None = ...) -> None: ...
def undo() -> None: ...

turtlesize = shapesize

# Functions copied from RawTurtle with a few tweaks:

def clone() -> Turtle: ...

# Extra functions present only in the global scope:

done = mainloop
