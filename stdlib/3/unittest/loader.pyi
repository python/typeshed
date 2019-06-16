import sys
import unittest.case
import unittest.result
import unittest.suite
from types import ModuleType
from typing import Any, Callable, List, Optional, Sequence, Type

class TestLoader:
    if sys.version_info >= (3, 5):
        errors: List[Type[BaseException]]
    testMethodPrefix: str
    sortTestMethodsUsing: Callable[[str, str], bool]
    suiteClass: Callable[[List[unittest.case.TestCase]], unittest.suite.TestSuite]
    def loadTestsFromTestCase(self, testCaseClass: Type[unittest.case.TestCase]) -> unittest.suite.TestSuite: ...
    if sys.version_info >= (3, 5):
        def loadTestsFromModule(self, module: ModuleType, *, pattern: Any = ...) -> unittest.suite.TestSuite: ...
    else:
        def loadTestsFromModule(self, module: ModuleType) -> unittest.suite.TestSuite: ...
    def loadTestsFromName(self, name: str, module: Optional[ModuleType] = ...) -> unittest.suite.TestSuite: ...
    def loadTestsFromNames(self, names: Sequence[str], module: Optional[ModuleType] = ...) -> unittest.suite.TestSuite: ...
    def getTestCaseNames(self, testCaseClass: Type[unittest.case.TestCase]) -> Sequence[str]: ...
    def discover(self, start_dir: str, pattern: str = ..., top_level_dir: Optional[str] = ...) -> unittest.suite.TestSuite: ...

defaultTestLoader: TestLoader
