from _typeshed import Incomplete

logger: Incomplete
ECR_URI_TEMPLATE: str
HUGGING_FACE_FRAMEWORK: str
HUGGING_FACE_LLM_FRAMEWORK: str
XGBOOST_FRAMEWORK: str
SKLEARN_FRAMEWORK: str
TRAINIUM_ALLOWED_FRAMEWORKS: str
INFERENCE_GRAVITON: str
DATA_WRANGLER_FRAMEWORK: str

def retrieve(
    framework,
    region,
    version: Incomplete | None = None,
    py_version: Incomplete | None = None,
    instance_type: Incomplete | None = None,
    accelerator_type: Incomplete | None = None,
    image_scope: Incomplete | None = None,
    container_version: Incomplete | None = None,
    distribution: Incomplete | None = None,
    base_framework_version: Incomplete | None = None,
    training_compiler_config: Incomplete | None = None,
    model_id: Incomplete | None = None,
    model_version: Incomplete | None = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
    sdk_version: Incomplete | None = None,
    inference_tool: Incomplete | None = None,
    serverless_inference_config: Incomplete | None = None,
) -> str: ...
def config_for_framework(framework): ...
def get_training_image_uri(
    region,
    framework,
    framework_version: Incomplete | None = None,
    py_version: Incomplete | None = None,
    image_uri: Incomplete | None = None,
    distribution: Incomplete | None = None,
    compiler_config: Incomplete | None = None,
    tensorflow_version: Incomplete | None = None,
    pytorch_version: Incomplete | None = None,
    instance_type: Incomplete | None = None,
) -> str: ...
def get_base_python_image_uri(region, py_version: str = "310") -> str: ...
