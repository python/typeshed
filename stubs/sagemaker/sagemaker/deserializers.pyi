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
    region: Optional[str] = None,
    model_id: Optional[str] = None,
    model_version: Optional[str] = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> List[BaseDeserializer]: ...
def retrieve_default(
    region: Optional[str] = None,
    model_id: Optional[str] = None,
    model_version: Optional[str] = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> BaseDeserializer: ...
