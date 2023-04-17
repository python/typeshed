from _typeshed import Incomplete
from enum import Enum
from pathlib import Path
from typing import Protocol
from typing_extensions import TypeAlias

from .. import Command, errors, namespaces
from ..dist import Distribution

# Actually from wheel.wheelfile import _WheelFile
_WheelFile: TypeAlias = Incomplete
_Path: TypeAlias = str | Path

class _EditableMode(Enum):
    STRICT: str
    LENIENT: str
    COMPAT: str
    @classmethod
    def convert(cls, mode: str | None) -> _EditableMode: ...

class editable_wheel(Command):
    description: str
    user_options: Incomplete
    dist_dir: Incomplete
    dist_info_dir: Incomplete
    project_dir: Incomplete
    mode: Incomplete
    def initialize_options(self) -> None: ...
    package_dir: Incomplete
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...

class EditableStrategy(Protocol):
    def __call__(self, wheel: _WheelFile, files: list[str], mapping: dict[str, str]): ...
    def __enter__(self) -> None: ...
    def __exit__(self, _exc_type, _exc_value, _traceback) -> None: ...

class _StaticPth:
    dist: Incomplete
    name: Incomplete
    path_entries: Incomplete
    def __init__(self, dist: Distribution, name: str, path_entries: list[Path]) -> None: ...
    def __call__(self, wheel: _WheelFile, files: list[str], mapping: dict[str, str]): ...
    def __enter__(self): ...
    def __exit__(self, _exc_type, _exc_value, _traceback) -> None: ...

class _LinkTree(_StaticPth):
    auxiliary_dir: Incomplete
    build_lib: Incomplete
    def __init__(self, dist: Distribution, name: str, auxiliary_dir: _Path, build_lib: _Path) -> None: ...
    def __call__(self, wheel: _WheelFile, files: list[str], mapping: dict[str, str]): ...
    def __enter__(self): ...
    def __exit__(self, _exc_type, _exc_value, _traceback) -> None: ...

class _TopLevelFinder:
    dist: Incomplete
    name: Incomplete
    def __init__(self, dist: Distribution, name: str) -> None: ...
    def __call__(self, wheel: _WheelFile, files: list[str], mapping: dict[str, str]): ...
    def __enter__(self): ...
    def __exit__(self, _exc_type, _exc_value, _traceback) -> None: ...

class _NamespaceInstaller(namespaces.Installer):
    distribution: Incomplete
    src_root: Incomplete
    installation_dir: Incomplete
    editable_name: Incomplete
    outputs: Incomplete
    dry_run: bool
    def __init__(self, distribution, installation_dir, editable_name, src_root) -> None: ...

class InformationOnly(UserWarning): ...
class LinksNotSupported(errors.FileError): ...

class _DebuggingTips(InformationOnly):
    @classmethod
    def warn(cls, project: str): ...
