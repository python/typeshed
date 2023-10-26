import importlib.abc
import pathlib
import zipfile


# Assert that some Path classes are Traversable.
def traverse(t: importlib.abc.Traversable) -> None:
    pass


p1: pathlib.Path
traverse(p1)
p2: zipfile.Path
traverse(p2)
