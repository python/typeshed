from typing import List, Any, Optional, Text

from bleach.linkifier import DEFAULT_CALLBACKS as DEFAULT_CALLBACKS, Linker as Linker
from bleach.sanitizer import (
    ALLOWED_ATTRIBUTES as ALLOWED_ATTRIBUTES,
    ALLOWED_PROTOCOLS as ALLOWED_PROTOCOLS,
    ALLOWED_STYLES as ALLOWED_STYLES,
    ALLOWED_TAGS as ALLOWED_TAGS,
    Cleaner as Clear,
)

from .linkifier import _Callback

__releasedate__: Text
__version__: Text
VERSION: Any  # packaging.version.Version

def clean(
    text: Text,
    tags: List[Text] = ...,
    attributes: Any = ...,
    styles: List[Text] = ...,
    protocols: List[Text] = ...,
    strip: bool = ...,
    strip_comments: bool = ...,
) -> Text: ...
def linkify(
    text: Text, callbacks: List[_Callback] = ..., skip_tags: Optional[List[Text]] = ..., parse_email: bool = ...
) -> Text: ...
