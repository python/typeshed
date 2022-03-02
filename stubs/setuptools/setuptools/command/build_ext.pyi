from distutils.command.build_ext import build_ext as _build_ext
from typing import Any

from setuptools import Command

have_rtld: bool
use_stubs: bool
libtype: str

def if_dl(s): ...
def get_abi3_suffix(): ...

class build_ext(_build_ext, Command):  # type: ignore
    inplace: Any
    def run(self) -> None: ...
    def copy_extensions_to_source(self) -> None: ...
    def get_ext_filename(self, fullname): ...
    shlib_compiler: Any
    shlibs: Any
    ext_map: Any
    def initialize_options(self) -> None: ...
    extensions: Any
    def finalize_options(self) -> None: ...
    def setup_shlib_compiler(self) -> None: ...
    def get_export_symbols(self, ext): ...
    compiler: Any
    def build_extension(self, ext) -> None: ...
    def links_to_dynamic(self, ext): ...
    def get_outputs(self): ...
    def write_stub(self, output_dir, ext, compile: bool = ...) -> None: ...

def link_shared_object(
    self,
    objects,
    output_libname,
    output_dir: Any | None = ...,
    libraries: Any | None = ...,
    library_dirs: Any | None = ...,
    runtime_library_dirs: Any | None = ...,
    export_symbols: Any | None = ...,
    debug: int = ...,
    extra_preargs: Any | None = ...,
    extra_postargs: Any | None = ...,
    build_temp: Any | None = ...,
    target_lang: Any | None = ...,
) -> None: ...
