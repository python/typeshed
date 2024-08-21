from _typeshed import Incomplete

from ruamel.yaml.compat import StreamTextType, VersionType
from ruamel.yaml.composer import Composer
from ruamel.yaml.constructor import BaseConstructor, Constructor, RoundTripConstructor, SafeConstructor
from ruamel.yaml.parser import Parser, RoundTripParser
from ruamel.yaml.reader import Reader
from ruamel.yaml.resolver import VersionedResolver
from ruamel.yaml.scanner import RoundTripScanner, Scanner

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
