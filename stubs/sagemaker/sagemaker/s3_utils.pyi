from _typeshed import Incomplete
from typing import Optional

logger: Incomplete

def parse_s3_url(url): ...
def s3_path_join(*args, with_end_slash: bool = False): ...
def determine_bucket_and_prefix(
    bucket: str | None = None, key_prefix: str | None = None, sagemaker_session: Incomplete | None = None
): ...
