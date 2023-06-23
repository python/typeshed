from _typeshed import Incomplete
from typing import Optional

from sagemaker.amazon.amazon_estimator import AmazonAlgorithmEstimatorBase
from sagemaker.amazon.hyperparameter import Hyperparameter as hp
from sagemaker.model import Model
from sagemaker.predictor import Predictor
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

class LinearLearner(AmazonAlgorithmEstimatorBase):
    repo_name: str
    repo_version: str
    DEFAULT_MINI_BATCH_SIZE: int
    binary_classifier_model_selection_criteria: hp
    target_recall: hp
    target_precision: hp
    positive_example_weight_mult: hp
    epochs: hp
    predictor_type: hp
    use_bias: hp
    num_models: hp
    num_calibration_samples: hp
    init_method: hp
    init_scale: hp
    init_sigma: hp
    init_bias: hp
    optimizer: hp
    loss: hp
    wd: hp
    l1: hp
    momentum: hp
    learning_rate: hp
    beta_1: hp
    beta_2: hp
    bias_lr_mult: hp
    bias_wd_mult: hp
    use_lr_scheduler: hp
    lr_scheduler_step: hp
    lr_scheduler_factor: hp
    lr_scheduler_minimum_lr: hp
    normalize_data: hp
    normalize_label: hp
    unbias_data: hp
    unbias_label: hp
    num_point_for_scaler: hp
    margin: hp
    quantile: hp
    loss_insensitivity: hp
    huber_delta: hp
    early_stopping_patience: hp
    early_stopping_tolerance: hp
    num_classes: hp
    accuracy_top_k: hp
    f_beta: hp
    balance_multiclass_weights: hp
    def __init__(
        self,
        role: Optional[str | PipelineVariable] = None,
        instance_count: Optional[int | PipelineVariable] = None,
        instance_type: Optional[str | PipelineVariable] = None,
        predictor_type: Optional[str] = None,
        binary_classifier_model_selection_criteria: Optional[str] = None,
        target_recall: Optional[float] = None,
        target_precision: Optional[float] = None,
        positive_example_weight_mult: Optional[float] = None,
        epochs: Optional[int] = None,
        use_bias: Optional[bool] = None,
        num_models: Optional[int] = None,
        num_calibration_samples: Optional[int] = None,
        init_method: Optional[str] = None,
        init_scale: Optional[float] = None,
        init_sigma: Optional[float] = None,
        init_bias: Optional[float] = None,
        optimizer: Optional[str] = None,
        loss: Optional[str] = None,
        wd: Optional[float] = None,
        l1: Optional[float] = None,
        momentum: Optional[float] = None,
        learning_rate: Optional[float] = None,
        beta_1: Optional[float] = None,
        beta_2: Optional[float] = None,
        bias_lr_mult: Optional[float] = None,
        bias_wd_mult: Optional[float] = None,
        use_lr_scheduler: Optional[bool] = None,
        lr_scheduler_step: Optional[int] = None,
        lr_scheduler_factor: Optional[float] = None,
        lr_scheduler_minimum_lr: Optional[float] = None,
        normalize_data: Optional[bool] = None,
        normalize_label: Optional[bool] = None,
        unbias_data: Optional[bool] = None,
        unbias_label: Optional[bool] = None,
        num_point_for_scaler: Optional[int] = None,
        margin: Optional[float] = None,
        quantile: Optional[float] = None,
        loss_insensitivity: Optional[float] = None,
        huber_delta: Optional[float] = None,
        early_stopping_patience: Optional[int] = None,
        early_stopping_tolerance: Optional[float] = None,
        num_classes: Optional[int] = None,
        accuracy_top_k: Optional[int] = None,
        f_beta: Optional[float] = None,
        balance_multiclass_weights: Optional[bool] = None,
        **kwargs,
    ) -> None: ...
    def create_model(self, vpc_config_override="VPC_CONFIG_DEFAULT", **kwargs): ...

class LinearLearnerPredictor(Predictor):
    def __init__(self, endpoint_name, sagemaker_session: Incomplete | None = None, serializer=..., deserializer=...) -> None: ...

class LinearLearnerModel(Model):
    def __init__(
        self,
        model_data: str | PipelineVariable,
        role: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        **kwargs,
    ) -> None: ...
