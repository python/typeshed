from typing import Text, Union, IO, Optional, Sequence, Mapping, Any
from typing_extensions import Protocol

from yaml.constructor import BaseConstructor, Constructor, SafeConstructor
from yaml.representer import BaseRepresenter, Representer, SafeRepresenter
from yaml.resolver import BaseResolver, Resolver
from yaml.serializer import Serializer

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

class CDangerLoader(CParser, Constructor, Resolver): ...  # undocumented

class CEmitter:
    def __init__(self, stream: IO[Any], canonical: Any = ..., indent: Optional[int] = ...,
                 width: Optional[int] = ..., allow_unicode: Any = ..., line_break: Optional[str] = ...,
                 encoding: Optional[str] = ..., explicit_start: Any = ..., explicit_end: Any = ...,
                 version: Optional[Sequence[int]] = ..., tags: Optional[Mapping[str, str]] = ...) -> None: ...

class CBaseDumper(CEmitter, BaseRepresenter, BaseResolver):
    def __init__(self, stream: IO[Any], default_style: Optional[str] = ...,
                 default_flow_style: Optional[bool] = ..., canonical: Any = ...,
                 indent: Optional[int] = ..., width: Optional[int] = ...,
                 allow_unicode: Any = ..., line_break: Optional[str] = ...,
                 encoding: Optional[str] = ..., explicit_start: Any = ..., explicit_end: Any = ...,
                 version: Optional[Sequence[int]] = ..., tags: Optional[Mapping[str, str]] = ...) -> None: ...

class CDumper(CEmitter, SafeRepresenter, Resolver): ...

CSafeDumper = CDumper

class CDangerDumper(CEmitter, Serializer, Representer, Resolver): ...  # undocumented
