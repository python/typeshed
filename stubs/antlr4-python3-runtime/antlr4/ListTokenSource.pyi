from _typeshed import Incomplete

from antlr4.CommonTokenFactory import CommonTokenFactory as CommonTokenFactory
from antlr4.Lexer import TokenSource as TokenSource
from antlr4.Token import Token as Token

class ListTokenSource(TokenSource):
    tokens: Incomplete
    sourceName: Incomplete
    pos: int
    eofToken: Incomplete
    def __init__(self, tokens: list[Token], sourceName: str = ...) -> None: ...
    @property
    def column(self) -> Incomplete: ...
    def nextToken(self) -> Incomplete: ...
    @property
    def line(self) -> Incomplete: ...
    def getInputStream(self) -> Incomplete: ...
    def getSourceName(self) -> Incomplete: ...
