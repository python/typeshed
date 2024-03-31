from _typeshed import Incomplete
from enum import Enum
from typing import Any, Final

from braintree.address import Address as Address
from braintree.configuration import Configuration as Configuration
from braintree.credit_card_verification import CreditCardVerification as CreditCardVerification
from braintree.resource import Resource as Resource

class CreditCard(Resource):
    class CardType:
        AmEx: Final = "American Express"
        CarteBlanche: Final = "Carte Blanche"
        ChinaUnionPay: Final = "China UnionPay"
        DinersClubInternational: Final = "Diners Club"
        Discover: Final = "Discover"
        Electron: Final = "Electron"
        Elo: Final = "Elo"
        Hiper: Final = "Hiper"
        Hipercard: Final = "Hipercard"
        JCB: Final = "JCB"
        Laser: Final = "Laser"
        UK_Maestro: Final = "UK Maestro"
        Maestro: Final = "Maestro"
        MasterCard: Final = "MasterCard"
        Solo: Final = "Solo"
        Switch: Final = "Switch"
        Visa: Final = "Visa"
        Unknown: Final = "Unknown"

    class CustomerLocation:
        International: Final = "international"
        US: Final = "us"

    class CardTypeIndicator:
        Yes: Final = "Yes"
        No: Final = "No"
        Unknown: Final = "Unknown"

    class DebitNetwork(Enum):
        Accel = "ACCEL"
        Maestro = "MAESTRO"
        Nyce = "NYCE"
        Pulse = "PULSE"
        Star = "STAR"
        Star_Access = "STAR_ACCESS"

    Commercial: Any
    DurbinRegulated: Any
    Debit: Any
    Healthcare: Any
    CountryOfIssuance: Any
    IssuingBank: Any
    Payroll: Any
    Prepaid: Any
    ProductId: Any
    @staticmethod
    def create(params: Incomplete | None = None): ...
    @staticmethod
    def update(credit_card_token, params: Incomplete | None = None): ...
    @staticmethod
    def delete(credit_card_token): ...
    @staticmethod
    def expired(): ...
    @staticmethod
    def expiring_between(start_date, end_date): ...
    @staticmethod
    def find(credit_card_token): ...
    @staticmethod
    def from_nonce(nonce): ...
    @staticmethod
    def create_signature(): ...
    @staticmethod
    def update_signature(): ...
    @staticmethod
    def signature(type): ...
    is_expired: Any
    billing_address: Any
    subscriptions: Any
    verification: Any
    def __init__(self, gateway, attributes): ...
    @property
    def expiration_date(self): ...
    @property
    def masked_number(self): ...
