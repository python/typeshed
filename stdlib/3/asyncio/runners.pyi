from typing import Awaitable, TypeVar


_T = TypeVar('_T')

def run(main: Awaitable[_T], *, debug: bool = False) -> _T: ...
