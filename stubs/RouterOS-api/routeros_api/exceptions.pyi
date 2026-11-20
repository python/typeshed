class RouterOsApiError(Exception): ...  # undocumented
class RouterOsApiConnectionError(RouterOsApiError): ...  # undocumented
class FatalRouterOsApiError(RouterOsApiError): ...  # undocumented
class RouterOsApiParsingError(RouterOsApiError): ...  # undocumented

class RouterOsApiCommunicationError(RouterOsApiError):  # undocumented
    original_message: bytes
    # The message is text, or the exception a registered exception type replaces.
    def __init__(self, message: object, original_message: bytes) -> None: ...

class RouterOsApiFatalCommunicationError(RouterOsApiError): ...  # undocumented
class RouterOsApiConnectionClosedError(RouterOsApiConnectionError): ...  # undocumented
