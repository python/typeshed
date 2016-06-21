# Stubs for unittest

# Based on http://docs.python.org/2.7/library/unittest.html

# Only a subset of functionality is included.

from typing import (
    Any, Callable, Iterable, Tuple, List, TextIO, Sequence,
    overload, TypeVar, Pattern
)
from abc import abstractmethod, ABCMeta

_T = TypeVar('_T')
_FT = TypeVar('_FT')

class Testable(metaclass=ABCMeta):
    @abstractmethod
    def run(self, result: 'TestResult') -> None: ...
    @abstractmethod
    def debug(self) -> None: ...
    @abstractmethod
    def countTestCases(self) -> int: ...

# TODO ABC for test runners?

class TestResult:
    errors = ... # type: List[Tuple[Testable, str]]
    failures = ... # type: List[Tuple[Testable, str]]
    testsRun = 0
    shouldStop = False

    def wasSuccessful(self) -> bool: ...
    def stop(self) -> None: ...
    def startTest(self, test: Testable) -> None: ...
    def stopTest(self, test: Testable) -> None: ...
    def addError(self, test: Testable,
                  err: Tuple[type, Any, Any]) -> None: ... # TODO
    def addFailure(self, test: Testable,
                    err: Tuple[type, Any, Any]) -> None: ... # TODO
    def addSuccess(self, test: Testable) -> None: ...

class _AssertRaisesBaseContext:
    expected = ... # type: Any
    failureException = ... # type: type
    obj_name = ...  # type: str
    expected_regex = ... # type: Pattern[str]

class _AssertRaisesContext(_AssertRaisesBaseContext):
    exception = ... # type: Any # TODO precise type
    def __enter__(self) -> _AssertRaisesContext: ...
    def __exit__(self, exc_type, exc_value, tb) -> bool: ...

class _AssertWarnsContext(_AssertRaisesBaseContext):
    warning = ... # type: Any # TODO precise type
    filename = ...  # type: str
    lineno = 0
    def __enter__(self) -> _AssertWarnsContext: ...
    def __exit__(self, exc_type, exc_value, tb) -> bool: ...

class TestCase(Testable):
    def __init__(self, methodName: str = ...) -> None: ...
    # TODO failureException
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def run(self, result: TestResult = ...) -> None: ...
    def debug(self) -> None: ...
    def assert_(self, expr: Any, msg: object = ...) -> None: ...
    def failUnless(self, expr: Any, msg: object = ...) -> None: ...
    def assertTrue(self, expr: Any, msg: object = ...) -> None: ...
    def assertEqual(self, first: Any, second: Any,
                    msg: object = ...) -> None: ...
    def failUnlessEqual(self, first: Any, second: Any,
                        msg: object = ...) -> None: ...
    def assertNotEqual(self, first: Any, second: Any,
                       msg: object = ...) -> None: ...
    def assertSequenceEqual(self, first: Sequence[Any], second: Sequence[Any],
                            msg: object = ...,
                            seq_type: type = ...) -> None: ...
    def failIfEqual(self, first: Any, second: Any,
                    msg: object = ...) -> None: ...
    def assertAlmostEqual(self, first: float, second: float, places: int = ...,
                          msg: object = ...,
                          delta: float = ...) -> None: ...
    def failUnlessAlmostEqual(self, first: float, second: float,
                              places: int = ...,
                              msg: object = ...) -> None: ...
    def assertNotAlmostEqual(self, first: float, second: float,
                             places: int = ..., msg: object = ...,
                             delta: float = ...) -> None: ...
    def failIfAlmostEqual(self, first: float, second: float, places: int = ...,
                          msg: object = ...) -> None: ...
    def assertGreater(self, first: Any, second: Any,
                      msg: object = ...) -> None: ...
    def assertGreaterEqual(self, first: Any, second: Any,
                      msg: object = ...) -> None: ...
    def assertListEqual(self, first: List[Any], second: List[Any],
                      msg: object = ...) -> None: ...
    def assertLess(self, first: Any, second: Any,
                   msg: object = ...) -> None: ...
    def assertLessEqual(self, first: Any, second: Any,
                        msg: object = ...) -> None: ...
    def assertRaises(self, expected_exception: type, *args: Any, **kwargs: Any) -> Any: ...
    def failIf(self, expr: Any, msg: object = ...) -> None: ...
    def assertFalse(self, expr: Any, msg: object = ...) -> None: ...
    def assertIs(self, first: object, second: object,
                 msg: object = ...) -> None: ...
    def assertIsNot(self, first: object, second: object,
                    msg: object = ...) -> None: ...
    def assertIsNone(self, expr: Any, msg: object = ...) -> None: ...
    def assertIsNotNone(self, expr: Any, msg: object = ...) -> None: ...
    def assertIn(self, first: _T, second: Iterable[_T],
                 msg: object = ...) -> None: ...
    def assertNotIn(self, first: _T, second: Iterable[_T],
                    msg: object = ...) -> None: ...
    def assertIsInstance(self, obj: Any, cls: type,
                         msg: object = ...) -> None: ...
    def assertNotIsInstance(self, obj: Any, cls: type,
                            msg: object = ...) -> None: ...
    def assertWarns(self, expected_warning: type, callable_obj: Any = ...,
                    *args: Any, **kwargs: Any) -> _AssertWarnsContext: ...
    def fail(self, msg: object = ...) -> None: ...
    def countTestCases(self) -> int: ...
    def defaultTestResult(self) -> TestResult: ...
    def id(self) -> str: ...
    def shortDescription(self) -> str: ... # May return None
    def addCleanup(function: Any, *args: Any, **kwargs: Any) -> None: ...
    def skipTest(self, reason: Any) -> None: ...

    assertEquals = assertEqual
    assertNotEquals = assertNotEqual
    assertAlmostEquals = assertAlmostEqual
    assertNotAlmostEquals = assertNotAlmostEqual
    assert_ = assertTrue

    failUnlessEqual = assertEqual
    failIfEqual = assertNotEqual
    failUnlessAlmostEqual = assertAlmostEqual
    failIfAlmostEqual = assertNotAlmostEqual
    failUnless = assertTrue
    failUnlessRaises = assertRaises
    failIf = assertFalse

class CallableTestCase(Testable):
    def __init__(self, testFunc: Callable[[], None],
                 setUp: Callable[[], None] = ...,
                 tearDown: Callable[[], None] = ...,
                 description: str = ...) -> None: ...
    def run(self, result: TestResult) -> None: ...
    def debug(self) -> None: ...
    def countTestCases(self) -> int: ...

class TestSuite(Testable):
    def __init__(self, tests: Iterable[Testable] = ...) -> None: ...
    def addTest(self, test: Testable) -> None: ...
    def addTests(self, tests: Iterable[Testable]) -> None: ...
    def run(self, result: TestResult) -> None: ...
    def debug(self) -> None: ...
    def countTestCases(self) -> int: ...

# TODO TestLoader
# TODO defaultTestLoader

class TextTestRunner:
    def __init__(self, stream: TextIO = ..., descriptions: bool = ...,
                 verbosity: int = ..., failfast: bool = ...) -> None: ...

class SkipTest(Exception):
    ...

# TODO precise types
def skipUnless(condition: Any, reason: str) -> Any: ...
def skipIf(condition: Any, reason: str) -> Any: ...
def expectedFailure(func: _FT) -> _FT: ...
def skip(reason: str) -> Any: ...

def main(module: str = ..., defaultTest: str = ...,
         argv: List[str] = ..., testRunner: Any = ...,
         testLoader: Any = ...) -> None: ... # TODO types
