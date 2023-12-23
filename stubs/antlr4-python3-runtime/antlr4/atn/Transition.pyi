from _typeshed import Incomplete

from antlr4.atn.ATNState import *
from antlr4.atn.SemanticContext import PrecedencePredicate as PrecedencePredicate, Predicate as Predicate
from antlr4.IntervalSet import IntervalSet as IntervalSet
from antlr4.Token import Token as Token

class Transition:
    EPSILON: int
    RANGE: int
    RULE: int
    PREDICATE: int
    ATOM: int
    ACTION: int
    SET: int
    NOT_SET: int
    WILDCARD: int
    PRECEDENCE: int
    serializationNames: Incomplete
    serializationTypes: Incomplete
    target: Incomplete
    isEpsilon: bool
    label: Incomplete
    def __init__(self, target: ATNState) -> None: ...

class AtomTransition(Transition):
    label_: Incomplete
    label: Incomplete
    serializationType: Incomplete
    def __init__(self, target: ATNState, label: int) -> None: ...
    def makeLabel(self) -> Incomplete: ...
    def matches(self, symbol: int, minVocabSymbol: int, maxVocabSymbol: int) -> Incomplete: ...

class RuleTransition(Transition):
    ruleIndex: Incomplete
    precedence: Incomplete
    followState: Incomplete
    serializationType: Incomplete
    isEpsilon: bool
    def __init__(self, ruleStart: RuleStartState, ruleIndex: int, precedence: int, followState: ATNState) -> None: ...
    def matches(self, symbol: int, minVocabSymbol: int, maxVocabSymbol: int) -> Incomplete: ...

class EpsilonTransition(Transition):
    serializationType: Incomplete
    isEpsilon: bool
    outermostPrecedenceReturn: Incomplete
    def __init__(self, target: Incomplete, outermostPrecedenceReturn: int = ...) -> None: ...
    def matches(self, symbol: int, minVocabSymbol: int, maxVocabSymbol: int) -> Incomplete: ...

class RangeTransition(Transition):
    serializationType: Incomplete
    start: Incomplete
    stop: Incomplete
    label: Incomplete
    def __init__(self, target: ATNState, start: int, stop: int) -> None: ...
    def makeLabel(self) -> Incomplete: ...
    def matches(self, symbol: int, minVocabSymbol: int, maxVocabSymbol: int) -> Incomplete: ...

class AbstractPredicateTransition(Transition):
    def __init__(self, target: ATNState) -> None: ...

class PredicateTransition(AbstractPredicateTransition):
    serializationType: Incomplete
    ruleIndex: Incomplete
    predIndex: Incomplete
    isCtxDependent: Incomplete
    isEpsilon: bool
    def __init__(self, target: ATNState, ruleIndex: int, predIndex: int, isCtxDependent: bool) -> None: ...
    def matches(self, symbol: int, minVocabSymbol: int, maxVocabSymbol: int) -> Incomplete: ...
    def getPredicate(self) -> Incomplete: ...

class ActionTransition(Transition):
    serializationType: Incomplete
    ruleIndex: Incomplete
    actionIndex: Incomplete
    isCtxDependent: Incomplete
    isEpsilon: bool
    def __init__(self, target: ATNState, ruleIndex: int, actionIndex: int = ..., isCtxDependent: bool = ...) -> None: ...
    def matches(self, symbol: int, minVocabSymbol: int, maxVocabSymbol: int) -> Incomplete: ...

class SetTransition(Transition):
    serializationType: Incomplete
    label: Incomplete
    def __init__(self, target: ATNState, set: IntervalSet) -> None: ...
    def matches(self, symbol: int, minVocabSymbol: int, maxVocabSymbol: int) -> Incomplete: ...

class NotSetTransition(SetTransition):
    serializationType: Incomplete
    def __init__(self, target: ATNState, set: IntervalSet) -> None: ...
    def matches(self, symbol: int, minVocabSymbol: int, maxVocabSymbol: int) -> Incomplete: ...

class WildcardTransition(Transition):
    serializationType: Incomplete
    def __init__(self, target: ATNState) -> None: ...
    def matches(self, symbol: int, minVocabSymbol: int, maxVocabSymbol: int) -> Incomplete: ...

class PrecedencePredicateTransition(AbstractPredicateTransition):
    serializationType: Incomplete
    precedence: Incomplete
    isEpsilon: bool
    def __init__(self, target: ATNState, precedence: int) -> None: ...
    def matches(self, symbol: int, minVocabSymbol: int, maxVocabSymbol: int) -> Incomplete: ...
    def getPredicate(self) -> Incomplete: ...
