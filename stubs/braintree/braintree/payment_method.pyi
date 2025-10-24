from _typeshed import Incomplete

from braintree.android_pay_card import AndroidPayCard
from braintree.apple_pay_card import ApplePayCard
from braintree.credit_card import CreditCard
from braintree.error_result import ErrorResult
from braintree.paypal_account import PayPalAccount
from braintree.resource import Resource
from braintree.successful_result import SuccessfulResult
from braintree.us_bank_account import UsBankAccount
from braintree.venmo_account import VenmoAccount
from braintree.visa_checkout_card import VisaCheckoutCard

class PaymentMethod(Resource):
    @staticmethod
    def create(params: dict[str, Incomplete] | None = None) -> SuccessfulResult | ErrorResult: ...
    @staticmethod
    def find(
        payment_method_token: str,
    ) -> AndroidPayCard | ApplePayCard | CreditCard | PayPalAccount | UsBankAccount | VenmoAccount | VisaCheckoutCard: ...
    @staticmethod
    def update(payment_method_token: str, params) -> SuccessfulResult | ErrorResult: ...
    @staticmethod
    def delete(payment_method_token: str, options=None) -> SuccessfulResult: ...
    @staticmethod
    def create_signature() -> (
        list[
            str
            | dict[str, list[str | dict[str, list[str]]]]
            | dict[str, list[str | dict[str, list[str]] | dict[str, list[str | dict[str, list[str | dict[str, list[str]]]]]]]]
            | dict[str, list[str]]
        ]
    ): ...
    @staticmethod
    def signature(
        type: str,
    ) -> list[
        str
        | dict[str, list[str | dict[str, list[str]]]]
        | dict[str, list[str | dict[str, list[str]] | dict[str, list[str | dict[str, list[str | dict[str, list[str]]]]]]]]
        | dict[str, list[str]]
    ]: ...
    @staticmethod
    def update_signature() -> list[str | dict[str, list[str | dict[str, list[str]]]] | dict[str, list[str]]]: ...
    @staticmethod
    def delete_signature() -> list[str]: ...
