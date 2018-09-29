# Stubs for unittest

from typing import (
    Any, AnyStr, Callable, Container, ContextManager, Dict, FrozenSet, Generic, Iterable,
    Iterator, List, NoReturn, Optional, overload, Pattern, Sequence, Set, TextIO,
    Tuple, Type, TypeVar, Union
)
import logging
import sys
from types import ModuleType, TracebackType


_T = TypeVar('_T')
_FT = TypeVar('_FT', bound=Callable[..., Any])
_E = TypeVar('_E', bound=Exception)


def expectedFailure(func: _FT) -> _FT: ...
def skip(reason: str) -> Callable[[_FT], _FT]: ...
def skipIf(condition: object, reason: str) -> Callable[[_FT], _FT]: ...
def skipUnless(condition: object, reason: str) -> Callable[[_FT], _FT]: ...

class SkipTest(Exception):
    def __init__(self, reason: str) -> None: ...


class TestCase:
    failureException = ...  # type: Type[BaseException]
    longMessage = ...  # type: bool
    maxDiff = ...  # type: Optional[int]
    # undocumented
    _testMethodName = ...  # type: str
    def __init__(self, methodName: str = ...) -> None: ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    @classmethod
    def setUpClass(cls) -> None: ...
    @classmethod
    def tearDownClass(cls) -> None: ...
    def run(self, result: Optional[TestResult] = ...) -> TestCase: ...
    def skipTest(self, reason: Any) -> None: ...
    def subTest(self, msg: Any = ..., **params: Any) -> ContextManager[None]: ...
    def debug(self) -> None: ...
    def assertEqual(self, first: Any, second: Any, msg: Any = ...) -> None: ...
    def assertNotEqual(self, first: Any, second: Any,
                       msg: Any = ...) -> None: ...
    def assertTrue(self, expr: Any, msg: Any = ...) -> None: ...
    def assertFalse(self, expr: Any, msg: Any = ...) -> None: ...
    def assertIs(self, first: Any, second: Any, msg: Any = ...) -> None: ...
    def assertIsNot(self, first: Any, second: Any,
                    msg: Any = ...) -> None: ...
    def assertIsNone(self, expr: Any, msg: Any = ...) -> None: ...
    def assertIsNotNone(self, expr: Any, msg: Any = ...) -> None: ...
    def assertIn(self, member: Any,
                 container: Union[Iterable[Any], Container[Any]],
                 msg: Any = ...) -> None: ...
    def assertNotIn(self, member: Any,
                    container: Union[Iterable[Any], Container[Any]],
                    msg: Any = ...) -> None: ...
    def assertIsInstance(self, obj: Any,
                         cls: Union[type, Tuple[type, ...]],
                         msg: Any = ...) -> None: ...
    def assertNotIsInstance(self, obj: Any,
                            cls: Union[type, Tuple[type, ...]],
                            msg: Any = ...) -> None: ...
    def assertGreater(self, first: Any, second: Any,
                      msg: Any = ...) -> None: ...
    def assertGreaterEqual(self, first: Any, second: Any,
                           msg: Any = ...) -> None: ...
    def assertLess(self, first: Any, second: Any, msg: Any = ...) -> None: ...
    def assertLessEqual(self, first: Any, second: Any,
                        msg: Any = ...) -> None: ...
    @overload
    def assertRaises(self,  # type: ignore
                     exception: Union[Type[BaseException], Tuple[Type[BaseException], ...]],
                     callable: Callable[..., Any],
                     *args: Any, **kwargs: Any) -> None: ...
    @overload
    def assertRaises(self,
                     exception: Union[Type[_E], Tuple[Type[_E], ...]],
                     msg: Any = ...) -> _AssertRaisesContext[_E]: ...
    @overload
    def assertRaisesRegex(self,  # type: ignore
                          exception: Union[Type[BaseException], Tuple[Type[BaseException], ...]],
                          callable: Callable[..., Any],
                          *args: Any, **kwargs: Any) -> None: ...
    @overload
    def assertRaisesRegex(self,
                          exception: Union[Type[_E], Tuple[Type[_E], ...]],
                          msg: Any = ...) -> _AssertRaisesContext[_E]: ...
    @overload
    def assertWarns(self,  # type: ignore
                    exception: Union[Type[Warning], Tuple[Type[Warning], ...]],
                    callable: Callable[..., Any],
                    *args: Any, **kwargs: Any) -> None: ...
    @overload
    def assertWarns(self,
                    exception: Union[Type[Warning], Tuple[Type[Warning], ...]],
                    msg: Any = ...) -> _AssertWarnsContext: ...
    @overload
    def assertWarnsRegex(self,  # type: ignore
                         exception: Union[Type[Warning], Tuple[Type[Warning], ...]],
                         callable: Callable[..., Any],
                         *args: Any, **kwargs: Any) -> None: ...
    @overload
    def assertWarnsRegex(self,
                         exception: Union[Type[Warning], Tuple[Type[Warning], ...]],
                         msg: Any = ...) -> _AssertWarnsContext: ...
    def assertLogs(
        self, logger: Optional[logging.Logger] = ...,
        level: Union[int, str, None] = ...
    ) -> _AssertLogsContext: ...
    def assertAlmostEqual(self, first: float, second: float, places: int = ...,
                          msg: Any = ..., delta: float = ...) -> None: ...
    def assertNotAlmostEqual(self, first: float, second: float,
                             places: int = ..., msg: Any = ...,
                             delta: float = ...) -> None: ...
    def assertRegex(self, text: AnyStr, regex: Union[AnyStr, Pattern[AnyStr]],
                    msg: Any = ...) -> None: ...
    def assertNotRegex(self, text: AnyStr, regex: Union[AnyStr, Pattern[AnyStr]],
                       msg: Any = ...) -> None: ...
    def assertCountEqual(self, first: Iterable[Any], second: Iterable[Any],
                         msg: Any = ...) -> None: ...
    def addTypeEqualityFunc(self, typeobj: Type[Any],
                            function: Callable[..., None]) -> None: ...
    def assertMultiLineEqual(self, first: str, second: str,
                             msg: Any = ...) -> None: ...
    def assertSequenceEqual(self, first: Sequence[Any], second: Sequence[Any],
                            msg: Any = ...,
                            seq_type: Type[Sequence[Any]] = ...) -> None: ...
    def assertListEqual(self, first: List[Any], second: List[Any],
                        msg: Any = ...) -> None: ...
    def assertTupleEqual(self, first: Tuple[Any, ...], second: Tuple[Any, ...],
                         msg: Any = ...) -> None: ...
    def assertSetEqual(self, first: Union[Set[Any], FrozenSet[Any]],
                       second: Union[Set[Any], FrozenSet[Any]], msg: Any = ...) -> None: ...
    def assertDictEqual(self, first: Dict[Any, Any], second: Dict[Any, Any],
                        msg: Any = ...) -> None: ...
    def fail(self, msg: Any = ...) -> NoReturn: ...
    def countTestCases(self) -> int: ...
    def defaultTestResult(self) -> TestResult: ...
    def id(self) -> str: ...
    def shortDescription(self) -> Optional[str]: ...
    def addCleanup(self, function: Callable[..., Any], *args: Any,
                   **kwargs: Any) -> None: ...
    def doCleanups(self) -> None: ...
    def _formatMessage(self, msg: Optional[str], standardMsg: str) -> str: ...  # undocumented
    def _getAssertEqualityFunc(self, first: Any, second: Any) -> Callable[..., None]: ...  # undocumented
    # below is deprecated
    def failUnlessEqual(self, first: Any, second: Any,
                        msg: Any = ...) -> None: ...
    def assertEquals(self, first: Any, second: Any, msg: Any = ...) -> None: ...
    def failIfEqual(self, first: Any, second: Any, msg: Any = ...) -> None: ...
    def assertNotEquals(self, first: Any, second: Any,
                        msg: Any = ...) -> None: ...
    def failUnless(self, expr: bool, msg: Any = ...) -> None: ...
    def assert_(self, expr: bool, msg: Any = ...) -> None: ...
    def failIf(self, expr: bool, msg: Any = ...) -> None: ...
    @overload
    def failUnlessRaises(self,  # type: ignore
                         exception: Union[Type[BaseException], Tuple[Type[BaseException], ...]],
                         callable: Callable[..., Any] = ...,
                         *args: Any, **kwargs: Any) -> None: ...
    @overload
    def failUnlessRaises(self,
                         exception: Union[Type[_E], Tuple[Type[_E], ...]],
                         msg: Any = ...) -> _AssertRaisesContext[_E]: ...
    def failUnlessAlmostEqual(self, first: float, second: float,
                              places: int = ..., msg: Any = ...) -> None: ...
    def assertAlmostEquals(self, first: float, second: float, places: int = ...,
                           msg: Any = ..., delta: float = ...) -> None: ...
    def failIfAlmostEqual(self, first: float, second: float, places: int = ...,
                          msg: Any = ...) -> None: ...
    def assertNotAlmostEquals(self, first: float, second: float,
                              places: int = ..., msg: Any = ...,
                              delta: float = ...) -> None: ...
    def assertRegexpMatches(self, text: AnyStr, regex: Union[AnyStr, Pattern[AnyStr]],
                            msg: Any = ...) -> None: ...
    @overload
    def assertRaisesRegexp(self,  # type: ignore
                           exception: Union[Type[BaseException], Tuple[Type[BaseException], ...]],
                           callable: Callable[..., Any] = ...,
                           *args: Any, **kwargs: Any) -> None: ...
    @overload
    def assertRaisesRegexp(self,
                           exception: Union[Type[_E], Tuple[Type[_E], ...]],
                           msg: Any = ...) -> _AssertRaisesContext[_E]: ...

class FunctionTestCase(TestCase):
    def __init__(self, testFunc: Callable[[], None],
                 setUp: Optional[Callable[[], None]] = ...,
                 tearDown: Optional[Callable[[], None]] = ...,
                 description: Optional[str] = ...) -> None: ...

class _AssertRaisesContext(Generic[_E]):
    exception = ...  # type: _E
    def __enter__(self) -> _AssertRaisesContext[_E]: ...
    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]) -> bool: ...

class _AssertWarnsContext:
    warning = ...  # type: Warning
    filename = ...  # type: str
    lineno = ...  # type: int
    def __enter__(self) -> _AssertWarnsContext: ...
    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]) -> bool: ...

class _AssertLogsContext:
    records = ...  # type: List[logging.LogRecord]
    output = ...  # type: List[str]
    def __enter__(self) -> _AssertLogsContext: ...
    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]) -> bool: ...


_TestType = Union[TestCase, TestSuite]

class TestSuite(Iterable[_TestType]):
    def __init__(self, tests: Iterable[_TestType] = ...) -> None: ...
    def addTest(self, test: _TestType) -> None: ...
    def addTests(self, tests: Iterable[_TestType]) -> None: ...
    def run(self, result: TestResult) -> TestResult: ...
    def debug(self) -> None: ...
    def countTestCases(self) -> int: ...
    def __iter__(self) -> Iterator[_TestType]: ...


class TestLoader:
    if sys.version_info >= (3, 5):
        errors = ...  # type: List[Type[BaseException]]
    testMethodPrefix = ...  # type: str
    sortTestMethodsUsing = ...  # type: Callable[[str, str], bool]
    suiteClass = ...  # type: Callable[[List[TestCase]], TestSuite]
    def loadTestsFromTestCase(self,
                              testCaseClass: Type[TestCase]) -> TestSuite: ...
    if sys.version_info >= (3, 5):
        def loadTestsFromModule(self, module: ModuleType,
                                *, pattern: Any = ...) -> TestSuite: ...
    else:
        def loadTestsFromModule(self,
                                module: ModuleType) -> TestSuite: ...
    def loadTestsFromName(self, name: str,
                          module: Optional[ModuleType] = ...) -> TestSuite: ...
    def loadTestsFromNames(self, names: Sequence[str],
                           module: Optional[ModuleType] = ...) -> TestSuite: ...
    def getTestCaseNames(self,
                         testCaseClass: Type[TestCase]) -> Sequence[str]: ...
    def discover(self, start_dir: str, pattern: str = ...,
                 top_level_dir: Optional[str] = ...) -> TestSuite: ...

_SysExcInfoType = Tuple[Optional[Type[BaseException]],
                        Optional[BaseException],
                        Optional[TracebackType]]

class TestResult:
    errors = ...  # type: List[Tuple[TestCase, str]]
    failures = ...  # type: List[Tuple[TestCase, str]]
    skipped = ...  # type: List[Tuple[TestCase, str]]
    expectedFailures = ...  # type: List[Tuple[TestCase, str]]
    unexpectedSuccesses = ...  # type: List[TestCase]
    shouldStop = ...  # type: bool
    testsRun = ...  # type: int
    buffer = ...  # type: bool
    failfast = ...  # type: bool
    tb_locals = ...  # type: bool
    def wasSuccessful(self) -> bool: ...
    def stop(self) -> None: ...
    def startTest(self, test: TestCase) -> None: ...
    def stopTest(self, test: TestCase) -> None: ...
    def startTestRun(self) -> None: ...
    def stopTestRun(self) -> None: ...
    def addError(self, test: TestCase, err: _SysExcInfoType) -> None: ...
    def addFailure(self, test: TestCase, err: _SysExcInfoType) -> None: ...
    def addSuccess(self, test: TestCase) -> None: ...
    def addSkip(self, test: TestCase, reason: str) -> None: ...
    def addExpectedFailure(self, test: TestCase,
                           err: _SysExcInfoType) -> None: ...
    def addUnexpectedSuccess(self, test: TestCase) -> None: ...
    def addSubTest(self, test: TestCase, subtest: TestCase,
                   outcome: Optional[_SysExcInfoType]) -> None: ...

class TextTestResult(TestResult):
    def __init__(self, stream: TextIO, descriptions: bool,
                 verbosity: int) -> None: ...
_TextTestResult = TextTestResult

defaultTestLoader = ...  # type: TestLoader

_ResultClassType = Callable[[TextIO, bool, int], TestResult]

class TestRunner:
    def run(self, test: Union[TestSuite, TestCase]) -> TestResult: ...

class TextTestRunner(TestRunner):
    if sys.version_info >= (3, 5):
        def __init__(self, stream: Optional[TextIO] = ...,
                     descriptions: bool = ..., verbosity: int = ...,
                     failfast: bool = ..., buffer: bool = ...,
                     resultclass: Optional[_ResultClassType] = ...,
                     warnings: Optional[Type[Warning]] = ...,
                     *, tb_locals: bool = ...) -> None: ...
    else:
        def __init__(self,
                     stream: Optional[TextIO] = ...,
                     descriptions: bool = ..., verbosity: int = ...,
                     failfast: bool = ..., buffer: bool = ...,
                     resultclass: Optional[_ResultClassType] = ...,
                     warnings: Optional[Type[Warning]] = ...) -> None: ...
    def _makeResult(self) -> TestResult: ...

# not really documented
class TestProgram:
    result = ...  # type: TestResult
    def runTests(self) -> None: ...  # undocumented

def main(module: Union[None, str, ModuleType] = ...,
         defaultTest: Union[str, Iterable[str], None] = ...,
         argv: Optional[List[str]] = ...,
         testRunner: Union[Type[TestRunner], TestRunner, None] = ...,
         testLoader: TestLoader = ..., exit: bool = ..., verbosity: int = ...,
         failfast: Optional[bool] = ..., catchbreak: Optional[bool] = ...,
         buffer: Optional[bool] = ...,
         warnings: Optional[str] = ...) -> TestProgram: ...

def load_tests(loader: TestLoader, tests: TestSuite,
               pattern: Optional[str]) -> TestSuite: ...

def installHandler() -> None: ...
def registerResult(result: TestResult) -> None: ...
def removeResult(result: TestResult) -> bool: ...
@overload
def removeHandler() -> None: ...
@overload
def removeHandler(function: _FT) -> _FT: ...
