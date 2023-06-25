from pandas import DataFrame as DataFrame

class LineageTableVisualizer:
    def __init__(self, sagemaker_session) -> None: ...
    def show(
        self,
        trial_component_name: str | None = None,
        training_job_name: str | None = None,
        processing_job_name: str | None = None,
        pipeline_execution_step: object | None = None,
        model_package_arn: str | None = None,
        endpoint_arn: str | None = None,
        artifact_arn: str | None = None,
        context_arn: str | None = None,
        actions_arn: str | None = None,
    ) -> DataFrame: ...
