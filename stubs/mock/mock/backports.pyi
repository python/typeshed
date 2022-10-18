import sys

if sys.version_info[:2] >= (3, 8):
    from asyncio import iscoroutinefunction as iscoroutinefunction  # pyright: ignore[reportGeneralTypeIssues]
    from unittest import IsolatedAsyncioTestCase as IsolatedAsyncioTestCase  # pyright: ignore[reportGeneralTypeIssues]
else:
    import unittest

    class IsolatedAsyncioTestCase(unittest.TestCase): ...  
    # It is a typeguard, but its signature is to complex to duplicate.
    def iscoroutinefunction(obj: object) -> bool: ...
