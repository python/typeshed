import abc
from _typeshed import Incomplete
from enum import Enum

from sagemaker.amazon.amazon_estimator import FileSystemRecordSet, RecordSet
from sagemaker.estimator import EstimatorBase
from sagemaker.inputs import FileSystemInput, TrainingInput
from sagemaker.job import _Job
from sagemaker.parameter import ParameterRange
from sagemaker.workflow.entities import PipelineVariable

AMAZON_ESTIMATOR_MODULE: str
AMAZON_ESTIMATOR_CLS_NAMES: Incomplete
HYPERPARAMETER_TUNING_JOB_NAME: str
PARENT_HYPERPARAMETER_TUNING_JOBS: str
WARM_START_TYPE: str
HYPERBAND_STRATEGY_CONFIG: str
HYPERBAND_MIN_RESOURCE: str
HYPERBAND_MAX_RESOURCE: str
GRID_SEARCH: str
MAX_NUMBER_OF_TRAINING_JOBS_NOT_IMPROVING: str
BEST_OBJECTIVE_NOT_IMPROVING: str
CONVERGENCE_DETECTED: str
COMPLETE_ON_CONVERGENCE_DETECTED: str
TARGET_OBJECTIVE_METRIC_VALUE: str
MAX_RUNTIME_IN_SECONDS: str
logger: Incomplete

class WarmStartTypes(Enum):
    IDENTICAL_DATA_AND_ALGORITHM: str
    TRANSFER_LEARNING: str

class WarmStartConfig:
    type: Incomplete
    parents: Incomplete
    def __init__(self, warm_start_type: WarmStartTypes, parents: set[str | PipelineVariable]) -> None: ...
    @classmethod
    def from_job_desc(cls, warm_start_config): ...
    def to_input_req(self): ...

class HyperbandStrategyConfig:
    min_resource: Incomplete
    max_resource: Incomplete
    def __init__(self, max_resource: int, min_resource: int) -> None: ...
    @classmethod
    def from_job_desc(cls, hyperband_strategy_config): ...
    def to_input_req(self): ...

class StrategyConfig:
    hyperband_strategy_config: Incomplete
    def __init__(self, hyperband_strategy_config: HyperbandStrategyConfig) -> None: ...
    @classmethod
    def from_job_desc(cls, strategy_config): ...
    def to_input_req(self): ...

class InstanceConfig:
    instance_count: Incomplete
    instance_type: Incomplete
    volume_size: Incomplete
    def __init__(
        self,
        instance_count: int | PipelineVariable | None = None,
        instance_type: str | PipelineVariable | None = None,
        volume_size: int | PipelineVariable = 30,
    ) -> None: ...
    @classmethod
    def from_job_desc(cls, instance_config): ...
    def to_input_req(self): ...

class TuningJobCompletionCriteriaConfig:
    max_number_of_training_jobs_not_improving: Incomplete
    complete_on_convergence: Incomplete
    target_objective_metric_value: Incomplete
    def __init__(
        self,
        max_number_of_training_jobs_not_improving: int | None = None,
        complete_on_convergence: bool | None = None,
        target_objective_metric_value: float | None = None,
    ) -> None: ...
    @classmethod
    def from_job_desc(cls, completion_criteria_config): ...
    def to_input_req(self): ...

class HyperparameterTuner:
    TUNING_JOB_NAME_MAX_LENGTH: int
    SAGEMAKER_ESTIMATOR_MODULE: str
    SAGEMAKER_ESTIMATOR_CLASS_NAME: str
    DEFAULT_ESTIMATOR_MODULE: str
    DEFAULT_ESTIMATOR_CLS_NAME: str
    estimator: Incomplete
    objective_metric_name: Incomplete
    metric_definitions: Incomplete
    estimator_dict: Incomplete
    objective_metric_name_dict: Incomplete
    metric_definitions_dict: Incomplete
    static_hyperparameters: Incomplete
    auto_parameters: Incomplete
    auto_parameters_dict: Incomplete
    hyperparameters_to_keep_static: Incomplete
    hyperparameters_to_keep_static_dict: Incomplete
    static_hyperparameters_dict: Incomplete
    strategy: Incomplete
    strategy_config: Incomplete
    completion_criteria_config: Incomplete
    objective_type: Incomplete
    max_jobs: Incomplete
    max_parallel_jobs: Incomplete
    max_runtime_in_seconds: Incomplete
    tags: Incomplete
    base_tuning_job_name: Incomplete
    latest_tuning_job: Incomplete
    warm_start_config: Incomplete
    early_stopping_type: Incomplete
    random_seed: Incomplete
    instance_configs_dict: Incomplete
    instance_configs: Incomplete
    autotune: Incomplete
    def __init__(
        self,
        estimator: EstimatorBase,
        objective_metric_name: str | PipelineVariable,
        hyperparameter_ranges: dict[str, ParameterRange],
        metric_definitions: list[dict[str, str | PipelineVariable]] | None = None,
        strategy: str | PipelineVariable = "Bayesian",
        objective_type: str | PipelineVariable = "Maximize",
        max_jobs: int | PipelineVariable | None = None,
        max_parallel_jobs: int | PipelineVariable = 1,
        max_runtime_in_seconds: int | PipelineVariable | None = None,
        tags: list[dict[str, str | PipelineVariable]] | None = None,
        base_tuning_job_name: str | None = None,
        warm_start_config: WarmStartConfig | None = None,
        strategy_config: StrategyConfig | None = None,
        completion_criteria_config: TuningJobCompletionCriteriaConfig | None = None,
        early_stopping_type: str | PipelineVariable = "Off",
        estimator_name: str | None = None,
        random_seed: int | None = None,
        autotune: bool = False,
        hyperparameters_to_keep_static: list[str] | None = None,
    ) -> None: ...
    def override_resource_config(self, instance_configs: list[InstanceConfig, dict[str, list[InstanceConfig]]]): ...
    def fit(
        self,
        inputs: str | dict | list | TrainingInput | FileSystemInput | RecordSet | FileSystemRecordSet | None = None,
        job_name: str | None = None,
        include_cls_metadata: bool | dict[str | bool] = False,
        estimator_kwargs: dict[str, dict] | None = None,
        wait: bool = True,
        **kwargs,
    ): ...
    @classmethod
    def attach(
        cls,
        tuning_job_name,
        sagemaker_session: Incomplete | None = None,
        job_details: Incomplete | None = None,
        estimator_cls: Incomplete | None = None,
    ): ...
    def deploy(
        self,
        initial_instance_count,
        instance_type,
        serializer: Incomplete | None = None,
        deserializer: Incomplete | None = None,
        accelerator_type: Incomplete | None = None,
        endpoint_name: Incomplete | None = None,
        wait: bool = True,
        model_name: Incomplete | None = None,
        kms_key: Incomplete | None = None,
        data_capture_config: Incomplete | None = None,
        **kwargs,
    ): ...
    def stop_tuning_job(self) -> None: ...
    def describe(self): ...
    def wait(self) -> None: ...
    def best_estimator(self, best_training_job: Incomplete | None = None): ...
    def best_training_job(self): ...
    def hyperparameter_ranges(self): ...
    def hyperparameter_ranges_dict(self): ...
    @property
    def sagemaker_session(self): ...
    def analytics(self): ...
    def transfer_learning_tuner(self, additional_parents: Incomplete | None = None, estimator: Incomplete | None = None): ...
    def identical_dataset_and_algorithm_tuner(self, additional_parents: Incomplete | None = None): ...
    @classmethod
    def create(
        cls,
        estimator_dict,
        objective_metric_name_dict,
        hyperparameter_ranges_dict,
        metric_definitions_dict: Incomplete | None = None,
        base_tuning_job_name: Incomplete | None = None,
        strategy: str = "Bayesian",
        strategy_config: Incomplete | None = None,
        completion_criteria_config: Incomplete | None = None,
        objective_type: str = "Maximize",
        max_jobs: Incomplete | None = None,
        max_parallel_jobs: int = 1,
        max_runtime_in_seconds: Incomplete | None = None,
        tags: Incomplete | None = None,
        warm_start_config: Incomplete | None = None,
        early_stopping_type: str = "Off",
        random_seed: Incomplete | None = None,
        autotune: bool = False,
        hyperparameters_to_keep_static_dict: Incomplete | None = None,
    ): ...
    delete_endpoint: Incomplete

class _TuningJob(_Job, metaclass=abc.ABCMeta):
    @classmethod
    def start_new(cls, tuner, inputs): ...
    def stop(self) -> None: ...
    def wait(self) -> None: ...

def create_identical_dataset_and_algorithm_tuner(
    parent, additional_parents: Incomplete | None = None, sagemaker_session: Incomplete | None = None
): ...
def create_transfer_learning_tuner(
    parent,
    additional_parents: Incomplete | None = None,
    estimator: Incomplete | None = None,
    sagemaker_session: Incomplete | None = None,
): ...
