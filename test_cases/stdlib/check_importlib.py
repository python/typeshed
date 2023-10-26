import importlib.abc
import pathlib
import sys
import zipfile

# Assert that some Path classes are Traversable.
if sys.version_info >= (3, 9):

    def traverse(t: importlib.abc.Traversable) -> None:
        pass

    traverse(pathlib.Path())
    traverse(zipfile.Path(""))
