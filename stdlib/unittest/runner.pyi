import sys
import unittest.case
import unittest.result
import unittest.suite
from collections.abc import Callable, Iterable
from typing import Any, Generic, Protocol, TextIO, TypeVar, type_check_only
from typing_extensions import Never, TypeAlias

# Build a Protocol from TextIO's methods.
# `TextTestRunner.stream` defaults to `sys.stderr` which is typed as `TextIO`
@type_check_only
class _TextIOLike(TextIO, Protocol): ...  # type: ignore[misc] # pyright: ignore[reportGeneralTypeIssues]

_ResultClassType: TypeAlias = Callable[[_TextIOLike, bool, int], unittest.result.TestResult]
_StreamT = TypeVar("_StreamT", bound=_TextIOLike, default=_TextIOLike)

# Note: doesn't actually inherit TextIO, but re-exposes all methods of the stream passed to __init__
class _WritelnDecorator(_TextIOLike):  # type: ignore[misc] # Is not abstract
    def __init__(self, stream: _TextIOLike) -> None: ...
    def __getattr__(self, attr: str) -> Any: ...  # Any attribute from the stream type passed to __init__
    def writeln(self, arg: str | None = None) -> str: ...
    # These attributes are prevented by __getattr__
    stream: Never
    __getstate__: Never

class TextTestResult(unittest.result.TestResult, Generic[_StreamT]):
    descriptions: bool  # undocumented
    dots: bool  # undocumented
    separator1: str
    separator2: str
    showAll: bool  # undocumented
    stream: _StreamT  # undocumented
    if sys.version_info >= (3, 12):
        durations: unittest.result._DurationsType | None
        def __init__(
            self, stream: _StreamT, descriptions: bool, verbosity: int, *, durations: unittest.result._DurationsType | None = None
        ) -> None: ...
    else:
        def __init__(self, stream: _StreamT, descriptions: bool, verbosity: int) -> None: ...

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
            stream: _TextIOLike | None = None,
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
            stream: _TextIOLike | None = None,
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
