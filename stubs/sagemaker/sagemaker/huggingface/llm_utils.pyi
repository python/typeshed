from sagemaker.session import Session

def get_huggingface_llm_image_uri(
    backend: str, session: Session | None = None, region: str | None = None, version: str | None = None
) -> str: ...
