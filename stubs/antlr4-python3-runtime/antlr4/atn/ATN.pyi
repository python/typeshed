from _typeshed import Incomplete

from antlr4.atn.ATNState import ATNState as ATNState, DecisionState as DecisionState
from antlr4.atn.ATNType import ATNType as ATNType
from antlr4.IntervalSet import IntervalSet as IntervalSet
from antlr4.RuleContext import RuleContext as RuleContext
from antlr4.Token import Token as Token

class ATN:
    INVALID_ALT_NUMBER: int
    grammarType: Incomplete
    maxTokenType: Incomplete
    states: Incomplete
    decisionToState: Incomplete
    ruleToStartState: Incomplete
    ruleToStopState: Incomplete
    modeNameToStartState: Incomplete
    ruleToTokenType: Incomplete
    lexerActions: Incomplete
    modeToStartState: Incomplete
    def __init__(self, grammarType: ATNType, maxTokenType: int) -> None: ...
    def nextTokensInContext(self, s: ATNState, ctx: RuleContext) -> Incomplete: ...
    def nextTokensNoContext(self, s: ATNState) -> Incomplete: ...
    def nextTokens(self, s: ATNState, ctx: RuleContext = ...) -> Incomplete: ...
    def addState(self, state: ATNState) -> Incomplete: ...
    def removeState(self, state: ATNState) -> Incomplete: ...
    def defineDecisionState(self, s: DecisionState) -> Incomplete: ...
    def getDecisionState(self, decision: int) -> Incomplete: ...
    def getExpectedTokens(self, stateNumber: int, ctx: RuleContext) -> Incomplete: ...
