# Stubs for requests.api (Python 2)

from typing import Union, Optional, Iterable, Mapping, Tuple

from .models import Response

_ParamsMappingValueType = Union[str, unicode, int, float, Iterable[Union[str, unicode, int, float]]]

def request(method: str, url: str, **kwargs) -> Response: ...
def get(url: Union[str, unicode],
        params: Optional[
            Union[Mapping[Union[str, unicode, int, float], _ParamsMappingValueType],
                  Union[str, unicode],
                  Tuple[Union[str, unicode, int, float], _ParamsMappingValueType],
                  Mapping[str, _ParamsMappingValueType],
                  Mapping[unicode, _ParamsMappingValueType],
                  Mapping[int, _ParamsMappingValueType],
                  Mapping[float, _ParamsMappingValueType]]] = None,
        **kwargs) -> Response: ...
def options(url: Union[str, unicode], **kwargs) -> Response: ...
def head(url: Union[str, unicode], **kwargs) -> Response: ...
def post(url: Union[str, unicode], data=..., json=...,
         **kwargs) -> Response: ...
def put(url: Union[str, unicode], data=..., **kwargs) -> Response: ...
def patch(url: Union[str, unicode], data=..., **kwargs) -> Response: ...
def delete(url: Union[str, unicode], **kwargs) -> Response: ...
