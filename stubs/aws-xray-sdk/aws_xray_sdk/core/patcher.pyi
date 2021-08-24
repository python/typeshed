from typing import Any

from aws_xray_sdk import global_sdk_config as global_sdk_config

from .utils.compat import PY2 as PY2, is_classmethod as is_classmethod, is_instance_method as is_instance_method

log: Any
SUPPORTED_MODULES: Any
NO_DOUBLE_PATCH: Any

def patch_all(double_patch: bool = ...) -> None: ...
def patch(modules_to_patch, raise_errors: bool = ..., ignore_module_patterns: Any | None = ...) -> None: ...
