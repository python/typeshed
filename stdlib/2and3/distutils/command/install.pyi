from distutils.cmd import Command
from typing import Union, Optional


class install(Command):
    user: Union[int, bool]
    prefix: Optional[str]
    home: Optional[str]
    root: Optional[str]
    install_lib: Optional[str]

    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
