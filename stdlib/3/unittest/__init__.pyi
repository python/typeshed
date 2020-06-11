# Stubs for unittest

from types import ModuleType
from typing import Iterable, List, Optional, Type, Union
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
    def runTests(self) -> None: ...  # undocumented

def main(
    module: Union[None, str, ModuleType] = ...,
    defaultTest: Union[str, Iterable[str], None] = ...,
    argv: Optional[List[str]] = ...,
    testRunner: Union[Type[TestRunner], TestRunner, None] = ...,
    testLoader: TestLoader = ...,
    exit: bool = ...,
    verbosity: int = ...,
    failfast: Optional[bool] = ...,
    catchbreak: Optional[bool] = ...,
    buffer: Optional[bool] = ...,
    warnings: Optional[str] = ...,
) -> TestProgram: ...
def load_tests(loader: TestLoader, tests: TestSuite, pattern: Optional[str]) -> TestSuite: ...
