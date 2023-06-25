from _typeshed import Incomplete

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
        role: str | PipelineVariable | None = None,
        instance_count: int | PipelineVariable | None = None,
        instance_type: str | PipelineVariable | None = None,
        predictor_type: str | None = None,
        binary_classifier_model_selection_criteria: str | None = None,
        target_recall: float | None = None,
        target_precision: float | None = None,
        positive_example_weight_mult: float | None = None,
        epochs: int | None = None,
        use_bias: bool | None = None,
        num_models: int | None = None,
        num_calibration_samples: int | None = None,
        init_method: str | None = None,
        init_scale: float | None = None,
        init_sigma: float | None = None,
        init_bias: float | None = None,
        optimizer: str | None = None,
        loss: str | None = None,
        wd: float | None = None,
        l1: float | None = None,
        momentum: float | None = None,
        learning_rate: float | None = None,
        beta_1: float | None = None,
        beta_2: float | None = None,
        bias_lr_mult: float | None = None,
        bias_wd_mult: float | None = None,
        use_lr_scheduler: bool | None = None,
        lr_scheduler_step: int | None = None,
        lr_scheduler_factor: float | None = None,
        lr_scheduler_minimum_lr: float | None = None,
        normalize_data: bool | None = None,
        normalize_label: bool | None = None,
        unbias_data: bool | None = None,
        unbias_label: bool | None = None,
        num_point_for_scaler: int | None = None,
        margin: float | None = None,
        quantile: float | None = None,
        loss_insensitivity: float | None = None,
        huber_delta: float | None = None,
        early_stopping_patience: int | None = None,
        early_stopping_tolerance: float | None = None,
        num_classes: int | None = None,
        accuracy_top_k: int | None = None,
        f_beta: float | None = None,
        balance_multiclass_weights: bool | None = None,
        **kwargs,
    ) -> None: ...
    def create_model(self, vpc_config_override="VPC_CONFIG_DEFAULT", **kwargs): ...

class LinearLearnerPredictor(Predictor):
    def __init__(self, endpoint_name, sagemaker_session: Incomplete | None = None, serializer=..., deserializer=...) -> None: ...

class LinearLearnerModel(Model):
    def __init__(
        self, model_data: str | PipelineVariable, role: str | None = None, sagemaker_session: Session | None = None, **kwargs
    ) -> None: ...
