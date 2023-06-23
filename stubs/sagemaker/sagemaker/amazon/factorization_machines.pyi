from _typeshed import Incomplete
from typing import Optional, Union

from sagemaker.amazon.amazon_estimator import AmazonAlgorithmEstimatorBase
from sagemaker.amazon.hyperparameter import Hyperparameter as hp
from sagemaker.model import Model
from sagemaker.predictor import Predictor
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

class FactorizationMachines(AmazonAlgorithmEstimatorBase):
    repo_name: str
    repo_version: str
    num_factors: hp
    predictor_type: hp
    epochs: hp
    clip_gradient: hp
    eps: hp
    rescale_grad: hp
    bias_lr: hp
    linear_lr: hp
    factors_lr: hp
    bias_wd: hp
    linear_wd: hp
    factors_wd: hp
    bias_init_method: hp
    bias_init_scale: hp
    bias_init_sigma: hp
    bias_init_value: hp
    linear_init_method: hp
    linear_init_scale: hp
    linear_init_sigma: hp
    linear_init_value: hp
    factors_init_method: hp
    factors_init_scale: hp
    factors_init_sigma: hp
    factors_init_value: hp
    def __init__(
        self,
        role: Optional[Union[str, PipelineVariable]] = None,
        instance_count: Optional[Union[int, PipelineVariable]] = None,
        instance_type: Optional[Union[str, PipelineVariable]] = None,
        num_factors: Optional[int] = None,
        predictor_type: Optional[str] = None,
        epochs: Optional[int] = None,
        clip_gradient: Optional[float] = None,
        eps: Optional[float] = None,
        rescale_grad: Optional[float] = None,
        bias_lr: Optional[float] = None,
        linear_lr: Optional[float] = None,
        factors_lr: Optional[float] = None,
        bias_wd: Optional[float] = None,
        linear_wd: Optional[float] = None,
        factors_wd: Optional[float] = None,
        bias_init_method: Optional[str] = None,
        bias_init_scale: Optional[float] = None,
        bias_init_sigma: Optional[float] = None,
        bias_init_value: Optional[float] = None,
        linear_init_method: Optional[str] = None,
        linear_init_scale: Optional[float] = None,
        linear_init_sigma: Optional[float] = None,
        linear_init_value: Optional[float] = None,
        factors_init_method: Optional[str] = None,
        factors_init_scale: Optional[float] = None,
        factors_init_sigma: Optional[float] = None,
        factors_init_value: Optional[float] = None,
        **kwargs,
    ) -> None: ...
    def create_model(self, vpc_config_override="VPC_CONFIG_DEFAULT", **kwargs): ...

class FactorizationMachinesPredictor(Predictor):
    def __init__(self, endpoint_name, sagemaker_session: Incomplete | None = None, serializer=..., deserializer=...) -> None: ...

class FactorizationMachinesModel(Model):
    def __init__(
        self,
        model_data: Union[str, PipelineVariable],
        role: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        **kwargs,
    ) -> None: ...
