from distutils.core import Command as _Command
from typing import Any

from ._deprecation_warning import SetuptoolsDeprecationWarning as SetuptoolsDeprecationWarning
from .depends import Require as Require
from .dist import Distribution as Distribution
from .extension import Extension as Extension

__version__: str

class PackageFinder:
    @classmethod
    def find(cls, where: str = ..., exclude=..., include=...): ...

class PEP420PackageFinder(PackageFinder): ...

find_packages: Any
find_namespace_packages: Any

def setup(**attrs): ...

class Command(_Command):
    __doc__: Any
    command_consumes_arguments: bool
    def __init__(self, dist, **kw) -> None: ...
    def ensure_string_list(self, option) -> None: ...
    def reinitialize_command(self, command, reinit_subcommands: int = ..., **kw): ...

class sic(str): ...
