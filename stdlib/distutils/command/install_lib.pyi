from typing import Any, ClassVar

from ..cmd import Command

PYTHON_SOURCE_EXTENSION: str

class install_lib(Command):
    description: str
    user_options: ClassVar[list[tuple[str, str | None, str]]]
    boolean_options: ClassVar[list[str]]
    negative_opt: ClassVar[dict[str, str]]
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
