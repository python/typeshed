# Stubs for email (Python 3.4)

from typing import Callable, Optional, BinaryIO, TextIO
import sys
from email.message import Message, Policy

if sys.version_info >= (3, 3):
    def message_from_string(s: str, _class: Callable[[], Message] = ..., *,
                            policy: Policy = ...) -> Message: ...
    def message_from_bytes(s: bytes, _class: Callable[[], Message] = ..., *,
                           policy: Policy = ...) -> Message: ...
    def message_from_file(fp: TextIO, _class: Callable[[], Message] = ..., *,
                           policy: Policy = ...) -> Message: ...
    def message_from_binary_file(fp: BinaryIO,
                                 _class: Callable[[], Message] = ..., *,
                                 policy: Policy = ...) -> Message: ...
elif sys.version_info >= (3, 2):
    def message_from_string(s: str,  # type: ignore
                            _class: Callable[[], Message] = ..., *,
                            strict: Optional[bool] = ...) -> Message: ...
    def message_from_bytes(s: bytes,  # type: ignore
                           _class: Callable[[], Message] = ..., *,
                           strict: Optional[bool] = ...) -> Message: ...
    def message_from_file(fp: TextIO,  # type: ignore
                          _class: Callable[[], Message] = ..., *,
                          strict: Optional[bool] = ...) -> Message: ...
    def message_from_binary_file(fp: BinaryIO,  # type: ignore
                                 _class: Callable[[], Message] = ..., *,
                                 strict: Optional[bool] = ...) -> Message: ...

# Names in __all__ with no definition:
#   base64mime
#   charset
#   encoders
#   errors
#   feedparser
#   generator
#   header
#   iterators
#   message
#   mime
#   parser
#   quoprimime
#   utils
