from _typeshed import Incomplete, StrPath, Unused
from typing import ClassVar

from setuptools.dist import Distribution

from .._distutils.cmd import _StrPathT
from .._distutils.command import build_py as orig

def make_writable(target) -> None: ...

class build_py(orig.build_py):
    distribution: Distribution  # override distutils.dist.Distribution with setuptools.dist.Distribution
    editable_mode: ClassVar[bool]
    package_data: dict[str, list[str]]
    exclude_package_data: dict[Incomplete, Incomplete]
    def finalize_options(self) -> None: ...
    def copy_file(  # type: ignore[override] # No overload, str support only
        self,
        infile: StrPath,
        outfile: _StrPathT,
        preserve_mode: bool = True,
        preserve_times: bool = True,
        link: str | None = None,
        level: Unused = 1,
    ) -> tuple[_StrPathT | str, bool]: ...
    def run(self) -> None: ...
    data_files: list[tuple[str, str, str, list[str]]]
    def __getattr__(self, attr: str): ...
    def get_data_files_without_manifest(self) -> list[tuple[str, str, str, list[str]]]: ...
    def find_data_files(self, package, src_dir) -> list[str]: ...
    def get_outputs(self, include_bytecode: bool = True) -> list[str]: ...  # type: ignore[override] # Using a real boolean instead of 0|1
    def build_package_data(self) -> None: ...
    manifest_files: dict[str, list[str]]
    def get_output_mapping(self) -> dict[str, str]: ...
    def analyze_manifest(self) -> None: ...
    def get_data_files(self) -> None: ...
    def check_package(self, package, package_dir): ...
    def initialize_options(self) -> None: ...
    packages_checked: dict[Incomplete, Incomplete]
    def get_package_dir(self, package: str) -> str: ...
    def exclude_data_files(self, package, src_dir, files): ...

def assert_relative(path): ...
