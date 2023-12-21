from _typeshed import Incomplete

from antlr4 import DFA as DFA
from antlr4.dfa.DFAState import DFAState as DFAState
from antlr4.Utils import str_list as str_list

class DFASerializer:
    dfa: Incomplete
    literalNames: Incomplete
    symbolicNames: Incomplete
    def __init__(self, dfa: DFA, literalNames: list[str] = ..., symbolicNames: list[str] = ...) -> None: ...
    def getEdgeLabel(self, i: int): ...
    def getStateString(self, s: DFAState): ...

class LexerDFASerializer(DFASerializer):
    def __init__(self, dfa: DFA) -> None: ...
    def getEdgeLabel(self, i: int): ...
