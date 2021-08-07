from typing import List, Optional, Tuple

class Extension:
    def __init__(
        self,
        name: str,
        sources: List[str],
        include_dirs: List[str] | None = ...,
        define_macros: List[Tuple[str, str | None]] | None = ...,
        undef_macros: List[str] | None = ...,
        library_dirs: List[str] | None = ...,
        libraries: List[str] | None = ...,
        runtime_library_dirs: List[str] | None = ...,
        extra_objects: List[str] | None = ...,
        extra_compile_args: List[str] | None = ...,
        extra_link_args: List[str] | None = ...,
        export_symbols: List[str] | None = ...,
        swig_opts: str | None = ...,  # undocumented
        depends: List[str] | None = ...,
        language: str | None = ...,
        optional: bool | None = ...,
    ) -> None: ...
