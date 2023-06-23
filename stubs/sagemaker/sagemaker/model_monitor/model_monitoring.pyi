from _typeshed import Incomplete
from typing import Optional, Union

from sagemaker.model_monitor.dataset_format import MonitoringDatasetFormat
from sagemaker.processing import ProcessingJob

DEFAULT_REPOSITORY_NAME: str
STATISTICS_JSON_DEFAULT_FILE_NAME: str
CONSTRAINTS_JSON_DEFAULT_FILE_NAME: str
CONSTRAINT_VIOLATIONS_JSON_DEFAULT_FILE_NAME: str
framework_name: str

class ModelMonitor:
    image_uri: Incomplete
    instance_count: Incomplete
    instance_type: Incomplete
    entrypoint: Incomplete
    volume_size_in_gb: Incomplete
    max_runtime_in_seconds: Incomplete
    base_job_name: Incomplete
    sagemaker_session: Incomplete
    tags: Incomplete
    baselining_jobs: Incomplete
    latest_baselining_job: Incomplete
    arguments: Incomplete
    latest_baselining_job_name: Incomplete
    monitoring_schedule_name: Incomplete
    job_definition_name: Incomplete
    role: Incomplete
    volume_kms_key: Incomplete
    output_kms_key: Incomplete
    network_config: Incomplete
    env: Incomplete
    def __init__(
        self,
        role: Incomplete | None = None,
        image_uri: Incomplete | None = None,
        instance_count: int = 1,
        instance_type: str = "ml.m5.xlarge",
        entrypoint: Incomplete | None = None,
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
    def run_baseline(
        self,
        baseline_inputs,
        output,
        arguments: Incomplete | None = None,
        wait: bool = True,
        logs: bool = True,
        job_name: Incomplete | None = None,
    ) -> None: ...
    def create_monitoring_schedule(
        self,
        endpoint_input: Incomplete | None = None,
        output: Incomplete | None = None,
        statistics: Incomplete | None = None,
        constraints: Incomplete | None = None,
        monitor_schedule_name: Incomplete | None = None,
        schedule_cron_expression: Incomplete | None = None,
        batch_transform_input: Incomplete | None = None,
        arguments: Incomplete | None = None,
    ) -> None: ...
    def update_monitoring_schedule(
        self,
        endpoint_input: Incomplete | None = None,
        output: Incomplete | None = None,
        statistics: Incomplete | None = None,
        constraints: Incomplete | None = None,
        schedule_cron_expression: Incomplete | None = None,
        instance_count: Incomplete | None = None,
        instance_type: Incomplete | None = None,
        entrypoint: Incomplete | None = None,
        volume_size_in_gb: Incomplete | None = None,
        volume_kms_key: Incomplete | None = None,
        output_kms_key: Incomplete | None = None,
        arguments: Incomplete | None = None,
        max_runtime_in_seconds: Incomplete | None = None,
        env: Incomplete | None = None,
        network_config: Incomplete | None = None,
        role: Incomplete | None = None,
        image_uri: Incomplete | None = None,
        batch_transform_input: Incomplete | None = None,
    ) -> None: ...
    def start_monitoring_schedule(self) -> None: ...
    def stop_monitoring_schedule(self) -> None: ...
    def delete_monitoring_schedule(self) -> None: ...
    def baseline_statistics(self, file_name="statistics.json"): ...
    def suggested_constraints(self, file_name="constraints.json"): ...
    def latest_monitoring_statistics(self, file_name="statistics.json"): ...
    def latest_monitoring_constraint_violations(self, file_name="constraint_violations.json"): ...
    def describe_latest_baselining_job(self): ...
    def describe_schedule(self): ...
    def list_executions(self): ...
    def update_monitoring_alert(
        self, monitoring_alert_name: str, data_points_to_alert: Optional[int], evaluation_period: Optional[int]
    ): ...
    def list_monitoring_alerts(self, next_token: Optional[str] = None, max_results: Optional[int] = 10): ...
    def list_monitoring_alert_history(
        self,
        monitoring_alert_name: Optional[str] = None,
        sort_by: Optional[str] = "CreationTime",
        sort_order: Optional[str] = "Descending",
        next_token: Optional[str] = None,
        max_results: Optional[int] = 10,
        creation_time_before: Optional[str] = None,
        creation_time_after: Optional[str] = None,
        status_equals: Optional[str] = None,
    ): ...
    @classmethod
    def attach(cls, monitor_schedule_name, sagemaker_session: Incomplete | None = None): ...
    @classmethod
    def monitoring_type(cls) -> None: ...

class DefaultModelMonitor(ModelMonitor):
    JOB_DEFINITION_BASE_NAME: str
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
    @classmethod
    def monitoring_type(cls): ...
    latest_baselining_job_name: Incomplete
    latest_baselining_job: Incomplete
    def suggest_baseline(
        self,
        baseline_dataset,
        dataset_format,
        record_preprocessor_script: Incomplete | None = None,
        post_analytics_processor_script: Incomplete | None = None,
        output_s3_uri: Incomplete | None = None,
        wait: bool = True,
        logs: bool = True,
        job_name: Incomplete | None = None,
        monitoring_config_override: Incomplete | None = None,
    ): ...
    job_definition_name: Incomplete
    monitoring_schedule_name: Incomplete
    def create_monitoring_schedule(
        self,
        endpoint_input: Incomplete | None = None,
        record_preprocessor_script: Incomplete | None = None,
        post_analytics_processor_script: Incomplete | None = None,
        output_s3_uri: Incomplete | None = None,
        constraints: Incomplete | None = None,
        statistics: Incomplete | None = None,
        monitor_schedule_name: Incomplete | None = None,
        schedule_cron_expression: Incomplete | None = None,
        enable_cloudwatch_metrics: bool = True,
        batch_transform_input: Incomplete | None = None,
    ) -> None: ...
    env: Incomplete
    instance_type: Incomplete
    instance_count: Incomplete
    volume_size_in_gb: Incomplete
    volume_kms_key: Incomplete
    output_kms_key: Incomplete
    max_runtime_in_seconds: Incomplete
    network_config: Incomplete
    role: Incomplete
    def update_monitoring_schedule(
        self,
        endpoint_input: Incomplete | None = None,
        record_preprocessor_script: Incomplete | None = None,
        post_analytics_processor_script: Incomplete | None = None,
        output_s3_uri: Incomplete | None = None,
        statistics: Incomplete | None = None,
        constraints: Incomplete | None = None,
        schedule_cron_expression: Incomplete | None = None,
        instance_count: Incomplete | None = None,
        instance_type: Incomplete | None = None,
        volume_size_in_gb: Incomplete | None = None,
        volume_kms_key: Incomplete | None = None,
        output_kms_key: Incomplete | None = None,
        max_runtime_in_seconds: Incomplete | None = None,
        env: Incomplete | None = None,
        network_config: Incomplete | None = None,
        enable_cloudwatch_metrics: Incomplete | None = None,
        role: Incomplete | None = None,
        batch_transform_input: Incomplete | None = None,
    ) -> None: ...
    def delete_monitoring_schedule(self) -> None: ...
    def run_baseline(self) -> None: ...
    @classmethod
    def attach(cls, monitor_schedule_name, sagemaker_session: Incomplete | None = None): ...
    def latest_monitoring_statistics(self): ...
    def latest_monitoring_constraint_violations(self): ...

class ModelQualityMonitor(ModelMonitor):
    JOB_DEFINITION_BASE_NAME: str
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
    @classmethod
    def monitoring_type(cls): ...
    latest_baselining_job_name: Incomplete
    latest_baselining_job: Incomplete
    def suggest_baseline(
        self,
        baseline_dataset,
        dataset_format,
        problem_type,
        inference_attribute: Incomplete | None = None,
        probability_attribute: Incomplete | None = None,
        ground_truth_attribute: Incomplete | None = None,
        probability_threshold_attribute: Incomplete | None = None,
        post_analytics_processor_script: Incomplete | None = None,
        output_s3_uri: Incomplete | None = None,
        wait: bool = False,
        logs: bool = False,
        job_name: Incomplete | None = None,
    ): ...
    job_definition_name: Incomplete
    monitoring_schedule_name: Incomplete
    def create_monitoring_schedule(
        self,
        endpoint_input: Incomplete | None = None,
        ground_truth_input: Incomplete | None = None,
        problem_type: Incomplete | None = None,
        record_preprocessor_script: Incomplete | None = None,
        post_analytics_processor_script: Incomplete | None = None,
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
        problem_type: Incomplete | None = None,
        record_preprocessor_script: Incomplete | None = None,
        post_analytics_processor_script: Incomplete | None = None,
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

class BaseliningJob(ProcessingJob):
    inputs: Incomplete
    outputs: Incomplete
    def __init__(self, sagemaker_session, job_name, inputs, outputs, output_kms_key: Incomplete | None = None) -> None: ...
    @classmethod
    def from_processing_job(cls, processing_job): ...
    def baseline_statistics(self, file_name="statistics.json", kms_key: Incomplete | None = None): ...
    def suggested_constraints(self, file_name="constraints.json", kms_key: Incomplete | None = None): ...

class MonitoringExecution(ProcessingJob):
    output: Incomplete
    def __init__(self, sagemaker_session, job_name, inputs, output, output_kms_key: Incomplete | None = None) -> None: ...
    @classmethod
    def from_processing_arn(cls, sagemaker_session, processing_job_arn): ...
    def statistics(self, file_name="statistics.json", kms_key: Incomplete | None = None): ...
    def constraint_violations(self, file_name="constraint_violations.json", kms_key: Incomplete | None = None): ...

class EndpointInput:
    endpoint_name: Incomplete
    destination: Incomplete
    s3_input_mode: Incomplete
    s3_data_distribution_type: Incomplete
    start_time_offset: Incomplete
    end_time_offset: Incomplete
    features_attribute: Incomplete
    inference_attribute: Incomplete
    probability_attribute: Incomplete
    probability_threshold_attribute: Incomplete
    def __init__(
        self,
        endpoint_name,
        destination,
        s3_input_mode: str = "File",
        s3_data_distribution_type: str = "FullyReplicated",
        start_time_offset: Incomplete | None = None,
        end_time_offset: Incomplete | None = None,
        features_attribute: Incomplete | None = None,
        inference_attribute: Incomplete | None = None,
        probability_attribute: Incomplete | None = None,
        probability_threshold_attribute: Incomplete | None = None,
    ) -> None: ...

class MonitoringInput:
    start_time_offset: str
    end_time_offset: str
    features_attribute: str
    inference_attribute: str
    probability_attribute: str | int
    probability_threshold_attribute: float
    def __init__(
        self,
        start_time_offset,
        end_time_offset,
        features_attribute,
        inference_attribute,
        probability_attribute,
        probability_threshold_attribute,
    ) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class BatchTransformInput(MonitoringInput):
    data_captured_destination_s3_uri: Incomplete
    destination: Incomplete
    s3_input_mode: Incomplete
    s3_data_distribution_type: Incomplete
    dataset_format: Incomplete
    def __init__(
        self,
        data_captured_destination_s3_uri: str,
        destination: str,
        dataset_format: MonitoringDatasetFormat,
        s3_input_mode: str = "File",
        s3_data_distribution_type: str = "FullyReplicated",
        start_time_offset: str = None,
        end_time_offset: str = None,
        features_attribute: str = None,
        inference_attribute: str = None,
        probability_attribute: str = None,
        probability_threshold_attribute: str = None,
    ) -> None: ...

class MonitoringOutput:
    source: Incomplete
    destination: Incomplete
    s3_upload_mode: Incomplete
    def __init__(self, source, destination: Incomplete | None = None, s3_upload_mode: str = "Continuous") -> None: ...
