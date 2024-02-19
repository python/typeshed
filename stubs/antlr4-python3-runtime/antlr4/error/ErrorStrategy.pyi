from _typeshed import Incomplete

from antlr4.atn.ATNState import ATNState as ATNState
from antlr4.error.Errors import (
    FailedPredicateException as FailedPredicateException,
    InputMismatchException as InputMismatchException,
    NoViableAltException as NoViableAltException,
    ParseCancellationException as ParseCancellationException,
    RecognitionException as RecognitionException,
)
from antlr4.IntervalSet import IntervalSet as IntervalSet
from antlr4.Token import Token as Token

class ErrorStrategy:
    def reset(self, recognizer): ...
    def recoverInline(self, recognizer): ...
    def recover(self, recognizer, e: RecognitionException): ...
    def sync(self, recognizer): ...
    def inErrorRecoveryMode(self, recognizer): ...
    def reportError(self, recognizer, e: RecognitionException): ...

class DefaultErrorStrategy(ErrorStrategy):
    errorRecoveryMode: bool
    lastErrorIndex: int
    lastErrorStates: Incomplete
    nextTokensContext: Incomplete
    nextTokenState: int
    def __init__(self) -> None: ...
    def reset(self, recognizer): ...
    def beginErrorCondition(self, recognizer): ...
    def inErrorRecoveryMode(self, recognizer): ...
    def endErrorCondition(self, recognizer): ...
    def reportMatch(self, recognizer): ...
    def reportError(self, recognizer, e: RecognitionException): ...
    def recover(self, recognizer, e: RecognitionException): ...
    nextTokensState: Incomplete
    def sync(self, recognizer): ...
    def reportNoViableAlternative(self, recognizer, e: NoViableAltException): ...
    def reportInputMismatch(self, recognizer, e: InputMismatchException): ...
    def reportFailedPredicate(self, recognizer, e) -> None: ...
    def reportUnwantedToken(self, recognizer): ...
    def reportMissingToken(self, recognizer): ...
    def recoverInline(self, recognizer): ...
    def singleTokenInsertion(self, recognizer): ...
    def singleTokenDeletion(self, recognizer): ...
    def getMissingSymbol(self, recognizer): ...
    def getExpectedTokens(self, recognizer): ...
    def getTokenErrorDisplay(self, t: Token): ...
    def escapeWSAndQuote(self, s: str): ...
    def getErrorRecoverySet(self, recognizer): ...
    def consumeUntil(self, recognizer, set_: set[int]): ...

class BailErrorStrategy(DefaultErrorStrategy):
    def recover(self, recognizer, e: RecognitionException): ...
    def recoverInline(self, recognizer): ...
    def sync(self, recognizer): ...
