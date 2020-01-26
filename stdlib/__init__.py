"""A simple package that returns the path to the stdlib stubs folder."""

__version__ = '1.0a1'

import pathlib

def get_stdlib_dir() -> pathlib.Path:
    return pathlib.Path(__file__).parent
