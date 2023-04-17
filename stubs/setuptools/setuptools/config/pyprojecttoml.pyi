import os
from _typeshed import Incomplete
from typing_extensions import TypeAlias

from ..dist import Distribution
from . import expand

_Path: TypeAlias = str | os.PathLike[Incomplete]

def load_file(filepath: _Path) -> dict[Incomplete, Incomplete]: ...
def validate(config: dict[Incomplete, Incomplete], filepath: _Path) -> bool: ...
def apply_configuration(dist: Distribution, filepath: _Path, ignore_option_errors: bool = False) -> Distribution: ...
def read_configuration(
    filepath: _Path, expand: bool = True, ignore_option_errors: bool = False, dist: Distribution | None = None
): ...
def expand_configuration(
    config: dict[Incomplete, Incomplete],
    root_dir: _Path | None = None,
    ignore_option_errors: bool = False,
    dist: Distribution | None = None,
) -> dict[Incomplete, Incomplete]: ...

class _ConfigExpander:
    config: Incomplete
    root_dir: Incomplete
    project_cfg: Incomplete
    dynamic: Incomplete
    setuptools_cfg: Incomplete
    dynamic_cfg: Incomplete
    ignore_option_errors: Incomplete
    def __init__(
        self,
        config: dict[Incomplete, Incomplete],
        root_dir: _Path | None = None,
        ignore_option_errors: bool = False,
        dist: Distribution | None = None,
    ) -> None: ...
    def expand(self): ...

class _EnsurePackagesDiscovered(expand.EnsurePackagesDiscovered):
    def __init__(
        self, distribution: Distribution, project_cfg: dict[Incomplete, Incomplete], setuptools_cfg: dict[Incomplete, Incomplete]
    ) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback): ...

class _BetaConfiguration(UserWarning): ...

class _InvalidFile(UserWarning):
    @classmethod
    def message(cls): ...
