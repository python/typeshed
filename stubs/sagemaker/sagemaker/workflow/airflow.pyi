from _typeshed import Incomplete

def prepare_framework(estimator, s3_operations) -> None: ...
def prepare_amazon_algorithm_estimator(estimator, inputs, mini_batch_size: Incomplete | None = None) -> None: ...
def training_base_config(
    estimator, inputs: Incomplete | None = None, job_name: Incomplete | None = None, mini_batch_size: Incomplete | None = None
): ...
def training_config(
    estimator, inputs: Incomplete | None = None, job_name: Incomplete | None = None, mini_batch_size: Incomplete | None = None
): ...
def tuning_config(
    tuner,
    inputs,
    job_name: Incomplete | None = None,
    include_cls_metadata: bool = False,
    mini_batch_size: Incomplete | None = None,
): ...
def update_submit_s3_uri(estimator, job_name) -> None: ...
def update_estimator_from_task(estimator, task_id, task_type) -> None: ...
def prepare_framework_container_def(model, instance_type, s3_operations): ...
def model_config(
    model, instance_type: Incomplete | None = None, role: Incomplete | None = None, image_uri: Incomplete | None = None
): ...
def model_config_from_estimator(
    estimator,
    task_id,
    task_type,
    instance_type: Incomplete | None = None,
    role: Incomplete | None = None,
    image_uri: Incomplete | None = None,
    name: Incomplete | None = None,
    model_server_workers: Incomplete | None = None,
    vpc_config_override="VPC_CONFIG_DEFAULT",
): ...
def transform_config(
    transformer,
    data,
    data_type: str = "S3Prefix",
    content_type: Incomplete | None = None,
    compression_type: Incomplete | None = None,
    split_type: Incomplete | None = None,
    job_name: Incomplete | None = None,
    input_filter: Incomplete | None = None,
    output_filter: Incomplete | None = None,
    join_source: Incomplete | None = None,
): ...
def transform_config_from_estimator(
    estimator,
    task_id,
    task_type,
    instance_count,
    instance_type,
    data,
    data_type: str = "S3Prefix",
    content_type: Incomplete | None = None,
    compression_type: Incomplete | None = None,
    split_type: Incomplete | None = None,
    job_name: Incomplete | None = None,
    model_name: Incomplete | None = None,
    strategy: Incomplete | None = None,
    assemble_with: Incomplete | None = None,
    output_path: Incomplete | None = None,
    output_kms_key: Incomplete | None = None,
    accept: Incomplete | None = None,
    env: Incomplete | None = None,
    max_concurrent_transforms: Incomplete | None = None,
    max_payload: Incomplete | None = None,
    tags: Incomplete | None = None,
    role: Incomplete | None = None,
    volume_kms_key: Incomplete | None = None,
    model_server_workers: Incomplete | None = None,
    image_uri: Incomplete | None = None,
    vpc_config_override: Incomplete | None = None,
    input_filter: Incomplete | None = None,
    output_filter: Incomplete | None = None,
    join_source: Incomplete | None = None,
): ...
def deploy_config(
    model, initial_instance_count, instance_type, endpoint_name: Incomplete | None = None, tags: Incomplete | None = None
): ...
def deploy_config_from_estimator(
    estimator,
    task_id,
    task_type,
    initial_instance_count,
    instance_type,
    model_name: Incomplete | None = None,
    endpoint_name: Incomplete | None = None,
    tags: Incomplete | None = None,
    **kwargs,
): ...
def processing_config(
    processor,
    inputs: Incomplete | None = None,
    outputs: Incomplete | None = None,
    job_name: Incomplete | None = None,
    experiment_config: Incomplete | None = None,
    container_arguments: Incomplete | None = None,
    container_entrypoint: Incomplete | None = None,
    kms_key_id: Incomplete | None = None,
): ...
def input_output_list_converter(object_list): ...
