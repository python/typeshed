from typing import Any
# from yaml.error import *
# from yaml.tokens import *
# from yaml.events import *
# from yaml.nodes import *
# from yaml.loader import *
# from yaml.dumper import *
# TODO: stubs for cyaml?
# from cyaml import *

__with_libyaml__ = ...  # type: Any

def scan(stream: Any, Loader: Any = ...) -> Any: ...
def parse(stream: Any, Loader: Any = ...) -> Any: ...
def compose(stream: Any, Loader: Any = ...) -> Any: ...
def compose_all(stream: Any, Loader: Any = ...) -> Any: ...
def load(stream: Any, Loader: Any = ...) -> Any: ...
def load_all(stream: Any, Loader: Any = ...) -> Any: ...
def safe_load(stream: Any) -> Any: ...
def safe_load_all(stream: Any) -> Any: ...
def emit(events: Any, stream: Any = ..., Dumper: Any = ..., canonical: Any = ..., indent: Any = ..., width: Any = ..., allow_unicode: Any = ..., line_break: Any = ...) -> Any: ...
def serialize_all(nodes: Any, stream: Any = ..., Dumper: Any = ..., canonical: Any = ..., indent: Any = ..., width: Any = ..., allow_unicode: Any = ..., line_break: Any = ..., encoding: Any = ..., explicit_start: Any = ..., explicit_end: Any = ..., version: Any = ..., tags: Any = ...) -> Any: ...
def serialize(node: Any, stream: Any = ..., Dumper: Any = ..., **kwds: Any) -> Any: ...
def dump_all(documents: Any, stream: Any = ..., Dumper: Any = ..., default_style: Any = ..., default_flow_style: Any = ..., canonical: Any = ..., indent: Any = ..., width: Any = ..., allow_unicode: Any = ..., line_break: Any = ..., encoding: Any = ..., explicit_start: Any = ..., explicit_end: Any = ..., version: Any = ..., tags: Any = ...) -> Any: ...
def dump(data: Any, stream: Any = ..., Dumper: Any = ..., **kwds: Any) -> Any: ...
def safe_dump_all(documents: Any, stream: Any = ..., **kwds: Any) -> Any: ...
def safe_dump(data: Any, stream: Any = ..., **kwds: Any) -> Any: ...
def add_implicit_resolver(tag: Any, regexp: Any, first: Any = ..., Loader: Any = ..., Dumper: Any = ...) -> Any: ...
def add_path_resolver(tag: Any, path: Any, kind: Any = ..., Loader: Any = ..., Dumper: Any = ...) -> Any: ...
def add_constructor(tag: Any, constructor: Any, Loader: Any = ...) -> Any: ...
def add_multi_constructor(tag_prefix: Any, multi_constructor: Any, Loader: Any = ...) -> Any: ...
def add_representer(data_type: Any, representer: Any, Dumper: Any = ...) -> Any: ...
def add_multi_representer(data_type: Any, multi_representer: Any, Dumper: Any = ...) -> Any: ...

class YAMLObjectMetaclass(type):
    def __init__(cls: Any, name: Any, bases: Any, kwds: Any) -> None: ...

class YAMLObject:
    __metaclass__ = YAMLObjectMetaclass
    yaml_loader = ...  # type: Any
    yaml_dumper = ...  # type: Any
    yaml_tag = ...  # type: Any
    yaml_flow_style = ...  # type: Any
    @classmethod
    def from_yaml(cls: Any, loader: Any, node: Any) -> Any: ...
    @classmethod
    def to_yaml(cls: Any, dumper: Any, data: Any) -> Any: ...
