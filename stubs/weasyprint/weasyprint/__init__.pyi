from _typeshed import Incomplete

from .document import Document as Document, Page as Page
from .urls import default_url_fetcher as default_url_fetcher

__all__ = ["CSS", "DEFAULT_OPTIONS", "HTML", "VERSION", "Attachment", "Document", "Page", "__version__", "default_url_fetcher"]

VERSION: str
__version__: str
DEFAULT_OPTIONS: Incomplete

class HTML:
    base_url: Incomplete
    url_fetcher: Incomplete
    media_type: Incomplete
    wrapper_element: Incomplete
    etree_element: Incomplete
    def __init__(
        self,
        guess=None,
        filename=None,
        url=None,
        file_obj=None,
        string=None,
        encoding=None,
        base_url=None,
        url_fetcher=None,
        media_type: str = "print",
    ) -> None: ...
    def render(self, font_config=None, counter_style=None, color_profiles=None, **options): ...
    def write_pdf(
        self, target=None, zoom: int = 1, finisher=None, font_config=None, counter_style=None, color_profiles=None, **options
    ): ...

class CSS:
    base_url: Incomplete
    matcher: Incomplete
    page_rules: Incomplete
    layers: Incomplete
    def __init__(
        self,
        guess=None,
        filename=None,
        url=None,
        file_obj=None,
        string=None,
        encoding=None,
        base_url=None,
        url_fetcher=None,
        _check_mime_type: bool = False,
        media_type: str = "print",
        font_config=None,
        counter_style=None,
        color_profiles=None,
        matcher=None,
        page_rules=None,
        layers=None,
        layer=None,
    ) -> None: ...

class Attachment:
    source: Incomplete
    name: Incomplete
    description: Incomplete
    relationship: Incomplete
    md5: Incomplete
    created: Incomplete
    modified: Incomplete
    def __init__(
        self,
        guess=None,
        filename=None,
        url=None,
        file_obj=None,
        string=None,
        base_url=None,
        url_fetcher=None,
        name=None,
        description=None,
        created=None,
        modified=None,
        relationship: str = "Unspecified",
    ) -> None: ...
