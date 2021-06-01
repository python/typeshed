from distutils.cmd import Command
from typing import Tuple

SCHEME_KEYS: Tuple[str, ...]

class install(Command):
    user: bool
    prefix: str | None
    home: str | None
    root: str | None
    install_lib: str | None
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
