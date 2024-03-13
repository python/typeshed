from _typeshed import Incomplete

from hvac.api.vault_api_base import VaultApiBase

DEFAULT_MOUNT_POINT: str

class Transit(VaultApiBase):
    def create_key(
        self,
        name,
        convergent_encryption: Incomplete | None = ...,
        derived: Incomplete | None = ...,
        exportable: Incomplete | None = ...,
        allow_plaintext_backup: Incomplete | None = ...,
        key_type: Incomplete | None = ...,
        mount_point=...,
        auto_rotate_period: Incomplete | None = ...,
    ): ...
    def read_key(self, name, mount_point=...): ...
    def list_keys(self, mount_point=...): ...
    def delete_key(self, name, mount_point=...): ...
    def update_key_configuration(
        self,
        name,
        min_decryption_version: Incomplete | None = ...,
        min_encryption_version: Incomplete | None = ...,
        deletion_allowed: Incomplete | None = ...,
        exportable: Incomplete | None = ...,
        allow_plaintext_backup: Incomplete | None = ...,
        mount_point=...,
        auto_rotate_period: Incomplete | None = ...,
    ): ...
    def rotate_key(self, name, mount_point=...): ...
    def export_key(self, name, key_type, version: Incomplete | None = ..., mount_point=...): ...
    def encrypt_data(
        self,
        name,
        plaintext: Incomplete | None = ...,
        context: Incomplete | None = ...,
        key_version: Incomplete | None = ...,
        nonce: Incomplete | None = ...,
        batch_input: Incomplete | None = ...,
        type: Incomplete | None = ...,
        convergent_encryption: Incomplete | None = ...,
        mount_point=...,
    ): ...
    def decrypt_data(
        self,
        name,
        ciphertext: Incomplete | None = ...,
        context: Incomplete | None = ...,
        nonce: Incomplete | None = ...,
        batch_input: Incomplete | None = ...,
        mount_point=...,
    ): ...
    def rewrap_data(
        self,
        name,
        ciphertext,
        context: Incomplete | None = ...,
        key_version: Incomplete | None = ...,
        nonce: Incomplete | None = ...,
        batch_input: Incomplete | None = ...,
        mount_point=...,
    ): ...
    def generate_data_key(
        self,
        name,
        key_type,
        context: Incomplete | None = ...,
        nonce: Incomplete | None = ...,
        bits: Incomplete | None = ...,
        mount_point=...,
    ): ...
    def generate_random_bytes(
        self, n_bytes: Incomplete | None = ..., output_format: Incomplete | None = ..., mount_point=...
    ): ...
    def hash_data(
        self, hash_input, algorithm: Incomplete | None = ..., output_format: Incomplete | None = ..., mount_point=...
    ): ...
    def generate_hmac(
        self, name, hash_input, key_version: Incomplete | None = ..., algorithm: Incomplete | None = ..., mount_point=...
    ): ...
    def sign_data(
        self,
        name,
        hash_input: Incomplete | None = ...,
        key_version: Incomplete | None = ...,
        hash_algorithm: Incomplete | None = ...,
        context: Incomplete | None = ...,
        prehashed: Incomplete | None = ...,
        signature_algorithm: Incomplete | None = ...,
        marshaling_algorithm: Incomplete | None = ...,
        salt_length: Incomplete | None = ...,
        mount_point=...,
        batch_input: Incomplete | None = ...,
    ): ...
    def verify_signed_data(
        self,
        name,
        hash_input,
        signature: Incomplete | None = ...,
        hmac: Incomplete | None = ...,
        hash_algorithm: Incomplete | None = ...,
        context: Incomplete | None = ...,
        prehashed: Incomplete | None = ...,
        signature_algorithm: Incomplete | None = ...,
        salt_length: Incomplete | None = ...,
        marshaling_algorithm: Incomplete | None = ...,
        mount_point=...,
    ): ...
    def backup_key(self, name, mount_point=...): ...
    def restore_key(self, backup, name: Incomplete | None = ..., force: Incomplete | None = ..., mount_point=...): ...
    def trim_key(self, name, min_version, mount_point=...): ...
