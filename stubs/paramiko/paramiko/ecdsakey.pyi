from typing import IO, Any, Callable, Sequence, Tuple, Type

from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurve, EllipticCurvePrivateKey, EllipticCurvePublicKey
from cryptography.hazmat.primitives.hashes import HashAlgorithm
from paramiko.message import Message
from paramiko.pkey import PKey

class _ECDSACurve:
    nist_name: str
    key_length: int
    key_format_identifier: str
    hash_object: Type[HashAlgorithm]
    curve_class: Type[EllipticCurve]
    def __init__(self, curve_class: Type[EllipticCurve], nist_name: str) -> None: ...

class _ECDSACurveSet:
    ecdsa_curves: Sequence[_ECDSACurve]
    def __init__(self, ecdsa_curves: Sequence[_ECDSACurve]) -> None: ...
    def get_key_format_identifier_list(self) -> list[str]: ...
    def get_by_curve_class(self, curve_class: Type[Any]) -> _ECDSACurve | None: ...
    def get_by_key_format_identifier(self, key_format_identifier: str) -> _ECDSACurve | None: ...
    def get_by_key_length(self, key_length: int) -> _ECDSACurve | None: ...

class ECDSAKey(PKey):
    verifying_key: EllipticCurvePublicKey
    signing_key: EllipticCurvePrivateKey
    public_blob: None
    ecdsa_curve: _ECDSACurve | None
    def __init__(
        self,
        msg: Message | None = ...,
        data: bytes | None = ...,
        filename: str | None = ...,
        password: str | None = ...,
        vals: tuple[EllipticCurvePrivateKey, EllipticCurvePublicKey] | None = ...,
        file_obj: IO[str] | None = ...,
        validate_point: bool = ...,
    ) -> None: ...
    @classmethod
    def supported_key_format_identifiers(cls: Any) -> list[str]: ...
    def asbytes(self) -> bytes: ...
    def __hash__(self) -> int: ...
    def get_name(self) -> str: ...
    def get_bits(self) -> int: ...
    def can_sign(self) -> bool: ...
    def sign_ssh_data(self, data: bytes) -> Message: ...
    def verify_ssh_sig(self, data: bytes, msg: Message) -> bool: ...
    def write_private_key_file(self, filename: str, password: str | None = ...) -> None: ...
    def write_private_key(self, file_obj: IO[str], password: str | None = ...) -> None: ...
    @classmethod
    def generate(
        cls, curve: EllipticCurve = ..., progress_func: Callable[..., Any] | None = ..., bits: int | None = ...
    ) -> ECDSAKey: ...
