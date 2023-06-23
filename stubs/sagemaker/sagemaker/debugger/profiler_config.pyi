from _typeshed import Incomplete
from typing import Optional, Union

from sagemaker.debugger.framework_profile import FrameworkProfile
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

class ProfilerConfig:
    s3_output_path: Incomplete
    system_monitor_interval_millis: Incomplete
    framework_profile_params: Incomplete
    disable_profiler: Incomplete
    def __init__(
        self,
        s3_output_path: Optional[str | PipelineVariable] = None,
        system_monitor_interval_millis: Optional[int | PipelineVariable] = None,
        framework_profile_params: Optional[FrameworkProfile] = None,
        disable_profiler: Optional[str | PipelineVariable] = False,
    ) -> None: ...
