from typing import Any

class Extension:
    name: Any
    sources: Any
    include_dirs: Any
    define_macros: Any
    undef_macros: Any
    library_dirs: Any
    libraries: Any
    runtime_library_dirs: Any
    extra_objects: Any
    extra_compile_args: Any
    extra_link_args: Any
    export_symbols: Any
    swig_opts: Any
    depends: Any
    language: Any
    optional: Any
    def __init__(
        self,
        name,
        sources,
        include_dirs: Any | None = ...,
        define_macros: Any | None = ...,
        undef_macros: Any | None = ...,
        library_dirs: Any | None = ...,
        libraries: Any | None = ...,
        runtime_library_dirs: Any | None = ...,
        extra_objects: Any | None = ...,
        extra_compile_args: Any | None = ...,
        extra_link_args: Any | None = ...,
        export_symbols: Any | None = ...,
        swig_opts: Any | None = ...,
        depends: Any | None = ...,
        language: Any | None = ...,
        optional: Any | None = ...,
        **kw,
    ) -> None: ...

def read_setup_file(filename): ...
