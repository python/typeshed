from _typeshed import Incomplete
from typing import List, Optional

from sagemaker.amazon.amazon_estimator import AmazonAlgorithmEstimatorBase
from sagemaker.amazon.hyperparameter import Hyperparameter as hp
from sagemaker.model import Model
from sagemaker.predictor import Predictor
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

class KMeans(AmazonAlgorithmEstimatorBase):
    repo_name: str
    repo_version: str
    k: hp
    init_method: hp
    max_iterations: hp
    tol: hp
    num_trials: hp
    local_init_method: hp
    half_life_time_size: hp
    epochs: hp
    center_factor: hp
    eval_metrics: hp
    def __init__(
        self,
        role: str | PipelineVariable | None = None,
        instance_count: int | PipelineVariable | None = None,
        instance_type: str | PipelineVariable | None = None,
        k: int | None = None,
        init_method: str | None = None,
        max_iterations: int | None = None,
        tol: float | None = None,
        num_trials: int | None = None,
        local_init_method: str | None = None,
        half_life_time_size: int | None = None,
        epochs: int | None = None,
        center_factor: int | None = None,
        eval_metrics: list[str | PipelineVariable] | None = None,
        **kwargs,
    ) -> None: ...
    def create_model(self, vpc_config_override="VPC_CONFIG_DEFAULT", **kwargs): ...
    def hyperparameters(self): ...

class KMeansPredictor(Predictor):
    def __init__(self, endpoint_name, sagemaker_session: Incomplete | None = None, serializer=..., deserializer=...) -> None: ...

class KMeansModel(Model):
    def __init__(
        self,
        model_data: str | PipelineVariable,
        role: str | None = None,
        sagemaker_session: Session | None = None,
        **kwargs,
    ) -> None: ...
