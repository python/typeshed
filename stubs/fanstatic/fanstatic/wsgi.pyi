from _typeshed.wsgi import WSGIApplication
from typing import Any

import webob
from fanstatic.core import Resource
from fanstatic.injector import InjectorPlugin
from fanstatic.publisher import Delegator

def Fanstatic(
    app: WSGIApplication, publisher_signature: str = ..., injector: InjectorPlugin | None = None, **config: Any
) -> Delegator: ...
def make_fanstatic(app: WSGIApplication, global_config: Any, **local_config: Any) -> Delegator: ...

class Serf:
    resource: Resource
    def __init__(self, resource: Resource) -> None: ...
    @webob.dec.wsgify
    def __call__(self, request: webob.Request) -> webob.Response: ...

def make_serf(global_config: Any, **local_config: Any) -> Serf: ...
def resolve(name: str, module: str | None = None) -> Any: ...
