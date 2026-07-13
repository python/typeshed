from _typeshed import Incomplete
from collections.abc import Callable, Mapping
from datetime import datetime
from pathlib import Path
from typing import IO, Any, Literal
from xml.etree.ElementTree import Element

from csselect2 import ElementWrapper

from .css import ColorProfile
from .css.counters import CounterStyle
from .document import Document as Document, Page as Page
from .text.fonts import FontConfiguration
from .urls import URLFetcher, default_url_fetcher as default_url_fetcher

__all__ = ["CSS", "DEFAULT_OPTIONS", "HTML", "VERSION", "Attachment", "Document", "Page", "__version__", "default_url_fetcher"]

VERSION: str
__version__: str
DEFAULT_OPTIONS: Mapping[
    Literal[
        "stylesheets",
        "attachments",
        "attachment_relationships",
        "pdf_identifier",
        "pdf_variant",
        "pdf_version",
        "pdf_forms",
        "pdf_tags",
        "uncompressed_pdf",
        "xmp_metadata",
        "custom_metadata",
        "presentational_hints",
        "output_intent",
        "optimize_images",
        "jpeg_quality",
        "dpi",
        "full_fonts",
        "hinting",
        "cache",
    ],
    None | False,
]

class HTML:
    base_url: str | Path | None  # undocumented
    url_fetcher: URLFetcher  # undocumented
    media_type: str  # undocumented
    wrapper_element: ElementWrapper  # undocumented
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
        **options,
    ) -> Document: ...
    def write_pdf(
        self,
        target: str | Path | IO | None = None,
        zoom: float = 1,
        finisher: Callable[[Document, PDF], Any] | None = None,
        font_config: FontConfiguration | None = None,
        counter_style: CounterStyle | None = None,
        color_profiles: dict[str, ColorProfile] | None = None,
        **options,
    ) -> bytes | None: ...

class CSS:
    base_url: str | Path | None
    matcher: Incomplete
    page_rules: Incomplete
    layers: Incomplete
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
        matcher=None,
        page_rules=None,
        layers=None,
        layer=None,
    ) -> None: ...

class Attachment:
    source: tuple[IO, str, str | None, str | None]
    name: str | None
    description: str | None
    relationship: str
    md5: None
    created: datetime
    modified: datetime
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
