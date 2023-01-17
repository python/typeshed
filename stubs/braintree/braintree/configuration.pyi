from _typeshed import Incomplete
from typing import Any

from braintree.credentials_parser import CredentialsParser as CredentialsParser
from braintree.environment import Environment as Environment
from braintree.exceptions.configuration_error import ConfigurationError as ConfigurationError
from braintree.util.graphql_client import GraphQLClient as GraphQLClient

class Configuration:
    @staticmethod
    def configure(environment, merchant_id, public_key, private_key, **kwargs) -> None: ...
    @staticmethod
    def for_partner(environment, partner_id, public_key, private_key, **kwargs): ...
    @staticmethod
    def gateway(): ...
    @staticmethod
    def instantiate(): ...
    @staticmethod
    def api_version(): ...
    @staticmethod
    def graphql_api_version(): ...
    environment: Any
    merchant_id: Any
    public_key: Any
    private_key: Any
    client_id: Any
    client_secret: Any
    access_token: Any
    timeout: Any
    wrap_http_exceptions: Any
    def __init__(
        self,
        environment: Incomplete | None = ...,
        merchant_id: Incomplete | None = ...,
        public_key: Incomplete | None = ...,
        private_key: Incomplete | None = ...,
        client_id: Incomplete | None = ...,
        client_secret: Incomplete | None = ...,
        access_token: Incomplete | None = ...,
        *args,
        **kwargs,
    ) -> None: ...
    def base_merchant_path(self): ...
    def base_url(self): ...
    def graphql_base_url(self): ...
    def http(self): ...
    def graphql_client(self): ...
    def http_strategy(self): ...
    def has_client_credentials(self): ...
    def assert_has_client_credentials(self) -> None: ...
    def has_access_token(self): ...