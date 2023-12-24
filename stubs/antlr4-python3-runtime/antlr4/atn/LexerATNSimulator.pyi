from _typeshed import Incomplete

from antlr4.atn.ATN import ATN as ATN
from antlr4.atn.ATNConfig import LexerATNConfig as LexerATNConfig
from antlr4.atn.ATNConfigSet import ATNConfigSet as ATNConfigSet, OrderedATNConfigSet as OrderedATNConfigSet
from antlr4.atn.ATNSimulator import ATNSimulator as ATNSimulator
from antlr4.atn.ATNState import ATNState as ATNState, RuleStopState as RuleStopState
from antlr4.atn.LexerActionExecutor import LexerActionExecutor as LexerActionExecutor
from antlr4.atn.Transition import Transition as Transition
from antlr4.dfa.DFA import DFA
from antlr4.dfa.DFAState import DFAState as DFAState
from antlr4.error.Errors import (
    LexerNoViableAltException as LexerNoViableAltException,
    UnsupportedOperationException as UnsupportedOperationException,
)
from antlr4.InputStream import InputStream as InputStream
from antlr4.PredictionContext import (
    PredictionContext as PredictionContext,
    PredictionContextCache as PredictionContextCache,
    SingletonPredictionContext as SingletonPredictionContext,
)
from antlr4.Token import Token as Token

class SimState:
    def __init__(self) -> None: ...
    index: int
    line: int
    column: int
    dfaState: Incomplete
    def reset(self) -> None: ...

Lexer: Incomplete

class LexerATNSimulator(ATNSimulator):
    debug: bool
    dfa_debug: bool
    MIN_DFA_EDGE: int
    MAX_DFA_EDGE: int
    ERROR: Incomplete
    decisionToDFA: Incomplete
    recog: Incomplete
    startIndex: int
    line: int
    column: int
    mode: Incomplete
    DEFAULT_MODE: Incomplete
    MAX_CHAR_VALUE: Incomplete
    prevAccept: Incomplete
    def __init__(self, recog: Lexer, atn: ATN, decisionToDFA: list[DFA], sharedContextCache: PredictionContextCache) -> None: ...
    def copyState(self, simulator: LexerATNSimulator) -> Incomplete: ...
    def match(self, input: InputStream, mode: int) -> Incomplete: ...
    def reset(self) -> None: ...
    def matchATN(self, input: InputStream) -> Incomplete: ...
    def execATN(self, input: InputStream, ds0: DFAState) -> Incomplete: ...
    def getExistingTargetState(self, s: DFAState, t: int) -> Incomplete: ...
    def computeTargetState(self, input: InputStream, s: DFAState, t: int) -> Incomplete: ...
    def failOrAccept(self, prevAccept: SimState, input: InputStream, reach: ATNConfigSet, t: int) -> Incomplete: ...
    def getReachableConfigSet(self, input: InputStream, closure: ATNConfigSet, reach: ATNConfigSet, t: int) -> Incomplete: ...
    def accept(
        self, input: InputStream, lexerActionExecutor: LexerActionExecutor, startIndex: int, index: int, line: int, charPos: int
    ) -> Incomplete: ...
    def getReachableTarget(self, trans: Transition, t: int) -> Incomplete: ...
    def computeStartState(self, input: InputStream, p: ATNState) -> Incomplete: ...
    def closure(
        self,
        input: InputStream,
        config: LexerATNConfig,
        configs: ATNConfigSet,
        currentAltReachedAcceptState: bool,
        speculative: bool,
        treatEofAsEpsilon: bool,
    ) -> Incomplete: ...
    def getEpsilonTarget(
        self,
        input: InputStream,
        config: LexerATNConfig,
        t: Transition,
        configs: ATNConfigSet,
        speculative: bool,
        treatEofAsEpsilon: bool,
    ) -> Incomplete: ...
    def evaluatePredicate(self, input: InputStream, ruleIndex: int, predIndex: int, speculative: bool) -> Incomplete: ...
    def captureSimState(self, settings: SimState, input: InputStream, dfaState: DFAState) -> Incomplete: ...
    def addDFAEdge(self, from_: DFAState, tk: int, to: DFAState | None = None, cfgs: ATNConfigSet | None = None) -> DFAState: ...
    def addDFAState(self, configs: ATNConfigSet) -> DFAState: ...
    def getDFA(self, mode: int) -> Incomplete: ...
    def getText(self, input: InputStream) -> Incomplete: ...
    def consume(self, input: InputStream) -> Incomplete: ...
    def getTokenName(self, t: int) -> Incomplete: ...
