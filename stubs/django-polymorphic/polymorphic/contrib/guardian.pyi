from typing import Any

from django.contrib.contenttypes.models import ContentType

def get_polymorphic_base_content_type(obj: Any) -> ContentType: ...
