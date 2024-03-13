from _typeshed import Incomplete

from hvac.api.vault_api_base import VaultApiBase

DEFAULT_MOUNT_POINT: str

class Ssh(VaultApiBase):
    def create_or_update_key(self, name: str = ...): ...
    def delete_key(self, name: str = ...): ...
    def create_role(
        self,
        name: str = ...,
        key: str = ...,
        admin_user: str = ...,
        default_user: str = ...,
        cidr_list: str = ...,
        exclude_cidr_list: str = ...,
        port: int = ...,
        key_type: str = ...,
        key_bits: int = ...,
        install_script: str = ...,
        allowed_users: str = ...,
        allowed_users_template: str = ...,
        allowed_domains: str = ...,
        key_option_specs: str = ...,
        ttl: str = ...,
        max_ttl: str = ...,
        allowed_critical_options: str = ...,
        allowed_extensions: str = ...,
        default_critical_options: Incomplete | None = ...,
        default_extensions: Incomplete | None = ...,
        allow_user_certificates: str = ...,
        allow_host_certificates: bool = ...,
        allow_bare_domains: bool = ...,
        allow_subdomains: bool = ...,
        allow_user_key_ids: bool = ...,
        key_id_format: str = ...,
        allowed_user_key_lengths: Incomplete | None = ...,
        algorithm_signer: str = ...,
        mount_point=...,
    ): ...
    def read_role(self, name: str = ...): ...
    def list_roles(self, mount_point=...): ...
    def delete_role(self, name: str = ...): ...
    def list_zeroaddress_roles(self, mount_point=...): ...
    def configure_zeroaddress_roles(self, roles: str = ...): ...
    def delete_zeroaddress_role(self, mount_point=...): ...
    def generate_ssh_credentials(self, name: str = ...): ...
    def list_roles_by_ip(self, ip: str = ...): ...
    def verify_ssh_otp(self, otp, mount_point=...): ...
    def submit_ca_information(
        self,
        private_key: str = ...,
        public_key: str = ...,
        generate_signing_key: bool = ...,
        key_type: str = ...,
        key_bits: int = ...,
        mount_point=...,
    ): ...
    def delete_ca_information(self, mount_point=...): ...
    def read_public_key(self, mount_point=...): ...
    def sign_ssh_key(
        self,
        name: str = ...,
        public_key: str = ...,
        ttl: str = ...,
        valid_principals: str = ...,
        cert_type: str = ...,
        key_id: str = ...,
        critical_options: Incomplete | None = ...,
        extensions: Incomplete | None = ...,
        mount_point=...,
    ): ...
