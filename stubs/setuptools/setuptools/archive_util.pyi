from _typeshed import Incomplete
from distutils.errors import DistutilsError
from typing import Any

class UnrecognizedFormat(DistutilsError): ...

def default_filter(src, dst): ...
def unpack_archive(filename, extract_dir, progress_filter=..., drivers: Incomplete | None = ...) -> None: ...
def unpack_directory(filename, extract_dir, progress_filter=...) -> None: ...
def unpack_zipfile(filename, extract_dir, progress_filter=...) -> None: ...
def unpack_tarfile(filename, extract_dir, progress_filter=...): ...

extraction_drivers: Any