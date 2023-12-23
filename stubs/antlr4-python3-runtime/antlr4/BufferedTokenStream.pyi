from _typeshed import Incomplete

from antlr4.error.Errors import IllegalStateException as IllegalStateException
from antlr4.Token import Token as Token

Lexer: Incomplete

class TokenStream: ...

class BufferedTokenStream(TokenStream):
    tokenSource: Incomplete
    tokens: Incomplete
    index: int
    fetchedEOF: bool
    def __init__(self, tokenSource: Lexer) -> None: ...
    def mark(self) -> int: ...
    def release(self, marker: int) -> None: ...
    def reset(self) -> None: ...
    def seek(self, index: int) -> None: ...
    def get(self, index: int) -> Token: ...
    def consume(self) -> None: ...
    def sync(self, i: int) -> bool: ...
    def fetch(self, n: int) -> int: ...
    def getTokens(self, start: int, stop: int, types: set[int] = ...) -> list[Token]: ...
    def LA(self, i: int) -> int: ...
    def LB(self, k: int) -> Token | None: ...
    def LT(self, k: int) -> Token | None: ...
    def adjustSeekIndex(self, i: int) -> Incomplete: ...
    def lazyInit(self) -> None: ...
    def setup(self) -> None: ...
    def setTokenSource(self, tokenSource: Lexer) -> Incomplete: ...
    def nextTokenOnChannel(self, i: int, channel: int) -> Incomplete: ...
    def previousTokenOnChannel(self, i: int, channel: int) -> Incomplete: ...
    def getHiddenTokensToRight(self, tokenIndex: int, channel: int = ...) -> Incomplete: ...
    def getHiddenTokensToLeft(self, tokenIndex: int, channel: int = ...) -> Incomplete: ...
    def filterForChannel(self, left: int, right: int, channel: int) -> Incomplete: ...
    def getSourceName(self) -> Incomplete: ...
    def getText(self, start: int = ..., stop: int = ...) -> Incomplete: ...
    def fill(self) -> None: ...
