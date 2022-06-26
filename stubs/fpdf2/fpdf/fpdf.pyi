import datetime
from _typeshed import StrPath
from collections import defaultdict
from collections.abc import Callable
from contextlib import _GeneratorContextManager
from enum import IntEnum
from io import BytesIO
from pathlib import Path
from typing import Any, NamedTuple, overload
from typing_extensions import Literal, TypeAlias

from PIL import Image

from .actions import Action
from .recorder import FPDFRecorder
from .syntax import DestinationXYZ
from .util import _Unit

_Orientation: TypeAlias = Literal["", "portrait", "p", "P", "landscape", "l", "L"]
_Format: TypeAlias = Literal["", "a3", "A3", "a4", "A4", "a5", "A5", "letter", "Letter", "legal", "Legal"]
_FontStyle: TypeAlias = Literal["", "B", "I"]
_FontStyles: TypeAlias = Literal["", "B", "I", "U", "BU", "UB", "BI", "IB", "IU", "UI", "BIU", "BUI", "IBU", "IUB", "UBI", "UIB"]
PAGE_FORMATS: dict[_Format, tuple[float, float]]

class DocumentState(IntEnum):
    UNINITIALIZED: int
    READY: int
    GENERATING_PAGE: int
    CLOSED: int

class Annotation(NamedTuple):
    type: str
    x: int
    y: int
    width: int
    height: int
    contents: str | None = ...
    link: str | int | None = ...
    alt_text: str | None = ...
    action: Action | None = ...

class TitleStyle(NamedTuple):
    font_family: str | None = ...
    font_style: str | None = ...
    font_size_pt: int | None = ...
    color: int | tuple[int, int, int] | None = ...
    underline: bool = ...
    t_margin: int | None = ...
    l_margin: int | None = ...
    b_margin: int | None = ...

class ToCPlaceholder(NamedTuple):
    render_function: Callable[[FPDF, Any], object]
    start_page: int
    y: int
    pages: int = ...

class SubsetMap:
    def __init__(self, identities: list[int]) -> None: ...
    def pick(self, unicode: int): ...
    def dict(self): ...

def get_page_format(format: _Format | tuple[float, float], k: float | None = ...) -> tuple[float, float]: ...

# TODO: TypedDicts
_Page: TypeAlias = dict[str, Any]
_Font: TypeAlias = dict[str, Any]
_FontFile: TypeAlias = dict[str, Any]
_Image: TypeAlias = dict[str, Any]

class FPDF:
    MARKDOWN_BOLD_MARKER: str
    MARKDOWN_ITALICS_MARKER: str
    MARKDOWN_UNDERLINE_MARKER: str
    offsets: dict[int, int]
    page: int
    n: int
    buffer: bytearray
    pages: dict[int, _Page]
    state: DocumentState
    fonts: dict[str, _Font]
    font_files: dict[str, _FontFile]
    diffs: dict[int, int]
    images: dict[str, _Image]
    annots: defaultdict[int, list[Annotation]]
    links: dict[int, DestinationXYZ]
    in_footer: int
    lasth: int
    current_font: _Font
    font_family: str
    font_style: str
    font_size_pt: int
    font_stretching: int
    str_alias_nb_pages: str
    underline: int
    draw_color: str
    fill_color: str
    text_color: str
    ws: int
    angle: int
    font_cache_dir: Any
    xmp_metadata: Any
    image_filter: str
    page_duration: int
    page_transition: Any
    struct_builder: Any
    section_title_styles: Any
    core_fonts: Any
    core_fonts_encoding: str
    font_aliases: Any
    k: float
    def_orientation: Any
    font_size: Any
    c_margin: Any
    line_width: float
    dw_pt: float
    dh_pt: float
    compress: bool
    pdf_version: str

    x: float
    y: float
    t_margin: float
    r_margin: float
    l_margin: float

    # Set during call to _set_orientation(), called from __init__().
    cur_orientation: Literal["P", "L"]
    w_pt: float
    h_pt: float
    w: float
    h: float
    def __init__(
        self,
        orientation: _Orientation = ...,
        unit: _Unit | float = ...,
        format: _Format | tuple[float, float] = ...,
        font_cache_dir: bool = ...,
    ) -> None: ...
    @property
    def unifontsubset(self): ...
    @property
    def epw(self): ...
    @property
    def eph(self): ...
    def set_margin(self, margin: float) -> None: ...
    def set_margins(self, left: float, top: float, right: float = ...) -> None: ...
    def set_left_margin(self, margin: float) -> None: ...
    def set_top_margin(self, margin: float) -> None: ...
    def set_right_margin(self, margin: float) -> None: ...
    auto_page_break: Any
    b_margin: Any
    page_break_trigger: Any
    def set_auto_page_break(self, auto: bool, margin: float = ...) -> None: ...
    zoom_mode: Any
    layout_mode: Any
    def set_display_mode(self, zoom, layout: str = ...) -> None: ...
    def set_compression(self, compress) -> None: ...
    title: Any
    def set_title(self, title: str) -> None: ...
    lang: Any
    def set_lang(self, lang: str) -> None: ...
    subject: Any
    def set_subject(self, subject: str) -> None: ...
    author: Any
    def set_author(self, author: str) -> None: ...
    keywords: Any
    def set_keywords(self, keywords: str) -> None: ...
    creator: Any
    def set_creator(self, creator: str) -> None: ...
    producer: Any
    def set_producer(self, producer: str) -> None: ...
    creation_date: Any
    def set_creation_date(self, date: datetime.datetime | None = ...) -> None: ...
    def set_xmp_metadata(self, xmp_metadata) -> None: ...
    def set_doc_option(self, opt, value) -> None: ...
    def set_image_filter(self, image_filter) -> None: ...
    def alias_nb_pages(self, alias: str = ...) -> None: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def add_page(
        self,
        orientation: _Orientation = ...,
        format: _Format | tuple[float, float] = ...,
        same: bool = ...,
        duration: int = ...,
        transition: Any | None = ...,
    ) -> None: ...
    def header(self) -> None: ...
    def footer(self) -> None: ...
    def page_no(self) -> int: ...
    def set_draw_color(self, r, g: int = ..., b: int = ...) -> None: ...
    def set_fill_color(self, r, g: int = ..., b: int = ...) -> None: ...
    def set_text_color(self, r, g: int = ..., b: int = ...) -> None: ...
    def get_string_width(self, s, normalized: bool = ..., markdown: bool = ...): ...
    def set_line_width(self, width: float) -> None: ...
    def line(self, x1: float, y1: float, x2: float, y2: float) -> None: ...
    def polyline(self, point_list, fill: bool = ..., polygon: bool = ...) -> None: ...
    def polygon(self, point_list, fill: bool = ...) -> None: ...
    def dashed_line(self, x1, y1, x2, y2, dash_length: int = ..., space_length: int = ...) -> None: ...
    def rect(self, x, y, w, h, style: Any | None = ...) -> None: ...
    def ellipse(self, x, y, w, h, style: Any | None = ...) -> None: ...
    def circle(self, x, y, r, style: Any | None = ...) -> None: ...
    def add_font(self, family: str, style: _FontStyle = ..., fname: str | None = ..., uni: bool = ...) -> None: ...
    def set_font(self, family: str | None = ..., style: _FontStyles = ..., size: int = ...) -> None: ...
    def set_font_size(self, size: int) -> None: ...
    def set_stretching(self, stretching) -> None: ...
    def add_link(self): ...
    def set_link(self, link, y: int = ..., x: int = ..., page: int = ..., zoom: str = ...) -> None: ...
    def link(self, x, y, w, h, link, alt_text: Any | None = ...) -> None: ...
    def text_annotation(self, x, y, text) -> None: ...
    def add_action(self, action, x, y, w, h) -> None: ...
    def text(self, x, y, txt: str = ...) -> None: ...
    def rotate(self, angle, x: Any | None = ..., y: Any | None = ...) -> None: ...
    def rotation(self, angle, x: Any | None = ..., y: Any | None = ...) -> _GeneratorContextManager[None]: ...
    @property
    def accept_page_break(self): ...
    def cell(
        self,
        w: float | None = ...,
        h: float | None = ...,
        txt: str = ...,
        border: bool | Literal[0, 1] | str = ...,
        ln: int = ...,
        align: str = ...,
        fill: bool = ...,
        link: str = ...,
        center: bool = ...,
        markdown: bool = ...,
    ): ...
    def will_page_break(self, height): ...
    def multi_cell(
        self,
        w: float,
        h: float | None = ...,
        txt: str = ...,
        border: bool | Literal[0, 1] | str = ...,
        align: str = ...,
        fill: bool = ...,
        split_only: bool = ...,
        link: str = ...,
        ln: int = ...,
        max_line_height: Any | None = ...,
        markdown: bool = ...,
    ): ...
    def write(self, h: Any | None = ..., txt: str = ..., link: str = ...) -> None: ...
    def image(
        self,
        name: str | Image.Image | BytesIO | StrPath,
        x: float | None = ...,
        y: float | None = ...,
        w: float = ...,
        h: float = ...,
        type: str = ...,
        link: str = ...,
        title: str | None = ...,
        alt_text: str | None = ...,
    ) -> _Image: ...
    def ln(self, h: Any | None = ...) -> None: ...
    def get_x(self) -> float: ...
    def set_x(self, x: float) -> None: ...
    def get_y(self) -> float: ...
    def set_y(self, y: float) -> None: ...
    def set_xy(self, x: float, y: float) -> None: ...
    @overload
    def output(self, name: Literal[""] = ...) -> bytearray: ...  # type: ignore[misc]
    @overload
    def output(self, name: str) -> None: ...
    def normalize_text(self, txt): ...
    def interleaved2of5(self, txt, x, y, w: int = ..., h: int = ...) -> None: ...
    def code39(self, txt, x, y, w: float = ..., h: int = ...) -> None: ...
    def rect_clip(self, x, y, w, h) -> _GeneratorContextManager[None]: ...
    def unbreakable(self) -> _GeneratorContextManager[FPDFRecorder]: ...
    def insert_toc_placeholder(self, render_toc_function, pages: int = ...) -> None: ...
    def set_section_title_styles(
        self,
        level0,
        level1: Any | None = ...,
        level2: Any | None = ...,
        level3: Any | None = ...,
        level4: Any | None = ...,
        level5: Any | None = ...,
        level6: Any | None = ...,
    ) -> None: ...
    def start_section(self, name, level: int = ...) -> None: ...
