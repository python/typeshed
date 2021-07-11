from distutils.errors import *
from typing import Any

class CCompiler:
    compiler_type: Any
    src_extensions: Any
    obj_extension: Any
    static_lib_extension: Any
    shared_lib_extension: Any
    static_lib_format: Any
    shared_lib_format: Any
    exe_extension: Any
    language_map: Any
    language_order: Any
    dry_run: Any
    force: Any
    verbose: Any
    output_dir: Any
    macros: Any
    include_dirs: Any
    libraries: Any
    library_dirs: Any
    runtime_library_dirs: Any
    objects: Any
    def __init__(self, verbose: int = ..., dry_run: int = ..., force: int = ...) -> None: ...
    def set_executables(self, **kwargs) -> None: ...
    def set_executable(self, key, value) -> None: ...
    def define_macro(self, name, value: Any | None = ...) -> None: ...
    def undefine_macro(self, name) -> None: ...
    def add_include_dir(self, dir) -> None: ...
    def set_include_dirs(self, dirs) -> None: ...
    def add_library(self, libname) -> None: ...
    def set_libraries(self, libnames) -> None: ...
    def add_library_dir(self, dir) -> None: ...
    def set_library_dirs(self, dirs) -> None: ...
    def add_runtime_library_dir(self, dir) -> None: ...
    def set_runtime_library_dirs(self, dirs) -> None: ...
    def add_link_object(self, object) -> None: ...
    def set_link_objects(self, objects) -> None: ...
    def detect_language(self, sources): ...
    def preprocess(
        self,
        source,
        output_file: Any | None = ...,
        macros: Any | None = ...,
        include_dirs: Any | None = ...,
        extra_preargs: Any | None = ...,
        extra_postargs: Any | None = ...,
    ) -> None: ...
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
    SHARED_OBJECT: str
    SHARED_LIBRARY: str
    EXECUTABLE: str
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
    def link_shared_lib(
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
    def link_shared_object(
        self,
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
    def link_executable(
        self,
        objects,
        output_progname,
        output_dir: Any | None = ...,
        libraries: Any | None = ...,
        library_dirs: Any | None = ...,
        runtime_library_dirs: Any | None = ...,
        debug: int = ...,
        extra_preargs: Any | None = ...,
        extra_postargs: Any | None = ...,
        target_lang: Any | None = ...,
    ) -> None: ...
    def library_dir_option(self, dir) -> None: ...
    def runtime_library_dir_option(self, dir) -> None: ...
    def library_option(self, lib) -> None: ...
    def has_function(
        self,
        funcname,
        includes: Any | None = ...,
        include_dirs: Any | None = ...,
        libraries: Any | None = ...,
        library_dirs: Any | None = ...,
    ): ...
    def find_library_file(self, dirs, lib, debug: int = ...) -> None: ...
    def object_filenames(self, source_filenames, strip_dir: int = ..., output_dir: str = ...): ...
    def shared_object_filename(self, basename, strip_dir: int = ..., output_dir: str = ...): ...
    def executable_filename(self, basename, strip_dir: int = ..., output_dir: str = ...): ...
    def library_filename(self, libname, lib_type: str = ..., strip_dir: int = ..., output_dir: str = ...): ...
    def announce(self, msg, level: int = ...) -> None: ...
    def debug_print(self, msg) -> None: ...
    def warn(self, msg) -> None: ...
    def execute(self, func, args, msg: Any | None = ..., level: int = ...) -> None: ...
    def spawn(self, cmd, **kwargs) -> None: ...
    def move_file(self, src, dst): ...
    def mkpath(self, name, mode: int = ...) -> None: ...

def get_default_compiler(osname: Any | None = ..., platform: Any | None = ...): ...

compiler_class: Any

def show_compilers() -> None: ...
def new_compiler(
    plat: Any | None = ..., compiler: Any | None = ..., verbose: int = ..., dry_run: int = ..., force: int = ...
): ...
def gen_preprocess_options(macros, include_dirs): ...
def gen_lib_options(compiler, library_dirs, runtime_library_dirs, libraries): ...
