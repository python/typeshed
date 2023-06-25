from typing import List, Optional

from sagemaker.base_deserializers import (
    BaseDeserializer,
    BytesDeserializer as BytesDeserializer,
    CSVDeserializer as CSVDeserializer,
    DeferredError as DeferredError,
    JSONDeserializer as JSONDeserializer,
    JSONLinesDeserializer as JSONLinesDeserializer,
    NumpyDeserializer as NumpyDeserializer,
    PandasDeserializer as PandasDeserializer,
    SimpleBaseDeserializer as SimpleBaseDeserializer,
    StreamDeserializer as StreamDeserializer,
    StringDeserializer as StringDeserializer,
)

def retrieve_options(
    region: str | None = None,
    model_id: str | None = None,
    model_version: str | None = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> list[BaseDeserializer]: ...
def retrieve_default(
    region: str | None = None,
    model_id: str | None = None,
    model_version: str | None = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> BaseDeserializer: ...
