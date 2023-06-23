from _typeshed import Incomplete
from typing import Optional

logger: Incomplete

def parse_s3_url(url): ...
def s3_path_join(*args, with_end_slash: bool = False): ...
def determine_bucket_and_prefix(
    bucket: Optional[str] = None, key_prefix: Optional[str] = None, sagemaker_session: Incomplete | None = None
): ...
