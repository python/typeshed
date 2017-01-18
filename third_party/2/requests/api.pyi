# Stubs for requests.api (Python 2)

from typing import Union, Optional, Iterable, Dict

from .models import Response

def request(method: str, url: str, **kwargs) -> Response: ...

def get(url: Union[str, unicode],
        params: Optional[
               Union[
                Dict[
                        Union[str, unicode, int, float], 
                        Union[str, unicode, int, float, Iterable]
                ], 
                Union[str, unicode], 
                Tuple[
                        Union[str, unicode, int, float], 
                        Union[str, unicode, int, float, Iterable]
                ]
               ]
              ]=None,
        **kwargs) -> Response: ...

def options(url: Union[str, unicode], **kwargs) -> Response: ...
def head(url: Union[str, unicode], **kwargs) -> Response: ...
def post(url: Union[str, unicode], data=..., json=...,
         **kwargs) -> Response: ...
def put(url: Union[str, unicode], data=..., **kwargs) -> Response: ...
def patch(url: Union[str, unicode], data=..., **kwargs) -> Response: ...
def delete(url: Union[str, unicode], **kwargs) -> Response: ...
