from distutils.ccompiler import CCompiler
from typing import Any

class UnixCCompiler(CCompiler):
    compiler_type: str
    executables: Any
    src_extensions: Any
    obj_extension: str
    static_lib_extension: str
    shared_lib_extension: str
    dylib_lib_extension: str
    xcode_stub_lib_extension: str
    static_lib_format: str
    shared_lib_format: str
    dylib_lib_format: str
    xcode_stub_lib_format: Any
    def preprocess(
        self,
        source,
        output_file: Any | None = ...,
        macros: Any | None = ...,
        include_dirs: Any | None = ...,
        extra_preargs: Any | None = ...,
        extra_postargs: Any | None = ...,
    ) -> None: ...
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
    def library_dir_option(self, dir): ...
    def runtime_library_dir_option(self, dir): ...
    def library_option(self, lib): ...
    def find_library_file(self, dirs, lib, debug: int = ...): ...
