from collections.abc import Iterable, Sequence
from typing import TypeVar
from typing_extensions import Literal, Self

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

_T = TypeVar("_T")

SEABORN_PALETTES: dict[str, list[str]]
MPL_QUAL_PALS: dict[str, int]
QUAL_PALETTE_SIZES: dict[str, int]
QUAL_PALETTES: list[str]

class _ColorPalette(list[_T]):
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: object) -> None: ...
    def as_hex(self) -> _ColorPalette[str]: ...

def color_palette(
    palette: str | Sequence[str | tuple[float, float, float]] | None = None,
    n_colors: int | None = None,
    desat: float | None = None,
    as_cmap: bool = False,
) -> _ColorPalette[tuple[float, float, float]] | Colormap | list[str]: ...
def hls_palette(
    n_colors: int = 6, h: float = 0.01, l: float = 0.6, s: float = 0.65, as_cmap: bool = False
) -> _ColorPalette[tuple[float, float, float]] | ListedColormap: ...
def husl_palette(
    n_colors: int = 6, h: float = 0.01, s: float = 0.9, l: float = 0.65, as_cmap: bool = False
) -> _ColorPalette[tuple[float, float, float]] | ListedColormap: ...
def mpl_palette(
    name: str, n_colors: int = 6, as_cmap: bool = False
) -> _ColorPalette[tuple[float, float, float]] | LinearSegmentedColormap: ...
def dark_palette(
    color: ColorType, n_colors: int = 6, reverse: bool = False, as_cmap: bool = False, input: str = "rgb"
) -> _ColorPalette[tuple[float, float, float]] | LinearSegmentedColormap: ...
def light_palette(
    color: ColorType, n_colors: int = 6, reverse: bool = False, as_cmap: bool = False, input: str = "rgb"
) -> _ColorPalette[tuple[float, float, float]] | LinearSegmentedColormap: ...
def diverging_palette(
    h_neg: float,
    h_pos: float,
    s: float = 75,
    l: float = 50,
    sep: int = 1,
    n: int = 6,
    center: Literal["light", "dark"] = "light",
    as_cmap: bool = False,
) -> _ColorPalette[tuple[float, float, float]] | LinearSegmentedColormap: ...
def blend_palette(
    colors: Iterable[ColorType], n_colors: int = 6, as_cmap: bool = False, input: str = "rgb"
) -> _ColorPalette[tuple[float, float, float]] | LinearSegmentedColormap: ...
def xkcd_palette(colors: Iterable[str]) -> _ColorPalette[tuple[float, float, float]]: ...
def crayon_palette(colors: Iterable[str]) -> _ColorPalette[tuple[float, float, float]]: ...
def cubehelix_palette(
    n_colors: int = 6,
    start: float = 0,
    rot: float = 0.4,
    gamma: float = 1.0,
    hue: float = 0.8,
    light: float = 0.85,
    dark: float = 0.15,
    reverse: bool = False,
    as_cmap: bool = False,
) -> _ColorPalette[tuple[float, float, float]] | ListedColormap: ...
def set_color_codes(palette: str = "deep") -> None: ...
