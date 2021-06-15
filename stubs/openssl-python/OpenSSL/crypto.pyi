import sys
from datetime import datetime
from typing import Callable, Iterable, List, Optional, Sequence, Set, Text, Tuple, Union

from cryptography.hazmat.primitives.asymmetric.dsa import DSAPrivateKey, DSAPublicKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from cryptography.x509 import Certificate, CertificateRevocationList, CertificateSigningRequest

FILETYPE_PEM: int
FILETYPE_ASN1: int
FILETYPE_TEXT: int
TYPE_RSA: int
TYPE_DSA: int

class Error(Exception): ...

_Key = Union[DSAPrivateKey, DSAPublicKey, RSAPrivateKey, RSAPublicKey]

class PKey:
    def __init__(self) -> None: ...
    def to_cryptography_key(self) -> _Key: ...
    @classmethod
    def from_cryptography_key(cls, crypto_key: _Key) -> PKey: ...
    def generate_key(self, type: int, bits: int) -> None: ...
    def check(self) -> bool: ...
    def type(self) -> int: ...
    def bits(self) -> int: ...

class _EllipticCurve:
    name: Text

def get_elliptic_curves() -> Set[_EllipticCurve]: ...
def get_elliptic_curve(name: _StrLike) -> _EllipticCurve: ...

if sys.version_info >= (3, 0):
    _BytesLike = bytes
    _StrLike = str
    _TextLike = Union[_BytesLike, _StrLike]
else:
    _BytesLike = str
    _StrLike = Union[str, unicode]
    _TextLike = _StrLike

class X509Name:
    def __init__(self, name: X509Name) -> None: ...
    countryName: _StrLike
    stateOrProvinceName: _StrLike
    localityName: _StrLike
    organizationName: _StrLike
    organizationalUnitName: _StrLike
    commonName: _StrLike
    emailAddress: _StrLike
    C: _StrLike
    ST: _StrLike
    L: _StrLike
    O: _StrLike
    OU: _StrLike
    CN: _StrLike
    def hash(self) -> int: ...
    def der(self) -> _BytesLike: ...
    def get_components(self) -> List[Tuple[str, str]]: ...

class X509Extension:
    def __init__(
        self, type_name: _BytesLike, critical: bool, value: _BytesLike, subject: Optional[X509] = ..., issuer: Optional[X509] = ...
    ) -> None: ...
    def get_critical(self) -> bool: ...
    def get_short_name(self) -> _BytesLike: ...
    def get_data(self) -> _BytesLike: ...

class X509Req:
    def __init__(self) -> None: ...
    def set_pubkey(self, pkey: PKey) -> None: ...
    def get_pubkey(self) -> PKey: ...
    def set_version(self, version: int) -> None: ...
    def get_version(self) -> int: ...
    def get_subject(self) -> X509Name: ...
    def add_extensions(self, extensions: Iterable[X509Extension]) -> None: ...
    def get_extensions(self) -> List[X509Extension]: ...
    def sign(self, pkey: PKey, digest: _TextLike) -> None: ...
    def verify(self, pkey: PKey) -> bool: ...
    @classmethod
    def from_cryptography(cls, crypto_req: CertificateSigningRequest) -> X509Req: ...
    def to_cryptography(self) -> CertificateSigningRequest: ...

class X509:
    def __init__(self) -> None: ...
    def set_version(self, version: int) -> None: ...
    def get_version(self) -> int: ...
    def get_pubkey(self) -> PKey: ...
    def set_pubkey(self, pkey: PKey) -> None: ...
    def sign(self, pkey: PKey, digest: _TextLike) -> None: ...
    def get_signature_algorithm(self) -> _BytesLike: ...
    def digest(self, digest_name: _BytesLike) -> _BytesLike: ...
    def subject_name_hash(self) -> _BytesLike: ...
    def set_serial_number(self, serial: int) -> None: ...
    def get_serial_number(self) -> int: ...
    def gmtime_adj_notAfter(self, amount: int) -> None: ...
    def gmtime_adj_notBefore(self, amount: int) -> None: ...
    def has_expired(self) -> bool: ...
    def get_notBefore(self) -> Optional[_BytesLike]: ...
    def set_notBefore(self, when: _BytesLike) -> None: ...
    def get_notAfter(self) -> Optional[_BytesLike]: ...
    def set_notAfter(self, when: _BytesLike) -> None: ...
    def get_issuer(self) -> X509Name: ...
    def set_issuer(self, issuer: X509Name) -> None: ...
    def get_subject(self) -> X509Name: ...
    def set_subject(self, subject: X509Name) -> None: ...
    def get_extension_count(self) -> int: ...
    def add_extensions(self, extensions: Iterable[X509Extension]) -> None: ...
    def get_extension(self, index: int) -> X509Extension: ...
    @classmethod
    def from_cryptography(cls, crypto_key: Certificate) -> X509: ...
    def to_cryptography(self) -> Certificate: ...

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

class X509Store:
    def __init__(self) -> None: ...
    def add_cert(self, cert: X509) -> None: ...
    def add_crl(self, crl: CRL) -> None: ...
    def set_flags(self, flags: int) -> None: ...
    def set_time(self, vfy_time: datetime) -> None: ...

class X509StoreContextError(Exception):
    certificate: X509
    def __init__(self, message: _TextLike, certificate: X509) -> None: ...

class X509StoreContext:
    def __init__(self, store: X509Store, certificate: X509, chain: Optional[Sequence[X509]]) -> None: ...
    def set_store(self, store: X509Store) -> None: ...
    def verify_certificate(self) -> None: ...

def load_certificate(type: int, buffer: _BytesLike) -> X509: ...
def dump_certificate(type: int, cert: X509) -> _BytesLike: ...
def dump_publickey(type: int, pkey: PKey) -> _BytesLike: ...
def dump_privatekey(
    type: int, pkey: PKey, cipher: Optional[_BytesLike] = ..., passphrase: Union[_BytesLike, Callable[[], _BytesLike], None] = ...
) -> _BytesLike: ...

class Revoked:
    def __init__(self) -> None: ...
    def set_serial(self, hex_str: _BytesLike) -> None: ...
    def get_serial(self) -> _BytesLike: ...
    def set_reason(self, reason: Optional[_BytesLike]) -> None: ...
    def get_reason(self) -> Optional[_BytesLike]: ...
    def all_reasons(self) -> List[_BytesLike]: ...
    def set_rev_date(self, when: _BytesLike) -> None: ...
    def get_rev_date(self) -> _BytesLike: ...

class CRL:
    def __init__(self) -> None: ...
    def get_revoked(self) -> Tuple[Revoked, ...]: ...
    def add_revoked(self, revoked: Revoked) -> None: ...
    def get_issuer(self) -> X509Name: ...
    def set_version(self, version: int) -> None: ...
    def set_lastUpdate(self, when: _BytesLike) -> None: ...
    def set_nextUpdate(self, when: _BytesLike) -> None: ...
    def sign(self, issuer_cert: X509, issuer_key: PKey, digest: _BytesLike) -> None: ...
    def export(self, cert: X509, key: PKey, type: int = ..., days: int = ..., digest: _BytesLike = ...) -> _BytesLike: ...
    @classmethod
    def from_cryptography(cls, crypto_crl: CertificateRevocationList) -> CRL: ...
    def to_cryptography(self) -> CertificateRevocationList: ...

class PKCS7:
    def type_is_signed(self) -> bool: ...
    def type_is_enveloped(self) -> bool: ...
    def type_is_signedAndEnveloped(self) -> bool: ...
    def type_is_data(self) -> bool: ...
    def get_type_name(self) -> _StrLike: ...

class PKCS12:
    def __init__(self) -> None: ...
    def get_certificate(self) -> X509: ...
    def set_certificate(self, cert: X509) -> None: ...
    def get_privatekey(self) -> PKey: ...
    def set_privatekey(self, pkey: PKey) -> None: ...
    def get_ca_certificates(self) -> Tuple[X509, ...]: ...
    def set_ca_certificates(self, cacerts: Optional[Iterable[X509]]) -> None: ...
    def set_friendlyname(self, name: Optional[_BytesLike]) -> None: ...
    def get_friendlyname(self) -> Optional[_BytesLike]: ...
    def export(self, passphrase: Optional[_BytesLike] = ..., iter: int = ..., maciter: int = ...) -> _BytesLike: ...

class NetscapeSPKI:
    def __init__(self) -> None: ...
    def sign(self, pkey: PKey, digest: _BytesLike) -> None: ...
    def verify(self, key: PKey) -> bool: ...
    def b64_encode(self) -> _BytesLike: ...
    def get_pubkey(self) -> PKey: ...
    def set_pubkey(self, pkey: PKey) -> None: ...

def load_publickey(type: int, buffer: _TextLike) -> PKey: ...
def load_privatekey(type: int, buffer: _TextLike, passphrase: Union[_BytesLike, Callable[[], _BytesLike], None] = ...) -> PKey: ...
def dump_certificate_request(type: int, cert: X509Req) -> _BytesLike: ...
def load_certificate_request(type: int, buffer: _BytesLike) -> X509Req: ...
def sign(pkey: PKey, data: _TextLike, digest: _TextLike) -> _BytesLike: ...
def verify(cert: X509, signature: _BytesLike, data: _TextLike, digest: _TextLike) -> None: ...
def dump_crl(type: int, crl: CRL) -> _BytesLike: ...
def load_crl(type: int, buffer: _TextLike) -> CRL: ...
def load_pkcs7_data(type: int, buffer: _TextLike) -> PKCS7: ...
def load_pkcs12(buffer: _TextLike, passphrase: Optional[_BytesLike] = ...) -> PKCS12: ...
