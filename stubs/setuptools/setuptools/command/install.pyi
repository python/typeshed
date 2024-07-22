from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any

from .._distutils.command import install as orig

class install(orig.install):
    user_options: Incomplete
    boolean_options: Incomplete
    # Any to work around variance issues
    new_commands: list[tuple[str, Callable[[Any], bool]] | None]
    old_and_unmanageable: Incomplete
    single_version_externally_managed: Incomplete
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    path_file: Incomplete
    extra_dirs: str
    def handle_extra_path(self): ...
    def run(self): ...
    def do_egg_install(self) -> None: ...
