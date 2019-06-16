from typing import Any, Container, Iterable, Optional, Text

from bleach.linkifier import DEFAULT_CALLBACKS as DEFAULT_CALLBACKS
from bleach.linkifier import Linker as Linker
from bleach.sanitizer import ALLOWED_ATTRIBUTES as ALLOWED_ATTRIBUTES
from bleach.sanitizer import ALLOWED_PROTOCOLS as ALLOWED_PROTOCOLS
from bleach.sanitizer import ALLOWED_STYLES as ALLOWED_STYLES
from bleach.sanitizer import ALLOWED_TAGS as ALLOWED_TAGS
from bleach.sanitizer import Cleaner as Cleaner

from .linkifier import _Callback

__releasedate__: Text
__version__: Text
VERSION: Any  # packaging.version.Version

def clean(
    text: Text,
    tags: Container[Text] = ...,
    attributes: Any = ...,
    styles: Container[Text] = ...,
    protocols: Container[Text] = ...,
    strip: bool = ...,
    strip_comments: bool = ...,
) -> Text: ...
def linkify(
    text: Text,
    callbacks: Iterable[_Callback] = ...,
    skip_tags: Optional[Container[Text]] = ...,
    parse_email: bool = ...,
) -> Text: ...
