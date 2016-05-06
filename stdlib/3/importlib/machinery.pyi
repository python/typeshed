# Stubs for importlib.machinery (Python 3.4)

from ._bootstrap import SOURCE_SUFFIXES as SOURCE_SUFFIXES, DEBUG_BYTECODE_SUFFIXES as DEBUG_BYTECODE_SUFFIXES, OPTIMIZED_BYTECODE_SUFFIXES as OPTIMIZED_BYTECODE_SUFFIXES, BYTECODE_SUFFIXES as BYTECODE_SUFFIXES, EXTENSION_SUFFIXES as EXTENSION_SUFFIXES
from ._bootstrap import ModuleSpec as ModuleSpec
from ._bootstrap import BuiltinImporter as BuiltinImporter
from ._bootstrap import FrozenImporter as FrozenImporter
from ._bootstrap import WindowsRegistryFinder as WindowsRegistryFinder
from ._bootstrap import PathFinder as PathFinder
from ._bootstrap import FileFinder as FileFinder
from ._bootstrap import SourceFileLoader as SourceFileLoader
from ._bootstrap import SourcelessFileLoader as SourcelessFileLoader
from ._bootstrap import ExtensionFileLoader as ExtensionFileLoader

from typing import List

def all_suffixes() -> List[str]: ...
