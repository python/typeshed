from _typeshed import Incomplete
from typing import Dict, NamedTuple, Optional, Union

from sagemaker.session_settings import SessionSettings
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

class UploadedCode(NamedTuple):
    s3_prefix: Incomplete
    script_name: Incomplete

PYTHON_2_DEPRECATION_WARNING: str
PARAMETER_SERVER_MULTI_GPU_WARNING: str
DEBUGGER_UNSUPPORTED_REGIONS: Incomplete
PROFILER_UNSUPPORTED_REGIONS: Incomplete
SINGLE_GPU_INSTANCE_TYPES: Incomplete
SM_DATAPARALLEL_SUPPORTED_INSTANCE_TYPES: Incomplete
SM_DATAPARALLEL_SUPPORTED_FRAMEWORK_VERSIONS: Incomplete
PYTORCHDDP_SUPPORTED_FRAMEWORK_VERSIONS: Incomplete
TORCH_DISTRIBUTED_GPU_SUPPORTED_FRAMEWORK_VERSIONS: Incomplete
TRAINIUM_SUPPORTED_DISTRIBUTION_STRATEGIES: Incomplete
TRAINIUM_SUPPORTED_TORCH_DISTRIBUTED_FRAMEWORK_VERSIONS: Incomplete
SMDISTRIBUTED_SUPPORTED_STRATEGIES: Incomplete
GRAVITON_ALLOWED_TARGET_INSTANCE_FAMILY: Incomplete
GRAVITON_ALLOWED_FRAMEWORKS: Incomplete

def validate_source_dir(script, directory): ...
def validate_source_code_input_against_pipeline_variables(
    entry_point: Optional[Union[str, PipelineVariable]] = None,
    source_dir: Optional[Union[str, PipelineVariable]] = None,
    git_config: Optional[Dict[str, str]] = None,
    enable_network_isolation: Union[bool, PipelineVariable] = False,
): ...
def parse_mp_parameters(params): ...
def get_mp_parameters(distribution): ...
def validate_mp_config(config) -> None: ...
def tar_and_upload_dir(
    session,
    bucket,
    s3_key_prefix,
    script,
    directory: Incomplete | None = None,
    dependencies: Incomplete | None = None,
    kms_key: Incomplete | None = None,
    s3_resource: Incomplete | None = None,
    settings: Optional[SessionSettings] = None,
) -> UploadedCode: ...
def framework_name_from_image(image_uri): ...
def framework_version_from_tag(image_tag): ...
def model_code_key_prefix(code_location_key_prefix, model_name, image): ...
def warn_if_parameter_server_with_multi_gpu(training_instance_type, distribution) -> None: ...
def profiler_config_deprecation_warning(profiler_config, image_uri, framework_name, framework_version) -> None: ...
def validate_smdistributed(
    instance_type, framework_name, framework_version, py_version, distribution, image_uri: Incomplete | None = None
) -> None: ...
def validate_distribution(distribution, instance_groups, framework_name, framework_version, py_version, image_uri, kwargs): ...
def validate_distribution_for_instance_type(instance_type, distribution) -> None: ...
def validate_pytorch_distribution(distribution, framework_name, framework_version, py_version, image_uri) -> None: ...
def validate_torch_distributed_distribution(
    instance_type, distribution, framework_version, py_version, image_uri, entry_point
) -> None: ...
def python_deprecation_warning(framework, latest_supported_version): ...
def validate_version_or_image_args(framework_version, py_version, image_uri) -> None: ...
def create_image_uri(
    region,
    framework,
    instance_type,
    framework_version,
    py_version: Incomplete | None = None,
    account: Incomplete | None = None,
    accelerator_type: Incomplete | None = None,
    optimized_families: Incomplete | None = None,
): ...
