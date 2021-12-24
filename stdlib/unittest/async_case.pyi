from collections.abc import Awaitable, Callable
import sys
from typing import Any

from .case import TestCase

if sys.version_info >= (3, 8):
    class IsolatedAsyncioTestCase(TestCase):
        async def asyncSetUp(self) -> None: ...
        async def asyncTearDown(self) -> None: ...
        def addAsyncCleanup(self, __func: Callable[..., Awaitable[Any]], *args: Any, **kwargs: Any) -> None: ...
