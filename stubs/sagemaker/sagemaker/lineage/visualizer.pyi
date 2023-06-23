from typing import Optional

from pandas import DataFrame as DataFrame

class LineageTableVisualizer:
    def __init__(self, sagemaker_session) -> None: ...
    def show(
        self,
        trial_component_name: Optional[str] = None,
        training_job_name: Optional[str] = None,
        processing_job_name: Optional[str] = None,
        pipeline_execution_step: Optional[object] = None,
        model_package_arn: Optional[str] = None,
        endpoint_arn: Optional[str] = None,
        artifact_arn: Optional[str] = None,
        context_arn: Optional[str] = None,
        actions_arn: Optional[str] = None,
    ) -> DataFrame: ...
