from _typeshed import Incomplete

from braintree.address import Address as Address
from braintree.amex_express_checkout_card import AmexExpressCheckoutCard as AmexExpressCheckoutCard
from braintree.android_pay_card import AndroidPayCard as AndroidPayCard
from braintree.apple_pay_card import ApplePayCard as ApplePayCard
from braintree.configuration import Configuration as Configuration
from braintree.credit_card import CreditCard as CreditCard
from braintree.error_result import ErrorResult as ErrorResult
from braintree.europe_bank_account import EuropeBankAccount as EuropeBankAccount
from braintree.exceptions.not_found_error import NotFoundError as NotFoundError
from braintree.ids_search import IdsSearch as IdsSearch
from braintree.masterpass_card import MasterpassCard as MasterpassCard
from braintree.paypal_account import PayPalAccount as PayPalAccount
from braintree.resource import Resource as Resource
from braintree.resource_collection import ResourceCollection as ResourceCollection
from braintree.samsung_pay_card import SamsungPayCard as SamsungPayCard
from braintree.successful_result import SuccessfulResult as SuccessfulResult
from braintree.us_bank_account import UsBankAccount as UsBankAccount
from braintree.util.http import Http as Http
from braintree.venmo_account import VenmoAccount as VenmoAccount
from braintree.visa_checkout_card import VisaCheckoutCard as VisaCheckoutCard

class Customer(Resource):
    @staticmethod
    def all(): ...
    @staticmethod
    def create(params: Incomplete | None = None): ...
    @staticmethod
    def delete(customer_id): ...
    @staticmethod
    def find(customer_id, association_filter_id: Incomplete | None = None): ...
    @staticmethod
    def search(*query): ...
    @staticmethod
    def update(customer_id, params: Incomplete | None = None): ...
    @staticmethod
    def create_signature(): ...
    @staticmethod
    def update_signature(): ...
    payment_methods: list[
        CreditCard
        | Address
        | PayPalAccount
        | ApplePayCard
        | AndroidPayCard
        | AmexExpressCheckoutCard
        | EuropeBankAccount
        | VenmoAccount
        | UsBankAccount
        | VisaCheckoutCard
        | MasterpassCard
        | SamsungPayCard
    ]
    credit_cards: list[CreditCard]
    addresses: list[Address]
    paypal_accounts: list[PayPalAccount]
    apple_pay_cards: list[ApplePayCard]
    android_pay_cards: list[AndroidPayCard]
    amex_express_checkout_cards: list[AmexExpressCheckoutCard]
    europe_bank_accounts: list[EuropeBankAccount]
    venmo_accounts: list[VenmoAccount]
    us_bank_accounts: list[UsBankAccount]
    visa_checkout_cards: list[VisaCheckoutCard]
    masterpass_cards: list[MasterpassCard]
    samsung_pay_cards: list[SamsungPayCard]
    def __init__(self, gateway, attributes) -> None: ...
