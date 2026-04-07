from google.auth._default import (
    default as default,
    load_credentials_from_dict as load_credentials_from_dict,
    load_credentials_from_file as load_credentials_from_file,
)

__all__ = ["default", "load_credentials_from_file", "load_credentials_from_dict"]

class Python37DeprecationWarning(DeprecationWarning): ...
