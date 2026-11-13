from _typeshed import FloatInt
from collections.abc import Iterable, Sequence
from typing import Literal, TypeAlias, TypeVar, overload
from typing_extensions import Self

from matplotlib.colors import Colormap, LinearSegmentedColormap, ListedColormap
from matplotlib.typing import ColorType

__all__ = [
    "color_palette",
    "hls_palette",
    "husl_palette",
    "mpl_palette",
    "dark_palette",
    "light_palette",
    "diverging_palette",
    "blend_palette",
    "xkcd_palette",
    "crayon_palette",
    "cubehelix_palette",
    "set_color_codes",
]

_ColorT = TypeVar("_ColorT", bound=ColorType)

SEABORN_PALETTES: dict[str, list[str]]
MPL_QUAL_PALS: dict[str, int]
QUAL_PALETTE_SIZES: dict[str, int]
QUAL_PALETTES: list[str]

class _ColorPalette(list[_ColorT]):
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: object) -> None: ...
    def as_hex(self) -> _ColorPalette[str]: ...

_RGBColorPalette: TypeAlias = _ColorPalette[tuple[FloatInt, FloatInt, FloatInt]]
_SeabornPaletteName: TypeAlias = Literal[
    "deep", "deep6", "muted", "muted6", "pastel", "pastel6", "bright", "bright6", "dark", "dark6", "colorblind", "colorblind6"
]

@overload
def color_palette(  # type: ignore[overload-overlap]
    palette: _SeabornPaletteName | None = None, n_colors: int | None = None, desat: FloatInt | None = None, *, as_cmap: Literal[True]
) -> list[str]: ...  # this might be a bug in seaborn because we expect the return type to be a Colormap instance
@overload
def color_palette(
    palette: str | Sequence[ColorType], n_colors: int | None = None, desat: FloatInt | None = None, *, as_cmap: Literal[True]
) -> Colormap: ...
@overload
def color_palette(
    palette: str | Sequence[ColorType] | None = None,
    n_colors: int | None = None,
    desat: FloatInt | None = None,
    as_cmap: Literal[False] = False,
) -> _RGBColorPalette: ...

@overload
def hls_palette(
    n_colors: int = 6, h: FloatInt = 0.01, l: FloatInt = 0.6, s: FloatInt = 0.65, *, as_cmap: Literal[True]
) -> ListedColormap: ...
@overload
def hls_palette(
    n_colors: int = 6, h: FloatInt = 0.01, l: FloatInt = 0.6, s: FloatInt = 0.65, as_cmap: Literal[False] = False
) -> _RGBColorPalette: ...

@overload
def husl_palette(
    n_colors: int = 6, h: FloatInt = 0.01, s: FloatInt = 0.9, l: FloatInt = 0.65, *, as_cmap: Literal[True]
) -> ListedColormap: ...
@overload
def husl_palette(
    n_colors: int = 6, h: FloatInt = 0.01, s: FloatInt = 0.9, l: FloatInt = 0.65, as_cmap: Literal[False] = False
) -> _RGBColorPalette: ...

@overload
def mpl_palette(name: str, n_colors: int = 6, *, as_cmap: Literal[True]) -> LinearSegmentedColormap: ...
@overload
def mpl_palette(name: str, n_colors: int = 6, as_cmap: Literal[False] = False) -> _RGBColorPalette: ...

@overload
def dark_palette(
    color: ColorType, n_colors: int = 6, reverse: bool = False, *, as_cmap: Literal[True], input: str = "rgb"
) -> LinearSegmentedColormap: ...
@overload
def dark_palette(
    color: ColorType, n_colors: int = 6, reverse: bool = False, as_cmap: Literal[False] = False, input: str = "rgb"
) -> _RGBColorPalette: ...

@overload
def light_palette(
    color: ColorType, n_colors: int = 6, reverse: bool = False, *, as_cmap: Literal[True], input: str = "rgb"
) -> LinearSegmentedColormap: ...
@overload
def light_palette(
    color: ColorType, n_colors: int = 6, reverse: bool = False, as_cmap: Literal[False] = False, input: str = "rgb"
) -> _RGBColorPalette: ...

@overload
def diverging_palette(
    h_neg: FloatInt,
    h_pos: FloatInt,
    s: FloatInt = 75,
    l: FloatInt = 50,
    sep: int = 1,
    n: int = 6,
    center: Literal["light", "dark"] = "light",
    *,
    as_cmap: Literal[True],
) -> LinearSegmentedColormap: ...
@overload
def diverging_palette(
    h_neg: FloatInt,
    h_pos: FloatInt,
    s: FloatInt = 75,
    l: FloatInt = 50,
    sep: int = 1,
    n: int = 6,
    center: Literal["light", "dark"] = "light",
    as_cmap: Literal[False] = False,
) -> _RGBColorPalette: ...

@overload
def blend_palette(
    colors: Iterable[ColorType], n_colors: int = 6, *, as_cmap: Literal[True], input: str = "rgb"
) -> LinearSegmentedColormap: ...
@overload
def blend_palette(
    colors: Iterable[ColorType], n_colors: int = 6, as_cmap: Literal[False] = False, input: str = "rgb"
) -> _RGBColorPalette: ...

def xkcd_palette(colors: Iterable[str]) -> _RGBColorPalette: ...
def crayon_palette(colors: Iterable[str]) -> _RGBColorPalette: ...

@overload
def cubehelix_palette(
    n_colors: int = 6,
    start: FloatInt = 0,
    rot: FloatInt = 0.4,
    gamma: FloatInt = 1.0,
    hue: FloatInt = 0.8,
    light: FloatInt = 0.85,
    dark: FloatInt = 0.15,
    reverse: bool = False,
    *,
    as_cmap: Literal[True],
) -> ListedColormap: ...
@overload
def cubehelix_palette(
    n_colors: int = 6,
    start: FloatInt = 0,
    rot: FloatInt = 0.4,
    gamma: FloatInt = 1.0,
    hue: FloatInt = 0.8,
    light: FloatInt = 0.85,
    dark: FloatInt = 0.15,
    reverse: bool = False,
    as_cmap: Literal[False] = False,
) -> _RGBColorPalette: ...

def set_color_codes(palette: str = "deep") -> None: ...
