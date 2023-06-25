from _typeshed import Incomplete

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
        s3_output_path: str | PipelineVariable | None = None,
        system_monitor_interval_millis: int | PipelineVariable | None = None,
        framework_profile_params: FrameworkProfile | None = None,
        disable_profiler: str | PipelineVariable | None = False,
    ) -> None: ...
