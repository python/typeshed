from enum import Enum
from typing import Any, Dict

from sagemaker.feature_store.inputs import Config

class FeatureTypeEnum(Enum):
    FRACTIONAL: str
    INTEGRAL: str
    STRING: str

class FeatureDefinition(Config):
    feature_name: str
    feature_type: FeatureTypeEnum
    def to_dict(self) -> Dict[str, Any]: ...
    def __init__(self, feature_name, feature_type) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class FractionalFeatureDefinition(FeatureDefinition):
    def __init__(self, feature_name: str) -> None: ...

class IntegralFeatureDefinition(FeatureDefinition):
    def __init__(self, feature_name: str) -> None: ...

class StringFeatureDefinition(FeatureDefinition):
    def __init__(self, feature_name: str) -> None: ...
