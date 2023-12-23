from _typeshed import Incomplete
from io import StringIO as StringIO
from typing import TextIO

from antlr4 import *

def serializedATN() -> Incomplete: ...

class XPathLexer(Lexer):
    atn: Incomplete
    decisionsToDFA: Incomplete
    TOKEN_REF: int
    RULE_REF: int
    ANYWHERE: int
    ROOT: int
    WILDCARD: int
    BANG: int
    ID: int
    STRING: int
    channelNames: Incomplete
    modeNames: Incomplete
    literalNames: Incomplete
    symbolicNames: Incomplete
    ruleNames: Incomplete
    grammarFileName: str
    def __init__(self, input: Incomplete | None = ..., output: TextIO = ...) -> None: ...
    def action(self, localctx: RuleContext, ruleIndex: int, actionIndex: int) -> Incomplete: ...
    type: Incomplete
    def ID_action(self, localctx: RuleContext, actionIndex: int) -> Incomplete: ...
