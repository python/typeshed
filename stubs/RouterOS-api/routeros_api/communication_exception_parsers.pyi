import re
from collections.abc import Callable
from typing import TypeAlias

from routeros_api.exceptions import RouterOsApiCommunicationError

# What builds the exception raised in an error's place, from the error and its original message;
# each is paired with a pattern searched for in that message.
_ExceptionType: TypeAlias = Callable[[RouterOsApiCommunicationError, bytes], BaseException]

class ExceptionHandler:  # undocumented
    message_to_class_map: list[tuple[bytes | re.Pattern[bytes], _ExceptionType]]
    def __init__(self) -> None: ...
    def add_exception_type(self, message_re: bytes | re.Pattern[bytes], exception_class: _ExceptionType) -> None: ...
    def handle(self, exception: BaseException) -> None: ...
