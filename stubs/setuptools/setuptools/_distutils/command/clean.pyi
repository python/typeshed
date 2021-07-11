from distutils.core import Command
from typing import Any

class clean(Command):
    description: str
    user_options: Any
    boolean_options: Any
    build_base: Any
    build_lib: Any
    build_temp: Any
    build_scripts: Any
    bdist_base: Any
    all: Any
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
