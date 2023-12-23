from _typeshed import Incomplete

from antlr4 import DFA as DFA
from antlr4.atn.ATNConfigSet import ATNConfigSet as ATNConfigSet
from antlr4.error.ErrorListener import ErrorListener as ErrorListener

class DiagnosticErrorListener(ErrorListener):
    exactOnly: Incomplete
    def __init__(self, exactOnly: bool = ...) -> None: ...
    def reportAmbiguity(
        self,
        recognizer: Incomplete,
        dfa: DFA,
        startIndex: int,
        stopIndex: int,
        exact: bool,
        ambigAlts: set[int],
        configs: ATNConfigSet,
    ) -> Incomplete: ...
    def reportAttemptingFullContext(
        self, recognizer: Incomplete, dfa: DFA, startIndex: int, stopIndex: int, conflictingAlts: set[int], configs: ATNConfigSet
    ) -> Incomplete: ...
    def reportContextSensitivity(
        self, recognizer: Incomplete, dfa: DFA, startIndex: int, stopIndex: int, prediction: int, configs: ATNConfigSet
    ) -> Incomplete: ...
    def getDecisionDescription(self, recognizer: Incomplete, dfa: DFA) -> Incomplete: ...
    def getConflictingAlts(self, reportedAlts: set[int], configs: ATNConfigSet) -> Incomplete: ...
