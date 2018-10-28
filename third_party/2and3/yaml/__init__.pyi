from typing import Any, IO, Iterator, Optional, overload, Sequence, Text, Union
import sys
from yaml.error import *  # noqa: F403
from yaml.tokens import *  # noqa: F403
from yaml.events import *  # noqa: F403
from yaml.nodes import *  # noqa: F403
from yaml.loader import *  # noqa: F403
from yaml.dumper import *  # noqa: F403
from . import resolver  # Help mypy a bit; this is implied by loader and dumper
from .cyaml import *

if sys.version_info < (3,):
    _Str = Union[Text, str]
else:
    _Str = str
# FIXME: the functions really return py2:unicode/py3:str if encoding is None, otherwise py2:str/py3:bytes. Waiting for Issue#5621
_Yaml = Any

__with_libyaml__ = ...  # type: Any
__version__ = ...  # type: str

def scan(stream, Loader=...): ...
def parse(stream, Loader=...): ...
def compose(stream, Loader=...): ...
def compose_all(stream, Loader=...): ...
def load(stream: Union[str, IO[str]], Loader=...) -> Any: ...
def load_all(stream: Union[str, IO[str]], Loader=...) -> Iterator[Any]: ...
def safe_load(stream: Union[str, IO[str]]) -> Any: ...
def safe_load_all(stream: Union[str, IO[str]]) -> Iterator[Any]: ...
def emit(events, stream=..., Dumper=..., canonical=..., indent=..., width=..., allow_unicode=..., line_break=...): ...

@overload
def serialize_all(nodes, stream: IO[str], Dumper=..., canonical=..., indent=..., width=..., allow_unicode=..., line_break=..., encoding=..., explicit_start=..., explicit_end=..., version=..., tags=...) -> None: ...
@overload
def serialize_all(nodes, stream: None=..., Dumper=..., canonical=..., indent=..., width=..., allow_unicode=..., line_break=..., encoding: Optional[_Str]=..., explicit_start=..., explicit_end=..., version=..., tags=...) -> _Yaml: ...

@overload
def serialize(node, stream: IO[str], Dumper=..., canonical=..., indent=..., width=..., allow_unicode=..., line_break=..., encoding=..., explicit_start=..., explicit_end=..., version=..., tags=...) -> None: ...
@overload
def serialize(node, stream: None=..., Dumper=..., canonical=..., indent=..., width=..., allow_unicode=..., line_break=..., encoding: Optional[_Str]=..., explicit_start=..., explicit_end=..., version=..., tags=...) -> _Yaml: ...

@overload
def dump_all(documents: Sequence[Any], stream: IO[str], Dumper=..., default_style=..., default_flow_style=..., canonical=..., indent=..., width=..., allow_unicode=..., line_break=..., encoding=..., explicit_start=..., explicit_end=..., version=..., tags=...) -> None: ...
@overload
def dump_all(documents: Sequence[Any], stream: None=..., Dumper=..., default_style=..., default_flow_style=..., canonical=..., indent=..., width=..., allow_unicode=..., line_break=..., encoding: Optional[_Str]=..., explicit_start=..., explicit_end=..., version=..., tags=...) -> _Yaml: ...

@overload
def dump(data: Any, stream: IO[str], Dumper=..., default_style=..., default_flow_style=..., canonical=..., indent=..., width=..., allow_unicode=..., line_break=..., encoding=..., explicit_start=..., explicit_end=..., version=..., tags=...) -> None: ...
@overload
def dump(data: Any, stream: None=..., Dumper=..., default_style=..., default_flow_style=..., canonical=..., indent=..., width=..., allow_unicode=..., line_break=..., encoding: Optional[_Str]=..., explicit_start=..., explicit_end=..., version=..., tags=...) -> _Yaml: ...

@overload
def save_dump_all(documents: Sequence[Any], stream: IO[str], default_style=..., default_flow_style=..., canonical=..., indent=..., width=..., allow_unicode=..., line_break=..., encoding=..., explicit_start=..., explicit_end=..., version=..., tags=...) -> None: ...
@overload
def save_dump_all(documents: Sequence[Any], stream: None=..., default_style=..., default_flow_style=..., canonical=..., indent=..., width=..., allow_unicode=..., line_break=..., encoding: Optional[_Str]=..., explicit_start=..., explicit_end=..., version=..., tags=...) -> _Yaml: ...

@overload
def save_dump(data: Any, stream: IO[str], default_style=..., default_flow_style=..., canonical=..., indent=..., width=..., allow_unicode=..., line_break=..., encoding=..., explicit_start=..., explicit_end=..., version=..., tags=...) -> None: ...
@overload
def save_dump(data: Any, stream: None=..., default_style=..., default_flow_style=..., canonical=..., indent=..., width=..., allow_unicode=..., line_break=..., encoding: Optional[_Str]=..., explicit_start=..., explicit_end=..., version=..., tags=...) -> _Yaml: ...

def add_implicit_resolver(tag, regexp, first=..., Loader=..., Dumper=...): ...
def add_path_resolver(tag, path, kind=..., Loader=..., Dumper=...): ...
def add_constructor(tag, constructor, Loader=...): ...
def add_multi_constructor(tag_prefix, multi_constructor, Loader=...): ...
def add_representer(data_type, representer, Dumper=...): ...
def add_multi_representer(data_type, multi_representer, Dumper=...): ...

class YAMLObjectMetaclass(type):
    def __init__(cls, name, bases, kwds) -> None: ...

class YAMLObject(metaclass=YAMLObjectMetaclass):
    yaml_loader = ...  # type: Any
    yaml_dumper = ...  # type: Any
    yaml_tag = ...  # type: Any
    yaml_flow_style = ...  # type: Any
    @classmethod
    def from_yaml(cls, loader, node): ...
    @classmethod
    def to_yaml(cls, dumper, data): ...
