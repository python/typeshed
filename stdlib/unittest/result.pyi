import unittest.case
from _typeshed import OptExcInfo
from collections.abc import Callable
from typing import Any, TextIO, TypeVar

_F = TypeVar("_F", bound=Callable[..., Any])

STDOUT_LINE: str
STDERR_LINE: str

# undocumented
def failfast(method: _F) -> _F: ...

class TestResult:
    errors: list[tuple[unittest.case.TestCase, str]]
    failures: list[tuple[unittest.case.TestCase, str]]
    skipped: list[tuple[unittest.case.TestCase, str]]
    expectedFailures: list[tuple[unittest.case.TestCase, str]]
    unexpectedSuccesses: list[unittest.case.TestCase]
    shouldStop: bool
    testsRun: int
    buffer: bool
    failfast: bool
    tb_locals: bool
    def __init__(self, stream: TextIO | None = None, descriptions: bool | None = None, verbosity: int | None = None) -> None: ...
    def printErrors(self) -> None: ...
    def wasSuccessful(self) -> bool: ...
    def stop(self) -> None: ...
    def startTest(self, test: unittest.case.TestCase) -> None: ...
    def stopTest(self, test: unittest.case.TestCase) -> None: ...
    def startTestRun(self) -> None: ...
    def stopTestRun(self) -> None: ...
    def addError(self, test: unittest.case.TestCase, err: OptExcInfo) -> None: ...
    def addFailure(self, test: unittest.case.TestCase, err: OptExcInfo) -> None: ...
    def addSuccess(self, test: unittest.case.TestCase) -> None: ...
    def addSkip(self, test: unittest.case.TestCase, reason: str) -> None: ...
    def addExpectedFailure(self, test: unittest.case.TestCase, err: OptExcInfo) -> None: ...
    def addUnexpectedSuccess(self, test: unittest.case.TestCase) -> None: ...
    def addSubTest(self, test: unittest.case.TestCase, subtest: unittest.case.TestCase, err: OptExcInfo | None) -> None: ...
