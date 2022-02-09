from _typeshed import StrPath, SupportsWrite
from typing import IO, Any, Mapping, MutableMapping, Text

class TomlDecodeError(Exception): ...

def load(f: StrPath | list[Text] | IO[str], _dict: type[MutableMapping[str, Any]] = ...) -> MutableMapping[str, Any]: ...
def loads(s: Text, _dict: type[MutableMapping[str, Any]] = ...) -> MutableMapping[str, Any]: ...
def dump(o: Mapping[str, Any], f: SupportsWrite[str]) -> str: ...
def dumps(o: Mapping[str, Any]) -> str: ...
