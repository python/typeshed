from _typeshed import Incomplete
from abc import ABC
from typing import List, Optional

from sagemaker.clarify import BiasConfig, DataConfig, ModelConfig, ModelPredictedLabelConfig, SHAPConfig
from sagemaker.workflow.check_job_config import CheckJobConfig
from sagemaker.workflow.entities import PipelineVariable, RequestType as RequestType
from sagemaker.workflow.step_collections import StepCollection
from sagemaker.workflow.steps import CacheConfig, Step

class ClarifyCheckConfig(ABC):
    data_config: DataConfig
    kms_key: str
    monitoring_analysis_config_uri: str
    def __init__(self, data_config, kms_key, monitoring_analysis_config_uri) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class DataBiasCheckConfig(ClarifyCheckConfig):
    data_bias_config: BiasConfig
    methods: str | list[str]
    def __init__(self, data_config, kms_key, monitoring_analysis_config_uri, data_bias_config, methods) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class ModelBiasCheckConfig(ClarifyCheckConfig):
    data_bias_config: BiasConfig
    model_config: ModelConfig
    model_predicted_label_config: ModelPredictedLabelConfig
    methods: str | list[str]
    def __init__(
        self,
        data_config,
        kms_key,
        monitoring_analysis_config_uri,
        data_bias_config,
        model_config,
        model_predicted_label_config,
        methods,
    ) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class ModelExplainabilityCheckConfig(ClarifyCheckConfig):
    model_config: ModelConfig
    explainability_config: SHAPConfig
    model_scores: str | int | ModelPredictedLabelConfig
    def __init__(
        self, data_config, kms_key, monitoring_analysis_config_uri, model_config, explainability_config, model_scores
    ) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class ClarifyCheckStep(Step):
    skip_check: Incomplete
    fail_on_violation: Incomplete
    register_new_baseline: Incomplete
    clarify_check_config: Incomplete
    check_job_config: Incomplete
    model_package_group_name: Incomplete
    supplied_baseline_constraints: Incomplete
    cache_config: Incomplete
    def __init__(
        self,
        name: str,
        clarify_check_config: ClarifyCheckConfig,
        check_job_config: CheckJobConfig,
        skip_check: bool | PipelineVariable = False,
        fail_on_violation: bool | PipelineVariable = True,
        register_new_baseline: bool | PipelineVariable = False,
        model_package_group_name: str | PipelineVariable | None = None,
        supplied_baseline_constraints: str | PipelineVariable | None = None,
        display_name: str | None = None,
        description: str | None = None,
        cache_config: CacheConfig | None = None,
        depends_on: list[str | Step | StepCollection] | None = None,
    ) -> None: ...
    @property
    def arguments(self) -> RequestType: ...
    @property
    def properties(self): ...
    def to_request(self) -> RequestType: ...
