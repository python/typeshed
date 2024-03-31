from typing import Any, Final

from braintree.resource import Resource as Resource

class ApplePayCard(Resource):
    class CardType:
        AmEx: Final = "Apple Pay - American Express"
        MasterCard: Final = "Apple Pay - MasterCard"
        Visa: Final = "Apple Pay - Visa"

    is_expired: Any
    subscriptions: Any
    def __init__(self, gateway, attributes) -> None: ...
    @property
    def expiration_date(self): ...
    @staticmethod
    def signature(): ...
