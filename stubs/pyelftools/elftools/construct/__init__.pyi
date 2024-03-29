from _typeshed import Incomplete

from .adapters import *
from .core import *
from .debug import Debugger as Debugger, Probe as Probe
from .macros import *

__all__ = [
    "AdaptationError",
    "Adapter",
    "Alias",
    "Aligned",
    "AlignedStruct",
    "Anchor",
    "Array",
    "ArrayError",
    "BFloat32",
    "BFloat64",
    "Bit",
    "BitField",
    "BitIntegerAdapter",
    "BitIntegerError",
    "BitStruct",
    "Bits",
    "Bitwise",
    "Buffered",
    "Byte",
    "Bytes",
    "CString",
    "CStringAdapter",
    "Const",
    "ConstAdapter",
    "ConstError",
    "Construct",
    "ConstructError",
    "Container",
    "Debugger",
    "Embed",
    "Embedded",
    "EmbeddedBitStruct",
    "Enum",
    "ExprAdapter",
    "Field",
    "FieldError",
    "Flag",
    "FlagsAdapter",
    "FlagsContainer",
    "FlagsEnum",
    "FormatField",
    "GreedyRange",
    "GreedyRepeater",
    "HexDumpAdapter",
    "If",
    "IfThenElse",
    "IndexingAdapter",
    "LFloat32",
    "LFloat64",
    "LazyBound",
    "LengthValueAdapter",
    "ListContainer",
    "MappingAdapter",
    "MappingError",
    "MetaArray",
    "MetaBytes",
    "MetaField",
    "MetaRepeater",
    "NFloat32",
    "NFloat64",
    "Nibble",
    "NoneOf",
    "NoneOfValidator",
    "Octet",
    "OnDemand",
    "OnDemandPointer",
    "OneOf",
    "OneOfValidator",
    "OpenRange",
    "Optional",
    "OptionalGreedyRange",
    "OptionalGreedyRepeater",
    "PaddedStringAdapter",
    "Padding",
    "PaddingAdapter",
    "PaddingError",
    "PascalString",
    "Pass",
    "Peek",
    "Pointer",
    "PrefixedArray",
    "Probe",
    "Range",
    "RangeError",
    "Reconfig",
    "Rename",
    "RepeatUntil",
    "Repeater",
    "Restream",
    "SBInt16",
    "SBInt32",
    "SBInt64",
    "SBInt8",
    "SLInt16",
    "SLInt32",
    "SLInt64",
    "SLInt8",
    "SNInt16",
    "SNInt32",
    "SNInt64",
    "SNInt8",
    "Select",
    "SelectError",
    "Sequence",
    "SizeofError",
    "SlicingAdapter",
    "StaticField",
    "StrictRepeater",
    "String",
    "StringAdapter",
    "Struct",
    "Subconstruct",
    "Switch",
    "SwitchError",
    "SymmetricMapping",
    "Terminator",
    "TerminatorError",
    "Tunnel",
    "TunnelAdapter",
    "UBInt16",
    "UBInt32",
    "UBInt64",
    "UBInt8",
    "ULInt16",
    "ULInt32",
    "ULInt64",
    "ULInt8",
    "UNInt16",
    "UNInt32",
    "UNInt64",
    "UNInt8",
    "Union",
    "ValidationError",
    "Validator",
    "Value",
    "Magic",
]

Bits = BitField
Byte = UBInt8
Bytes = Field
Const = ConstAdapter
Tunnel = TunnelAdapter
Embed = Embedded
MetaBytes: Incomplete
GreedyRepeater: Incomplete
OptionalGreedyRepeater: Incomplete
Repeater: Incomplete
StrictRepeater: Incomplete
MetaRepeater: Incomplete
OneOfValidator: Incomplete
NoneOfValidator: Incomplete

# Names in __all__ with no definition:
#   AdaptationError
#   Adapter
#   Alias
#   Aligned
#   AlignedStruct
#   Anchor
#   Array
#   ArrayError
#   BFloat32
#   BFloat64
#   Bit
#   BitField
#   BitIntegerAdapter
#   BitIntegerError
#   BitStruct
#   Bitwise
#   Buffered
#   CString
#   CStringAdapter
#   ConstAdapter
#   ConstError
#   Construct
#   ConstructError
#   Container
#   Embedded
#   EmbeddedBitStruct
#   Enum
#   ExprAdapter
#   Field
#   FieldError
#   Flag
#   FlagsAdapter
#   FlagsContainer
#   FlagsEnum
#   FormatField
#   GreedyRange
#   HexDumpAdapter
#   If
#   IfThenElse
#   IndexingAdapter
#   LFloat32
#   LFloat64
#   LazyBound
#   LengthValueAdapter
#   ListContainer
#   Magic
#   MappingAdapter
#   MappingError
#   MetaArray
#   MetaField
#   NFloat32
#   NFloat64
#   Nibble
#   NoneOf
#   Octet
#   OnDemand
#   OnDemandPointer
#   OneOf
#   OpenRange
#   Optional
#   OptionalGreedyRange
#   PaddedStringAdapter
#   Padding
#   PaddingAdapter
#   PaddingError
#   PascalString
#   Pass
#   Peek
#   Pointer
#   PrefixedArray
#   Range
#   RangeError
#   Reconfig
#   Rename
#   RepeatUntil
#   Restream
#   SBInt16
#   SBInt32
#   SBInt64
#   SBInt8
#   SLInt16
#   SLInt32
#   SLInt64
#   SLInt8
#   SNInt16
#   SNInt32
#   SNInt64
#   SNInt8
#   Select
#   SelectError
#   Sequence
#   SizeofError
#   SlicingAdapter
#   StaticField
#   String
#   StringAdapter
#   Struct
#   Subconstruct
#   Switch
#   SwitchError
#   SymmetricMapping
#   Terminator
#   TerminatorError
#   TunnelAdapter
#   UBInt16
#   UBInt32
#   UBInt64
#   UBInt8
#   ULInt16
#   ULInt32
#   ULInt64
#   ULInt8
#   UNInt16
#   UNInt32
#   UNInt64
#   UNInt8
#   Union
#   ValidationError
#   Validator
#   Value
