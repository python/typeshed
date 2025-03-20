import os
from _typeshed import Incomplete
from collections.abc import Iterable
from typing import ClassVar, TypeAlias

from . import base

_Macro: TypeAlias = tuple[str] | tuple[str, str | None]

class Compiler(base.Compiler):
    src_extensions: ClassVar[list[str]]
    obj_extension: ClassVar[str]
    static_lib_extension: ClassVar[str]
    shared_lib_extension: ClassVar[str]
    dylib_lib_extension: ClassVar[str]
    xcode_stub_lib_extension: ClassVar[str]
    static_lib_format: ClassVar[str]
    shared_lib_format: ClassVar[str]
    dylib_lib_format: ClassVar[str]
    xcode_stub_lib_format: ClassVar[str]
    def preprocess(
        self,
        source: str | os.PathLike[str],
        output_file: str | os.PathLike[str] | None = None,
        macros: list[_Macro] | None = None,
        include_dirs: list[str] | tuple[str, ...] | None = None,
        extra_preargs: list[str] | None = None,
        extra_postargs: Iterable[str] | None = None,
    ) -> None: ...
    def create_static_lib(
        self,
        objects,
        output_libname,
        output_dir: Incomplete | None = None,
        debug: bool = False,
        target_lang: Incomplete | None = None,
    ) -> None: ...
    def link(
        self,
        target_desc,
        objects: list[str] | tuple[str, ...],
        output_filename,
        output_dir: str | None = None,
        libraries: list[str] | tuple[str, ...] | None = None,
        library_dirs: list[str] | tuple[str, ...] | None = None,
        runtime_library_dirs: list[str] | tuple[str, ...] | None = None,
        export_symbols: Incomplete | None = None,
        debug: bool = False,
        extra_preargs: Incomplete | None = None,
        extra_postargs: Incomplete | None = None,
        build_temp: Incomplete | None = None,
        target_lang: Incomplete | None = None,
    ) -> None: ...
    def library_dir_option(self, dir: str) -> str: ...
    def runtime_library_dir_option(self, dir: str) -> str | list[str]: ...  # type: ignore[override]
    def library_option(self, lib: str) -> str: ...
    def find_library_file(self, dirs, lib, debug: bool = False) -> str | None: ...
