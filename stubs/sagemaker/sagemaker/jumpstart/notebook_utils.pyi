from typing import List, Tuple

from sagemaker.jumpstart.filters import Operator

def extract_framework_task_model(model_id: str) -> Tuple[str, str, str]: ...
def list_jumpstart_tasks(filter: Operator | str = ..., region: str = "eu-west-1") -> List[str]: ...
def list_jumpstart_frameworks(filter: Operator | str = ..., region: str = "eu-west-1") -> List[str]: ...
def list_jumpstart_scripts(filter: Operator | str = ..., region: str = "eu-west-1") -> List[str]: ...
def list_jumpstart_models(
    filter: Operator | str = ...,
    region: str = "eu-west-1",
    list_incomplete_models: bool = False,
    list_old_models: bool = False,
    list_versions: bool = False,
) -> List[Tuple[str, Tuple[str, str]]]: ...
def get_model_url(model_id: str, model_version: str, region: str = "eu-west-1") -> str: ...
