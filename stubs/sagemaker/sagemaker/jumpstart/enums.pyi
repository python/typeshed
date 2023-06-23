from enum import Enum

class ModelFramework(str, Enum):
    PYTORCH: str
    TENSORFLOW: str
    MXNET: str
    HUGGINGFACE: str
    LIGHTGBM: str
    CATBOOST: str
    XGBOOST: str
    SKLEARN: str

class VariableScope(str, Enum):
    CONTAINER: str
    ALGORITHM: str

class JumpStartScriptScope(str, Enum):
    INFERENCE: str
    TRAINING: str

class HyperparameterValidationMode(str, Enum):
    VALIDATE_PROVIDED: str
    VALIDATE_ALGORITHM: str
    VALIDATE_ALL: str

class VariableTypes(str, Enum):
    TEXT: str
    INT: str
    FLOAT: str
    BOOL: str

class JumpStartTag(str, Enum):
    INFERENCE_MODEL_URI: str
    INFERENCE_SCRIPT_URI: str
    TRAINING_MODEL_URI: str
    TRAINING_SCRIPT_URI: str

class SerializerType(str, Enum):
    TEXT: str
    JSON: str
    CSV: str
    RAW_BYTES: str

class DeserializerType(str, Enum):
    JSON: str

class MIMEType(str, Enum):
    X_IMAGE: str
    LIST_TEXT: str
    X_TEXT: str
    JSON: str
    CSV: str
    WAV: str
    @staticmethod
    def from_suffixed_type(mime_type_with_suffix: str) -> MIMEType: ...
