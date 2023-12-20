from _typeshed import Incomplete
from antlr4.InputStream import InputStream as InputStream

class FileStream(InputStream):
    fileName: Incomplete
    def __init__(self, fileName: str, encoding: str = ..., errors: str = ...) -> None: ...
    def readDataFrom(self, fileName: str, encoding: str, errors: str = ...): ...
