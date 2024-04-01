from _typeshed import Incomplete
from enum import Enum

from braintree.address import Address as Address
from braintree.configuration import Configuration as Configuration
from braintree.credit_card_verification import CreditCardVerification as CreditCardVerification
from braintree.resource import Resource as Resource
from braintree.subscription import Subscription

class CreditCard(Resource):
    class CardType:
        AmEx: str
        CarteBlanche: str
        ChinaUnionPay: str
        DinersClubInternational: str
        Discover: str
        Electron: str
        Elo: str
        Hiper: str
        Hipercard: str
        JCB: str
        Laser: str
        UK_Maestro: str
        Maestro: str
        MasterCard: str
        Solo: str
        Switch: str
        Visa: str
        Unknown: str

    class CustomerLocation:
        International: str
        US: str

    class CardTypeIndicator:
        Yes: str
        No: str
        Unknown: str

    class DebitNetwork(Enum):
        Accel = "ACCEL"
        Maestro = "MAESTRO"
        Nyce = "NYCE"
        Pulse = "PULSE"
        Star = "STAR"
        Star_Access = "STAR_ACCESS"

    Commercial: type[CardTypeIndicator]
    DurbinRegulated: type[CardTypeIndicator]
    Debit: type[CardTypeIndicator]
    Healthcare: type[CardTypeIndicator]
    CountryOfIssuance: type[CardTypeIndicator]
    IssuingBank: type[CardTypeIndicator]
    Payroll: type[CardTypeIndicator]
    Prepaid: type[CardTypeIndicator]
    ProductId: type[CardTypeIndicator]
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
    is_expired = expired
    billing_address: Address | None
    subscriptions: list[Subscription]
    verification: CreditCardVerification
    def __init__(self, gateway, attributes): ...
    @property
    def expiration_date(self): ...
    @property
    def masked_number(self): ...
