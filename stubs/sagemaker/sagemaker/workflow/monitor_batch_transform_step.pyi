from _typeshed import Incomplete
from typing import Optional, Union

from sagemaker.workflow.check_job_config import CheckJobConfig
from sagemaker.workflow.clarify_check_step import ClarifyCheckConfig
from sagemaker.workflow.entities import PipelineVariable
from sagemaker.workflow.pipeline_context import _JobStepArguments
from sagemaker.workflow.quality_check_step import QualityCheckConfig
from sagemaker.workflow.step_collections import StepCollection

class MonitorBatchTransformStep(StepCollection):
    name: Incomplete
    steps: Incomplete
    def __init__(
        self,
        name: str,
        transform_step_args: _JobStepArguments,
        monitor_configuration: QualityCheckConfig | ClarifyCheckConfig,
        check_job_configuration: CheckJobConfig,
        monitor_before_transform: bool = False,
        fail_on_violation: bool | PipelineVariable = True,
        supplied_baseline_statistics: str | PipelineVariable = None,
        supplied_baseline_constraints: str | PipelineVariable = None,
        display_name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> None: ...
