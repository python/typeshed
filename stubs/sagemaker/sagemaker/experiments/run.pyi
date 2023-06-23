import datetime
from _typeshed import Incomplete
from enum import Enum
from typing import Dict, List, Optional, Union

from numpy import array
from sagemaker import Session

logger: Incomplete
RUN_NAME_BASE: Incomplete
TRIAL_NAME_TEMPLATE: str
MAX_RUN_TC_ARTIFACTS_LEN: int
MAX_NAME_LEN_IN_BACKEND: int
EXPERIMENT_NAME: str
TRIAL_NAME: str
RUN_NAME: str
DELIMITER: str
RUN_TC_TAG_KEY: str
RUN_TC_TAG_VALUE: str
RUN_TC_TAG: Incomplete

class SortByType(Enum):
    CREATION_TIME: str
    NAME: str

class SortOrderType(Enum):
    ASCENDING: str
    DESCENDING: str

class Run:
    experiment_name: Incomplete
    run_name: Incomplete
    run_group_name: Incomplete
    def __init__(
        self,
        experiment_name: str,
        run_name: Optional[str] = None,
        experiment_display_name: Optional[str] = None,
        run_display_name: Optional[str] = None,
        tags: Optional[List[Dict[str, str]]] = None,
        sagemaker_session: Optional["Session"] = None,
    ) -> None: ...
    @property
    def experiment_config(self) -> dict: ...
    def log_parameter(self, name: str, value: Union[str, int, float]): ...
    def log_parameters(self, parameters: Dict[str, Union[str, int, float]]): ...
    def log_metric(self, name: str, value: float, timestamp: Optional[datetime.datetime] = None, step: Optional[int] = None): ...
    def log_precision_recall(
        self,
        y_true: Union[list, array],
        predicted_probabilities: Union[list, array],
        positive_label: Optional[Union[str, int]] = None,
        title: Optional[str] = None,
        is_output: bool = True,
        no_skill: Optional[int] = None,
    ): ...
    def log_roc_curve(
        self, y_true: Union[list, array], y_score: Union[list, array], title: Optional[str] = None, is_output: bool = True
    ): ...
    def log_confusion_matrix(
        self, y_true: Union[list, array], y_pred: Union[list, array], title: Optional[str] = None, is_output: bool = True
    ): ...
    def log_artifact(self, name: str, value: str, media_type: Optional[str] = None, is_output: bool = True): ...
    def log_file(self, file_path: str, name: Optional[str] = None, media_type: Optional[str] = None, is_output: bool = True): ...
    def close(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, exc_traceback) -> None: ...

def load_run(
    run_name: Optional[str] = None, experiment_name: Optional[str] = None, sagemaker_session: Optional["Session"] = None
) -> Run: ...
def list_runs(
    experiment_name: str,
    created_before: Optional[datetime.datetime] = None,
    created_after: Optional[datetime.datetime] = None,
    sagemaker_session: Optional["Session"] = None,
    max_results: Optional[int] = None,
    next_token: Optional[str] = None,
    sort_by: SortByType = ...,
    sort_order: SortOrderType = ...,
) -> list: ...
