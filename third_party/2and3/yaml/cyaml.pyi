from _yaml import CParser
from yaml.constructor import BaseConstructor, SafeConstructor
from yaml.resolver import BaseResolver, Resolver

class CBaseLoader(CParser, BaseConstructor, BaseResolver):
    def __init__(self, stream) -> None: ...

class CLoader(CParser, SafeConstructor, Resolver):
    def __init__(self, stream) -> None: ...

class CSafeLoader(CParser, SafeConstructor, Resolver):
    def __init__(self, stream) -> None: ...