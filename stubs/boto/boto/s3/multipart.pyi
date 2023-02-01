from _typeshed import Incomplete
from typing import Any

class CompleteMultiPartUpload:
    bucket: Any
    location: Any
    bucket_name: Any
    key_name: Any
    etag: Any
    version_id: Any
    encrypted: Any
    def __init__(self, bucket: Incomplete | None = ...) -> None: ...
    def startElement(self, name, attrs, connection): ...
    def endElement(self, name, value, connection): ...

class Part:
    bucket: Any
    part_number: Any
    last_modified: Any
    etag: Any
    size: Any
    def __init__(self, bucket: Incomplete | None = ...) -> None: ...
    def startElement(self, name, attrs, connection): ...
    def endElement(self, name, value, connection): ...

def part_lister(mpupload, part_number_marker: Incomplete | None = ...): ...

class MultiPartUpload:
    bucket: Any
    bucket_name: Any
    key_name: Any
    id: Any
    initiator: Any
    owner: Any
    storage_class: Any
    initiated: Any
    part_number_marker: Any
    next_part_number_marker: Any
    max_parts: Any
    is_truncated: bool
    def __init__(self, bucket: Incomplete | None = ...) -> None: ...
    def __iter__(self): ...
    def to_xml(self): ...
    def startElement(self, name, attrs, connection): ...
    def endElement(self, name, value, connection): ...
    def get_all_parts(
        self,
        max_parts: Incomplete | None = ...,
        part_number_marker: Incomplete | None = ...,
        encoding_type: Incomplete | None = ...,
    ): ...
    def upload_part_from_file(
        self,
        fp,
        part_num,
        headers: Incomplete | None = ...,
        replace: bool = ...,
        cb: Incomplete | None = ...,
        num_cb: int = ...,
        md5: Incomplete | None = ...,
        size: Incomplete | None = ...,
    ): ...
    def copy_part_from_key(
        self,
        src_bucket_name,
        src_key_name,
        part_num,
        start: Incomplete | None = ...,
        end: Incomplete | None = ...,
        src_version_id: Incomplete | None = ...,
        headers: Incomplete | None = ...,
    ): ...
    def complete_upload(self): ...
    def cancel_upload(self): ...
