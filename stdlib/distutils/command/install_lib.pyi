from typing import Any, Final

from ..cmd import Command

PYTHON_SOURCE_EXTENSION: Final[str]

class install_lib(Command):
    description: str
    user_options: Any
    boolean_options: Any
    negative_opt: Any
    install_dir: Any
    build_dir: Any
    force: int
    compile: Any
    optimize: Any
    skip_build: Any
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def build(self) -> None: ...
    def install(self): ...
    def byte_compile(self, files) -> None: ...
    def get_outputs(self): ...
    def get_inputs(self): ...
