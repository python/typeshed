from distutils.core import Command
from distutils.errors import *
from typing import Any

class bdist_wininst(Command):
    description: str
    user_options: Any
    boolean_options: Any
    def __init__(self, *args, **kw) -> None: ...
    bdist_dir: Any
    plat_name: Any
    keep_temp: int
    no_target_compile: int
    no_target_optimize: int
    target_version: Any
    dist_dir: Any
    bitmap: Any
    title: Any
    skip_build: Any
    install_script: Any
    pre_install_script: Any
    user_access_control: Any
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def get_inidata(self): ...
    def create_exe(self, arcname, fullname, bitmap: Any | None = ...) -> None: ...
    def get_installer_filename(self, fullname): ...
    def get_exe_bytes(self): ...
