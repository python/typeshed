from __future__ import annotations

import distutils.command.sdist
from _typeshed import StrPath
from pathlib import Path
from typing import List

from setuptools._distutils.ccompiler import CCompiler

c = distutils.command.sdist.sdist

# Test CCompiler().compile with varied sources

compiler = CCompiler()
compiler.compile(sources=["file1.c", "file2.c"])

paths: List[StrPath] = [Path("file1.c"), Path("file2.c")]
compiler.compile(sources=paths)

mixed: List[StrPath] = [Path("file1.c"), "file2.c"]
compiler.compile(sources=mixed)
