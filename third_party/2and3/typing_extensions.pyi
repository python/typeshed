import sys
import typing
from typing import ClassVar as ClassVar
from typing import ContextManager as ContextManager
from typing import Counter as Counter
from typing import DefaultDict as DefaultDict
from typing import Deque as Deque
from typing import NewType as NewType
from typing import overload as overload
from typing import Text as Text
from typing import Type as Type
from typing import TYPE_CHECKING as TYPE_CHECKING

if sys.version_info >= (3, 3):
    from typing import ChainMap as ChainMap

if sys.version_info >= (3, 5):
    from typing import AsyncIterable as AsyncIterable
    from typing import AsyncIterator as AsyncIterator
    from typing import AsyncContextManager as AsyncContextManager
    from typing import Awaitable as Awaitable
    from typing import Coroutine as Coroutine

if sys.version_info >= (3, 6):
    from typing import AsyncGenerator as AsyncGenerator

# Return type that indicates a function does not return.
# This type is equivalent to the None type, but the no-op Union is necessary to
# distinguish the None type from the None value.
#
# TODO: Replace with direct import from typing once NoReturn is added to
# typing.pyi.
NoReturn = typing.Union[None]
