import sys
import unittest.case
import unittest.result
import unittest.suite
from collections.abc import Callable, Iterable
from typing import Any, TextIO
from typing_extensions import TypeAlias

_ResultClassType: TypeAlias = Callable[[TextIO, bool, int], unittest.result.TestResult]

# Note: doesn't actually inherit TextIO, but re-exposes all methods of the stream passed to __init__
class _WritelnDecorator(TextIO):
    def __init__(self, stream: TextIO) -> None: ...
    def __getattr__(self, attr: str) -> Any: ...  # Any attribute from the stream type passed to __init__
    def writeln(self, arg: str | None = None) -> str: ...

class TextTestResult(unittest.result.TestResult):
    descriptions: bool  # undocumented
    dots: bool  # undocumented
    separator1: str
    separator2: str
    showAll: bool  # undocumented
    stream: TextIO  # undocumented
    if sys.version_info >= (3, 12):
        durations: unittest.result._DurationsType | None
        def __init__(
            self, stream: TextIO, descriptions: bool, verbosity: int, *, durations: unittest.result._DurationsType | None = None
        ) -> None: ...
    else:
        def __init__(self, stream: TextIO, descriptions: bool, verbosity: int) -> None: ...

    def getDescription(self, test: unittest.case.TestCase) -> str: ...
    def printErrorList(self, flavour: str, errors: Iterable[tuple[unittest.case.TestCase, str]]) -> None: ...

class TextTestRunner:
    resultclass: _ResultClassType
    stream: _WritelnDecorator
    descriptions: bool
    verbosity: int
    failfast: bool
    buffer: bool
    warnings: str | None
    tb_locals: bool

    if sys.version_info >= (3, 12):
        durations: unittest.result._DurationsType | None
        def __init__(
            self,
            stream: TextIO | None = None,
            descriptions: bool = True,
            verbosity: int = 1,
            failfast: bool = False,
            buffer: bool = False,
            resultclass: _ResultClassType | None = None,
            warnings: str | None = None,
            *,
            tb_locals: bool = False,
            durations: unittest.result._DurationsType | None = None,
        ) -> None: ...
    else:
        def __init__(
            self,
            stream: TextIO | None = None,
            descriptions: bool = True,
            verbosity: int = 1,
            failfast: bool = False,
            buffer: bool = False,
            resultclass: _ResultClassType | None = None,
            warnings: str | None = None,
            *,
            tb_locals: bool = False,
        ) -> None: ...

    def _makeResult(self) -> unittest.result.TestResult: ...
    def run(self, test: unittest.suite.TestSuite | unittest.case.TestCase) -> unittest.result.TestResult: ...
