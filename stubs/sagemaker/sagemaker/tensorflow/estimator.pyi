from _typeshed import Incomplete
from typing import Dict, Optional

from sagemaker.estimator import Framework
from sagemaker.tensorflow.training_compiler.config import TrainingCompilerConfig
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

class TensorFlow(Framework):
    framework_version: Incomplete
    py_version: Incomplete
    instance_type: Incomplete
    model_dir: Incomplete
    distribution: Incomplete
    compiler_config: Incomplete
    def __init__(
        self,
        py_version: Optional[str] = None,
        framework_version: Optional[str] = None,
        model_dir: Optional[str | PipelineVariable] = None,
        image_uri: Optional[str | PipelineVariable] = None,
        distribution: Optional[Dict[str, str]] = None,
        compiler_config: Optional[TrainingCompilerConfig] = None,
        **kwargs,
    ) -> None: ...
    def create_model(
        self,
        role: Incomplete | None = None,
        vpc_config_override="VPC_CONFIG_DEFAULT",
        entry_point: Incomplete | None = None,
        source_dir: Incomplete | None = None,
        dependencies: Incomplete | None = None,
        **kwargs,
    ): ...
    def hyperparameters(self): ...
    def transformer(
        self,
        instance_count,
        instance_type,
        strategy: Incomplete | None = None,
        assemble_with: Incomplete | None = None,
        output_path: Incomplete | None = None,
        output_kms_key: Incomplete | None = None,
        accept: Incomplete | None = None,
        env: Incomplete | None = None,
        max_concurrent_transforms: Incomplete | None = None,
        max_payload: Incomplete | None = None,
        tags: Incomplete | None = None,
        role: Incomplete | None = None,
        volume_kms_key: Incomplete | None = None,
        entry_point: Incomplete | None = None,
        vpc_config_override="VPC_CONFIG_DEFAULT",
        enable_network_isolation: Incomplete | None = None,
        model_name: Incomplete | None = None,
    ): ...
