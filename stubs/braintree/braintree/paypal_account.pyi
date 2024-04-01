from _typeshed import Incomplete

from braintree.configuration import Configuration as Configuration
from braintree.resource import Resource as Resource
from braintree.subscription import Subscription

class PayPalAccount(Resource):
    @staticmethod
    def find(paypal_account_token): ...
    @staticmethod
    def delete(paypal_account_token): ...
    @staticmethod
    def update(paypal_account_token, params: Incomplete | None = None): ...
    @staticmethod
    def signature(): ...
    subscriptions: list[Subscription]
    def __init__(self, gateway, attributes) -> None: ...
