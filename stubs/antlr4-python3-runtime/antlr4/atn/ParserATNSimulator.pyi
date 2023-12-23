from _typeshed import Incomplete

from antlr4 import DFA as DFA
from antlr4.atn.ATN import ATN as ATN
from antlr4.atn.ATNConfig import ATNConfig as ATNConfig
from antlr4.atn.ATNConfigSet import ATNConfigSet as ATNConfigSet
from antlr4.atn.ATNSimulator import ATNSimulator as ATNSimulator
from antlr4.atn.ATNState import ATNState as ATNState, DecisionState as DecisionState, RuleStopState as RuleStopState
from antlr4.atn.PredictionMode import PredictionMode as PredictionMode
from antlr4.atn.SemanticContext import SemanticContext as SemanticContext, andContext as andContext, orContext as orContext
from antlr4.atn.Transition import (
    ActionTransition as ActionTransition,
    AtomTransition as AtomTransition,
    NotSetTransition as NotSetTransition,
    PrecedencePredicateTransition as PrecedencePredicateTransition,
    PredicateTransition as PredicateTransition,
    RuleTransition as RuleTransition,
    SetTransition as SetTransition,
    Transition as Transition,
)
from antlr4.BufferedTokenStream import TokenStream as TokenStream
from antlr4.dfa.DFAState import DFAState as DFAState, PredPrediction as PredPrediction
from antlr4.error.Errors import NoViableAltException as NoViableAltException
from antlr4.Parser import Parser as Parser
from antlr4.ParserRuleContext import ParserRuleContext as ParserRuleContext
from antlr4.PredictionContext import (
    PredictionContext as PredictionContext,
    PredictionContextCache as PredictionContextCache,
    PredictionContextFromRuleContext as PredictionContextFromRuleContext,
    SingletonPredictionContext as SingletonPredictionContext,
)
from antlr4.RuleContext import RuleContext as RuleContext
from antlr4.Token import Token as Token
from antlr4.Utils import str_list as str_list

class ParserATNSimulator(ATNSimulator):
    debug: bool
    trace_atn_sim: bool
    dfa_debug: bool
    retry_debug: bool
    parser: Incomplete
    decisionToDFA: Incomplete
    predictionMode: Incomplete
    mergeCache: Incomplete
    def __init__(
        self, parser: Parser, atn: ATN, decisionToDFA: list[DFA], sharedContextCache: PredictionContextCache
    ) -> None: ...
    def reset(self) -> None: ...
    def adaptivePredict(self, input: TokenStream, decision: int, outerContext: ParserRuleContext) -> Incomplete: ...
    def execATN(
        self, dfa: DFA, s0: DFAState, input: TokenStream, startIndex: int, outerContext: ParserRuleContext
    ) -> Incomplete: ...
    def getExistingTargetState(self, previousD: DFAState, t: int) -> Incomplete: ...
    def computeTargetState(self, dfa: DFA, previousD: DFAState, t: int) -> Incomplete: ...
    def predicateDFAState(self, dfaState: DFAState, decisionState: DecisionState) -> Incomplete: ...
    def execATNWithFullContext(
        self, dfa: DFA, D: DFAState, s0: ATNConfigSet, input: TokenStream, startIndex: int, outerContext: ParserRuleContext
    ) -> Incomplete: ...
    def computeReachSet(self, closure: ATNConfigSet, t: int, fullCtx: bool) -> Incomplete: ...
    def removeAllConfigsNotInRuleStopState(self, configs: ATNConfigSet, lookToEndOfRule: bool) -> Incomplete: ...
    def computeStartState(self, p: ATNState, ctx: RuleContext, fullCtx: bool) -> Incomplete: ...
    def applyPrecedenceFilter(self, configs: ATNConfigSet) -> Incomplete: ...
    def getReachableTarget(self, trans: Transition, ttype: int) -> Incomplete: ...
    def getPredsForAmbigAlts(self, ambigAlts: set[int], configs: ATNConfigSet, nalts: int) -> Incomplete: ...
    def getPredicatePredictions(self, ambigAlts: set[int], altToPred: list[int]) -> Incomplete: ...
    def getSynValidOrSemInvalidAltThatFinishedDecisionEntryRule(
        self, configs: ATNConfigSet, outerContext: ParserRuleContext
    ) -> Incomplete: ...
    def getAltThatFinishedDecisionEntryRule(self, configs: ATNConfigSet) -> Incomplete: ...
    def splitAccordingToSemanticValidity(self, configs: ATNConfigSet, outerContext: ParserRuleContext) -> Incomplete: ...
    def evalSemanticContext(
        self, predPredictions: list[Incomplete], outerContext: ParserRuleContext, complete: bool
    ) -> Incomplete: ...
    def closure(
        self,
        config: ATNConfig,
        configs: ATNConfigSet,
        closureBusy: set[Incomplete],
        collectPredicates: bool,
        fullCtx: bool,
        treatEofAsEpsilon: bool,
    ) -> Incomplete: ...
    def closureCheckingStopState(
        self,
        config: ATNConfig,
        configs: ATNConfigSet,
        closureBusy: set[Incomplete],
        collectPredicates: bool,
        fullCtx: bool,
        depth: int,
        treatEofAsEpsilon: bool,
    ) -> Incomplete: ...
    def closure_(
        self,
        config: ATNConfig,
        configs: ATNConfigSet,
        closureBusy: set[Incomplete],
        collectPredicates: bool,
        fullCtx: bool,
        depth: int,
        treatEofAsEpsilon: bool,
    ) -> Incomplete: ...
    def canDropLoopEntryEdgeInLeftRecursiveRule(self, config: Incomplete) -> Incomplete: ...
    def getRuleName(self, index: int) -> Incomplete: ...
    epsilonTargetMethods: Incomplete
    def getEpsilonTarget(
        self, config: ATNConfig, t: Transition, collectPredicates: bool, inContext: bool, fullCtx: bool, treatEofAsEpsilon: bool
    ) -> Incomplete: ...
    def actionTransition(self, config: ATNConfig, t: ActionTransition) -> Incomplete: ...
    def precedenceTransition(
        self, config: ATNConfig, pt: PrecedencePredicateTransition, collectPredicates: bool, inContext: bool, fullCtx: bool
    ) -> Incomplete: ...
    def predTransition(
        self, config: ATNConfig, pt: PredicateTransition, collectPredicates: bool, inContext: bool, fullCtx: bool
    ) -> Incomplete: ...
    def ruleTransition(self, config: ATNConfig, t: RuleTransition) -> Incomplete: ...
    def getConflictingAlts(self, configs: ATNConfigSet) -> Incomplete: ...
    def getConflictingAltsOrUniqueAlt(self, configs: ATNConfigSet) -> Incomplete: ...
    def getTokenName(self, t: int) -> Incomplete: ...
    def getLookaheadName(self, input: TokenStream) -> Incomplete: ...
    def dumpDeadEndConfigs(self, nvae: NoViableAltException) -> Incomplete: ...
    def noViableAlt(
        self, input: TokenStream, outerContext: ParserRuleContext, configs: ATNConfigSet, startIndex: int
    ) -> Incomplete: ...
    def getUniqueAlt(self, configs: ATNConfigSet) -> Incomplete: ...
    def addDFAEdge(self, dfa: DFA, from_: DFAState, t: int, to: DFAState) -> Incomplete: ...
    def addDFAState(self, dfa: DFA, D: DFAState) -> Incomplete: ...
    def reportAttemptingFullContext(
        self, dfa: DFA, conflictingAlts: set[Incomplete], configs: ATNConfigSet, startIndex: int, stopIndex: int
    ) -> Incomplete: ...
    def reportContextSensitivity(
        self, dfa: DFA, prediction: int, configs: ATNConfigSet, startIndex: int, stopIndex: int
    ) -> Incomplete: ...
    def reportAmbiguity(
        self,
        dfa: DFA,
        D: DFAState,
        startIndex: int,
        stopIndex: int,
        exact: bool,
        ambigAlts: set[Incomplete],
        configs: ATNConfigSet,
    ) -> Incomplete: ...
