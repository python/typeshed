from typing import List, Any, Optional

from bleach.linkifier import DEFAULT_CALLBACKS as DEFAULT_CALLBACKS, Linker as Linker
from bleach.sanitizer import (
    ALLOWED_ATTRIBUTES as ALLOWED_ATTRIBUTES,
    ALLOWED_PROTOCOLS as ALLOWED_PROTOCOLS,
    ALLOWED_STYLES as ALLOWED_STYLES,
    ALLOWED_TAGS as ALLOWED_TAGS,
    Cleaner as Clear,
)

from .linkifier import _Callback

__version__: str
VERSION: Any  # packaging.version.Version

def clean(
    text: str,
    tags: List[str] = ...,
    attributes: Any = ...,
    styles: List[str] = ...,
    protocols: List[str] = ...,
    strip: bool = ...,
    strip_comments: bool = ...,
) -> str: ...
def linkify(
    text: str, callbacks: List[_Callback] = ..., skip_tags: Optional[List[str]] = ..., parse_email: bool = ...
) -> str: ...
