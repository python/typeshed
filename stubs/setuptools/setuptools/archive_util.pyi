from _typeshed import Incomplete
from typing import Any

from setuptools._distutils.errors import DistutilsError

class UnrecognizedFormat(DistutilsError): ...

def default_filter(src, dst): ...
def unpack_archive(filename, extract_dir, progress_filter=..., drivers: Incomplete | None = ...) -> None: ...
def unpack_directory(filename, extract_dir, progress_filter=...) -> None: ...
def unpack_zipfile(filename, extract_dir, progress_filter=...) -> None: ...
def unpack_tarfile(filename, extract_dir, progress_filter=...): ...

extraction_drivers: Any
