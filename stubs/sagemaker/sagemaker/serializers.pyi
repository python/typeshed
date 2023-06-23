from typing import List, Optional

from sagemaker.base_serializers import (
    BaseSerializer,
    CSVSerializer as CSVSerializer,
    DataSerializer as DataSerializer,
    IdentitySerializer as IdentitySerializer,
    JSONLinesSerializer as JSONLinesSerializer,
    JSONSerializer as JSONSerializer,
    LibSVMSerializer as LibSVMSerializer,
    NumpySerializer as NumpySerializer,
    SimpleBaseSerializer as SimpleBaseSerializer,
    SparseMatrixSerializer as SparseMatrixSerializer,
)

def retrieve_options(
    region: Optional[str] = None,
    model_id: Optional[str] = None,
    model_version: Optional[str] = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> List[BaseSerializer]: ...
def retrieve_default(
    region: Optional[str] = None,
    model_id: Optional[str] = None,
    model_version: Optional[str] = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> BaseSerializer: ...
