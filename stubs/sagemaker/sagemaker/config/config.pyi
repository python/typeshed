from _typeshed import Incomplete
from typing import List

logger: Incomplete
ENV_VARIABLE_ADMIN_CONFIG_OVERRIDE: str
ENV_VARIABLE_USER_CONFIG_OVERRIDE: str
S3_PREFIX: str

def load_sagemaker_config(additional_config_paths: list[str] | None = None, s3_resource: Incomplete | None = None) -> dict: ...
def validate_sagemaker_config(sagemaker_config: dict | None = None): ...
