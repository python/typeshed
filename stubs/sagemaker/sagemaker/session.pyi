from _typeshed import Incomplete
from typing import Any, Dict, List, Optional, Sequence

from sagemaker.inputs import BatchDataCaptureConfig

LOGGER: Incomplete
NOTEBOOK_METADATA_FILE: str

class LogState:
    STARTING: int
    WAIT_IN_PROGRESS: int
    TAILING: int
    JOB_COMPLETE: int
    COMPLETE: int

class Session:
    default_bucket_prefix: Incomplete
    s3_resource: Incomplete
    s3_client: Incomplete
    resource_groups_client: Incomplete
    resource_group_tagging_client: Incomplete
    config: Incomplete
    lambda_client: Incomplete
    settings: Incomplete
    def __init__(
        self,
        boto_session: Incomplete | None = None,
        sagemaker_client: Incomplete | None = None,
        sagemaker_runtime_client: Incomplete | None = None,
        sagemaker_featurestore_runtime_client: Incomplete | None = None,
        default_bucket: Incomplete | None = None,
        settings=...,
        sagemaker_metrics_client: Incomplete | None = None,
        sagemaker_config: dict = None,
        default_bucket_prefix: str = None,
    ) -> None: ...
    @property
    def boto_region_name(self): ...
    def upload_data(
        self, path, bucket: Incomplete | None = None, key_prefix: str = "data", extra_args: Incomplete | None = None
    ): ...
    def upload_string_as_file_body(self, body, bucket, key, kms_key: Incomplete | None = None): ...
    def download_data(self, path, bucket, key_prefix: str = "", extra_args: Incomplete | None = None): ...
    def read_s3_file(self, bucket, key_prefix): ...
    def list_s3_files(self, bucket, key_prefix): ...
    def default_bucket(self): ...
    def train(
        self,
        input_mode,
        input_config,
        role: Incomplete | None = None,
        job_name: Incomplete | None = None,
        output_config: Incomplete | None = None,
        resource_config: Incomplete | None = None,
        vpc_config: Incomplete | None = None,
        hyperparameters: Incomplete | None = None,
        stop_condition: Incomplete | None = None,
        tags: Incomplete | None = None,
        metric_definitions: Incomplete | None = None,
        enable_network_isolation: Incomplete | None = None,
        image_uri: Incomplete | None = None,
        training_image_config: Incomplete | None = None,
        container_entry_point: Incomplete | None = None,
        container_arguments: Incomplete | None = None,
        algorithm_arn: Incomplete | None = None,
        encrypt_inter_container_traffic: Incomplete | None = None,
        use_spot_instances: bool = False,
        checkpoint_s3_uri: Incomplete | None = None,
        checkpoint_local_path: Incomplete | None = None,
        experiment_config: Incomplete | None = None,
        debugger_rule_configs: Incomplete | None = None,
        debugger_hook_config: Incomplete | None = None,
        tensorboard_output_config: Incomplete | None = None,
        enable_sagemaker_metrics: Incomplete | None = None,
        profiler_rule_configs: Incomplete | None = None,
        profiler_config: Incomplete | None = None,
        environment: Optional[Dict[str, str]] = None,
        retry_strategy: Incomplete | None = None,
    ): ...
    def update_training_job(
        self,
        job_name,
        profiler_rule_configs: Incomplete | None = None,
        profiler_config: Incomplete | None = None,
        resource_config: Incomplete | None = None,
    ) -> None: ...
    def process(
        self,
        inputs,
        output_config,
        job_name,
        resources,
        stopping_condition,
        app_specification,
        environment: Optional[Dict[str, str]] = None,
        network_config: Incomplete | None = None,
        role_arn: Incomplete | None = None,
        tags: Incomplete | None = None,
        experiment_config: Incomplete | None = None,
    ): ...
    def create_monitoring_schedule(
        self,
        monitoring_schedule_name,
        schedule_expression,
        statistics_s3_uri,
        constraints_s3_uri,
        monitoring_inputs,
        monitoring_output_config,
        instance_count,
        instance_type,
        volume_size_in_gb,
        volume_kms_key: Incomplete | None = None,
        image_uri: Incomplete | None = None,
        entrypoint: Incomplete | None = None,
        arguments: Incomplete | None = None,
        record_preprocessor_source_uri: Incomplete | None = None,
        post_analytics_processor_source_uri: Incomplete | None = None,
        max_runtime_in_seconds: Incomplete | None = None,
        environment: Incomplete | None = None,
        network_config: Incomplete | None = None,
        role_arn: Incomplete | None = None,
        tags: Incomplete | None = None,
    ) -> None: ...
    def update_monitoring_schedule(
        self,
        monitoring_schedule_name,
        schedule_expression: Incomplete | None = None,
        statistics_s3_uri: Incomplete | None = None,
        constraints_s3_uri: Incomplete | None = None,
        monitoring_inputs: Incomplete | None = None,
        monitoring_output_config: Incomplete | None = None,
        instance_count: Incomplete | None = None,
        instance_type: Incomplete | None = None,
        volume_size_in_gb: Incomplete | None = None,
        volume_kms_key: Incomplete | None = None,
        image_uri: Incomplete | None = None,
        entrypoint: Incomplete | None = None,
        arguments: Incomplete | None = None,
        record_preprocessor_source_uri: Incomplete | None = None,
        post_analytics_processor_source_uri: Incomplete | None = None,
        max_runtime_in_seconds: Incomplete | None = None,
        environment: Incomplete | None = None,
        network_config: Incomplete | None = None,
        role_arn: Incomplete | None = None,
    ) -> None: ...
    def start_monitoring_schedule(self, monitoring_schedule_name) -> None: ...
    def stop_monitoring_schedule(self, monitoring_schedule_name) -> None: ...
    def delete_monitoring_schedule(self, monitoring_schedule_name) -> None: ...
    def describe_monitoring_schedule(self, monitoring_schedule_name): ...
    def list_monitoring_executions(
        self, monitoring_schedule_name, sort_by: str = "ScheduledTime", sort_order: str = "Descending", max_results: int = 100
    ): ...
    def list_monitoring_schedules(
        self,
        endpoint_name: Incomplete | None = None,
        sort_by: str = "CreationTime",
        sort_order: str = "Descending",
        max_results: int = 100,
    ): ...
    def update_monitoring_alert(
        self, monitoring_schedule_name: str, monitoring_alert_name: str, data_points_to_alert: int, evaluation_period: int
    ): ...
    def list_monitoring_alerts(
        self, monitoring_schedule_name: str, next_token: Optional[str] = None, max_results: Optional[int] = 10
    ) -> Dict: ...
    def list_monitoring_alert_history(
        self,
        monitoring_schedule_name: Optional[str] = None,
        monitoring_alert_name: Optional[str] = None,
        sort_by: Optional[str] = "CreationTime",
        sort_order: Optional[str] = "Descending",
        next_token: Optional[str] = None,
        max_results: Optional[int] = 10,
        creation_time_before: Optional[str] = None,
        creation_time_after: Optional[str] = None,
        status_equals: Optional[str] = None,
    ) -> Dict: ...
    def was_processing_job_successful(self, job_name): ...
    def describe_processing_job(self, job_name): ...
    def stop_processing_job(self, job_name) -> None: ...
    def stop_training_job(self, job_name) -> None: ...
    def describe_training_job(self, job_name): ...
    def auto_ml(
        self,
        input_config,
        output_config,
        auto_ml_job_config,
        role: Incomplete | None = None,
        job_name: Incomplete | None = None,
        problem_type: Incomplete | None = None,
        job_objective: Incomplete | None = None,
        generate_candidate_definitions_only: bool = False,
        tags: Incomplete | None = None,
        model_deploy_config: Incomplete | None = None,
    ) -> None: ...
    def describe_auto_ml_job(self, job_name): ...
    def list_candidates(
        self,
        job_name,
        status_equals: Incomplete | None = None,
        candidate_name: Incomplete | None = None,
        candidate_arn: Incomplete | None = None,
        sort_order: Incomplete | None = None,
        sort_by: Incomplete | None = None,
        max_results: Incomplete | None = None,
    ): ...
    def wait_for_auto_ml_job(self, job, poll: int = 5): ...
    def logs_for_auto_ml_job(self, job_name, wait: bool = False, poll: int = 10): ...
    def compile_model(
        self,
        input_model_config,
        output_model_config,
        role: Incomplete | None = None,
        job_name: Incomplete | None = None,
        stop_condition: Incomplete | None = None,
        tags: Incomplete | None = None,
    ) -> None: ...
    def package_model_for_edge(
        self,
        output_model_config,
        role: Incomplete | None = None,
        job_name: Incomplete | None = None,
        compilation_job_name: Incomplete | None = None,
        model_name: Incomplete | None = None,
        model_version: Incomplete | None = None,
        resource_key: Incomplete | None = None,
        tags: Incomplete | None = None,
    ) -> None: ...
    def tune(
        self,
        job_name,
        strategy,
        objective_type,
        objective_metric_name,
        max_jobs,
        max_parallel_jobs,
        parameter_ranges,
        static_hyperparameters,
        input_mode,
        metric_definitions,
        role,
        input_config,
        output_config,
        resource_config,
        stop_condition,
        tags,
        warm_start_config,
        max_runtime_in_seconds: Incomplete | None = None,
        strategy_config: Incomplete | None = None,
        completion_criteria_config: Incomplete | None = None,
        enable_network_isolation: bool = False,
        image_uri: Incomplete | None = None,
        algorithm_arn: Incomplete | None = None,
        early_stopping_type: str = "Off",
        encrypt_inter_container_traffic: bool = False,
        vpc_config: Incomplete | None = None,
        use_spot_instances: bool = False,
        checkpoint_s3_uri: Incomplete | None = None,
        checkpoint_local_path: Incomplete | None = None,
        random_seed: Incomplete | None = None,
        environment: Incomplete | None = None,
        hpo_resource_config: Incomplete | None = None,
        autotune: bool = False,
        auto_parameters: Incomplete | None = None,
    ) -> None: ...
    def create_tuning_job(
        self,
        job_name,
        tuning_config,
        training_config: Incomplete | None = None,
        training_config_list: Incomplete | None = None,
        warm_start_config: Incomplete | None = None,
        tags: Incomplete | None = None,
        autotune: bool = False,
    ) -> None: ...
    def describe_tuning_job(self, job_name): ...
    def stop_tuning_job(self, name) -> None: ...
    def transform(
        self,
        job_name,
        model_name,
        strategy,
        max_concurrent_transforms,
        max_payload,
        input_config,
        output_config,
        resource_config,
        experiment_config,
        env: Optional[Dict[str, str]] = None,
        tags: Incomplete | None = None,
        data_processing: Incomplete | None = None,
        model_client_config: Incomplete | None = None,
        batch_data_capture_config: BatchDataCaptureConfig = None,
    ): ...
    def create_model(
        self,
        name,
        role: Incomplete | None = None,
        container_defs: Incomplete | None = None,
        vpc_config: Incomplete | None = None,
        enable_network_isolation: Incomplete | None = None,
        primary_container: Incomplete | None = None,
        tags: Incomplete | None = None,
    ): ...
    def create_model_from_job(
        self,
        training_job_name,
        name: Incomplete | None = None,
        role: Incomplete | None = None,
        image_uri: Incomplete | None = None,
        model_data_url: Incomplete | None = None,
        env: Incomplete | None = None,
        enable_network_isolation: Incomplete | None = None,
        vpc_config_override="VPC_CONFIG_DEFAULT",
        tags: Incomplete | None = None,
    ): ...
    def create_model_package_from_algorithm(self, name, description, algorithm_arn, model_data) -> None: ...
    def create_model_package_from_containers(
        self,
        containers: Incomplete | None = None,
        content_types: Incomplete | None = None,
        response_types: Incomplete | None = None,
        inference_instances: Incomplete | None = None,
        transform_instances: Incomplete | None = None,
        model_package_name: Incomplete | None = None,
        model_package_group_name: Incomplete | None = None,
        model_metrics: Incomplete | None = None,
        metadata_properties: Incomplete | None = None,
        marketplace_cert: bool = False,
        approval_status: str = "PendingManualApproval",
        description: Incomplete | None = None,
        drift_check_baselines: Incomplete | None = None,
        customer_metadata_properties: Incomplete | None = None,
        validation_specification: Incomplete | None = None,
        domain: Incomplete | None = None,
        sample_payload_url: Incomplete | None = None,
        task: Incomplete | None = None,
    ): ...
    def wait_for_model_package(self, model_package_name, poll: int = 5): ...
    def describe_model(self, name): ...
    def create_endpoint_config(
        self,
        name,
        model_name,
        initial_instance_count,
        instance_type,
        accelerator_type: Incomplete | None = None,
        tags: Incomplete | None = None,
        kms_key: Incomplete | None = None,
        data_capture_config_dict: Incomplete | None = None,
        volume_size: Incomplete | None = None,
        model_data_download_timeout: Incomplete | None = None,
        container_startup_health_check_timeout: Incomplete | None = None,
        explainer_config_dict: Incomplete | None = None,
    ): ...
    def create_endpoint_config_from_existing(
        self,
        existing_config_name,
        new_config_name,
        new_tags: Incomplete | None = None,
        new_kms_key: Incomplete | None = None,
        new_data_capture_config_dict: Incomplete | None = None,
        new_production_variants: Incomplete | None = None,
        new_explainer_config_dict: Incomplete | None = None,
    ) -> None: ...
    def create_endpoint(self, endpoint_name, config_name, tags: Incomplete | None = None, wait: bool = True): ...
    def update_endpoint(self, endpoint_name, endpoint_config_name, wait: bool = True): ...
    def delete_endpoint(self, endpoint_name) -> None: ...
    def delete_endpoint_config(self, endpoint_config_name) -> None: ...
    def delete_model(self, model_name) -> None: ...
    def list_group_resources(self, group, filters, next_token: str = ""): ...
    def delete_resource_group(self, group): ...
    def get_resource_group_query(self, group): ...
    def get_tagging_resources(self, tag_filters, resource_type_filters): ...
    def create_group(self, name, resource_query, tags): ...
    def list_tags(self, resource_arn, max_results: int = 50): ...
    def wait_for_job(self, job, poll: int = 5): ...
    def wait_for_processing_job(self, job, poll: int = 5): ...
    def wait_for_compilation_job(self, job, poll: int = 5): ...
    def wait_for_edge_packaging_job(self, job, poll: int = 5): ...
    def wait_for_tuning_job(self, job, poll: int = 5): ...
    def describe_transform_job(self, job_name): ...
    def wait_for_transform_job(self, job, poll: int = 5): ...
    def stop_transform_job(self, name) -> None: ...
    def wait_for_endpoint(self, endpoint, poll: int = 30): ...
    def endpoint_from_job(
        self,
        job_name,
        initial_instance_count,
        instance_type,
        image_uri: Incomplete | None = None,
        name: Incomplete | None = None,
        role: Incomplete | None = None,
        wait: bool = True,
        model_environment_vars: Incomplete | None = None,
        vpc_config_override="VPC_CONFIG_DEFAULT",
        accelerator_type: Incomplete | None = None,
        data_capture_config: Incomplete | None = None,
    ): ...
    def endpoint_from_model_data(
        self,
        model_s3_location,
        image_uri,
        initial_instance_count,
        instance_type,
        name: Incomplete | None = None,
        role: Incomplete | None = None,
        wait: bool = True,
        model_environment_vars: Incomplete | None = None,
        model_vpc_config: Incomplete | None = None,
        accelerator_type: Incomplete | None = None,
        data_capture_config: Incomplete | None = None,
        tags: Incomplete | None = None,
    ): ...
    def endpoint_from_production_variants(
        self,
        name,
        production_variants,
        tags: Incomplete | None = None,
        kms_key: Incomplete | None = None,
        wait: bool = True,
        data_capture_config_dict: Incomplete | None = None,
        async_inference_config_dict: Incomplete | None = None,
        explainer_config_dict: Incomplete | None = None,
    ): ...
    def expand_role(self, role): ...
    def get_caller_identity_arn(self): ...
    def logs_for_job(
        self, job_name, wait: bool = False, poll: int = 10, log_type: str = "All", timeout: Incomplete | None = None
    ) -> None: ...
    def logs_for_processing_job(self, job_name, wait: bool = False, poll: int = 10): ...
    def logs_for_transform_job(self, job_name, wait: bool = False, poll: int = 10): ...
    def delete_feature_group(self, feature_group_name: str): ...
    def create_feature_group(
        self,
        feature_group_name: str,
        record_identifier_name: str,
        event_time_feature_name: str,
        feature_definitions: Sequence[Dict[str, str]],
        role_arn: str = None,
        online_store_config: Dict[str, str] = None,
        offline_store_config: Dict[str, str] = None,
        description: str = None,
        tags: List[Dict[str, str]] = None,
    ) -> Dict[str, Any]: ...
    def describe_feature_group(self, feature_group_name: str, next_token: str = None) -> Dict[str, Any]: ...
    def update_feature_group(self, feature_group_name: str, feature_additions: Sequence[Dict[str, str]]) -> Dict[str, Any]: ...
    def list_feature_groups(
        self,
        name_contains,
        feature_group_status_equals,
        offline_store_status_equals,
        creation_time_after,
        creation_time_before,
        sort_order,
        sort_by,
        max_results,
        next_token,
    ) -> Dict[str, Any]: ...
    def update_feature_metadata(
        self,
        feature_group_name: str,
        feature_name: str,
        description: str = None,
        parameter_additions: Sequence[Dict[str, str]] = None,
        parameter_removals: Sequence[str] = None,
    ) -> Dict[str, Any]: ...
    def describe_feature_metadata(self, feature_group_name: str, feature_name: str) -> Dict[str, Any]: ...
    def search(
        self,
        resource: str,
        search_expression: Dict[str, any] = None,
        sort_by: str = None,
        sort_order: str = None,
        next_token: str = None,
        max_results: int = None,
    ) -> Dict[str, Any]: ...
    def put_record(self, feature_group_name: str, record: Sequence[Dict[str, str]]): ...
    def delete_record(
        self, feature_group_name: str, record_identifier_value_as_string: str, event_time: str, deletion_mode: str = None
    ): ...
    def get_record(
        self, record_identifier_value_as_string: str, feature_group_name: str, feature_names: Sequence[str]
    ) -> Dict[str, Sequence[Dict[str, str]]]: ...
    def batch_get_record(self, identifiers: Sequence[Dict[str, Any]]) -> Dict[str, Any]: ...
    def start_query_execution(
        self, catalog: str, database: str, query_string: str, output_location: str, kms_key: str = None, workgroup: str = None
    ) -> Dict[str, str]: ...
    def get_query_execution(self, query_execution_id: str) -> Dict[str, Any]: ...
    def wait_for_athena_query(self, query_execution_id: str, poll: int = 5): ...
    def download_athena_query_result(self, bucket: str, prefix: str, query_execution_id: str, filename: str): ...
    def account_id(self) -> str: ...
    def create_inference_recommendations_job(
        self,
        role: str,
        sample_payload_url: str,
        supported_content_types: List[str],
        job_name: str = None,
        job_type: str = "Default",
        model_name: str = None,
        model_package_version_arn: str = None,
        job_duration_in_seconds: int = None,
        nearest_model_name: str = None,
        supported_instance_types: List[str] = None,
        framework: str = None,
        framework_version: str = None,
        endpoint_configurations: List[Dict[str, any]] = None,
        traffic_pattern: Dict[str, any] = None,
        stopping_conditions: Dict[str, any] = None,
        resource_limit: Dict[str, any] = None,
    ): ...
    def wait_for_inference_recommendations_job(
        self, job_name: str, poll: int = 120, log_level: str = "Verbose"
    ) -> Dict[str, Any]: ...

def get_model_package_args(
    content_types,
    response_types,
    inference_instances: Incomplete | None = None,
    transform_instances: Incomplete | None = None,
    model_package_name: Incomplete | None = None,
    model_package_group_name: Incomplete | None = None,
    model_data: Incomplete | None = None,
    image_uri: Incomplete | None = None,
    model_metrics: Incomplete | None = None,
    metadata_properties: Incomplete | None = None,
    marketplace_cert: bool = False,
    approval_status: Incomplete | None = None,
    description: Incomplete | None = None,
    tags: Incomplete | None = None,
    container_def_list: Incomplete | None = None,
    drift_check_baselines: Incomplete | None = None,
    customer_metadata_properties: Incomplete | None = None,
    validation_specification: Incomplete | None = None,
    domain: Incomplete | None = None,
    sample_payload_url: Incomplete | None = None,
    task: Incomplete | None = None,
): ...
def get_create_model_package_request(
    model_package_name: Incomplete | None = None,
    model_package_group_name: Incomplete | None = None,
    containers: Incomplete | None = None,
    content_types: Incomplete | None = None,
    response_types: Incomplete | None = None,
    inference_instances: Incomplete | None = None,
    transform_instances: Incomplete | None = None,
    model_metrics: Incomplete | None = None,
    metadata_properties: Incomplete | None = None,
    marketplace_cert: bool = False,
    approval_status: str = "PendingManualApproval",
    description: Incomplete | None = None,
    tags: Incomplete | None = None,
    drift_check_baselines: Incomplete | None = None,
    customer_metadata_properties: Incomplete | None = None,
    validation_specification: Incomplete | None = None,
    domain: Incomplete | None = None,
    sample_payload_url: Incomplete | None = None,
    task: Incomplete | None = None,
): ...
def update_args(args: Dict[str, Any], **kwargs): ...
def container_def(
    image_uri,
    model_data_url: Incomplete | None = None,
    env: Incomplete | None = None,
    container_mode: Incomplete | None = None,
    image_config: Incomplete | None = None,
): ...
def pipeline_container_def(models, instance_type: Incomplete | None = None): ...
def production_variant(
    model_name,
    instance_type: Incomplete | None = None,
    initial_instance_count: Incomplete | None = None,
    variant_name: str = "AllTraffic",
    initial_weight: int = 1,
    accelerator_type: Incomplete | None = None,
    serverless_inference_config: Incomplete | None = None,
    volume_size: Incomplete | None = None,
    model_data_download_timeout: Incomplete | None = None,
    container_startup_health_check_timeout: Incomplete | None = None,
): ...
def get_execution_role(sagemaker_session: Incomplete | None = None): ...
def generate_default_sagemaker_bucket_name(boto_session): ...
def get_log_events_for_inference_recommender(cw_client, log_group_name, log_stream_name): ...

s3_input: Incomplete
