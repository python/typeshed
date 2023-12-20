from enum import Enum

from antlr4.atn.ATN import ATN as ATN
from antlr4.atn.ATNConfig import ATNConfig as ATNConfig
from antlr4.atn.ATNConfigSet import ATNConfigSet as ATNConfigSet
from antlr4.atn.ATNState import RuleStopState as RuleStopState
from antlr4.atn.SemanticContext import SemanticContext as SemanticContext

class PredictionMode(Enum):
    SLL: int
    LL: int
    LL_EXACT_AMBIG_DETECTION: int
    @classmethod
    def hasSLLConflictTerminatingPrediction(cls, mode: PredictionMode, configs: ATNConfigSet): ...
    @classmethod
    def hasConfigInRuleStopState(cls, configs: ATNConfigSet): ...
    @classmethod
    def allConfigsInRuleStopStates(cls, configs: ATNConfigSet): ...
    @classmethod
    def resolvesToJustOneViableAlt(cls, altsets: list): ...
    @classmethod
    def allSubsetsConflict(cls, altsets: list): ...
    @classmethod
    def hasNonConflictingAltSet(cls, altsets: list): ...
    @classmethod
    def hasConflictingAltSet(cls, altsets: list): ...
    @classmethod
    def allSubsetsEqual(cls, altsets: list): ...
    @classmethod
    def getUniqueAlt(cls, altsets: list): ...
    @classmethod
    def getAlts(cls, altsets: list): ...
    @classmethod
    def getConflictingAltSubsets(cls, configs: ATNConfigSet): ...
    @classmethod
    def getStateToAltMap(cls, configs: ATNConfigSet): ...
    @classmethod
    def hasStateAssociatedWithOneAlt(cls, configs: ATNConfigSet): ...
    @classmethod
    def getSingleViableAlt(cls, altsets: list): ...
