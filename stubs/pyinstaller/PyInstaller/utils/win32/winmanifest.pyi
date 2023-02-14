from _typeshed import Incomplete

# Used by other types referenced in https://pyinstaller.org/en/stable/spec-files.html#spec-file-operation
class Manifest:
    filename: Incomplete
    optional: Incomplete
    manifestType: Incomplete
    manifestVersion: Incomplete
    noInheritable: Incomplete
    noInherit: Incomplete
    type: Incomplete
    name: Incomplete
    language: Incomplete
    processorArchitecture: Incomplete
    version: Incomplete
    publicKeyToken: Incomplete
    applyPublisherPolicy: Incomplete
    description: Incomplete
    requestedExecutionLevel: Incomplete
    uiAccess: Incomplete
    dependentAssemblies: Incomplete
    bindingRedirects: Incomplete
    files: Incomplete
    comInterfaceExternalProxyStubs: Incomplete
    def __init__(
        self,
        manifestType: str = ...,
        manifestVersion: Incomplete | None = ...,
        noInheritable: bool = ...,
        noInherit: bool = ...,
        type_: Incomplete | None = ...,
        name: Incomplete | None = ...,
        language: Incomplete | None = ...,
        processorArchitecture: Incomplete | None = ...,
        version: Incomplete | None = ...,
        publicKeyToken: Incomplete | None = ...,
        description: Incomplete | None = ...,
        requestedExecutionLevel: Incomplete | None = ...,
        uiAccess: Incomplete | None = ...,
        dependentAssemblies: Incomplete | None = ...,
        files: Incomplete | None = ...,
        comInterfaceExternalProxyStubs: Incomplete | None = ...,
    ) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def add_dependent_assembly(
        self,
        manifestVersion: Incomplete | None = ...,
        noInheritable: bool = ...,
        noInherit: bool = ...,
        type_: Incomplete | None = ...,
        name: Incomplete | None = ...,
        language: Incomplete | None = ...,
        processorArchitecture: Incomplete | None = ...,
        version: Incomplete | None = ...,
        publicKeyToken: Incomplete | None = ...,
        description: Incomplete | None = ...,
        requestedExecutionLevel: Incomplete | None = ...,
        uiAccess: Incomplete | None = ...,
        dependentAssemblies: Incomplete | None = ...,
        files: Incomplete | None = ...,
        comInterfaceExternalProxyStubs: Incomplete | None = ...,
    ) -> None: ...
    def add_file(
        self,
        name: str = ...,
        hashalg: str = ...,
        hash: str = ...,
        comClasses: Incomplete | None = ...,
        typelibs: Incomplete | None = ...,
        comInterfaceProxyStubs: Incomplete | None = ...,
        windowClasses: Incomplete | None = ...,
    ) -> None: ...
    @classmethod
    def get_winsxs_dir(cls): ...
    @classmethod
    def get_manifest_dir(cls): ...
    @classmethod
    def get_policy_dir(cls): ...
    def get_policy_redirect(self, language: Incomplete | None = ..., version: Incomplete | None = ...): ...
    def find_files(self, ignore_policies: bool = ...): ...
    def getid(self, language: Incomplete | None = ..., version: Incomplete | None = ...): ...
    def getlanguage(self, language: Incomplete | None = ..., windowsversion: Incomplete | None = ...): ...
    def getpolicyid(self, fuzzy: bool = ..., language: Incomplete | None = ..., windowsversion: Incomplete | None = ...): ...
    def load_dom(self, domtree, initialize: bool = ...) -> None: ...
    def parse(self, filename_or_file, initialize: bool = ...) -> None: ...
    def parse_string(self, xmlstr, initialize: bool = ...) -> None: ...
    def same_id(self, manifest, skip_version_check: bool = ...): ...
    def todom(self): ...
    def toprettyxml(self, indent: str = ..., newl=..., encoding: str = ...): ...
    def toxml(self, encoding: str = ...): ...
    def update_resources(self, dstpath, names: Incomplete | None = ..., languages: Incomplete | None = ...) -> None: ...
    def writeprettyxml(
        self, filename_or_file: Incomplete | None = ..., indent: str = ..., newl=..., encoding: str = ...
    ) -> None: ...
    def writexml(self, filename_or_file: Incomplete | None = ..., indent: str = ..., newl=..., encoding: str = ...) -> None: ...
