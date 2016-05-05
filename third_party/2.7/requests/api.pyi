# Stubs for requests.api (Python 3)

from typing import Union

from .models import Response

def request(method: str, url: str, **kwargs) -> Response: ...
def get(url: Union[str, unicode], **kwargs) -> Response: ...
def options(url: Union[str, unicode], **kwargs) -> Response: ...
def head(url: Union[str, unicode], **kwargs) -> Response: ...
def post(url: Union[str, unicode], data=..., json=...,
         **kwargs) -> Response: ...
def put(url: Union[str, unicode], data=..., **kwargs) -> Response: ...
def patch(url: Union[str, unicode], data=..., **kwargs) -> Response: ...
def delete(url: Union[str, unicode], **kwargs) -> Response: ...
