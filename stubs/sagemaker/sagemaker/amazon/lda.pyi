from _typeshed import Incomplete
from typing import Optional, Union

from sagemaker.amazon.amazon_estimator import AmazonAlgorithmEstimatorBase
from sagemaker.amazon.hyperparameter import Hyperparameter as hp
from sagemaker.model import Model
from sagemaker.predictor import Predictor
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

class LDA(AmazonAlgorithmEstimatorBase):
    repo_name: str
    repo_version: str
    num_topics: hp
    alpha0: hp
    max_restarts: hp
    max_iterations: hp
    tol: hp
    def __init__(
        self,
        role: Optional[str | PipelineVariable] = None,
        instance_type: Optional[str | PipelineVariable] = None,
        num_topics: Optional[int] = None,
        alpha0: Optional[float] = None,
        max_restarts: Optional[int] = None,
        max_iterations: Optional[int] = None,
        tol: Optional[float] = None,
        **kwargs,
    ) -> None: ...
    def create_model(self, vpc_config_override="VPC_CONFIG_DEFAULT", **kwargs): ...

class LDAPredictor(Predictor):
    def __init__(self, endpoint_name, sagemaker_session: Incomplete | None = None, serializer=..., deserializer=...) -> None: ...

class LDAModel(Model):
    def __init__(
        self,
        model_data: str | PipelineVariable,
        role: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        **kwargs,
    ) -> None: ...
