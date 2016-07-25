# Stubs for mimetypes

from typing import Any, Optional

def guess_type(url, strict: bool = ...): ...
def guess_all_extensions(type, strict: bool = ...): ...
def guess_extension(type, strict: bool = ...): ...

def init(files: Optional[Any] = ...): ...
def read_mime_types(filename): ...
def add_type(type, ext, strict: bool = ...): ...

inited = ...  # type: Any
knownfiles = ...  # type: Any
suffix_map = ...  # type: Any
encodings_map = ...  # type: Any
types_map = ...  # type: Any
common_types = ...  # type: Any

class MimeTypes:
    suffix_map = ...  # type: Any
    encodings_map = ...  # type: Any
    types_map = ...  # type: Any
    types_map_inv = ...  # type: Any
    def __init__(self, filenames: Any = ..., strict: bool = ...) -> None: ...
    def guess_extension(self, type, strict: bool = ...): ...
    def guess_type(self, url, strict: bool = ...): ...
    def guess_all_extensions(self, type, strict: bool = ...): ...
    def read(self, filename, strict: bool = ...): ...
    def readfp(self, fp, strict: bool = ...): ...
    def read_windows_registry(self, strict: bool = ...): ...
