from typing import List, Optional, Tuple, Type
from types import TracebackType
import unittest.case


_SysExcInfoType = Union[
    Tuple[Type[BaseException], BaseException, types.TracebackType],
    Tuple[None, None, None],
]


class TestResult:
    errors: List[Tuple[unittest.case.TestCase, str]]
    failures: List[Tuple[unittest.case.TestCase, str]]
    skipped: List[Tuple[unittest.case.TestCase, str]]
    expectedFailures: List[Tuple[unittest.case.TestCase, str]]
    unexpectedSuccesses: List[unittest.case.TestCase]
    shouldStop: bool
    testsRun: int
    buffer: bool
    failfast: bool
    tb_locals: bool
    def wasSuccessful(self) -> bool: ...
    def stop(self) -> None: ...
    def startTest(self, test: unittest.case.TestCase) -> None: ...
    def stopTest(self, test: unittest.case.TestCase) -> None: ...
    def startTestRun(self) -> None: ...
    def stopTestRun(self) -> None: ...
    def addError(self, test: unittest.case.TestCase, err: _SysExcInfoType) -> None: ...
    def addFailure(self, test: unittest.case.TestCase, err: _SysExcInfoType) -> None: ...
    def addSuccess(self, test: unittest.case.TestCase) -> None: ...
    def addSkip(self, test: unittest.case.TestCase, reason: str) -> None: ...
    def addExpectedFailure(self, test: unittest.case.TestCase,
                           err: _SysExcInfoType) -> None: ...
    def addUnexpectedSuccess(self, test: unittest.case.TestCase) -> None: ...
    def addSubTest(self, test: unittest.case.TestCase, subtest: unittest.case.TestCase,
                   outcome: Optional[_SysExcInfoType]) -> None: ...
