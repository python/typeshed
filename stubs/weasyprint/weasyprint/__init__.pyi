from _typeshed import Incomplete
from collections.abc import Callable
from datetime import datetime
from pathlib import Path
from typing import IO, Any, TypeAlias, TypedDict
from typing_extensions import Unpack
from xml.etree.ElementTree import Element

from pypdf import PDF

from .css import ColorProfile
from .css.counters import CounterStyle
from .document import Document as Document, Page as Page
from .text.fonts import FontConfiguration
from .urls import URLFetcher, default_url_fetcher as default_url_fetcher

_ElementWrapper: TypeAlias = Any  # actually csselect2.ElementWrapper
_Matcher: TypeAlias = Any  # actually csselect2.Matcher

__all__ = [
    "CSS",
    "DEFAULT_OPTIONS",
    "HTML",
    "VERSION",
    "Attachment",
    "Document",
    "Page",
    "__version__",
    "default_url_fetcher",
    "Options",
    "PageRule",
    "Selector",
]

VERSION: str
__version__: str
DEFAULT_OPTIONS: Options

class Options(TypedDict):
    stylesheets: Incomplete
    attachments: Incomplete
    attachment_relationships: Incomplete
    pdf_identifier: Incomplete
    pdf_variant: Incomplete
    pdf_version: Incomplete
    pdf_forms: Incomplete
    pdf_tags: Incomplete
    uncompressed_pdf: Incomplete
    xmp_metadata: Incomplete
    custom_metadata: Incomplete
    presentational_hints: Incomplete
    output_intent: Incomplete
    optimize_images: Incomplete
    jpeg_quality: Incomplete
    dpi: Incomplete
    full_fonts: Incomplete
    hinting: Incomplete
    cache: Incomplete

Selector: TypeAlias = tuple[Incomplete, str | None, Incomplete]
PageRule: TypeAlias = tuple[Incomplete, list[Selector], Incomplete]

class HTML:
    base_url: str | Path | None  # undocumented
    url_fetcher: URLFetcher  # undocumented
    media_type: str  # undocumented
    wrapper_element: _ElementWrapper  # undocumented
    etree_element: Element  # undocumented
    def __init__(
        self,
        guess: str | Path | IO | None = None,
        filename: str | Path | None = None,
        url: str | None = None,
        file_obj: IO | None = None,
        string: str | None = None,
        encoding: str | None = None,
        base_url: str | Path | None = None,
        url_fetcher: URLFetcher | None = None,
        media_type: str = "print",
    ) -> None: ...
    def render(
        self,
        font_config: FontConfiguration | None = None,
        counter_style: CounterStyle | None = None,
        color_profiles: dict[str, ColorProfile] | None = None,
        **options: Unpack[Options],
    ) -> Document: ...
    def write_pdf(
        self,
        target: str | Path | IO | None = None,
        zoom: float = 1,
        finisher: Callable[[Document, PDF], Any] | None = None,
        font_config: FontConfiguration | None = None,
        counter_style: CounterStyle | None = None,
        color_profiles: dict[str, ColorProfile] | None = None,
        **options: Unpack[Options],
    ) -> bytes | None: ...

class CSS:
    base_url: str | Path | None  # undocumented
    matcher: _Matcher  # undocumented
    page_rules: list[PageRule]  # undocumented
    layers: list[str]  # undocumented
    def __init__(
        self,
        guess: str | Path | IO | None = None,
        filename: str | Path | None = None,
        url: str | None = None,
        file_obj: IO | None = None,
        string: str | None = None,
        encoding: str | None = None,
        base_url: str | Path | None = None,
        url_fetcher: URLFetcher | None = None,
        _check_mime_type: bool = False,
        media_type: str = "print",
        font_config: FontConfiguration | None = None,
        counter_style: CounterStyle | None = None,
        color_profiles: dict[str, ColorProfile] | None = None,
        matcher: Matcher | None = None,
        page_rules: list[PageRule] | None = None,
        layers: list[str] | None = None,
        layer: str | None = None,
    ) -> None: ...

class Attachment:
    source: tuple[IO, str, str | None, str | None]  # undocumented
    name: str | None  # undocumented
    description: str | None  # undocumented
    relationship: str  # undocumented
    md5: Incomplete  # undocumented
    created: datetime  # undocumented
    modified: datetime  # undocumented
    def __init__(
        self,
        guess: str | Path | IO | None = None,
        filename: str | Path | None = None,
        url: str | None = None,
        file_obj: IO | None = None,
        string: str | None = None,
        base_url: str | Path | None = None,
        url_fetcher: URLFetcher | None = None,
        name: str | None = None,
        description: str | None = None,
        created: datetime | None = None,
        modified: datetime | None = None,
        relationship: str = "Unspecified",
    ) -> None: ...
