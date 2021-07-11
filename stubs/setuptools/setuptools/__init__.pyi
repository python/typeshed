from typing import Any

from setuptools.depends import Require as Require
from setuptools.dist import Distribution as Distribution
from setuptools.extension import Extension as Extension

from ._deprecation_warning import SetuptoolsDeprecationWarning as SetuptoolsDeprecationWarning

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
