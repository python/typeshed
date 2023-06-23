from _typeshed import Incomplete
from typing import Optional, Union

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
        role: Optional[Union[str, PipelineVariable]] = None,
        instance_count: Optional[Union[int, PipelineVariable]] = None,
        instance_type: Optional[Union[str, PipelineVariable]] = None,
        num_components: Optional[int] = None,
        algorithm_mode: Optional[str] = None,
        subtract_mean: Optional[bool] = None,
        extra_components: Optional[int] = None,
        **kwargs,
    ) -> None: ...
    def create_model(self, vpc_config_override="VPC_CONFIG_DEFAULT", **kwargs): ...

class PCAPredictor(Predictor):
    def __init__(self, endpoint_name, sagemaker_session: Incomplete | None = None, serializer=..., deserializer=...) -> None: ...

class PCAModel(Model):
    def __init__(
        self,
        model_data: Union[str, PipelineVariable],
        role: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        **kwargs,
    ) -> None: ...
