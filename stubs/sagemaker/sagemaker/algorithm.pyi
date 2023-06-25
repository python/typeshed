from _typeshed import Incomplete
from typing import Dict, List, Optional

from sagemaker.estimator import EstimatorBase
from sagemaker.inputs import FileSystemInput, TrainingInput
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

class AlgorithmEstimator(EstimatorBase):
    algorithm_arn: Incomplete
    algorithm_spec: Incomplete
    hyperparameter_definitions: Incomplete
    def __init__(
        self,
        algorithm_arn: str,
        role: str | None = None,
        instance_count: int | PipelineVariable | None = None,
        instance_type: str | PipelineVariable | None = None,
        volume_size: int | PipelineVariable = 30,
        volume_kms_key: str | PipelineVariable | None = None,
        max_run: int | PipelineVariable = 86400,
        input_mode: str | PipelineVariable = "File",
        output_path: str | PipelineVariable | None = None,
        output_kms_key: str | PipelineVariable | None = None,
        base_job_name: str | None = None,
        sagemaker_session: Session | None = None,
        hyperparameters: dict[str, str | PipelineVariable] | None = None,
        tags: list[dict[str, str | PipelineVariable]] | None = None,
        subnets: list[str | PipelineVariable] | None = None,
        security_group_ids: list[str | PipelineVariable] | None = None,
        model_uri: str | None = None,
        model_channel_name: str | PipelineVariable = "model",
        metric_definitions: list[dict[str, str | PipelineVariable]] | None = None,
        encrypt_inter_container_traffic: bool | PipelineVariable = False,
        use_spot_instances: bool | PipelineVariable = False,
        max_wait: int | PipelineVariable | None = None,
        **kwargs,
    ) -> None: ...
    def validate_train_spec(self) -> None: ...
    def set_hyperparameters(self, **kwargs) -> None: ...
    def hyperparameters(self): ...
    def training_image_uri(self) -> None: ...
    def enable_network_isolation(self): ...
    def create_model(
        self,
        role: Incomplete | None = None,
        predictor_cls: Incomplete | None = None,
        serializer=...,
        deserializer=...,
        vpc_config_override="VPC_CONFIG_DEFAULT",
        **kwargs,
    ): ...
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
    ): ...
    def fit(
        self,
        inputs: str | dict | TrainingInput | FileSystemInput | None = None,
        wait: bool = True,
        logs: bool = True,
        job_name: str | None = None,
    ): ...
