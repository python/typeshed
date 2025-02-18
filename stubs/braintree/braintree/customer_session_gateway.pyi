from _typeshed import Incomplete

from braintree.error_result import ErrorResult as ErrorResult
from braintree.exceptions.unexpected_error import UnexpectedError as UnexpectedError
from braintree.graphql import (
    CreateCustomerSessionInput as CreateCustomerSessionInput,
    CustomerRecommendations as CustomerRecommendations,
    CustomerRecommendationsInput as CustomerRecommendationsInput,
    CustomerRecommendationsPayload as CustomerRecommendationsPayload,
    PaymentOptions as PaymentOptions,
    UpdateCustomerSessionInput as UpdateCustomerSessionInput,
)
from braintree.successful_result import SuccessfulResult as SuccessfulResult
from braintree.util.graphql_client import GraphQLClient as GraphQLClient

class CustomerSessionGateway:
    gateway: Incomplete
    graphql_client: Incomplete
    def __init__(self, gateway) -> None: ...
    def create_customer_session(self, customer_session_input: CreateCustomerSessionInput) -> SuccessfulResult | ErrorResult: ...
    def update_customer_session(
        self, update_customer_session_input: UpdateCustomerSessionInput
    ) -> SuccessfulResult | ErrorResult: ...
    def get_customer_recommendations(
        self, customer_recommendations_input: CustomerRecommendationsInput
    ) -> SuccessfulResult | ErrorResult: ...
