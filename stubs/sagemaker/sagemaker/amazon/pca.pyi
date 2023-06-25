from _typeshed import Incomplete
from typing import Optional

from sagemaker.amazon.amazon_estimator import AmazonAlgorithmEstimatorBase
from sagemaker.amazon.hyperparameter import Hyperparameter as hp
from sagemaker.model import Model
from sagemaker.predictor import Predictor
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

class PCA(AmazonAlgorithmEstimatorBase):
    repo_name: str
    repo_version: str
    DEFAULT_MINI_BATCH_SIZE: int
    num_components: hp
    algorithm_mode: hp
    subtract_mean: hp
    extra_components: hp
    def __init__(
        self,
        role: str | PipelineVariable | None = None,
        instance_count: int | PipelineVariable | None = None,
        instance_type: str | PipelineVariable | None = None,
        num_components: int | None = None,
        algorithm_mode: str | None = None,
        subtract_mean: bool | None = None,
        extra_components: int | None = None,
        **kwargs,
    ) -> None: ...
    def create_model(self, vpc_config_override="VPC_CONFIG_DEFAULT", **kwargs): ...

class PCAPredictor(Predictor):
    def __init__(self, endpoint_name, sagemaker_session: Incomplete | None = None, serializer=..., deserializer=...) -> None: ...

class PCAModel(Model):
    def __init__(
        self,
        model_data: str | PipelineVariable,
        role: str | None = None,
        sagemaker_session: Session | None = None,
        **kwargs,
    ) -> None: ...
