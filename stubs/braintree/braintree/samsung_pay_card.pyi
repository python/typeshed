from braintree.address import Address as Address
from braintree.resource import Resource as Resource
from braintree.subscription import Subscription

class SamsungPayCard(Resource):
    billing_address: Address | None
    subscriptions: list[Subscription]
    def __init__(self, gateway, attributes) -> None: ...
    @property
    def expiration_date(self): ...
    @property
    def masked_number(self): ...
