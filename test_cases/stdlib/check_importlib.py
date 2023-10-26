import importlib.abc
import pathlib
import zipfile


# Assert that some Path classes are Traversable.
def traverse(t: importlib.abc.Traversable) -> None:
    pass


traverse(pathlib.Path())
traverse(zipfile.Path(""))
