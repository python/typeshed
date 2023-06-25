from _typeshed import Incomplete

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
        role: str | PipelineVariable | None = None,
        instance_count: int | PipelineVariable | None = None,
        instance_type: str | PipelineVariable | None = None,
        num_factors: int | None = None,
        predictor_type: str | None = None,
        epochs: int | None = None,
        clip_gradient: float | None = None,
        eps: float | None = None,
        rescale_grad: float | None = None,
        bias_lr: float | None = None,
        linear_lr: float | None = None,
        factors_lr: float | None = None,
        bias_wd: float | None = None,
        linear_wd: float | None = None,
        factors_wd: float | None = None,
        bias_init_method: str | None = None,
        bias_init_scale: float | None = None,
        bias_init_sigma: float | None = None,
        bias_init_value: float | None = None,
        linear_init_method: str | None = None,
        linear_init_scale: float | None = None,
        linear_init_sigma: float | None = None,
        linear_init_value: float | None = None,
        factors_init_method: str | None = None,
        factors_init_scale: float | None = None,
        factors_init_sigma: float | None = None,
        factors_init_value: float | None = None,
        **kwargs,
    ) -> None: ...
    def create_model(self, vpc_config_override="VPC_CONFIG_DEFAULT", **kwargs): ...

class FactorizationMachinesPredictor(Predictor):
    def __init__(self, endpoint_name, sagemaker_session: Incomplete | None = None, serializer=..., deserializer=...) -> None: ...

class FactorizationMachinesModel(Model):
    def __init__(
        self, model_data: str | PipelineVariable, role: str | None = None, sagemaker_session: Session | None = None, **kwargs
    ) -> None: ...
