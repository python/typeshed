from braintree.credit_card import CreditCard as CreditCard
from braintree.search import Search as Search
from braintree.transaction import Transaction as Transaction
from braintree.util import Constants as Constants

class TransactionSearch:
    billing_company: Search.TextNodeBuilder
    billing_country_name: Search.TextNodeBuilder
    billing_extended_address: Search.TextNodeBuilder
    billing_first_name: Search.TextNodeBuilder
    billing_last_name: Search.TextNodeBuilder
    billing_locality: Search.TextNodeBuilder
    billing_postal_code: Search.TextNodeBuilder
    billing_region: Search.TextNodeBuilder
    billing_street_address: Search.TextNodeBuilder
    credit_card_cardholder_name: Search.TextNodeBuilder
    currency: Search.TextNodeBuilder
    customer_company: Search.TextNodeBuilder
    customer_email: Search.TextNodeBuilder
    customer_fax: Search.TextNodeBuilder
    customer_first_name: Search.TextNodeBuilder
    customer_id: Search.TextNodeBuilder
    customer_last_name: Search.TextNodeBuilder
    customer_phone: Search.TextNodeBuilder
    customer_website: Search.TextNodeBuilder
    id: Search.TextNodeBuilder
    order_id: Search.TextNodeBuilder
    payment_method_token: Search.TextNodeBuilder
    processor_authorization_code: Search.TextNodeBuilder
    europe_bank_account_iban: Search.TextNodeBuilder
    settlement_batch_id: Search.TextNodeBuilder
    shipping_company: Search.TextNodeBuilder
    shipping_country_name: Search.TextNodeBuilder
    shipping_extended_address: Search.TextNodeBuilder
    shipping_first_name: Search.TextNodeBuilder
    shipping_last_name: Search.TextNodeBuilder
    shipping_locality: Search.TextNodeBuilder
    shipping_postal_code: Search.TextNodeBuilder
    shipping_region: Search.TextNodeBuilder
    shipping_street_address: Search.TextNodeBuilder
    paypal_payer_email: Search.TextNodeBuilder
    paypal_payment_id: Search.TextNodeBuilder
    paypal_authorization_id: Search.TextNodeBuilder
    sepa_debit_paypal_v2_order_id: Search.TextNodeBuilder
    credit_card_unique_identifier: Search.TextNodeBuilder
    store_id: Search.TextNodeBuilder
    credit_card_expiration_date: Search.EqualityNodeBuilder
    credit_card_number: Search.PartialMatchNodeBuilder
    user: Search.MultipleValueNodeBuilder
    ids: Search.MultipleValueNodeBuilder
    merchant_account_id: Search.MultipleValueNodeBuilder
    payment_instrument_type: Search.MultipleValueNodeBuilder
    store_ids: Search.MultipleValueNodeBuilder
    created_using: Search.MultipleValueNodeBuilder
    credit_card_card_type: Search.MultipleValueNodeBuilder
    credit_card_customer_location: Search.MultipleValueNodeBuilder
    debit_network: Search.MultipleValueNodeBuilder
    source: Search.MultipleValueNodeBuilder
    status: Search.MultipleValueNodeBuilder
    type: Search.MultipleValueNodeBuilder
    refund: Search.KeyValueNodeBuilder
    amount: Search.RangeNodeBuilder
    authorization_expired_at: Search.RangeNodeBuilder
    authorized_at: Search.RangeNodeBuilder
    created_at: Search.RangeNodeBuilder
    disbursement_date: Search.RangeNodeBuilder
    dispute_date: Search.RangeNodeBuilder
    failed_at: Search.RangeNodeBuilder
    gateway_rejected_at: Search.RangeNodeBuilder
    processor_declined_at: Search.RangeNodeBuilder
    settled_at: Search.RangeNodeBuilder
    submitted_for_settlement_at: Search.RangeNodeBuilder
    voided_at: Search.RangeNodeBuilder
    ach_return_responses_created_at: Search.RangeNodeBuilder
    reason_code: Search.MultipleValueNodeBuilder
