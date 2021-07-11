from distutils.ccompiler import CCompiler
from typing import Any

PLAT_SPEC_TO_RUNTIME: Any
PLAT_TO_VCVARS: Any

class MSVCCompiler(CCompiler):
    compiler_type: str
    executables: Any
    src_extensions: Any
    res_extension: str
    obj_extension: str
    static_lib_extension: str
    shared_lib_extension: str
    static_lib_format: str
    shared_lib_format: str
    exe_extension: str
    plat_name: Any
    initialized: bool
    def __init__(self, verbose: int = ..., dry_run: int = ..., force: int = ...) -> None: ...
    cc: Any
    linker: Any
    lib: Any
    rc: Any
    mc: Any
    mt: Any
    preprocess_options: Any
    compile_options: Any
    compile_options_debug: Any
    ldflags_exe: Any
    ldflags_exe_debug: Any
    ldflags_shared: Any
    ldflags_shared_debug: Any
    ldflags_static: Any
    ldflags_static_debug: Any
    def initialize(self, plat_name: Any | None = ...) -> None: ...
    def object_filenames(self, source_filenames, strip_dir: int = ..., output_dir: str = ...): ...
    def compile(
        self,
        sources,
        output_dir: Any | None = ...,
        macros: Any | None = ...,
        include_dirs: Any | None = ...,
        debug: int = ...,
        extra_preargs: Any | None = ...,
        extra_postargs: Any | None = ...,
        depends: Any | None = ...,
    ): ...
    def create_static_lib(
        self, objects, output_libname, output_dir: Any | None = ..., debug: int = ..., target_lang: Any | None = ...
    ) -> None: ...
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
    def spawn(self, cmd): ...
    def library_dir_option(self, dir): ...
    def runtime_library_dir_option(self, dir) -> None: ...
    def library_option(self, lib): ...
    def find_library_file(self, dirs, lib, debug: int = ...): ...
