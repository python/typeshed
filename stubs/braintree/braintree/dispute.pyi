from typing import Any, Final

from braintree.attribute_getter import AttributeGetter as AttributeGetter
from braintree.configuration import Configuration as Configuration
from braintree.dispute_details import (
    DisputeEvidence as DisputeEvidence,
    DisputePayPalMessage as DisputePayPalMessage,
    DisputeStatusHistory as DisputeStatusHistory,
)
from braintree.transaction_details import TransactionDetails as TransactionDetails

class Dispute(AttributeGetter):
    class Status:
        Accepted: Final = "accepted"
        AutoAccepted: Final = "auto_accepted"
        Disputed: Final = "disputed"
        Expired: Final = "expired"
        Lost: Final = "lost"
        Open: Final = "open"
        UnderReview: Final = "under_review"
        Won: Final = "won"

    class Reason:
        CancelledRecurringTransaction: Final = "cancelled_recurring_transaction"
        CreditNotProcessed: Final = "credit_not_processed"
        Duplicate: Final = "duplicate"
        Fraud: Final = "fraud"
        General: Final = "general"
        InvalidAccount: Final = "invalid_account"
        NotRecognized: Final = "not_recognized"
        ProductNotReceived: Final = "product_not_received"
        ProductUnsatisfactory: Final = "product_unsatisfactory"
        Retrieval: Final = "retrieval"
        TransactionAmountDiffers: Final = "transaction_amount_differs"

    class Kind:
        Chargeback: Final = "chargeback"
        PreArbitration: Final = "pre_arbitration"
        Retrieval: Final = "retrieval"

    class ChargebackProtectionLevel:
        Effortless: Final = "effortless"
        Standard: Final = "standard"
        NotProtected: Final = "not_protected"

    class PreDisputeProgram:
        NONE: Final = "none"
        VisaRdr: Final = "visa_rdr"

    class ProtectionLevel:
        EffortlessCBP: Final = "Effortless Chargeback Protection tool"
        StandardCBP: Final = "Chargeback Protection tool"
        NoProtection: Final = "No Protection"

    @staticmethod
    def accept(id): ...
    @staticmethod
    def add_file_evidence(dispute_id, document_upload_id): ...
    @staticmethod
    def add_text_evidence(id, content_or_request): ...
    @staticmethod
    def finalize(id): ...
    @staticmethod
    def find(id): ...
    @staticmethod
    def remove_evidence(id, evidence_id): ...
    @staticmethod
    def search(*query): ...
    amount: Any
    amount_disputed: Any
    amount_won: Any
    transaction_details: Any
    transaction: Any
    evidence: Any
    paypal_messages: Any
    status_history: Any
    forwarded_comments: Any
    def __init__(self, attributes) -> None: ...
