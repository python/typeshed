from _typeshed import Incomplete

from sagemaker.model_monitor import model_monitoring as mm

class ClarifyModelMonitor(mm.ModelMonitor):
    latest_baselining_job_config: Incomplete
    def __init__(
        self,
        role: Incomplete | None = None,
        instance_count: int = 1,
        instance_type: str = "ml.m5.xlarge",
        volume_size_in_gb: int = 30,
        volume_kms_key: Incomplete | None = None,
        output_kms_key: Incomplete | None = None,
        max_runtime_in_seconds: Incomplete | None = None,
        base_job_name: Incomplete | None = None,
        sagemaker_session: Incomplete | None = None,
        env: Incomplete | None = None,
        tags: Incomplete | None = None,
        network_config: Incomplete | None = None,
    ) -> None: ...
    def run_baseline(self, **_) -> None: ...
    def latest_monitoring_statistics(self, **_) -> None: ...
    def list_executions(self): ...

class ModelBiasMonitor(ClarifyModelMonitor):
    JOB_DEFINITION_BASE_NAME: str
    @classmethod
    def monitoring_type(cls): ...
    latest_baselining_job_config: Incomplete
    latest_baselining_job_name: Incomplete
    latest_baselining_job: Incomplete
    def suggest_baseline(
        self,
        data_config,
        bias_config,
        model_config,
        model_predicted_label_config: Incomplete | None = None,
        wait: bool = False,
        logs: bool = False,
        job_name: Incomplete | None = None,
        kms_key: Incomplete | None = None,
    ): ...
    job_definition_name: Incomplete
    monitoring_schedule_name: Incomplete
    def create_monitoring_schedule(
        self,
        endpoint_input: Incomplete | None = None,
        ground_truth_input: Incomplete | None = None,
        analysis_config: Incomplete | None = None,
        output_s3_uri: Incomplete | None = None,
        constraints: Incomplete | None = None,
        monitor_schedule_name: Incomplete | None = None,
        schedule_cron_expression: Incomplete | None = None,
        enable_cloudwatch_metrics: bool = True,
        batch_transform_input: Incomplete | None = None,
    ) -> None: ...
    role: Incomplete
    instance_count: Incomplete
    instance_type: Incomplete
    volume_size_in_gb: Incomplete
    volume_kms_key: Incomplete
    output_kms_key: Incomplete
    max_runtime_in_seconds: Incomplete
    env: Incomplete
    network_config: Incomplete
    def update_monitoring_schedule(
        self,
        endpoint_input: Incomplete | None = None,
        ground_truth_input: Incomplete | None = None,
        analysis_config: Incomplete | None = None,
        output_s3_uri: Incomplete | None = None,
        constraints: Incomplete | None = None,
        schedule_cron_expression: Incomplete | None = None,
        enable_cloudwatch_metrics: Incomplete | None = None,
        role: Incomplete | None = None,
        instance_count: Incomplete | None = None,
        instance_type: Incomplete | None = None,
        volume_size_in_gb: Incomplete | None = None,
        volume_kms_key: Incomplete | None = None,
        output_kms_key: Incomplete | None = None,
        max_runtime_in_seconds: Incomplete | None = None,
        env: Incomplete | None = None,
        network_config: Incomplete | None = None,
        batch_transform_input: Incomplete | None = None,
    ) -> None: ...
    def delete_monitoring_schedule(self) -> None: ...
    @classmethod
    def attach(cls, monitor_schedule_name, sagemaker_session: Incomplete | None = None): ...

class BiasAnalysisConfig:
    analysis_config: Incomplete
    def __init__(self, bias_config, headers: Incomplete | None = None, label: Incomplete | None = None) -> None: ...

class ModelExplainabilityMonitor(ClarifyModelMonitor):
    JOB_DEFINITION_BASE_NAME: str
    @classmethod
    def monitoring_type(cls): ...
    latest_baselining_job_config: Incomplete
    latest_baselining_job_name: Incomplete
    latest_baselining_job: Incomplete
    def suggest_baseline(
        self,
        data_config,
        explainability_config,
        model_config,
        model_scores: Incomplete | None = None,
        wait: bool = False,
        logs: bool = False,
        job_name: Incomplete | None = None,
        kms_key: Incomplete | None = None,
    ): ...
    job_definition_name: Incomplete
    monitoring_schedule_name: Incomplete
    def create_monitoring_schedule(
        self,
        endpoint_input: Incomplete | None = None,
        analysis_config: Incomplete | None = None,
        output_s3_uri: Incomplete | None = None,
        constraints: Incomplete | None = None,
        monitor_schedule_name: Incomplete | None = None,
        schedule_cron_expression: Incomplete | None = None,
        enable_cloudwatch_metrics: bool = True,
        batch_transform_input: Incomplete | None = None,
    ) -> None: ...
    role: Incomplete
    instance_count: Incomplete
    instance_type: Incomplete
    volume_size_in_gb: Incomplete
    volume_kms_key: Incomplete
    output_kms_key: Incomplete
    max_runtime_in_seconds: Incomplete
    env: Incomplete
    network_config: Incomplete
    def update_monitoring_schedule(
        self,
        endpoint_input: Incomplete | None = None,
        analysis_config: Incomplete | None = None,
        output_s3_uri: Incomplete | None = None,
        constraints: Incomplete | None = None,
        schedule_cron_expression: Incomplete | None = None,
        enable_cloudwatch_metrics: Incomplete | None = None,
        role: Incomplete | None = None,
        instance_count: Incomplete | None = None,
        instance_type: Incomplete | None = None,
        volume_size_in_gb: Incomplete | None = None,
        volume_kms_key: Incomplete | None = None,
        output_kms_key: Incomplete | None = None,
        max_runtime_in_seconds: Incomplete | None = None,
        env: Incomplete | None = None,
        network_config: Incomplete | None = None,
        batch_transform_input: Incomplete | None = None,
    ) -> None: ...
    def delete_monitoring_schedule(self) -> None: ...
    @classmethod
    def attach(cls, monitor_schedule_name, sagemaker_session: Incomplete | None = None): ...

class ExplainabilityAnalysisConfig:
    analysis_config: Incomplete
    def __init__(
        self, explainability_config, model_config, headers: Incomplete | None = None, label_headers: Incomplete | None = None
    ) -> None: ...

class ClarifyBaseliningConfig:
    analysis_config: Incomplete
    features_attribute: Incomplete
    inference_attribute: Incomplete
    probability_attribute: Incomplete
    probability_threshold_attribute: Incomplete
    def __init__(
        self,
        analysis_config,
        features_attribute: Incomplete | None = None,
        inference_attribute: Incomplete | None = None,
        probability_attribute: Incomplete | None = None,
        probability_threshold_attribute: Incomplete | None = None,
    ) -> None: ...

class ClarifyBaseliningJob(mm.BaseliningJob):
    def __init__(self, processing_job) -> None: ...
    def baseline_statistics(self, **_) -> None: ...
    def suggested_constraints(self, file_name: Incomplete | None = None, kms_key: Incomplete | None = None): ...

class ClarifyMonitoringExecution(mm.MonitoringExecution):
    def __init__(self, sagemaker_session, job_name, inputs, output, output_kms_key: Incomplete | None = None) -> None: ...
    def statistics(self, **_) -> None: ...
