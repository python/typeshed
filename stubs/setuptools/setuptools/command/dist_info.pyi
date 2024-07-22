from _typeshed import Incomplete
from typing import ClassVar

from .._distutils.cmd import Command

class dist_info(Command):
    description: str
    user_options: Incomplete
    boolean_options: ClassVar[list[str]]
    negative_opt: ClassVar[dict[str, str]]
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
