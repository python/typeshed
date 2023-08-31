from _typeshed import Incomplete

NO_SUCH_KEY_CODE: str

class ModelMonitoringFile:
    body_dict: Incomplete
    file_s3_uri: Incomplete
    kms_key: Incomplete
    session: Incomplete
    def __init__(self, body_dict, file_s3_uri, kms_key, sagemaker_session) -> None: ...
    def save(self, new_save_location_s3_uri: Incomplete | None = None): ...

class Statistics(ModelMonitoringFile):
    def __init__(
        self, body_dict, statistics_file_s3_uri, kms_key: Incomplete | None = None, sagemaker_session: Incomplete | None = None
    ) -> None: ...
    @classmethod
    def from_s3_uri(
        cls, statistics_file_s3_uri, kms_key: Incomplete | None = None, sagemaker_session: Incomplete | None = None
    ): ...
    @classmethod
    def from_string(
        cls,
        statistics_file_string,
        kms_key: Incomplete | None = None,
        file_name: Incomplete | None = None,
        sagemaker_session: Incomplete | None = None,
    ): ...
    @classmethod
    def from_file_path(
        cls, statistics_file_path, kms_key: Incomplete | None = None, sagemaker_session: Incomplete | None = None
    ): ...

class Constraints(ModelMonitoringFile):
    def __init__(
        self, body_dict, constraints_file_s3_uri, kms_key: Incomplete | None = None, sagemaker_session: Incomplete | None = None
    ) -> None: ...
    @classmethod
    def from_s3_uri(
        cls, constraints_file_s3_uri, kms_key: Incomplete | None = None, sagemaker_session: Incomplete | None = None
    ): ...
    @classmethod
    def from_string(
        cls,
        constraints_file_string,
        kms_key: Incomplete | None = None,
        file_name: Incomplete | None = None,
        sagemaker_session: Incomplete | None = None,
    ): ...
    @classmethod
    def from_file_path(
        cls, constraints_file_path, kms_key: Incomplete | None = None, sagemaker_session: Incomplete | None = None
    ): ...
    def set_monitoring(self, enable_monitoring, feature_name: Incomplete | None = None) -> None: ...

class ConstraintViolations(ModelMonitoringFile):
    def __init__(
        self,
        body_dict,
        constraint_violations_file_s3_uri,
        kms_key: Incomplete | None = None,
        sagemaker_session: Incomplete | None = None,
    ) -> None: ...
    @classmethod
    def from_s3_uri(
        cls, constraint_violations_file_s3_uri, kms_key: Incomplete | None = None, sagemaker_session: Incomplete | None = None
    ): ...
    @classmethod
    def from_string(
        cls,
        constraint_violations_file_string,
        kms_key: Incomplete | None = None,
        file_name: Incomplete | None = None,
        sagemaker_session: Incomplete | None = None,
    ): ...
    @classmethod
    def from_file_path(
        cls, constraint_violations_file_path, kms_key: Incomplete | None = None, sagemaker_session: Incomplete | None = None
    ): ...
