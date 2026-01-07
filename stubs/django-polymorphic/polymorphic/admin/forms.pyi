from typing import Any

from django import forms

class PolymorphicModelChoiceForm(forms.Form):
    type_label: str
    ct_id: forms.ChoiceField
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
