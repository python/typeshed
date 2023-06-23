import io
from _typeshed import Incomplete
from typing import Union

from sagemaker.s3_utils import determine_bucket_and_prefix as determine_bucket_and_prefix

logger: Incomplete

class S3Uploader:
    @staticmethod
    def upload(local_path, desired_s3_uri, kms_key: Incomplete | None = None, sagemaker_session: Incomplete | None = None): ...
    @staticmethod
    def upload_string_as_file_body(
        body: str,
        desired_s3_uri: Incomplete | None = None,
        kms_key: Incomplete | None = None,
        sagemaker_session: Incomplete | None = None,
    ): ...
    @staticmethod
    def upload_bytes(
        b: Union[bytes, io.BytesIO], s3_uri, kms_key: Incomplete | None = None, sagemaker_session: Incomplete | None = None
    ): ...

class S3Downloader:
    @staticmethod
    def download(s3_uri, local_path, kms_key: Incomplete | None = None, sagemaker_session: Incomplete | None = None): ...
    @staticmethod
    def read_file(s3_uri, sagemaker_session: Incomplete | None = None) -> str: ...
    @staticmethod
    def read_bytes(s3_uri, sagemaker_session: Incomplete | None = None) -> bytes: ...
    @staticmethod
    def list(s3_uri, sagemaker_session: Incomplete | None = None): ...
