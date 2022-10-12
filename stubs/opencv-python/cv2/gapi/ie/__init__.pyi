from typing import overload

from cv2.cv2 import gapi_ie_PyParams

TRAIT_AS_IMAGE: int
TRAIT_AS_TENSOR: int
TraitAs_IMAGE: int
TraitAs_TENSOR: int

@overload
def params(tag: str, model: str, device: str) -> gapi_ie_PyParams: ...
@overload
def params(tag: str, model: str, weights: str, device: str) -> gapi_ie_PyParams: ...
