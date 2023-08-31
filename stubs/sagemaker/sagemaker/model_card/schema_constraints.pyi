from _typeshed import Incomplete
from enum import Enum

class ModelCardStatusEnum(str, Enum):
    DRAFT: str
    PENDING_REVIEW: str
    APPROVED: str
    ARCHIVED: str

class RiskRatingEnum(str, Enum):
    HIGH: str
    MEDIUM: str
    LOW: str
    UNKNOWN: str

class ObjectiveFunctionEnum(str, Enum):
    MAXIMIZE: str
    MINIMIZE: str

class FacetEnum(str, Enum):
    LOSS: str
    ACCURACY: str
    RMSE: str
    MAE: str
    AUC: str

class MetricTypeEnum(str, Enum):
    NUMBER: str
    LINEAR_GRAPH: str
    STRING: str
    BOOLEAN: str
    MATRIX: str
    BAR_CHART: str

METRIC_VALUE_TYPE_MAP: Incomplete
PYTHON_TYPE_TO_METRIC_VALUE_TYPE: Incomplete
MODEL_ARTIFACT_MAX_SIZE: int
ENVIRONMENT_CONTAINER_IMAGES_MAX_SIZE: int
TRAINING_DATASETS_MAX_SIZE: int
TRAINING_METRICS_MAX_SIZE: int
USER_PROVIDED_TRAINING_METRICS_MAX_SIZE: int
HYPER_PARAMETERS_MAX_SIZE: int
USER_PROVIDED_HYPER_PARAMETERS_MAX_SIZE: int
EVALUATION_DATASETS_MAX_SIZE: int
