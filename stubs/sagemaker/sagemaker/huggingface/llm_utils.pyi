from typing import Optional

from sagemaker.session import Session

def get_huggingface_llm_image_uri(
    backend: str, session: Optional[Session] = None, region: Optional[str] = None, version: Optional[str] = None
) -> str: ...
