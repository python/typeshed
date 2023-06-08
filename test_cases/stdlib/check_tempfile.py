from __future__ import annotations

import io
import sys
from tempfile import TemporaryFile
from typing_extensions import assert_type

if sys.platform != "win32":
    assert_type(TemporaryFile(), io.BufferedRandom)
    assert_type(TemporaryFile(buffering=0), io.FileIO)
    assert_type(TemporaryFile(mode="w+"), io.TextIOWrapper)
    assert_type(TemporaryFile(mode="w+b"), io.BufferedRandom)
    assert_type(TemporaryFile(mode="wb"), io.BufferedWriter)
    assert_type(TemporaryFile(mode="rb"), io.BufferedReader)
    assert_type(TemporaryFile("wb"), io.BufferedWriter)
    assert_type(TemporaryFile("wb", 0), io.FileIO)
