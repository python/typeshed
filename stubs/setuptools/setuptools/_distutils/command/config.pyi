from distutils.core import Command
from typing import Any

LANG_EXT: Any

class config(Command):
    description: str
    user_options: Any
    compiler: Any
    cc: Any
    include_dirs: Any
    libraries: Any
    library_dirs: Any
    noisy: int
    dump_source: int
    temp_files: Any
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def try_cpp(self, body: Any | None = ..., headers: Any | None = ..., include_dirs: Any | None = ..., lang: str = ...): ...
    def search_cpp(
        self, pattern, body: Any | None = ..., headers: Any | None = ..., include_dirs: Any | None = ..., lang: str = ...
    ): ...
    def try_compile(self, body, headers: Any | None = ..., include_dirs: Any | None = ..., lang: str = ...): ...
    def try_link(
        self,
        body,
        headers: Any | None = ...,
        include_dirs: Any | None = ...,
        libraries: Any | None = ...,
        library_dirs: Any | None = ...,
        lang: str = ...,
    ): ...
    def try_run(
        self,
        body,
        headers: Any | None = ...,
        include_dirs: Any | None = ...,
        libraries: Any | None = ...,
        library_dirs: Any | None = ...,
        lang: str = ...,
    ): ...
    def check_func(
        self,
        func,
        headers: Any | None = ...,
        include_dirs: Any | None = ...,
        libraries: Any | None = ...,
        library_dirs: Any | None = ...,
        decl: int = ...,
        call: int = ...,
    ): ...
    def check_lib(
        self,
        library,
        library_dirs: Any | None = ...,
        headers: Any | None = ...,
        include_dirs: Any | None = ...,
        other_libraries=...,
    ): ...
    def check_header(self, header, include_dirs: Any | None = ..., library_dirs: Any | None = ..., lang: str = ...): ...

def dump_file(filename, head: Any | None = ...) -> None: ...
