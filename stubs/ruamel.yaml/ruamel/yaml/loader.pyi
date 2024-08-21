from _typeshed import Incomplete

from .compat import StreamTextType, VersionType
from .composer import Composer
from .constructor import BaseConstructor, Constructor, RoundTripConstructor, SafeConstructor
from .parser import Parser, RoundTripParser
from .reader import Reader
from .resolver import VersionedResolver
from .scanner import RoundTripScanner, Scanner

__all__ = ["BaseLoader", "SafeLoader", "Loader", "RoundTripLoader"]

class BaseLoader(Reader, Scanner, Parser, Composer, BaseConstructor, VersionedResolver):
    comment_handling: Incomplete
    def __init__(
        self, stream: StreamTextType, version: VersionType | None = None, preserve_quotes: bool | None = None
    ) -> None: ...

class SafeLoader(Reader, Scanner, Parser, Composer, SafeConstructor, VersionedResolver):
    comment_handling: Incomplete
    def __init__(
        self, stream: StreamTextType, version: VersionType | None = None, preserve_quotes: bool | None = None
    ) -> None: ...

class Loader(Reader, Scanner, Parser, Composer, Constructor, VersionedResolver):
    comment_handling: Incomplete
    def __init__(
        self, stream: StreamTextType, version: VersionType | None = None, preserve_quotes: bool | None = None
    ) -> None: ...

class RoundTripLoader(Reader, RoundTripScanner, RoundTripParser, Composer, RoundTripConstructor, VersionedResolver):
    comment_handling: Incomplete
    def __init__(
        self, stream: StreamTextType, version: VersionType | None = None, preserve_quotes: bool | None = None
    ) -> None: ...
