import winreg
from distutils.ccompiler import CCompiler
from typing import Any

RegOpenKeyEx = winreg.OpenKeyEx
RegEnumKey = winreg.EnumKey
RegEnumValue = winreg.EnumValue
RegError: Any
HKEYS: Any
NATIVE_WIN64: Any
VS_BASE: str
WINSDK_BASE: str
NET_BASE: str
PLAT_TO_VCVARS: Any

class Reg:
    def get_value(cls, path, key): ...
    get_value: Any
    def read_keys(cls, base, key): ...
    read_keys: Any
    def read_values(cls, base, key): ...
    read_values: Any
    def convert_mbcs(s): ...
    convert_mbcs: Any

class MacroExpander:
    macros: Any
    vsbase: Any
    def __init__(self, version) -> None: ...
    def set_macro(self, macro, path, key) -> None: ...
    def load_macros(self, version) -> None: ...
    def sub(self, s): ...

def get_build_version(): ...
def normalize_and_reduce_paths(paths): ...
def removeDuplicates(variable): ...
def find_vcvarsall(version): ...
def query_vcvarsall(version, arch: str = ...): ...

VERSION: Any

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
    def manifest_setup_ldargs(self, output_filename, build_temp, ld_args) -> None: ...
    def manifest_get_embed_info(self, target_desc, ld_args): ...
    def library_dir_option(self, dir): ...
    def runtime_library_dir_option(self, dir) -> None: ...
    def library_option(self, lib): ...
    def find_library_file(self, dirs, lib, debug: int = ...): ...
    def find_exe(self, exe): ...
