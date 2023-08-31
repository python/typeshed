import abc
from _typeshed import Incomplete
from abc import ABC
from enum import Enum

class EvaluationMetricTypeEnum(str, Enum):
    MODEL_CARD_METRIC_SCHEMA: str
    CLARIFY_BIAS: str
    CLARIFY_EXPLAINABILITY: str
    REGRESSION: str
    BINARY_CLASSIFICATION: str
    MULTICLASS_CLASSIFICATION: str

class ParserBase(ABC, metaclass=abc.ABCMeta):
    def run(self, json_data: dict): ...

class DefaultParser(ParserBase): ...
class ClarifyBiasParser(ParserBase): ...
class ClarifyExplainabilityParser(ParserBase): ...
class ModelMonitorModelQualityParserBase(ParserBase, metaclass=abc.ABCMeta): ...
class RegressionParser(ModelMonitorModelQualityParserBase): ...
class ClassificationParser(ModelMonitorModelQualityParserBase): ...

EVALUATION_METRIC_PARSERS: Incomplete
