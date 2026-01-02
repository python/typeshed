from typing import Any

from django.contrib.contenttypes.forms import BaseGenericInlineFormSet

from .models import PolymorphicFormSetChild

class GenericPolymorphicFormSetChild(PolymorphicFormSetChild): ...
class BaseGenericPolymorphicInlineFormSet(BaseGenericInlineFormSet[Any, Any]): ...

def generic_polymorphic_inlineformset_factory(*args: Any, **kwargs: Any) -> type[BaseGenericPolymorphicInlineFormSet]: ...
