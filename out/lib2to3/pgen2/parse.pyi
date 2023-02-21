from . import token as token
from _typeshed import Incomplete

class ParseError(Exception):
    msg: Incomplete
    type: Incomplete
    value: Incomplete
    context: Incomplete
    def __init__(self, msg, type, value, context) -> None: ...
    def __reduce__(self): ...

class Parser:
    grammar: Incomplete
    convert: Incomplete
    def __init__(self, grammar, convert: Incomplete | None = ...) -> None: ...
    stack: Incomplete
    rootnode: Incomplete
    used_names: Incomplete
    def setup(self, start: Incomplete | None = ...) -> None: ...
    def addtoken(self, type, value, context): ...
    def classify(self, type, value, context): ...
    def shift(self, type, value, newstate, context) -> None: ...
    def push(self, type, newdfa, newstate, context) -> None: ...
    def pop(self) -> None: ...
