from distutils.ccompiler import CCompiler
from typing import Any

class BCPPCompiler(CCompiler):
    compiler_type: str
    executables: Any
    src_extensions: Any
    obj_extension: str
    static_lib_extension: str
    shared_lib_extension: str
    static_lib_format: str
    shared_lib_format: str
    exe_extension: str
    cc: str
    linker: str
    lib: str
    preprocess_options: Any
    compile_options: Any
    compile_options_debug: Any
    ldflags_shared: Any
    ldflags_shared_debug: Any
    ldflags_static: Any
    ldflags_exe: Any
    ldflags_exe_debug: Any
    def __init__(self, verbose: int = ..., dry_run: int = ..., force: int = ...) -> None: ...
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
    def find_library_file(self, dirs, lib, debug: int = ...): ...
    def object_filenames(self, source_filenames, strip_dir: int = ..., output_dir: str = ...): ...
    def preprocess(
        self,
        source,
        output_file: Any | None = ...,
        macros: Any | None = ...,
        include_dirs: Any | None = ...,
        extra_preargs: Any | None = ...,
        extra_postargs: Any | None = ...,
    ) -> None: ...
