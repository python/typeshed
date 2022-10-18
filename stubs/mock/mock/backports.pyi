import sys

if sys.version_info[:2] >= (3, 8):
    from asyncio import iscoroutinefunction as iscoroutinefunction
    from unittest import IsolatedAsyncioTestCase as IsolatedAsyncioTestCase
else:
    import unittest

    class IsolatedAsyncioTestCase(unittest.TestCase): ...  # pyright: ignore[reportGeneralTypeIssues]
    # It is a typeguard, but its signature is to complex to duplicate.
    def iscoroutinefunction(obj: object) -> bool: ...  # pyright: ignore[reportGeneralTypeIssues]
