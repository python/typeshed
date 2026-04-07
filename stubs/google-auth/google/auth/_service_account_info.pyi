from collections.abc import Mapping, Sequence

from google.auth import crypt as _crypt

def from_dict(data: Mapping[str, str], require: Sequence[str] | None = None, use_rsa_signer: bool = True) -> _crypt.Signer: ...
def from_filename(
    filename: str, require: Sequence[str] | None = None, use_rsa_signer: bool = True
) -> tuple[Mapping[str, str], _crypt.Signer]: ...
