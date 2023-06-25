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
    region: str | None = None,
    model_id: str | None = None,
    model_version: str | None = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> list[BaseSerializer]: ...
def retrieve_default(
    region: str | None = None,
    model_id: str | None = None,
    model_version: str | None = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> BaseSerializer: ...
