from datetime import datetime
from typing import Any, Callable, Iterable, Sequence, Text, Tuple, Union

from cryptography.hazmat.primitives.asymmetric.dsa import DSAPrivateKey, DSAPublicKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from cryptography.x509 import Certificate, CertificateRevocationList, CertificateSigningRequest

_Key = DSAPrivateKey | DSAPublicKey | RSAPrivateKey | RSAPublicKey

FILETYPE_PEM: int
FILETYPE_ASN1: int
FILETYPE_TEXT: int

TYPE_RSA: int
TYPE_DSA: int

class _EllipticCurve:
    def __init__(self, lib: Any | None, nid: int, name: str) -> None: ...

class Error(Exception): ...

class PKey:
    def __init__(self) -> None: ...
    def bits(self) -> int: ...
    def check(self) -> bool: ...
    @classmethod
    def from_cryptography_key(cls, crypto_key: _Key) -> PKey: ...
    def generate_key(self, type: int, bits: int) -> None: ...
    def to_cryptography_key(self) -> _Key: ...
    def type(self) -> int: ...

class X509Name:
    countryName: Text
    C: Text
    stateOrProvinceName: Text
    ST: Text
    localityName: Text
    L: Text
    organizationName: Text
    O: Text
    organizationalUnitName: Text
    OU: Text
    commonName: Text
    CN: Text
    emailAddress: Text
    def __init__(self, name: X509Name) -> None: ...
    def der(self) -> bytes: ...
    def get_components(self) -> list[tuple[bytes, bytes]]: ...
    def hash(self) -> int: ...

class X509:
    def __init__(self) -> None: ...
    def add_extensions(self, extensions: Iterable[X509Extension]) -> None: ...
    def digest(self, digest_name: bytes) -> bytes: ...
    @classmethod
    def from_cryptography(cls, crypto_cert: Certificate) -> X509: ...
    def get_extension(self, index: int) -> X509Extension: ...
    def get_extension_count(self) -> int: ...
    def get_issuer(self) -> X509Name: ...
    def get_notAfter(self) -> bytes | None: ...
    def get_notBefore(self) -> bytes | None: ...
    def get_pubkey(self) -> PKey: ...
    def get_serial_number(self) -> int: ...
    def get_signature_algorithm(self) -> bytes: ...
    def get_subject(self) -> X509Name: ...
    def get_version(self) -> int: ...
    def gmtime_adj_notAfter(self, amount: int) -> None: ...
    def gmtime_adj_notBefore(self, amount: int) -> None: ...
    def has_expired(self) -> bool: ...
    def set_issuer(self, issuer: X509Name) -> None: ...
    def set_notAfter(self, when: bytes) -> None: ...
    def set_notBefore(self, when: bytes) -> None: ...
    def set_pubkey(self, pkey: PKey) -> None: ...
    def set_serial_number(self, serial: int) -> None: ...
    def set_subject(self, subject: X509Name) -> None: ...
    def set_version(self, version: int) -> None: ...
    def sign(self, pkey: PKey, digest: Text | bytes) -> None: ...
    def subject_name_hash(self) -> bytes: ...
    def to_cryptography(self) -> Certificate: ...

class X509Req:
    def __init__(self) -> None: ...
    def add_extensions(self, extensions: Iterable[X509Extension]) -> None: ...
    @classmethod
    def from_cryptography(cls, crypto_req: CertificateSigningRequest) -> X509Req: ...
    def get_extensions(self) -> list[X509Extension]: ...
    def get_pubkey(self) -> PKey: ...
    def get_subject(self) -> X509Name: ...
    def get_version(self) -> int: ...
    def set_pubkey(self, pkey: PKey) -> None: ...
    def set_version(self, version: int) -> None: ...
    def sign(self, pkey: PKey, digest: Text | bytes) -> None: ...
    def to_cryptography(self) -> CertificateSigningRequest: ...
    def verify(self, pkey: PKey) -> bool: ...

class X509Extension:
    def __init__(
        self, type_name: bytes, critical: bool, value: bytes, subject: X509 | None = ..., issuer: X509 | None = ...
    ) -> None: ...
    def get_critical(self) -> bool: ...
    def get_data(self) -> bytes: ...
    def get_short_name(self) -> bytes: ...

class Revoked:
    def __init__(self) -> None: ...
    def all_reasons(self) -> list[bytes]: ...
    def get_reason(self) -> bytes | None: ...
    def get_rev_date(self) -> bytes: ...
    def get_serial(self) -> bytes: ...
    def set_reason(self, reason: bytes | None) -> None: ...
    def set_rev_date(self, when: bytes) -> None: ...
    def set_serial(self, hex_str: bytes) -> None: ...

class CRL:
    def __init__(self) -> None: ...
    def add_revoked(self, revoked: Revoked) -> None: ...
    def export(self, cert: X509, key: PKey, type: int = ..., days: int = ..., digest: bytes = ...) -> bytes: ...
    @classmethod
    def from_cryptography(cls, crypto_crl: CertificateRevocationList) -> CRL: ...
    def get_issuer(self) -> X509Name: ...
    def get_revoked(self) -> Tuple[Revoked, ...]: ...
    def set_lastUpdate(self, when: bytes) -> None: ...
    def set_nextUpdate(self, when: bytes) -> None: ...
    def set_version(self, version: int) -> None: ...
    def sign(self, issuer_cert: X509, issuer_key: PKey, digest: bytes) -> None: ...
    def to_cryptography(self) -> CertificateRevocationList: ...

class X509Store:
    def __init__(self) -> None: ...
    def add_cert(self, cert: X509) -> None: ...
    def add_crl(self, crl: CRL) -> None: ...
    def load_locations(self, cafile: Text | bytes, capath: Text | bytes | None = ...) -> None: ...
    def set_flags(self, flags: int) -> None: ...
    def set_time(self, vfy_time: datetime) -> None: ...

class X509StoreContext:
    def __init__(self, store: X509Store, certificate: X509, chain: Sequence[X509] | None = ...) -> None: ...
    def get_verified_chain(self) -> list[X509]: ...
    def set_store(self, store: X509Store) -> None: ...
    def verify_certificate(self) -> None: ...

class X509StoreContextError(Exception):
    certificate: X509
    def __init__(self, message: Text | bytes, certificate: X509) -> None: ...

class X509StoreFlags:
    CRL_CHECK: int
    CRL_CHECK_ALL: int
    IGNORE_CRITICAL: int
    X509_STRICT: int
    ALLOW_PROXY_CERTS: int
    POLICY_CHECK: int
    EXPLICIT_POLICY: int
    INHIBIT_MAP: int
    NOTIFY_POLICY: int
    CHECK_SS_SIGNATURE: int
    CB_ISSUER_CHECK: int

class PKCS7:
    def get_type_name(self) -> Text: ...
    def type_is_data(self) -> bool: ...
    def type_is_enveloped(self) -> bool: ...
    def type_is_signed(self) -> bool: ...
    def type_is_signedAndEnveloped(self) -> bool: ...

class PKCS12:
    def __init__(self) -> None: ...
    def export(self, passphrase: bytes | None = ..., iter: int = ..., maciter: int = ...) -> bytes: ...
    def get_ca_certificates(self) -> Tuple[X509, ...]: ...
    def get_certificate(self) -> X509: ...
    def get_friendlyname(self) -> bytes | None: ...
    def get_privatekey(self) -> PKey: ...
    def set_ca_certificates(self, cacerts: Iterable[X509] | None) -> None: ...
    def set_certificate(self, cert: X509) -> None: ...
    def set_friendlyname(self, name: bytes | None) -> None: ...
    def set_privatekey(self, pkey: PKey) -> None: ...

class NetscapeSPKI:
    def __init__(self) -> None: ...
    def b64_encode(self) -> bytes: ...
    def get_pubkey(self) -> PKey: ...
    def set_pubkey(self, pkey: PKey) -> None: ...
    def sign(self, pkey: PKey, digest: bytes) -> None: ...
    def verify(self, key: PKey) -> bool: ...

def get_elliptic_curves() -> set[_EllipticCurve]: ...
def get_elliptic_curve(name: Text) -> _EllipticCurve: ...
def dump_certificate(type: int, cert: X509) -> bytes: ...
def load_certificate(type: int, buffer: bytes) -> X509: ...
def dump_certificate_request(type: int, req: X509Req) -> bytes: ...
def load_certificate_request(type: int, buffer: bytes) -> X509Req: ...
def dump_privatekey(
    type: int, pkey: PKey, cipher: bytes | None = ..., passphrase: bytes | Callable[[], bytes] | None = ...
) -> bytes: ...
def load_privatekey(type: int, buffer: Text | bytes, passphrase: bytes | Callable[[], bytes] | None = ...) -> PKey: ...
def dump_publickey(type: int, pkey: PKey) -> bytes: ...
def load_publickey(type: int, buffer: Text | bytes) -> PKey: ...
def dump_crl(type: int, crl: CRL) -> bytes: ...
def load_crl(type: int, buffer: Text | bytes) -> CRL: ...
def load_pkcs7_data(type: int, buffer: Text | bytes) -> PKCS7: ...
def load_pkcs12(buffer: Text | bytes, passphrase: bytes | None = ...) -> PKCS12: ...
def sign(pkey: PKey, data: Text | bytes, digest: Text | bytes) -> bytes: ...
def verify(cert: X509, signature: bytes, data: Text | bytes, digest: Text | bytes) -> None: ...
