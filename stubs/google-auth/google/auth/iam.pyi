import google
import google.auth
import google.auth.transport
from google.auth import credentials
from google.auth.crypt import base

IAM_RETRY_CODES: set[int]

class Signer(base.Signer):
    def __init__(
        self, request: google.auth.transport.Request, credentials: credentials.Credentials, service_account_email: str
    ) -> None: ...
    @property
    def key_id(self) -> str: ...
    def sign(self, message: str | bytes) -> bytes: ...
