from _typeshed import Unused
from typing import TypeAlias

from .compat import VersionType, _ReadStream
from .composer import Composer
from .constructor import BaseConstructor, Constructor, RoundTripConstructor, SafeConstructor
from .parser import Parser, RoundTripParser
from .reader import Reader
from .resolver import VersionedResolver
from .scanner import RoundTripScanner, Scanner

__all__ = ["BaseLoader", "SafeLoader", "Loader", "RoundTripLoader"]

_Loader: TypeAlias = Loader | BaseLoader | SafeLoader | RoundTripLoader  # noqa: Y047

class BaseLoader(Reader, Scanner, Parser, Composer, BaseConstructor, VersionedResolver):
    comment_handling: int | None
    def __init__(self, stream: _ReadStream, version: VersionType | None = None, preserve_quotes: Unused = None) -> None: ...

class SafeLoader(Reader, Scanner, Parser, Composer, SafeConstructor, VersionedResolver):
    comment_handling: int | None
    def __init__(self, stream: _ReadStream, version: VersionType | None = None, preserve_quotes: Unused = None) -> None: ...

class Loader(Reader, Scanner, Parser, Composer, Constructor, VersionedResolver):
    comment_handling: int | None
    def __init__(self, stream: _ReadStream, version: VersionType | None = None, preserve_quotes: Unused = None) -> None: ...

class RoundTripLoader(Reader, RoundTripScanner, RoundTripParser, Composer, RoundTripConstructor, VersionedResolver):
    comment_handling: int | None
    def __init__(self, stream: _ReadStream, version: VersionType | None = None, preserve_quotes: bool | None = None) -> None: ...
