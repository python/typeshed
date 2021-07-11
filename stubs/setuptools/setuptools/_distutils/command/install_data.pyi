from distutils.core import Command
from typing import Any

class install_data(Command):
    description: str
    user_options: Any
    boolean_options: Any
    install_dir: Any
    outfiles: Any
    root: Any
    force: int
    data_files: Any
    warn_dir: int
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def get_inputs(self): ...
    def get_outputs(self): ...
