from _typeshed import Incomplete
from typing import Dict, Optional, Union

from sagemaker.estimator import Framework
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

class XGBoost(Framework):
    py_version: Incomplete
    framework_version: Incomplete
    image_uri: Incomplete
    def __init__(
        self,
        entry_point: str | PipelineVariable,
        framework_version: str,
        source_dir: Optional[str | PipelineVariable] = None,
        hyperparameters: Optional[Dict[str, str | PipelineVariable]] = None,
        py_version: str = "py3",
        image_uri: Optional[str | PipelineVariable] = None,
        image_uri_region: Optional[str] = None,
        **kwargs,
    ) -> None: ...
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
    @classmethod
    def attach(cls, training_job_name, sagemaker_session: Incomplete | None = None, model_channel_name: str = "model"): ...
