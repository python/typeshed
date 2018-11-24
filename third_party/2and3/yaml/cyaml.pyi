from typing import Text, Union
from typing_extensions import Protocol

from yaml.constructor import BaseConstructor, SafeConstructor
from yaml.resolver import BaseResolver, Resolver

class _Readable(Protocol):
    def read(self, size: int) -> Union[Text, bytes]: ...

class CParser:
    def __init__(self, stream: Union[str, bytes, _Readable]) -> None: ...

class CBaseLoader(CParser, BaseConstructor, BaseResolver):
    def __init__(self, stream: Union[str, bytes, _Readable]) -> None: ...

class CLoader(CParser, SafeConstructor, Resolver):
    def __init__(self, stream: Union[str, bytes, _Readable]) -> None: ...

class CSafeLoader(CParser, SafeConstructor, Resolver):
    def __init__(self, stream: Union[str, bytes, _Readable]) -> None: ...
