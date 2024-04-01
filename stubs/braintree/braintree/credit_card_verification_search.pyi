from braintree.credit_card import CreditCard as CreditCard
from braintree.credit_card_verification import CreditCardVerification as CreditCardVerification
from braintree.search import Search as Search
from braintree.util import Constants as Constants

class CreditCardVerificationSearch:
    credit_card_cardholder_name: Search.TextNodeBuilder
    id: Search.TextNodeBuilder
    credit_card_expiration_date: Search.EqualityNodeBuilder
    credit_card_number: Search.PartialMatchNodeBuilder
    credit_card_card_type: Search.MultipleValueNodeBuilder
    ids: Search.MultipleValueNodeBuilder
    created_at: Search.RangeNodeBuilder
    status: Search.MultipleValueNodeBuilder
    billing_postal_code: Search.TextNodeBuilder
    customer_email: Search.TextNodeBuilder
    customer_id: Search.TextNodeBuilder
    payment_method_token: Search.TextNodeBuilder
