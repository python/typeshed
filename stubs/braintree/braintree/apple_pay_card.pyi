from _typeshed import Incomplete

from braintree.resource import Resource as Resource
from braintree.subscription import Subscription

class ApplePayCard(Resource):
    class CardType:
        AmEx: str
        MasterCard: str
        Visa: str

    is_expired: Incomplete
    subscriptions: list[Subscription]
    def __init__(self, gateway, attributes) -> None: ...
    @property
    def expiration_date(self): ...
    @staticmethod
    def signature(): ...
