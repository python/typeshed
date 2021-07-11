from distutils.unixccompiler import UnixCCompiler
from typing import Any

def get_msvcr(): ...

class CygwinCCompiler(UnixCCompiler):
    compiler_type: str
    obj_extension: str
    static_lib_extension: str
    shared_lib_extension: str
    static_lib_format: str
    shared_lib_format: str
    exe_extension: str
    cc: Any
    cxx: Any
    linker_dll: Any
    dll_libraries: Any
    def __init__(self, verbose: int = ..., dry_run: int = ..., force: int = ...) -> None: ...
    def link(
        self,
        target_desc,
        objects,
        output_filename,
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
    def object_filenames(self, source_filenames, strip_dir: int = ..., output_dir: str = ...): ...

class Mingw32CCompiler(CygwinCCompiler):
    compiler_type: str
    dll_libraries: Any
    def __init__(self, verbose: int = ..., dry_run: int = ..., force: int = ...) -> None: ...

CONFIG_H_OK: str
CONFIG_H_NOTOK: str
CONFIG_H_UNCERTAIN: str

def check_config_h(): ...

RE_VERSION: Any

def get_versions(): ...
def is_cygwincc(cc): ...
