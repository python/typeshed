from hvac.api.vault_api_base import VaultApiBase

class Cert(VaultApiBase):
    def create_ca_certificate_role(
        self,
        name,
        certificate: str = ...,
        certificate_file: str = ...,
        allowed_common_names: str = ...,
        allowed_dns_sans: str = ...,
        allowed_email_sans: str = ...,
        allowed_uri_sans: str = ...,
        allowed_organizational_units: str = ...,
        required_extensions: str = ...,
        display_name: str = ...,
        token_ttl: int = ...,
        token_max_ttl: int = ...,
        token_policies=[],
        token_bound_cidrs=[],
        token_explicit_max_ttl: int = ...,
        token_no_default_policy: bool = ...,
        token_num_uses: int = ...,
        token_period: int = ...,
        token_type: str = ...,
        mount_point: str = ...,
    ): ...
    def read_ca_certificate_role(self, name, mount_point: str = ...): ...
    def list_certificate_roles(self, mount_point: str = ...): ...
    def delete_certificate_role(self, name, mount_point: str = ...): ...
    def configure_tls_certificate(self, mount_point: str = ...): ...
    def login(
        self,
        name: str = ...,
        cacert: bool = ...,
        cert_pem: str = ...,
        key_pem: str = ...,
        mount_point: str = ...,
        use_token: bool = ...,
    ): ...

    class CertificateAuthError(Exception): ...
