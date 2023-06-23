from _typeshed import Incomplete
from typing import List, Optional, Union

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
        role: Optional[Union[str, PipelineVariable]] = None,
        instance_count: Optional[Union[int, PipelineVariable]] = None,
        instance_type: Optional[Union[str, PipelineVariable]] = None,
        k: Optional[int] = None,
        init_method: Optional[str] = None,
        max_iterations: Optional[int] = None,
        tol: Optional[float] = None,
        num_trials: Optional[int] = None,
        local_init_method: Optional[str] = None,
        half_life_time_size: Optional[int] = None,
        epochs: Optional[int] = None,
        center_factor: Optional[int] = None,
        eval_metrics: Optional[List[Union[str, PipelineVariable]]] = None,
        **kwargs,
    ) -> None: ...
    def create_model(self, vpc_config_override="VPC_CONFIG_DEFAULT", **kwargs): ...
    def hyperparameters(self): ...

class KMeansPredictor(Predictor):
    def __init__(self, endpoint_name, sagemaker_session: Incomplete | None = None, serializer=..., deserializer=...) -> None: ...

class KMeansModel(Model):
    def __init__(
        self,
        model_data: Union[str, PipelineVariable],
        role: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        **kwargs,
    ) -> None: ...
