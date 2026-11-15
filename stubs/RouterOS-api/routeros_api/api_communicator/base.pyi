from collections.abc import Callable, Iterable
from typing import TypeVar, overload

from routeros_api.exceptions import RouterOsApiCommunicationError
from routeros_api.sentence import CommandSentence

_T = TypeVar("_T")
_S = TypeVar("_S")

# A reply: the list of its rows, with the done message the router ends it with.
class AsynchronousResponse(list[_T]):
    # The command the reply answers.
    command: CommandSentence
    done_message: _T
    done: bool
    error: bytes | None

    @overload
    def __init__(self, *, command: CommandSentence) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[_T], /, *, command: CommandSentence) -> None: ...

    @property
    def error_as_exception(self) -> RouterOsApiCommunicationError | None: ...
    # Applied to each row and to the done message.
    def map(self, function: Callable[[_T], _S]) -> AsynchronousResponse[_S]: ...
