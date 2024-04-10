from _typeshed import Incomplete

class DescriptorPool:
    def __new__(cls, descriptor_db: Incomplete | None = None): ...
    def __init__(  # pyright: ignore[reportInconsistentConstructor]
        self, descriptor_db: Incomplete | None = None, use_deprecated_legacy_json_field_conflicts: bool = False
    ) -> None: ...
    def Add(self, file_desc_proto): ...
    def AddSerializedFile(self, serialized_file_desc_proto): ...
    def AddDescriptor(self, desc): ...
    def AddServiceDescriptor(self, service_desc): ...
    def AddExtensionDescriptor(self, extension): ...
    def AddFileDescriptor(self, file_desc): ...
    def FindFileByName(self, file_name): ...
    def FindFileContainingSymbol(self, symbol): ...
    def FindMessageTypeByName(self, full_name): ...
    def FindEnumTypeByName(self, full_name): ...
    def FindFieldByName(self, full_name): ...
    def FindOneofByName(self, full_name): ...
    def FindExtensionByName(self, full_name): ...
    def FindExtensionByNumber(self, message_descriptor, number): ...
    def FindAllExtensions(self, message_descriptor): ...
    def FindServiceByName(self, full_name): ...
    def FindMethodByName(self, full_name): ...

def Default(): ...
