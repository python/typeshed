from _typeshed import Incomplete

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
        role: str | PipelineVariable | None = None,
        instance_type: str | PipelineVariable | None = None,
        num_topics: int | None = None,
        alpha0: float | None = None,
        max_restarts: int | None = None,
        max_iterations: int | None = None,
        tol: float | None = None,
        **kwargs,
    ) -> None: ...
    def create_model(self, vpc_config_override="VPC_CONFIG_DEFAULT", **kwargs): ...

class LDAPredictor(Predictor):
    def __init__(self, endpoint_name, sagemaker_session: Incomplete | None = None, serializer=..., deserializer=...) -> None: ...

class LDAModel(Model):
    def __init__(
        self, model_data: str | PipelineVariable, role: str | None = None, sagemaker_session: Session | None = None, **kwargs
    ) -> None: ...
