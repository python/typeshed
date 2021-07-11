import winreg
from distutils.ccompiler import CCompiler
from distutils.msvc9compiler import MSVCCompiler
from typing import Any

import win32con

hkey_mod = winreg
RegOpenKeyEx = winreg.OpenKeyEx
RegEnumKey = winreg.EnumKey
RegEnumValue = winreg.EnumValue
RegError: Any
hkey_mod = win32con
HKEYS: Any

def read_keys(base, key): ...
def read_values(base, key): ...
def convert_mbcs(s): ...

class MacroExpander:
    macros: Any
    def __init__(self, version) -> None: ...
    def set_macro(self, macro, path, key) -> None: ...
    def load_macros(self, version) -> None: ...
    def sub(self, s): ...

def get_build_version(): ...
def get_build_architecture(): ...
def normalize_and_reduce_paths(paths): ...

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
    initialized: bool
    def __init__(self, verbose: int = ..., dry_run: int = ..., force: int = ...) -> None: ...
    cc: str
    linker: str
    lib: str
    rc: str
    mc: str
    preprocess_options: Any
    compile_options: Any
    compile_options_debug: Any
    ldflags_shared: Any
    ldflags_shared_debug: Any
    ldflags_static: Any
    def initialize(self) -> None: ...
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
    def library_dir_option(self, dir): ...
    def runtime_library_dir_option(self, dir) -> None: ...
    def library_option(self, lib): ...
    def find_library_file(self, dirs, lib, debug: int = ...): ...
    def find_exe(self, exe): ...
    def get_msvc_paths(self, path, platform: str = ...): ...
    def set_path_env_var(self, name) -> None: ...

OldMSVCCompiler = MSVCCompiler
