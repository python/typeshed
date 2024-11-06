from pathlib import Path

from setuptools import Extension

# Dummy extensions
ext1 = Extension(name="test1", sources=["file1.c", "file2.c"])  # list of str(s)
ext2 = Extension(name="test2", sources=[Path("file1.c"), Path("file2.c")])  # list of Path(s)
ext3 = Extension(name="test3", sources=[Path("file1.c"), "file2.c"])  # mixed str(s) and Path(s)
