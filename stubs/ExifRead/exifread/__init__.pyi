from _typeshed import Incomplete
from typing import BinaryIO

from exifread.utils import make_string as make_string

logger: Incomplete

def process_file(
    fh: BinaryIO,
    stop_tag=...,
    details: bool = ...,
    strict: bool = ...,
    debug: bool = ...,
    truncate_tags: bool = ...,
    auto_seek: bool = ...,
): ...
