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
        role: str = None,
        instance_count: Optional[int | PipelineVariable] = None,
        instance_type: Optional[str | PipelineVariable] = None,
        volume_size: int | PipelineVariable = 30,
        volume_kms_key: Optional[str | PipelineVariable] = None,
        max_run: int | PipelineVariable = 86400,
        input_mode: str | PipelineVariable = "File",
        output_path: Optional[str | PipelineVariable] = None,
        output_kms_key: Optional[str | PipelineVariable] = None,
        base_job_name: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        hyperparameters: Optional[Dict[str, str | PipelineVariable]] = None,
        tags: Optional[List[Dict[str, str | PipelineVariable]]] = None,
        subnets: Optional[List[str | PipelineVariable]] = None,
        security_group_ids: Optional[List[str | PipelineVariable]] = None,
        model_uri: Optional[str] = None,
        model_channel_name: str | PipelineVariable = "model",
        metric_definitions: Optional[List[Dict[str, str | PipelineVariable]]] = None,
        encrypt_inter_container_traffic: bool | PipelineVariable = False,
        use_spot_instances: bool | PipelineVariable = False,
        max_wait: Optional[int | PipelineVariable] = None,
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
        inputs: Optional[str | Dict | TrainingInput | FileSystemInput] = None,
        wait: bool = True,
        logs: bool = True,
        job_name: Optional[str] = None,
    ): ...
