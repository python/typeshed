from .errors import FPDFException as FPDFException
from typing import Any

SUPPORTED_IMAGE_FILTERS: Any

def load_image(filename): ...
def get_img_info(img, image_filter: str = ...): ...
