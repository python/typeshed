from _typeshed import Incomplete
from typing import Any

from braintree.add_on import AddOn as AddOn
from braintree.configuration import Configuration as Configuration
from braintree.discount import Discount as Discount
from braintree.resource import Resource as Resource
from braintree.resource_collection import ResourceCollection as ResourceCollection
from braintree.util.http import Http as Http

class Plan(Resource):
    add_ons: Any
    discounts: Any
    def __init__(self, gateway, attributes) -> None: ...
    @staticmethod
    def all(): ...
    @staticmethod
    def create(params: Incomplete | None = None): ...
    @staticmethod
    def find(subscription_id): ...
    @staticmethod
    def update(subscription_id, params: Incomplete | None = None): ...
    @staticmethod
    def create_signature(): ...
    @staticmethod
    def update_signature(): ...
