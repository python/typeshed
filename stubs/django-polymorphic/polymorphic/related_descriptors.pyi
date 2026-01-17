from typing import Any

from django.db.models.fields.related_descriptors import ForwardOneToOneDescriptor, ReverseOneToOneDescriptor
from django.db.models.query import QuerySet

class NonPolymorphicForwardOneToOneDescriptor(ForwardOneToOneDescriptor[Any]):
    def get_queryset(self, **hints: Any) -> QuerySet[Any]: ...

class NonPolymorphicReverseOneToOneDescriptor(ReverseOneToOneDescriptor[Any, Any]):
    def get_queryset(self, **hints: Any) -> QuerySet[Any]: ...
