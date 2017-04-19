import sys

import six
from six import StringIO, BytesIO
from typing import Union, Dict, SupportsFloat, Any

import leancloud
from leancloud.object_ import Object
from leancloud.acl import ACL


if six.PY3:
    from io import IOBase
    file_type = IOBase
    buffer_type = memoryview
else:
    file_type = file
    buffer_type = buffer

class File(object):

    def __init__(self, name: str, data: Union[StringIO, BytesIO, file_type, buffer_type]=None, type_: str=None) -> None:...

    @classmethod
    def create_with_url(cls, name: str, url: str, meta_data: Dict =None, type_: str=None) -> File:...

    @classmethod
    def create_without_data(cls, object_id: str) -> File:...

    def get_acl(self) -> ACL:...

    def set_acl(self, acl: ACL) -> File:...

    @property
    def name(self) -> str:...

    @property
    def url(self) -> str:...

    @property
    def size(self) -> int:...

    @property
    def owner_id(self) -> str:...

    @property
    def metadata(self) -> Dict:...

    def get_thumbnail_url(self, width: SupportsFloat, height: SupportsFloat, quality: SupportsFloat, scale_to_fit: bool=True, fmt: str='png') -> str:...

    def destroy(self) -> None:...

    def _save_to_qiniu(self) -> None:...

    def _save_to_leancloud(self) -> None:...

    def save(self) -> None:...

    def _save_external(self) -> None:...

    def _save_to_cos(self) -> None:...

    def fetch(self) -> None:...
