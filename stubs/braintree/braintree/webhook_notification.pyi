from typing import Any, Final

from braintree.configuration import Configuration as Configuration
from braintree.dispute import Dispute as Dispute
from braintree.error_result import ErrorResult as ErrorResult
from braintree.granted_payment_instrument_update import GrantedPaymentInstrumentUpdate as GrantedPaymentInstrumentUpdate
from braintree.merchant_account import MerchantAccount as MerchantAccount
from braintree.oauth_access_revocation import OAuthAccessRevocation as OAuthAccessRevocation
from braintree.partner_merchant import PartnerMerchant as PartnerMerchant
from braintree.resource import Resource as Resource
from braintree.revoked_payment_method_metadata import RevokedPaymentMethodMetadata as RevokedPaymentMethodMetadata
from braintree.subscription import Subscription as Subscription
from braintree.transaction import Transaction as Transaction
from braintree.validation_error_collection import ValidationErrorCollection as ValidationErrorCollection

class WebhookNotification(Resource):
    class Kind:
        AccountUpdaterDailyReport: Final = "account_updater_daily_report"
        Check: Final = "check"
        ConnectedMerchantPayPalStatusChanged: Final = "connected_merchant_paypal_status_changed"
        ConnectedMerchantStatusTransitioned: Final = "connected_merchant_status_transitioned"
        Disbursement: Final = "disbursement"
        DisbursementException: Final = "disbursement_exception"
        DisputeAccepted: Final = "dispute_accepted"
        DisputeAutoAccepted: Final = "dispute_auto_accepted"
        DisputeDisputed: Final = "dispute_disputed"
        DisputeExpired: Final = "dispute_expired"
        DisputeLost: Final = "dispute_lost"
        DisputeOpened: Final = "dispute_opened"
        DisputeUnderReview: Final = "dispute_under_review"
        DisputeWon: Final = "dispute_won"
        GrantedPaymentMethodRevoked: Final = "granted_payment_method_revoked"
        GrantorUpdatedGrantedPaymentMethod: Final = "grantor_updated_granted_payment_method"
        LocalPaymentCompleted: Final = "local_payment_completed"
        LocalPaymentExpired: Final = "local_payment_expired"
        LocalPaymentFunded: Final = "local_payment_funded"
        LocalPaymentReversed: Final = "local_payment_reversed"
        OAuthAccessRevoked: Final = "oauth_access_revoked"
        PartnerMerchantConnected: Final = "partner_merchant_connected"
        PartnerMerchantDeclined: Final = "partner_merchant_declined"
        PartnerMerchantDisconnected: Final = "partner_merchant_disconnected"
        PaymentMethodCustomerDataUpdated: Final = "payment_method_customer_data_updated"
        PaymentMethodRevokedByCustomer: Final = "payment_method_revoked_by_customer"
        RecipientUpdatedGrantedPaymentMethod: Final = "recipient_updated_granted_payment_method"
        SubMerchantAccountApproved: Final = "sub_merchant_account_approved"
        SubMerchantAccountDeclined: Final = "sub_merchant_account_declined"
        SubscriptionBillingSkipped: Final = "subscription_billing_skipped"
        SubscriptionCanceled: Final = "subscription_canceled"
        SubscriptionChargedSuccessfully: Final = "subscription_charged_successfully"
        SubscriptionChargedUnsuccessfully: Final = "subscription_charged_unsuccessfully"
        SubscriptionExpired: Final = "subscription_expired"
        SubscriptionTrialEnded: Final = "subscription_trial_ended"
        SubscriptionWentActive: Final = "subscription_went_active"
        SubscriptionWentPastDue: Final = "subscription_went_past_due"
        TransactionDisbursed: Final = "transaction_disbursed"
        TransactionReviewed: Final = "transaction_reviewed"
        TransactionSettled: Final = "transaction_settled"
        TransactionSettlementDeclined: Final = "transaction_settlement_declined"

    @staticmethod
    def parse(signature, payload): ...
    @staticmethod
    def verify(challenge): ...
    source_merchant_id: Any
    subscription: Any
    merchant_account: Any
    transaction: Any
    connected_merchant_status_transitioned: Any
    connected_merchant_paypal_status_changed: Any
    partner_merchant: Any
    oauth_access_revocation: Any
    disbursement: Any
    dispute: Any
    account_updater_daily_report: Any
    granted_payment_instrument_update: Any
    revoked_payment_method_metadata: Any
    local_payment_completed: Any
    local_payment_reversed: Any
    errors: Any
    message: Any
    def __init__(self, gateway, attributes) -> None: ...
