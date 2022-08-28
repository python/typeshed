from typing import Any, ClassVar, Iterator, List, overload
from typing_extensions import Annotated

import lief
import lief.ELF

class Binary(lief.ELF.Binary):
    class it_classes:
        def __init__(self, *args, **kwargs) -> None: ...
        def __getitem__(self, index) -> Any: ...
        def __iter__(self) -> Iterator: ...
        def __len__(self) -> int: ...
        def __next__(self) -> Any: ...
    class it_dex_files:
        def __init__(self, *args, **kwargs) -> None: ...
        def __getitem__(self, index) -> Any: ...
        def __iter__(self) -> Iterator: ...
        def __len__(self) -> int: ...
        def __next__(self) -> Any: ...
    class it_methods:
        def __init__(self, *args, **kwargs) -> None: ...
        def __getitem__(self, index) -> Any: ...
        def __iter__(self) -> Iterator: ...
        def __len__(self) -> int: ...
        def __next__(self) -> Any: ...
    class it_oat_dex_files:
        def __init__(self, *args, **kwargs) -> None: ...
        def __getitem__(self, index) -> Any: ...
        def __iter__(self) -> Iterator: ...
        def __len__(self) -> int: ...
        def __next__(self) -> Any: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def get_class(self, *args, **kwargs) -> Any: ...
    def __eq__(self, arg0: Binary) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, arg0: Binary) -> bool: ...
    @property
    def classes(self) -> Binary.it_classes: ...
    @property
    def dex2dex_json_info(self) -> str: ...
    @property
    def dex_files(self) -> Binary.it_dex_files: ...
    @property
    def has_class(self) -> bool: ...
    @property
    def header(self) -> Any: ...
    @property
    def methods(self) -> Binary.it_methods: ...
    @property
    def oat_dex_files(self) -> Binary.it_oat_dex_files: ...

class Class(lief.Object):
    class it_methods:
        def __init__(self, *args, **kwargs) -> None: ...
        def __getitem__(self, index) -> Any: ...
        def __iter__(self) -> Iterator: ...
        def __len__(self) -> int: ...
        def __next__(self) -> Any: ...
    def __init__(self) -> None: ...
    def has_dex_class(self) -> bool: ...
    @overload
    def is_quickened(self, dex_method) -> bool: ...
    @overload
    def is_quickened(self, method_index: int) -> bool: ...
    @overload
    def method_offsets_index(self, arg0) -> int: ...
    @overload
    def method_offsets_index(self, arg0: int) -> int: ...
    def __eq__(self, arg0: Class) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, arg0: Class) -> bool: ...
    @property
    def bitmap(self) -> List[int]: ...
    @property
    def fullname(self) -> str: ...
    @property
    def index(self) -> int: ...
    @property
    def methods(self) -> Class.it_methods: ...
    @property
    def status(self) -> OAT_CLASS_STATUS: ...
    @property
    def type(self) -> OAT_CLASS_TYPES: ...

class DexFile(lief.Object):
    checksum: int
    dex_offset: int
    location: str
    def __init__(self) -> None: ...
    def __eq__(self, arg0: DexFile) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, arg0: DexFile) -> bool: ...
    @property
    def dex_file(self) -> Any: ...
    @property
    def has_dex_file(self) -> bool: ...

class HEADER_KEYS:
    __members__: ClassVar[dict] = ...  # read-only
    BOOT_CLASS_PATH: ClassVar[HEADER_KEYS] = ...
    CLASS_PATH: ClassVar[HEADER_KEYS] = ...
    COMPILER_FILTER: ClassVar[HEADER_KEYS] = ...
    CONCURRENT_COPYING: ClassVar[HEADER_KEYS] = ...
    DEBUGGABLE: ClassVar[HEADER_KEYS] = ...
    DEX2OAT_CMD_LINE: ClassVar[HEADER_KEYS] = ...
    DEX2OAT_HOST: ClassVar[HEADER_KEYS] = ...
    HAS_PATCH_INFO: ClassVar[HEADER_KEYS] = ...
    IMAGE_LOCATION: ClassVar[HEADER_KEYS] = ...
    NATIVE_DEBUGGABLE: ClassVar[HEADER_KEYS] = ...
    PIC: ClassVar[HEADER_KEYS] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class Header(lief.Object):
    class it_key_values_t:
        class value_type:
            value: str
            def __init__(self, *args, **kwargs) -> None: ...
            @property
            def key(self) -> HEADER_KEYS: ...
        def __init__(self, *args, **kwargs) -> None: ...
        def __getitem__(self, arg0: int) -> Header.it_key_values_t.value_type: ...
        def __iter__(self) -> Header.it_key_values_t: ...
        def __len__(self) -> int: ...
        def __next__(self) -> Header.it_key_values_t.value_type: ...
    def __init__(self) -> None: ...
    def get(self, key: HEADER_KEYS) -> str: ...
    def set(self, key: HEADER_KEYS, value: str) -> Header: ...
    def __eq__(self, arg0: Header) -> bool: ...
    def __getitem__(self, arg0: HEADER_KEYS) -> str: ...
    def __hash__(self) -> int: ...
    def __ne__(self, arg0: Header) -> bool: ...
    def __setitem__(self, arg0: HEADER_KEYS, arg1: str) -> Header: ...
    @property
    def checksum(self) -> int: ...
    @property
    def executable_offset(self) -> int: ...
    @property
    def i2c_code_bridge_offset(self) -> int: ...
    @property
    def i2i_bridge_offset(self) -> int: ...
    @property
    def image_file_location_oat_checksum(self) -> int: ...
    @property
    def image_file_location_oat_data_begin(self) -> int: ...
    @property
    def image_patch_delta(self) -> int: ...
    @property
    def instruction_set(self) -> INSTRUCTION_SETS: ...
    @property
    def jni_dlsym_lookup_offset(self) -> int: ...
    @property
    def key_value_size(self) -> int: ...
    @property
    def key_values(self) -> Header.it_key_values_t: ...
    @property
    def keys(self) -> List[HEADER_KEYS]: ...
    @property
    def magic(self) -> Annotated[bytearray, 4]: ...
    @property
    def nb_dex_files(self) -> int: ...
    @property
    def oat_dex_files_offset(self) -> int: ...
    @property
    def quick_generic_jni_trampoline_offset(self) -> int: ...
    @property
    def quick_imt_conflict_trampoline_offset(self) -> int: ...
    @property
    def quick_resolution_trampoline_offset(self) -> int: ...
    @property
    def quick_to_interpreter_bridge_offset(self) -> int: ...
    @property
    def values(self) -> List[str]: ...
    @property
    def version(self) -> int: ...

class INSTRUCTION_SETS:
    __members__: ClassVar[dict] = ...  # read-only
    ARM: ClassVar[INSTRUCTION_SETS] = ...
    ARM_64: ClassVar[INSTRUCTION_SETS] = ...
    MIPS: ClassVar[INSTRUCTION_SETS] = ...
    MIPS_64: ClassVar[INSTRUCTION_SETS] = ...
    NONE: ClassVar[INSTRUCTION_SETS] = ...
    THUMB2: ClassVar[INSTRUCTION_SETS] = ...
    X86: ClassVar[INSTRUCTION_SETS] = ...
    X86_64: ClassVar[INSTRUCTION_SETS] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class Method(lief.Object):
    quick_code: List[int]
    def __init__(self) -> None: ...
    def __eq__(self, arg0: Method) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, arg0: Method) -> bool: ...
    @property
    def dex_method(self) -> Any: ...
    @property
    def has_dex_method(self) -> bool: ...
    @property
    def is_compiled(self) -> bool: ...
    @property
    def is_dex2dex_optimized(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def oat_class(self) -> Class: ...

class OAT_CLASS_STATUS:
    __members__: ClassVar[dict] = ...  # read-only
    ERROR: ClassVar[OAT_CLASS_STATUS] = ...
    IDX: ClassVar[OAT_CLASS_STATUS] = ...
    INITIALIZED: ClassVar[OAT_CLASS_STATUS] = ...
    INITIALIZING: ClassVar[OAT_CLASS_STATUS] = ...
    LOADED: ClassVar[OAT_CLASS_STATUS] = ...
    NOTREADY: ClassVar[OAT_CLASS_STATUS] = ...
    RESOLVED: ClassVar[OAT_CLASS_STATUS] = ...
    RESOLVING: ClassVar[OAT_CLASS_STATUS] = ...
    RETIRED: ClassVar[OAT_CLASS_STATUS] = ...
    VERIFICATION_AT_RUNTIME: ClassVar[OAT_CLASS_STATUS] = ...
    VERIFIED: ClassVar[OAT_CLASS_STATUS] = ...
    VERIFYING: ClassVar[OAT_CLASS_STATUS] = ...
    VERIFYING_AT_RUNTIME: ClassVar[OAT_CLASS_STATUS] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class OAT_CLASS_TYPES:
    __members__: ClassVar[dict] = ...  # read-only
    ALL_COMPILED: ClassVar[OAT_CLASS_TYPES] = ...
    NONE_COMPILED: ClassVar[OAT_CLASS_TYPES] = ...
    SOME_COMPILED: ClassVar[OAT_CLASS_TYPES] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

def android_version(*args, **kwargs) -> Any: ...
@overload
def is_oat(binary: lief.ELF.Binary) -> bool: ...
@overload
def is_oat(path: str) -> bool: ...
@overload
def is_oat(raw: List[int]) -> bool: ...
def parse(*args, **kwargs) -> Any: ...
@overload
def version(binary: lief.ELF.Binary) -> int: ...
@overload
def version(file: str) -> int: ...
@overload
def version(raw: List[int]) -> int: ...
