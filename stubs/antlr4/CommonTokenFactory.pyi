from _typeshed import Incomplete
from antlr4.Token import CommonToken as CommonToken

class TokenFactory: ...

class CommonTokenFactory(TokenFactory):
    DEFAULT: Incomplete
    copyText: Incomplete
    def __init__(self, copyText: bool = ...) -> None: ...
    def create(self, source, type: int, text: str, channel: int, start: int, stop: int, line: int, column: int): ...
    def createThin(self, type: int, text: str): ...
