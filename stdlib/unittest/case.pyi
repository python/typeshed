import datetime
import logging
import sys
import unittest.result
from _typeshed import Self
from collections.abc import Set  # equivalent to typing.AbstractSet, not builtins.set
from contextlib import AbstractContextManager
from types import TracebackType
from typing import (
    Any,
    AnyStr,
    Callable,
    Container,
    Generic,
    Iterable,
    Mapping,
    NamedTuple,
    NoReturn,
    Pattern,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    overload,
)
from warnings import WarningMessage

if sys.version_info >= (3, 9):
    from types import GenericAlias

_E = TypeVar("_E", bound=BaseException)
_FT = TypeVar("_FT", bound=Callable[..., Any])

if sys.version_info >= (3, 8):
    def addModuleCleanup(__function: Callable[..., Any], *args: Any, **kwargs: Any) -> None: ...
    def doModuleCleanups() -> None: ...

def expectedFailure(test_item: _FT) -> _FT: ...
def skip(reason: str) -> Callable[[_FT], _FT]: ...
def skipIf(condition: object, reason: str) -> Callable[[_FT], _FT]: ...
def skipUnless(condition: object, reason: str) -> Callable[[_FT], _FT]: ...

class SkipTest(Exception):
    def __init__(self, reason: str) -> None: ...

class TestCase:
    failureException: Type[BaseException]
    longMessage: bool
    maxDiff: int | None
    # undocumented
    _testMethodName: str
    # undocumented
    _testMethodDoc: str
    def __init__(self, methodName: str = ...) -> None: ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    @classmethod
    def setUpClass(cls) -> None: ...
    @classmethod
    def tearDownClass(cls) -> None: ...
    def run(self, result: unittest.result.TestResult | None = ...) -> unittest.result.TestResult | None: ...
    def __call__(self, result: unittest.result.TestResult | None = ...) -> unittest.result.TestResult | None: ...
    def skipTest(self, reason: Any) -> None: ...
    def subTest(self, msg: Any = ..., **params: Any) -> AbstractContextManager[None]: ...
    def debug(self) -> None: ...
    def _addSkip(self, result: unittest.result.TestResult, test_case: TestCase, reason: str) -> None: ...
    def assertEqual(self, first: Any, second: Any, msg: Any = ...) -> None: ...
    def assertNotEqual(self, first: Any, second: Any, msg: Any = ...) -> None: ...
    def assertTrue(self, expr: Any, msg: Any = ...) -> None: ...
    def assertFalse(self, expr: Any, msg: Any = ...) -> None: ...
    def assertIs(self, expr1: Any, expr2: Any, msg: Any = ...) -> None: ...
    def assertIsNot(self, expr1: Any, expr2: Any, msg: Any = ...) -> None: ...
    def assertIsNone(self, obj: Any, msg: Any = ...) -> None: ...
    def assertIsNotNone(self, obj: Any, msg: Any = ...) -> None: ...
    def assertIn(self, member: Any, container: Iterable[Any] | Container[Any], msg: Any = ...) -> None: ...
    def assertNotIn(self, member: Any, container: Iterable[Any] | Container[Any], msg: Any = ...) -> None: ...
    def assertIsInstance(self, obj: Any, cls: type | Tuple[type, ...], msg: Any = ...) -> None: ...
    def assertNotIsInstance(self, obj: Any, cls: type | Tuple[type, ...], msg: Any = ...) -> None: ...
    def assertGreater(self, a: Any, b: Any, msg: Any = ...) -> None: ...
    def assertGreaterEqual(self, a: Any, b: Any, msg: Any = ...) -> None: ...
    def assertLess(self, a: Any, b: Any, msg: Any = ...) -> None: ...
    def assertLessEqual(self, a: Any, b: Any, msg: Any = ...) -> None: ...
    @overload
    def assertRaises(  # type: ignore[misc]
        self,
        expected_exception: Type[BaseException] | Tuple[Type[BaseException], ...],
        callable: Callable[..., Any],
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    @overload
    def assertRaises(self, expected_exception: Type[_E] | Tuple[Type[_E], ...], msg: Any = ...) -> _AssertRaisesContext[_E]: ...
    @overload
    def assertRaisesRegex(  # type: ignore[misc]
        self,
        expected_exception: Type[BaseException] | Tuple[Type[BaseException], ...],
        expected_regex: str | bytes | Pattern[str] | Pattern[bytes],
        callable: Callable[..., Any],
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    @overload
    def assertRaisesRegex(
        self,
        expected_exception: Type[_E] | Tuple[Type[_E], ...],
        expected_regex: str | bytes | Pattern[str] | Pattern[bytes],
        msg: Any = ...,
    ) -> _AssertRaisesContext[_E]: ...
    @overload
    def assertWarns(  # type: ignore[misc]
        self, expected_warning: Type[Warning] | Tuple[Type[Warning], ...], callable: Callable[..., Any], *args: Any, **kwargs: Any
    ) -> None: ...
    @overload
    def assertWarns(self, expected_warning: Type[Warning] | Tuple[Type[Warning], ...], msg: Any = ...) -> _AssertWarnsContext: ...
    @overload
    def assertWarnsRegex(  # type: ignore[misc]
        self,
        expected_warning: Type[Warning] | Tuple[Type[Warning], ...],
        expected_regex: str | bytes | Pattern[str] | Pattern[bytes],
        callable: Callable[..., Any],
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    @overload
    def assertWarnsRegex(
        self,
        expected_warning: Type[Warning] | Tuple[Type[Warning], ...],
        expected_regex: str | bytes | Pattern[str] | Pattern[bytes],
        msg: Any = ...,
    ) -> _AssertWarnsContext: ...
    def assertLogs(self, logger: str | logging.Logger | None = ..., level: int | str | None = ...) -> _AssertLogsContext: ...
    @overload
    def assertAlmostEqual(
        self, first: float, second: float, places: int | None = ..., msg: Any = ..., delta: float | None = ...
    ) -> None: ...
    @overload
    def assertAlmostEqual(
        self,
        first: datetime.datetime,
        second: datetime.datetime,
        places: int | None = ...,
        msg: Any = ...,
        delta: datetime.timedelta | None = ...,
    ) -> None: ...
    @overload
    def assertNotAlmostEqual(self, first: float, second: float, *, msg: Any = ...) -> None: ...
    @overload
    def assertNotAlmostEqual(self, first: float, second: float, places: int | None = ..., msg: Any = ...) -> None: ...
    @overload
    def assertNotAlmostEqual(self, first: float, second: float, *, msg: Any = ..., delta: float | None = ...) -> None: ...
    @overload
    def assertNotAlmostEqual(
        self,
        first: datetime.datetime,
        second: datetime.datetime,
        places: int | None = ...,
        msg: Any = ...,
        delta: datetime.timedelta | None = ...,
    ) -> None: ...
    def assertRegex(self, text: AnyStr, expected_regex: AnyStr | Pattern[AnyStr], msg: Any = ...) -> None: ...
    def assertNotRegex(self, text: AnyStr, unexpected_regex: AnyStr | Pattern[AnyStr], msg: Any = ...) -> None: ...
    def assertCountEqual(self, first: Iterable[Any], second: Iterable[Any], msg: Any = ...) -> None: ...
    def addTypeEqualityFunc(self, typeobj: Type[Any], function: Callable[..., None]) -> None: ...
    def assertMultiLineEqual(self, first: str, second: str, msg: Any = ...) -> None: ...
    def assertSequenceEqual(
        self, seq1: Sequence[Any], seq2: Sequence[Any], msg: Any = ..., seq_type: Type[Sequence[Any]] | None = ...
    ) -> None: ...
    def assertListEqual(self, list1: list[Any], list2: list[Any], msg: Any = ...) -> None: ...
    def assertTupleEqual(self, tuple1: Tuple[Any, ...], tuple2: Tuple[Any, ...], msg: Any = ...) -> None: ...
    def assertSetEqual(self, set1: Set[object], set2: Set[object], msg: Any = ...) -> None: ...
    def assertDictEqual(self, d1: Mapping[Any, object], d2: Mapping[Any, object], msg: Any = ...) -> None: ...
    def fail(self, msg: Any = ...) -> NoReturn: ...
    def countTestCases(self) -> int: ...
    def defaultTestResult(self) -> unittest.result.TestResult: ...
    def id(self) -> str: ...
    def shortDescription(self) -> str | None: ...
    if sys.version_info >= (3, 8):
        def addCleanup(self, __function: Callable[..., Any], *args: Any, **kwargs: Any) -> None: ...
    else:
        def addCleanup(self, function: Callable[..., Any], *args: Any, **kwargs: Any) -> None: ...
    def doCleanups(self) -> None: ...
    if sys.version_info >= (3, 8):
        @classmethod
        def addClassCleanup(cls, __function: Callable[..., Any], *args: Any, **kwargs: Any) -> None: ...
        @classmethod
        def doClassCleanups(cls) -> None: ...
    def _formatMessage(self, msg: str | None, standardMsg: str) -> str: ...  # undocumented
    def _getAssertEqualityFunc(self, first: Any, second: Any) -> Callable[..., None]: ...  # undocumented
    if sys.version_info < (3, 11):
        def failUnlessEqual(self, first: Any, second: Any, msg: Any = ...) -> None: ...
        def assertEquals(self, first: Any, second: Any, msg: Any = ...) -> None: ...
        def failIfEqual(self, first: Any, second: Any, msg: Any = ...) -> None: ...
        def assertNotEquals(self, first: Any, second: Any, msg: Any = ...) -> None: ...
        def failUnless(self, expr: bool, msg: Any = ...) -> None: ...
        def assert_(self, expr: bool, msg: Any = ...) -> None: ...
        def failIf(self, expr: bool, msg: Any = ...) -> None: ...
        @overload
        def failUnlessRaises(  # type: ignore[misc]
            self,
            exception: Type[BaseException] | Tuple[Type[BaseException], ...],
            callable: Callable[..., Any] = ...,
            *args: Any,
            **kwargs: Any,
        ) -> None: ...
        @overload
        def failUnlessRaises(self, exception: Type[_E] | Tuple[Type[_E], ...], msg: Any = ...) -> _AssertRaisesContext[_E]: ...
        def failUnlessAlmostEqual(self, first: float, second: float, places: int = ..., msg: Any = ...) -> None: ...
        def assertAlmostEquals(
            self, first: float, second: float, places: int = ..., msg: Any = ..., delta: float = ...
        ) -> None: ...
        def failIfAlmostEqual(self, first: float, second: float, places: int = ..., msg: Any = ...) -> None: ...
        def assertNotAlmostEquals(
            self, first: float, second: float, places: int = ..., msg: Any = ..., delta: float = ...
        ) -> None: ...
        def assertRegexpMatches(self, text: AnyStr, regex: AnyStr | Pattern[AnyStr], msg: Any = ...) -> None: ...
        def assertNotRegexpMatches(self, text: AnyStr, regex: AnyStr | Pattern[AnyStr], msg: Any = ...) -> None: ...
        @overload
        def assertRaisesRegexp(  # type: ignore[misc]
            self,
            exception: Type[BaseException] | Tuple[Type[BaseException], ...],
            expected_regex: str | bytes | Pattern[str] | Pattern[bytes],
            callable: Callable[..., Any],
            *args: Any,
            **kwargs: Any,
        ) -> None: ...
        @overload
        def assertRaisesRegexp(
            self,
            exception: Type[_E] | Tuple[Type[_E], ...],
            expected_regex: str | bytes | Pattern[str] | Pattern[bytes],
            msg: Any = ...,
        ) -> _AssertRaisesContext[_E]: ...
        def assertDictContainsSubset(
            self, subset: Mapping[Any, Any], dictionary: Mapping[Any, Any], msg: object = ...
        ) -> None: ...

class FunctionTestCase(TestCase):
    def __init__(
        self,
        testFunc: Callable[[], None],
        setUp: Callable[[], None] | None = ...,
        tearDown: Callable[[], None] | None = ...,
        description: str | None = ...,
    ) -> None: ...
    def runTest(self) -> None: ...

class _LoggingWatcher(NamedTuple):
    records: list[logging.LogRecord]
    output: list[str]

class _AssertRaisesContext(Generic[_E]):
    exception: _E
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> bool: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...

class _AssertWarnsContext:
    warning: WarningMessage
    filename: str
    lineno: int
    warnings: list[WarningMessage]
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...

class _AssertLogsContext:
    LOGGING_FORMAT: str
    records: list[logging.LogRecord]
    output: list[str]
    def __init__(self, test_case: TestCase, logger_name: str, level: int) -> None: ...
    if sys.version_info >= (3, 10):
        def __enter__(self) -> _LoggingWatcher | None: ...
    else:
        def __enter__(self) -> _LoggingWatcher: ...
    def __exit__(
        self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> bool | None: ...
