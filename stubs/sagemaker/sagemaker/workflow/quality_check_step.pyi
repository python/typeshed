from _typeshed import Incomplete
from abc import ABC
from typing import List, Optional, Union

from sagemaker.workflow.check_job_config import CheckJobConfig
from sagemaker.workflow.entities import PipelineVariable, RequestType as RequestType
from sagemaker.workflow.step_collections import StepCollection
from sagemaker.workflow.steps import CacheConfig, Step

class QualityCheckConfig(ABC):
    baseline_dataset: Union[str, PipelineVariable]
    dataset_format: dict
    output_s3_uri: Union[str, PipelineVariable]
    post_analytics_processor_script: str
    def __init__(self, baseline_dataset, dataset_format, output_s3_uri, post_analytics_processor_script) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class DataQualityCheckConfig(QualityCheckConfig):
    record_preprocessor_script: str
    def __init__(
        self, baseline_dataset, dataset_format, output_s3_uri, post_analytics_processor_script, record_preprocessor_script
    ) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class ModelQualityCheckConfig(QualityCheckConfig):
    problem_type: Union[str, PipelineVariable]
    inference_attribute: Union[str, PipelineVariable]
    probability_attribute: Union[str, PipelineVariable]
    ground_truth_attribute: Union[str, PipelineVariable]
    probability_threshold_attribute: Union[str, PipelineVariable]
    def __init__(
        self,
        baseline_dataset,
        dataset_format,
        output_s3_uri,
        post_analytics_processor_script,
        problem_type,
        inference_attribute,
        probability_attribute,
        ground_truth_attribute,
        probability_threshold_attribute,
    ) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class QualityCheckStep(Step):
    skip_check: Incomplete
    fail_on_violation: Incomplete
    register_new_baseline: Incomplete
    check_job_config: Incomplete
    quality_check_config: Incomplete
    model_package_group_name: Incomplete
    supplied_baseline_statistics: Incomplete
    supplied_baseline_constraints: Incomplete
    cache_config: Incomplete
    def __init__(
        self,
        name: str,
        quality_check_config: QualityCheckConfig,
        check_job_config: CheckJobConfig,
        skip_check: Union[bool, PipelineVariable] = False,
        fail_on_violation: Union[bool, PipelineVariable] = True,
        register_new_baseline: Union[bool, PipelineVariable] = False,
        model_package_group_name: Union[str, PipelineVariable] = None,
        supplied_baseline_statistics: Union[str, PipelineVariable] = None,
        supplied_baseline_constraints: Union[str, PipelineVariable] = None,
        display_name: str = None,
        description: str = None,
        cache_config: CacheConfig = None,
        depends_on: Optional[List[Union[str, Step, StepCollection]]] = None,
    ) -> None: ...
    @property
    def arguments(self) -> RequestType: ...
    @property
    def properties(self): ...
    def to_request(self) -> RequestType: ...
