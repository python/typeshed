from _typeshed import Incomplete
from typing import Dict, List, Optional

from sagemaker.huggingface.estimator import HuggingFace
from sagemaker.network import NetworkConfig
from sagemaker.processing import FrameworkProcessor
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

class HuggingFaceProcessor(FrameworkProcessor):
    estimator_cls = HuggingFace
    pytorch_version: Incomplete
    tensorflow_version: Incomplete
    def __init__(
        self,
        role: str | PipelineVariable | None = None,
        instance_count: int | PipelineVariable | None = None,
        instance_type: str | PipelineVariable | None = None,
        transformers_version: str | None = None,
        tensorflow_version: str | None = None,
        pytorch_version: str | None = None,
        py_version: str = "py36",
        image_uri: str | PipelineVariable | None = None,
        command: list[str] | None = None,
        volume_size_in_gb: int | PipelineVariable = 30,
        volume_kms_key: str | PipelineVariable | None = None,
        output_kms_key: str | PipelineVariable | None = None,
        code_location: str | None = None,
        max_runtime_in_seconds: int | PipelineVariable | None = None,
        base_job_name: str | None = None,
        sagemaker_session: Session | None = None,
        env: dict[str, str | PipelineVariable] | None = None,
        tags: list[dict[str, str | PipelineVariable]] | None = None,
        network_config: NetworkConfig | None = None,
    ) -> None: ...
