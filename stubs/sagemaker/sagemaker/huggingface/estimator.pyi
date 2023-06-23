from _typeshed import Incomplete
from typing import Dict, Optional

from sagemaker.estimator import Framework
from sagemaker.huggingface.training_compiler.config import TrainingCompilerConfig
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

class HuggingFace(Framework):
    LAUNCH_PYTORCH_DDP_ENV_NAME: str
    LAUNCH_TORCH_DISTRIBUTED_ENV_NAME: str
    INSTANCE_TYPE_ENV_NAME: str
    framework_version: Incomplete
    py_version: Incomplete
    tensorflow_version: Incomplete
    pytorch_version: Incomplete
    base_framework_name: Incomplete
    base_framework_version: Incomplete
    distribution: Incomplete
    compiler_config: Incomplete
    def __init__(
        self,
        py_version: str,
        entry_point: str | PipelineVariable,
        transformers_version: Optional[str] = None,
        tensorflow_version: Optional[str] = None,
        pytorch_version: Optional[str] = None,
        source_dir: Optional[str | PipelineVariable] = None,
        hyperparameters: Optional[Dict[str, str | PipelineVariable]] = None,
        image_uri: Optional[str | PipelineVariable] = None,
        distribution: Optional[Dict] = None,
        compiler_config: Optional[TrainingCompilerConfig] = None,
        **kwargs,
    ) -> None: ...
    def hyperparameters(self): ...
    def create_model(
        self,
        model_server_workers: Incomplete | None = None,
        role: Incomplete | None = None,
        vpc_config_override="VPC_CONFIG_DEFAULT",
        entry_point: Incomplete | None = None,
        source_dir: Incomplete | None = None,
        dependencies: Incomplete | None = None,
        **kwargs,
    ): ...
