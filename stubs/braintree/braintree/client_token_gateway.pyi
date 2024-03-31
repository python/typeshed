from _typeshed import Incomplete

from braintree import exceptions as exceptions
from braintree.client_token import ClientToken as ClientToken
from braintree.resource import Resource as Resource

class ClientTokenGateway:
    gateway: Incomplete
    config: Incomplete
    def __init__(self, gateway) -> None: ...
    def generate(self, params: Incomplete | None = None): ...
