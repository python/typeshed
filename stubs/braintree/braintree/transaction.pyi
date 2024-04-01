from _typeshed import Incomplete
from decimal import Decimal

from braintree.add_on import AddOn as AddOn
from braintree.address import Address as Address
from braintree.amex_express_checkout_card import AmexExpressCheckoutCard as AmexExpressCheckoutCard
from braintree.android_pay_card import AndroidPayCard as AndroidPayCard
from braintree.apple_pay_card import ApplePayCard as ApplePayCard
from braintree.authorization_adjustment import AuthorizationAdjustment as AuthorizationAdjustment
from braintree.configuration import Configuration as Configuration
from braintree.credit_card import CreditCard as CreditCard
from braintree.customer import Customer as Customer
from braintree.descriptor import Descriptor as Descriptor
from braintree.disbursement_detail import DisbursementDetail as DisbursementDetail
from braintree.discount import Discount as Discount
from braintree.dispute import Dispute as Dispute
from braintree.error_result import ErrorResult as ErrorResult
from braintree.europe_bank_account import EuropeBankAccount as EuropeBankAccount
from braintree.exceptions.not_found_error import NotFoundError as NotFoundError
from braintree.facilitated_details import FacilitatedDetails as FacilitatedDetails
from braintree.facilitator_details import FacilitatorDetails as FacilitatorDetails
from braintree.local_payment import LocalPayment as LocalPayment
from braintree.masterpass_card import MasterpassCard as MasterpassCard
from braintree.meta_checkout_card import MetaCheckoutCard
from braintree.meta_checkout_token import MetaCheckoutToken
from braintree.package_details import PackageDetails
from braintree.payment_instrument_type import PaymentInstrumentType as PaymentInstrumentType
from braintree.paypal_account import PayPalAccount as PayPalAccount
from braintree.paypal_here import PayPalHere as PayPalHere
from braintree.resource import Resource as Resource
from braintree.resource_collection import ResourceCollection as ResourceCollection
from braintree.risk_data import RiskData as RiskData
from braintree.samsung_pay_card import SamsungPayCard as SamsungPayCard
from braintree.sepa_direct_debit_account import SepaDirectDebitAccount
from braintree.status_event import StatusEvent as StatusEvent
from braintree.subscription_details import SubscriptionDetails as SubscriptionDetails
from braintree.successful_result import SuccessfulResult as SuccessfulResult
from braintree.three_d_secure_info import ThreeDSecureInfo as ThreeDSecureInfo
from braintree.transaction_line_item import TransactionLineItem as TransactionLineItem
from braintree.us_bank_account import UsBankAccount as UsBankAccount
from braintree.venmo_account import VenmoAccount as VenmoAccount
from braintree.visa_checkout_card import VisaCheckoutCard as VisaCheckoutCard

class Transaction(Resource):
    class CreatedUsing:
        FullInformation: str
        Token: str

    class GatewayRejectionReason:
        ApplicationIncomplete: str
        Avs: str
        AvsAndCvv: str
        Cvv: str
        Duplicate: str
        ExcessiveRetry: str
        Fraud: str
        RiskThreshold: str
        ThreeDSecure: str
        TokenIssuance: str

    class ReasonCode:
        ANY_REASON_CODE: str

    class Source:
        Api: str
        ControlPanel: str
        Recurring: str

    class EscrowStatus:
        HoldPending: str
        Held: str
        ReleasePending: str
        Released: str
        Refunded: str

    class Status:
        AuthorizationExpired: str
        Authorized: str
        Authorizing: str
        Failed: str
        GatewayRejected: str
        ProcessorDeclined: str
        Settled: str
        SettlementConfirmed: str
        SettlementDeclined: str
        SettlementFailed: str
        SettlementPending: str
        Settling: str
        SubmittedForSettlement: str
        Voided: str

    class Type:
        Credit: str
        Sale: str

    class IndustryType:
        Lodging: str
        TravelAndCruise: str
        TravelAndFlight: str

    class AdditionalCharge:
        Restaurant: str
        GiftShop: str
        MiniBar: str
        Telephone: str
        Laundry: str
        Other: str

    @staticmethod
    def adjust_authorization(transaction_id, amount): ...
    @staticmethod
    def clone_transaction(transaction_id, params): ...
    @staticmethod
    def cancel_release(transaction_id): ...
    @staticmethod
    def credit(params: Incomplete | None = None): ...
    @staticmethod
    def find(transaction_id): ...
    @staticmethod
    def hold_in_escrow(transaction_id): ...
    @staticmethod
    def refund(transaction_id, amount_or_options: Incomplete | None = None): ...
    @staticmethod
    def sale(params: Incomplete | None = None): ...
    @staticmethod
    def search(*query): ...
    @staticmethod
    def release_from_escrow(transaction_id): ...
    @staticmethod
    def submit_for_settlement(transaction_id, amount: Incomplete | None = None, params: Incomplete | None = None): ...
    @staticmethod
    def update_details(transaction_id, params: Incomplete | None = None): ...
    @staticmethod
    def void(transaction_id): ...
    @staticmethod
    def create(params): ...
    @staticmethod
    def clone_signature(): ...
    @staticmethod
    def create_signature(): ...
    @staticmethod
    def submit_for_settlement_signature(): ...
    @staticmethod
    def package_tracking_signature(): ...
    @staticmethod
    def package_tracking(transaction_id, params: Incomplete | None = None): ...
    @staticmethod
    def update_details_signature(): ...
    @staticmethod
    def refund_signature(): ...
    @staticmethod
    def submit_for_partial_settlement(transaction_id, amount, params: Incomplete | None = None): ...
    amount: Decimal
    tax_amount: Decimal | None
    discount_amount: Decimal | None
    shipping_amount: Decimal | None
    billing_details: Address
    credit_card_details: CreditCard
    packages: list[PackageDetails]
    paypal_details: PayPalAccount
    paypal_here_details: PayPalHere
    local_payment_details: LocalPayment
    sepa_direct_debit_account_details: SepaDirectDebitAccount
    europe_bank_account_details: EuropeBankAccount
    us_bank_account: UsBankAccount
    apple_pay_details: ApplePayCard
    android_pay_card_details: AndroidPayCard
    amex_express_checkout_card_details: AmexExpressCheckoutCard
    venmo_account_details: VenmoAccount
    visa_checkout_card_details: VisaCheckoutCard
    masterpass_card_details: MasterpassCard
    samsung_pay_card_details: SamsungPayCard
    meta_checkout_card_details: MetaCheckoutCard
    meta_checkout_token_details: MetaCheckoutToken
    sca_exemption_requested: Incomplete
    customer_details: Customer
    shipping_details: Address
    add_ons: list[AddOn]
    discounts: list[Discount]
    status_history: list[StatusEvent]
    subscription_details: SubscriptionDetails
    descriptor: Descriptor
    disbursement_details: DisbursementDetail
    disputes: list[Dispute]
    authorization_adjustments: list[AuthorizationAdjustment]
    payment_instrument_type: Incomplete
    risk_data: RiskData | None
    three_d_secure_info: ThreeDSecureInfo | None
    facilitated_details: FacilitatedDetails
    facilitator_details: FacilitatorDetails
    network_transaction_id: Incomplete
    def __init__(self, gateway, attributes) -> None: ...
    @property
    def vault_billing_address(self): ...
    @property
    def vault_credit_card(self): ...
    @property
    def vault_customer(self): ...
    @property
    def is_disbursed(self): ...
    @property
    def line_items(self): ...
