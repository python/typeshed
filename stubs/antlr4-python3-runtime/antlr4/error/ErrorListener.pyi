from _typeshed import Incomplete

class ErrorListener:
    def syntaxError(
        self,
        recognizer: Incomplete,
        offendingSymbol: Incomplete,
        line: Incomplete,
        column: Incomplete,
        msg: Incomplete,
        e: Incomplete,
    ) -> None: ...
    def reportAmbiguity(
        self,
        recognizer: Incomplete,
        dfa: Incomplete,
        startIndex: Incomplete,
        stopIndex: Incomplete,
        exact: Incomplete,
        ambigAlts: Incomplete,
        configs: Incomplete,
    ) -> None: ...
    def reportAttemptingFullContext(
        self,
        recognizer: Incomplete,
        dfa: Incomplete,
        startIndex: Incomplete,
        stopIndex: Incomplete,
        conflictingAlts: Incomplete,
        configs: Incomplete,
    ) -> None: ...
    def reportContextSensitivity(
        self,
        recognizer: Incomplete,
        dfa: Incomplete,
        startIndex: Incomplete,
        stopIndex: Incomplete,
        prediction: Incomplete,
        configs: Incomplete,
    ) -> None: ...

class ConsoleErrorListener(ErrorListener):
    INSTANCE: Incomplete
    def syntaxError(
        self,
        recognizer: Incomplete,
        offendingSymbol: Incomplete,
        line: Incomplete,
        column: Incomplete,
        msg: Incomplete,
        e: Incomplete,
    ) -> None: ...

class ProxyErrorListener(ErrorListener):
    delegates: Incomplete
    def __init__(self, delegates: Incomplete) -> None: ...
    def syntaxError(
        self,
        recognizer: Incomplete,
        offendingSymbol: Incomplete,
        line: Incomplete,
        column: Incomplete,
        msg: Incomplete,
        e: Incomplete,
    ) -> None: ...
    def reportAmbiguity(
        self,
        recognizer: Incomplete,
        dfa: Incomplete,
        startIndex: Incomplete,
        stopIndex: Incomplete,
        exact: Incomplete,
        ambigAlts: Incomplete,
        configs: Incomplete,
    ) -> None: ...
    def reportAttemptingFullContext(
        self,
        recognizer: Incomplete,
        dfa: Incomplete,
        startIndex: Incomplete,
        stopIndex: Incomplete,
        conflictingAlts: Incomplete,
        configs: Incomplete,
    ) -> None: ...
    def reportContextSensitivity(
        self,
        recognizer: Incomplete,
        dfa: Incomplete,
        startIndex: Incomplete,
        stopIndex: Incomplete,
        prediction: Incomplete,
        configs: Incomplete,
    ) -> None: ...
