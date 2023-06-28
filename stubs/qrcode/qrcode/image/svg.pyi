import abc
from _typeshed import Incomplete
from decimal import Decimal
from typing import Optional, Type, Union, overload
from typing_extensions import Literal
from xml.etree.ElementTree import Element

import qrcode.image.base
from qrcode.image.styles.moduledrawers.base import QRModuleDrawer

class SvgFragmentImage(qrcode.image.base.BaseImageWithDrawer, metaclass=abc.ABCMeta):
    kind: str
    allowed_kinds: Incomplete
    default_drawer_class: Type[QRModuleDrawer]
    unit_size: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    @overload
    def units(self, pixels: Union[int, Decimal], text: Literal[False]) -> Decimal: ...
    @overload
    def units(self, pixels: Union[int, Decimal], text: Literal[True] = True) -> str: ...
    def save(self, stream, kind: Incomplete | None = None) -> None: ...
    def to_string(self, **kwargs): ...
    def new_image(self, **kwargs): ...

class SvgImage(SvgFragmentImage, metaclass=abc.ABCMeta):
    background: Optional[str]
    drawer_aliases: qrcode.image.base.DrawerAliases

class SvgPathImage(SvgImage, metaclass=abc.ABCMeta):
    QR_PATH_STYLE: Incomplete
    needs_processing: bool
    path: Optional[Element]
    default_drawer_class: Type[QRModuleDrawer]
    drawer_aliases: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def process(self) -> None: ...

class SvgFillImage(SvgImage, metaclass=abc.ABCMeta):
    background: str

class SvgPathFillImage(SvgPathImage, metaclass=abc.ABCMeta):
    background: str
