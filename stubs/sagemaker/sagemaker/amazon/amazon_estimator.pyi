import abc
from _typeshed import Incomplete
from typing import Dict, Optional

from sagemaker.amazon.hyperparameter import Hyperparameter as hp
from sagemaker.estimator import EstimatorBase
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

class AmazonAlgorithmEstimatorBase(EstimatorBase, metaclass=abc.ABCMeta):
    feature_dim: hp
    mini_batch_size: hp
    repo_name: str | None
    repo_version: str | None
    DEFAULT_MINI_BATCH_SIZE: int | None
    def __init__(
        self,
        role: str | PipelineVariable | None = None,
        instance_count: int | PipelineVariable | None = None,
        instance_type: str | PipelineVariable | None = None,
        data_location: str | None = None,
        enable_network_isolation: bool | PipelineVariable = False,
        **kwargs,
    ) -> None: ...
    def training_image_uri(self): ...
    def hyperparameters(self): ...
    @property
    def data_location(self): ...
    @data_location.setter
    def data_location(self, data_location: str): ...
    def prepare_workflow_for_training(
        self, records: Incomplete | None = None, mini_batch_size: Incomplete | None = None, job_name: Incomplete | None = None
    ) -> None: ...
    latest_training_job: Incomplete
    def fit(
        self,
        records: RecordSet,
        mini_batch_size: int | None = None,
        wait: bool = True,
        logs: bool = True,
        job_name: str | None = None,
        experiment_config: dict[str, str] | None = None,
    ): ...
    def record_set(self, train, labels: Incomplete | None = None, channel: str = "train", encrypt: bool = False): ...

class RecordSet:
    s3_data: Incomplete
    feature_dim: Incomplete
    num_records: Incomplete
    s3_data_type: Incomplete
    channel: Incomplete
    def __init__(
        self,
        s3_data: str | PipelineVariable,
        num_records: int,
        feature_dim: int,
        s3_data_type: str | PipelineVariable = "ManifestFile",
        channel: str | PipelineVariable = "train",
    ) -> None: ...
    def data_channel(self): ...
    def records_s3_input(self): ...

class FileSystemRecordSet:
    file_system_input: Incomplete
    feature_dim: Incomplete
    num_records: Incomplete
    channel: Incomplete
    def __init__(
        self,
        file_system_id,
        file_system_type,
        directory_path,
        num_records,
        feature_dim,
        file_system_access_mode: str = "ro",
        channel: str = "train",
    ) -> None: ...
    def data_channel(self): ...

def upload_numpy_to_s3_shards(
    num_shards, s3, bucket, key_prefix, array, labels: Incomplete | None = None, encrypt: bool = False
): ...
def get_image_uri(region_name, repo_name, repo_version: str = "1"): ...
