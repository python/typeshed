from typing import Any, Optional, Text, Union

from boto.exceptions import BotoServerError
from boto.gs.acl import CannedACLStrings as CannedGSACLStrings
from boto.pyami.config import Config
from boto.s3.acl import Acl, Policy
from boto.s3.acl import CannedACLStrings as CannedS3ACLStrings

HEADER_PREFIX_KEY = ...  # type: Text
METADATA_PREFIX_KEY = ...  # type: Text
AWS_HEADER_PREFIX = ...  # type: Text
GOOG_HEADER_PREFIX = ...  # type: Text
ACL_HEADER_KEY = ...  # type: Text
AUTH_HEADER_KEY = ...  # type: Text
COPY_SOURCE_HEADER_KEY = ...  # type: Text
COPY_SOURCE_VERSION_ID_HEADER_KEY = ...  # type: Text
COPY_SOURCE_RANGE_HEADER_KEY = ...  # type: Text
DELETE_MARKER_HEADER_KEY = ...  # type: Text
DATE_HEADER_KEY = ...  # type: Text
METADATA_DIRECTIVE_HEADER_KEY = ...  # type: Text
RESUMABLE_UPLOAD_HEADER_KEY = ...  # type: Text
SECURITY_TOKEN_HEADER_KEY = ...  # type: Text
STORAGE_CLASS_HEADER_KEY = ...  # type: Text
MFA_HEADER_KEY = ...  # type: Text
SERVER_SIDE_ENCRYPTION_KEY = ...  # type: Text
VERSION_ID_HEADER_KEY = ...  # type: Text
RESTORE_HEADER_KEY = ...  # type: Text
STORAGE_COPY_ERROR = ...  # type: Text
STORAGE_CREATE_ERROR = ...  # type: Text
STORAGE_DATA_ERROR = ...  # type: Text
STORAGE_PERMISSIONS_ERROR = ...  # type: Text
STORAGE_RESPONSE_ERROR = ...  # type: Text
NO_CREDENTIALS_PROVIDED = ...  # type: object

class ProfileNotFoundError(ValueError): ...

class Provider:
    CredentialMap = ...  # type: Dict[Text, Tuple[Text, Text, Text, Text]
    AclClassMap = ...  # type: Dict[Text, Union[Policy, Acl]]
    CannedAclsMap = ...  # type: Dict[Text, Union[CannedS3ACLStrings, CannedGSACLStrings]]
    HostKeyMap = ...  # type: Dict[Text, Text]
    ChunkedTransferSupport = ...  # type: Dict[Text, bool]
    MetadataServiceSupport = ...  # type: Dict[Text, bool]
    HeaderInfoMap = ...  # type: Dict[Text, Dict[Text, Optional[Text]]]
    ErrorMap = ...  # type: Dict[Text, BotoServerError]

    host = ...  # type: Optional[Text]
    port = ...  # type: Optional[int]
    host_header = ...  # type: Optional[Text]
    access_key = ...  # type: Text
    secret_key = ...  # type: Text
    security_token = ...  # type: Optional[Text]
    profile_name = ...  # type: Optional[Text]
    name = ...  # type: Text
    acl_class = ...  # type: Union[Policy, Acl]
    canned_acls = ...  # type: Union[CannedS3ACLStrings, CannedGSACLStrings]
    shared_credentials = ...  # type: Any

    def __init__(
        self,
        name: Text,
        access_key: Optional[Text] = ...,
        secret_key: Optional[Text] = ...,
        security_token: Optional[Text] = ...,
        profile_name: Optional[Text] = ...,
    ): ...
    def get_access_key(self): ...
    def set_access_key(self, value: Text): ...
    def get_secret_key(self): ...
    def set_secret_key(self, value: Text): ...
    def get_security_token(self): ...
    def set_security_token(self, value: Text): ...
    def get_credentials(
        self,
        access_key: Optional[Text] = ...,
        secret_key: Optional[Text] = ...,
        security_token: Optional[Text] = ...,
        profile_name: Optional[Text] = ...,
    ):...

    metadata_prefix = ...  # type: Text
    header_prefix = ...  # type: Text
    acl_header = ...  # type: Text
    auth_header = ...  # type: Text
    copy_source_header = ...  # type: Text
    copy_source_version_id = ...  # type: Text
    copy_source_range_header = ...  # type: Optional[Text]
    date_header = ...  # type: Text
    delete_marker = ...  # type: Text
    metadata_directive_header = ...  # type: Text
    security_token_header = ...  # type: Text
    resumable_upload_header = ...  # type: Optional[Text]
    server_side_encryption_header = ...  # type: Optional[Text]
    storage_class_header = ...  # type: Text
    version_id = ...  # type: Text
    mfa_header = ...  # type: Optional[Text]
    restore_header = ...  # type: Optional[Text]

    def configure_headers(self): ...

    storage_copy_error = ...  # type: BotoServerError
    storage_create_error = ...  # type: BotoServerError
    storage_data_error = ...  # type: BotoServerError
    storage_permissions_error = ...  # type: BotoServerError
    storage_response_error = ...  # type: BotoServerError

    def configure_errors(self): ...
    def get_provider_name(self) -> Text: ...
    def supports_chunked_transfer(self) -> bool: ...

def get_default() -> Provider: ...
