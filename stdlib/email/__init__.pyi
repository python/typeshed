from collections.abc import Callable
from email.message import Message
from email.policy import Policy
from typing import IO
from typing_extensions import TypeAlias

# These aren't actually imported here at runtime. This is a work-around for the
# fact that they're included in __all__ anyway.
from . import (
    base64mime as base64mime,
    charset as charset,
    encoders as encoders,
    errors as errors,
    feedparser as feedparser,
    generator as generator,
    header as header,
    iterators as iterators,
    message as message,
    mime as mime,
    parser as parser,
    quoprimime as quoprimime,
    utils as utils,
)

__all__ = [
    "base64mime",
    "charset",
    "encoders",
    "errors",
    "feedparser",
    "generator",
    "header",
    "iterators",
    "message",
    "message_from_file",
    "message_from_binary_file",
    "message_from_string",
    "message_from_bytes",
    "mime",
    "parser",
    "quoprimime",
    "utils",
]

# Definitions imported by multiple submodules in typeshed
_ParamType: TypeAlias = str | tuple[str | None, str | None, str]  # noqa: Y047
_ParamsType: TypeAlias = str | None | tuple[str, str | None, str]  # noqa: Y047

def message_from_string(s: str, _class: Callable[[], Message] = ..., *, policy: Policy = ...) -> Message: ...
def message_from_bytes(s: bytes | bytearray, _class: Callable[[], Message] = ..., *, policy: Policy = ...) -> Message: ...
def message_from_file(fp: IO[str], _class: Callable[[], Message] = ..., *, policy: Policy = ...) -> Message: ...
def message_from_binary_file(fp: IO[bytes], _class: Callable[[], Message] = ..., *, policy: Policy = ...) -> Message: ...
