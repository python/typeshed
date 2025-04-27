from _typeshed import Incomplete
from collections.abc import Iterable, Mapping
from typing import ClassVar

from google.protobuf import descriptor, message
from google.protobuf.internal import containers

DESCRIPTOR: descriptor.FileDescriptor

class ServerReflectionRequest(message.Message):
    __slots__ = ("host", "file_by_filename", "file_containing_symbol", "file_containing_extension", "all_extension_numbers_of_type", "list_services")
    HOST_FIELD_NUMBER: ClassVar[int]
    FILE_BY_FILENAME_FIELD_NUMBER: ClassVar[int]
    FILE_CONTAINING_SYMBOL_FIELD_NUMBER: ClassVar[int]
    FILE_CONTAINING_EXTENSION_FIELD_NUMBER: ClassVar[int]
    ALL_EXTENSION_NUMBERS_OF_TYPE_FIELD_NUMBER: ClassVar[int]
    LIST_SERVICES_FIELD_NUMBER: ClassVar[int]
    host: str
    file_by_filename: str
    file_containing_symbol: str
    file_containing_extension: ExtensionRequest
    all_extension_numbers_of_type: str
    list_services: str
    def __init__(self, host: str | None = ..., file_by_filename: str | None = ..., file_containing_symbol: str | None = ..., file_containing_extension: ExtensionRequest | Mapping[Incomplete, Incomplete] | None = ..., all_extension_numbers_of_type: str | None = ..., list_services: str | None = ...) -> None: ...

class ExtensionRequest(message.Message):
    __slots__ = ("containing_type", "extension_number")
    CONTAINING_TYPE_FIELD_NUMBER: ClassVar[int]
    EXTENSION_NUMBER_FIELD_NUMBER: ClassVar[int]
    containing_type: str
    extension_number: int
    def __init__(self, containing_type: str | None = ..., extension_number: int | None = ...) -> None: ...

class ServerReflectionResponse(message.Message):
    __slots__ = ("valid_host", "original_request", "file_descriptor_response", "all_extension_numbers_response", "list_services_response", "error_response")
    VALID_HOST_FIELD_NUMBER: ClassVar[int]
    ORIGINAL_REQUEST_FIELD_NUMBER: ClassVar[int]
    FILE_DESCRIPTOR_RESPONSE_FIELD_NUMBER: ClassVar[int]
    ALL_EXTENSION_NUMBERS_RESPONSE_FIELD_NUMBER: ClassVar[int]
    LIST_SERVICES_RESPONSE_FIELD_NUMBER: ClassVar[int]
    ERROR_RESPONSE_FIELD_NUMBER: ClassVar[int]
    valid_host: str
    original_request: ServerReflectionRequest
    file_descriptor_response: FileDescriptorResponse
    all_extension_numbers_response: ExtensionNumberResponse
    list_services_response: ListServiceResponse
    error_response: ErrorResponse
    def __init__(self, valid_host: str | None = ..., original_request: ServerReflectionRequest | Mapping[Incomplete, Incomplete] | None = ..., file_descriptor_response: FileDescriptorResponse | Mapping[Incomplete, Incomplete] | None = ..., all_extension_numbers_response: ExtensionNumberResponse | Mapping[Incomplete, Incomplete] | None = ..., list_services_response: ListServiceResponse | Mapping[Incomplete, Incomplete] | None = ..., error_response: ErrorResponse | Mapping[Incomplete, Incomplete] | None = ...) -> None: ...

class FileDescriptorResponse(message.Message):
    __slots__ = ("file_descriptor_proto",)
    FILE_DESCRIPTOR_PROTO_FIELD_NUMBER: ClassVar[int]
    file_descriptor_proto: containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, file_descriptor_proto: Iterable[bytes] | None = ...) -> None: ...

class ExtensionNumberResponse(message.Message):
    __slots__ = ("base_type_name", "extension_number")
    BASE_TYPE_NAME_FIELD_NUMBER: ClassVar[int]
    EXTENSION_NUMBER_FIELD_NUMBER: ClassVar[int]
    base_type_name: str
    extension_number: containers.RepeatedScalarFieldContainer[int]
    def __init__(self, base_type_name: str | None = ..., extension_number: Iterable[int] | None = ...) -> None: ...

class ListServiceResponse(message.Message):
    __slots__ = ("service",)
    SERVICE_FIELD_NUMBER: ClassVar[int]
    service: containers.RepeatedCompositeFieldContainer[ServiceResponse]
    def __init__(self, service: Iterable[ServiceResponse | Mapping[Incomplete, Incomplete]] | None = ...) -> None: ...

class ServiceResponse(message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: ClassVar[int]
    name: str
    def __init__(self, name: str | None = ...) -> None: ...

class ErrorResponse(message.Message):
    __slots__ = ("error_code", "error_message")
    ERROR_CODE_FIELD_NUMBER: ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: ClassVar[int]
    error_code: int
    error_message: str
    def __init__(self, error_code: int | None = ..., error_message: str | None = ...) -> None: ...
