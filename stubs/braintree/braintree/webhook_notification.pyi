from _typeshed import Incomplete

from braintree.account_updater_daily_report import AccountUpdaterDailyReport as AccountUpdaterDailyReport
from braintree.configuration import Configuration as Configuration
from braintree.connected_merchant_paypal_status_changed import (
    ConnectedMerchantPayPalStatusChanged as ConnectedMerchantPayPalStatusChanged,
)
from braintree.connected_merchant_status_transitioned import (
    ConnectedMerchantStatusTransitioned as ConnectedMerchantStatusTransitioned,
)
from braintree.disbursement import Disbursement as Disbursement
from braintree.dispute import Dispute as Dispute
from braintree.error_result import ErrorResult as ErrorResult
from braintree.granted_payment_instrument_update import GrantedPaymentInstrumentUpdate as GrantedPaymentInstrumentUpdate
from braintree.local_payment_completed import LocalPaymentCompleted as LocalPaymentCompleted
from braintree.local_payment_expired import LocalPaymentExpired
from braintree.local_payment_funded import LocalPaymentFunded
from braintree.local_payment_reversed import LocalPaymentReversed as LocalPaymentReversed
from braintree.merchant_account import MerchantAccount as MerchantAccount
from braintree.oauth_access_revocation import OAuthAccessRevocation as OAuthAccessRevocation
from braintree.partner_merchant import PartnerMerchant as PartnerMerchant
from braintree.payment_method_customer_data_updated_metadata import PaymentMethodCustomerDataUpdatedMetadata
from braintree.resource import Resource as Resource
from braintree.revoked_payment_method_metadata import RevokedPaymentMethodMetadata as RevokedPaymentMethodMetadata
from braintree.subscription import Subscription as Subscription
from braintree.transaction import Transaction as Transaction
from braintree.transaction_review import TransactionReview
from braintree.validation_error_collection import ValidationErrorCollection as ValidationErrorCollection

class WebhookNotification(Resource):
    class Kind:
        AccountUpdaterDailyReport: str
        Check: str
        ConnectedMerchantPayPalStatusChanged: str
        ConnectedMerchantStatusTransitioned: str
        Disbursement: str
        DisbursementException: str
        DisputeAccepted: str
        DisputeAutoAccepted: str
        DisputeDisputed: str
        DisputeExpired: str
        DisputeLost: str
        DisputeOpened: str
        DisputeUnderReview: str
        DisputeWon: str
        GrantedPaymentMethodRevoked: str
        GrantorUpdatedGrantedPaymentMethod: str
        LocalPaymentCompleted: str
        LocalPaymentExpired: str
        LocalPaymentFunded: str
        LocalPaymentReversed: str
        OAuthAccessRevoked: str
        PartnerMerchantConnected: str
        PartnerMerchantDeclined: str
        PartnerMerchantDisconnected: str
        PaymentMethodCustomerDataUpdated: str
        PaymentMethodRevokedByCustomer: str
        RecipientUpdatedGrantedPaymentMethod: str
        SubMerchantAccountApproved: str
        SubMerchantAccountDeclined: str
        SubscriptionBillingSkipped: str
        SubscriptionCanceled: str
        SubscriptionChargedSuccessfully: str
        SubscriptionChargedUnsuccessfully: str
        SubscriptionExpired: str
        SubscriptionTrialEnded: str
        SubscriptionWentActive: str
        SubscriptionWentPastDue: str
        TransactionDisbursed: str
        TransactionReviewed: str
        TransactionSettled: str
        TransactionSettlementDeclined: str

    @staticmethod
    def parse(signature, payload): ...
    @staticmethod
    def verify(challenge): ...
    source_merchant_id: Incomplete
    subscription: Subscription
    merchant_account: MerchantAccount
    transaction: Transaction
    transaction_review: TransactionReview
    connected_merchant_status_transitioned: ConnectedMerchantStatusTransitioned
    connected_merchant_paypal_status_changed: ConnectedMerchantPayPalStatusChanged
    partner_merchant: PartnerMerchant
    oauth_access_revocation: OAuthAccessRevocation
    disbursement: Disbursement
    dispute: Dispute
    account_updater_daily_report: AccountUpdaterDailyReport
    granted_payment_instrument_update: GrantedPaymentInstrumentUpdate
    revoked_payment_method_metadata: RevokedPaymentMethodMetadata
    local_payment_completed: LocalPaymentCompleted
    local_payment_expired: LocalPaymentExpired
    local_payment_funded: LocalPaymentFunded
    local_payment_reversed: LocalPaymentReversed
    payment_method_customer_data_updated_metadata: PaymentMethodCustomerDataUpdatedMetadata
    errors: ValidationErrorCollection
    message: Incomplete
    def __init__(self, gateway, attributes) -> None: ...
