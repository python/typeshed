from _typeshed import Incomplete
from datetime import datetime

from .actions import Action
from .enums import AnnotationFlag, AnnotationName, AssociatedFileRelationship, FileAttachmentAnnotationName
from .syntax import Destination, Name, PDFContentStream, PDFObject, PDFString

DEFAULT_ANNOT_FLAGS: tuple[AnnotationFlag, ...]

class AnnotationMixin:
    type: Name
    subtype: Name
    rect: str
    border: str
    f_t: Name | None
    v: Incomplete | None
    f: int  # AnnotationFlags bitmask
    contents: str | None
    a: Action | None
    dest: Destination | None
    c: str | None
    t: str | None
    m: str | None
    quad_points: str | None
    p: Incomplete | None
    name: AnnotationName | FileAttachmentAnnotationName | None
    ink_list: str | None
    f_s: str | None
    d_a: str | None
    def __init__(
        self,
        subtype: str,
        x: int,
        y: int,
        width: int,
        height: int,
        flags: tuple[AnnotationFlag | str, ...] = ...,
        contents: str | None = None,
        dest: Destination | None = None,
        action: Action | None = None,
        color: tuple[int, int, int] | None = None,
        modification_time: datetime | None = None,
        title: str | None = None,
        quad_points: tuple[float, ...] | None = None,  # multiple of 8 floats
        border_width: int = 0,
        name: AnnotationName | FileAttachmentAnnotationName | None = None,
        ink_list: tuple[int, ...] = (),
        file_spec: str | None = None,
        field_type: str | None = None,
        value=None,
        default_appearance: str | None = None,
    ) -> None: ...

class PDFAnnotation(AnnotationMixin, PDFObject): ...

class AnnotationDict(AnnotationMixin):
    __slots__ = (
        "type",
        "subtype",
        "rect",
        "border",
        "f_t",
        "v",
        "f",
        "contents",
        "a",
        "dest",
        "c",
        "t",
        "quad_points",
        "p",
        "name",
        "ink_list",
        "f_s",
        "d_a",
    )
    def serialize(self) -> str: ...

class PDFEmbeddedFile(PDFContentStream):
    type: Name
    params: str
    def __init__(
        self,
        basename: str,
        contents: bytes,
        desc: str = "",
        creation_date: datetime | None = None,
        modification_date: datetime | None = None,
        mime_type: str | None = None,
        af_relationship: AssociatedFileRelationship | None = None,
        compress: bool = False,
        checksum: bool = False,
    ) -> None: ...
    def globally_enclosed(self) -> bool: ...
    def set_globally_enclosed(self, value: bool) -> None: ...
    def basename(self) -> str: ...
    def file_spec(self) -> FileSpec: ...

class FileSpec(PDFObject):
    type: Name
    f: PDFString
    uf: PDFString
    embedded_file: PDFEmbeddedFile
    desc: PDFString  # Only exists if provided to __init__
    a_f_relationship: Name  # Only exists if provided to __init__
    basename: str
    def __init__(
        self,
        embedded_file: PDFEmbeddedFile,
        basename: str,
        desc: str | None = None,
        af_relationship: AssociatedFileRelationship | None = None,
    ) -> None: ...
    @property
    def e_f(self) -> str: ...
