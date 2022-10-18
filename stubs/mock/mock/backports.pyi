if sys.version_info[:2] < (3, 8):
    import unittest

    class IsolatedAsyncioTestCase(unittest.TestCase): ...

    # It is a typeguard, but its signature is to complex to duplicate.
    def iscoroutinefunction(obj: object) -> bool: ...
else:
    from asyncio import iscoroutinefunction as iscoroutinefunction
    from unittest import IsolatedAsyncioTestCase as IsolatedAsyncioTestCase
