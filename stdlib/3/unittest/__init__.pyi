# Stubs for unittest

from typing import Any, Iterable, List, Optional, Type, Union
from types import ModuleType

from unittest.async_case import *
from unittest.case import *
from unittest.loader import *
from unittest.result import TestResult as TestResult
from unittest.runner import *
from unittest.signals import *
from unittest.suite import *


# not really documented
class TestProgram:
    result: TestResult
    module: Union[None, str, ModuleType]
    verbosity: int
    failfast: Optional[bool]
    catchbreak: Optional[bool]
    buffer: Optional[bool]
    progName: Optional[str]
    warnings: Optional[str]
    def __init__(self, module: Union[None, str, ModuleType] = ...,
                 defaultTest: Union[str, Iterable[str], None] = ...,
                 argv: Optional[List[str]] = ...,
                 testRunner: Union[Type[TestRunner], TestRunner, None] = ...,
                 testLoader: TestLoader = ..., exit: bool = ..., verbosity: int = ...,
                 failfast: Optional[bool] = ..., catchbreak: Optional[bool] = ...,
                 buffer: Optional[bool] = ...,
                 warnings: Optional[str] = ..., *,
                 tb_locals: bool = ...) -> None: ...
    def usageExit(self, msg: Any = ...) -> None: ...
    def parseArgs(self, argv: List[str]) -> None: ...
    def createTests(self) -> None: ...
    def runTests(self) -> None: ...  # undocumented

main = TestProgram

def load_tests(loader: TestLoader, tests: TestSuite,
               pattern: Optional[str]) -> TestSuite: ...
