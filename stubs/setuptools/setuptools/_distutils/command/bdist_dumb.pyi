from distutils.core import Command
from distutils.errors import *
from typing import Any

class bdist_dumb(Command):
    description: str
    user_options: Any
    boolean_options: Any
    default_format: Any
    bdist_dir: Any
    plat_name: Any
    format: Any
    keep_temp: int
    dist_dir: Any
    skip_build: Any
    relative: int
    owner: Any
    group: Any
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
