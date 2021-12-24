from collections.abc import Iterable, Iterator
import unittest.case
import unittest.result
from typing import Union

_TestType = Union[unittest.case.TestCase, TestSuite]

class BaseTestSuite(Iterable[_TestType]):
    _tests: list[unittest.case.TestCase]
    _removed_tests: int
    def __init__(self, tests: Iterable[_TestType] = ...) -> None: ...
    def __call__(self, result: unittest.result.TestResult) -> unittest.result.TestResult: ...
    def addTest(self, test: _TestType) -> None: ...
    def addTests(self, tests: Iterable[_TestType]) -> None: ...
    def run(self, result: unittest.result.TestResult) -> unittest.result.TestResult: ...
    def debug(self) -> None: ...
    def countTestCases(self) -> int: ...
    def __iter__(self) -> Iterator[_TestType]: ...

class TestSuite(BaseTestSuite):
    def run(self, result: unittest.result.TestResult, debug: bool = ...) -> unittest.result.TestResult: ...
