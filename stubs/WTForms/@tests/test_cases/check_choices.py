from __future__ import annotations

from enum import Enum, auto

from wtforms import Field, Form, SelectChoice, SelectField, StringField
from wtforms.fields import enum_choices, enum_coerce

# construct SelectChoice from old inputs
SelectChoice.from_input("")
SelectChoice.from_input(("", ""))
SelectChoice.from_input(("", "", {}))
# non-str values are no longer allowed/encouraged
# technically they never were, it just never was enforced
# coerce(value) is supposed to yield the object that gets stored in data
# so values in choices are intended to be pre-serialized to str in the
# format coerce expects
SelectChoice.from_input((1, "1"))  # type: ignore[arg-type]
SelectChoice.from_input((True, "t", {}))  # type: ignore[arg-type]
SelectChoice.from_input((False, "f", {}))  # type: ignore[arg-type]

# provide choices as any iterable of SelectChoice
SelectField(choices=[SelectChoice("")])

# new style of grouped choices
SelectField(choices=[SelectChoice("A", optgroup="a"), SelectChoice("B", optgroup="b")])

# provide a callback without arguments that generates a sequence of SelectChoice
SelectField(choices=lambda: [SelectChoice("")])


# or a callback that receives the form as its first and the field as its second argument
def generate_choices(form: Form, field: SelectField) -> list[SelectChoice]:
    return []


def generate_choices_generous_field_type(form: Form, field: Field) -> list[SelectChoice]:
    return []


def generate_choices_wrong_field_type(form: Form, field: StringField) -> list[SelectChoice]:
    return []


SelectField(choices=lambda form, field: [SelectChoice("")])
SelectField(choices=generate_choices)
SelectField(choices=generate_choices_generous_field_type)
SelectField(choices=generate_choices_wrong_field_type)  # type: ignore


# provide choices based on enum
class TestEnum(Enum):
    foo = auto()
    bar = auto()
    baz = auto()


SelectField(choices=enum_choices(TestEnum), coerce=enum_coerce(TestEnum))

# deprecated ways of providing choices:
# any way we can specify the choices inline with a literal should work

# tuple of tuples
SelectField(choices=(("", ""),))  # pyright: ignore[reportDeprecated]
SelectField(choices=((1, "1"),))  # pyright: ignore[reportDeprecated]
SelectField(choices=(("", "", {}),))  # pyright: ignore[reportDeprecated]
SelectField(choices=((True, "t", {}),))  # pyright: ignore[reportDeprecated]
SelectField(choices=((True, "t"), (False, "f", {})))  # pyright: ignore[reportDeprecated]

# list of tuples
SelectField(choices=[("", "")])  # pyright: ignore[reportDeprecated]
SelectField(choices=[(1, "1")])  # pyright: ignore[reportDeprecated]
SelectField(choices=[("", "", {})])  # pyright: ignore[reportDeprecated]
SelectField(choices=[(True, "t", {})])  # pyright: ignore[reportDeprecated]
SelectField(choices=[(True, "t"), (False, "f", {})])  # pyright: ignore[reportDeprecated]

# dict of tuple of tuples
SelectField(choices={"a": (("", ""),)})  # pyright: ignore[reportDeprecated]
SelectField(choices={"a": ((1, "1"),)})  # pyright: ignore[reportDeprecated]
SelectField(choices={"a": (("", "", {}),)})  # pyright: ignore[reportDeprecated]
SelectField(choices={"a": ((True, "t", {}),)})  # pyright: ignore[reportDeprecated]
SelectField(choices={"a": ((True, "t"), (False, "f", {}))})  # pyright: ignore[reportDeprecated]
SelectField(choices={"a": ((True, "", {}),), "b": ((False, "f"),)})  # pyright: ignore[reportDeprecated]

# dict of list of tuples
SelectField(choices={"a": [("", "")]})  # pyright: ignore[reportDeprecated]
SelectField(choices={"a": [(1, "1")]})  # pyright: ignore[reportDeprecated]
SelectField(choices={"a": [("", "", {})]})  # pyright: ignore[reportDeprecated]
SelectField(choices={"a": [(True, "t", {})]})  # pyright: ignore[reportDeprecated]
SelectField(choices={"a": [(True, "t"), (False, "f", {})]})  # pyright: ignore[reportDeprecated]
SelectField(choices={"a": [(True, "", {})], "b": [(False, "f")]})  # pyright: ignore[reportDeprecated]

# the same should be true for lambdas

# tuple of tuples
SelectField(choices=lambda: (("", ""),))  # pyright: ignore[reportDeprecated]
SelectField(choices=lambda: ((1, "1"),))  # pyright: ignore[reportDeprecated]
SelectField(choices=lambda: (("", "", {}),))  # pyright: ignore[reportDeprecated]
SelectField(choices=lambda: ((True, "t", {}),))  # pyright: ignore[reportDeprecated]
SelectField(choices=lambda: ((True, "t"), (False, "f", {})))  # pyright: ignore[reportDeprecated]

# list of tuples
SelectField(choices=lambda: [("", "")])  # pyright: ignore[reportDeprecated]
SelectField(choices=lambda: [(1, "1")])  # pyright: ignore[reportDeprecated]
SelectField(choices=lambda: [("", "", {})])  # pyright: ignore[reportDeprecated]
SelectField(choices=lambda: [(True, "t", {})])  # pyright: ignore[reportDeprecated]
SelectField(choices=lambda: [(True, "t"), (False, "f", {})])  # pyright: ignore[reportDeprecated]

# dict of tuple of tuples
SelectField(choices=lambda: {"a": (("", ""),)})  # pyright: ignore[reportDeprecated]
SelectField(choices=lambda: {"a": ((1, "1"),)})  # pyright: ignore[reportDeprecated]
SelectField(choices=lambda: {"a": (("", "", {}),)})  # pyright: ignore[reportDeprecated]
SelectField(choices=lambda: {"a": ((True, "t", {}),)})  # pyright: ignore[reportDeprecated]
SelectField(choices=lambda: {"a": ((True, "t"), (False, "f", {}))})  # pyright: ignore[reportDeprecated]
SelectField(choices=lambda: {"a": ((True, "", {}),), "b": ((False, "f"),)})  # pyright: ignore[reportDeprecated]

# dict of list of tuples
SelectField(choices=lambda: {"a": [("", "")]})  # pyright: ignore[reportDeprecated]
SelectField(choices=lambda: {"a": [(1, "1")]})  # pyright: ignore[reportDeprecated]
SelectField(choices=lambda: {"a": [("", "", {})]})  # pyright: ignore[reportDeprecated]
SelectField(choices=lambda: {"a": [(True, "t", {})]})  # pyright: ignore[reportDeprecated]
SelectField(choices=lambda: {"a": [(True, "t"), (False, "f", {})]})  # pyright: ignore[reportDeprecated]
SelectField(choices=lambda: {"a": [(True, "", {})], "b": [(False, "f")]})  # pyright: ignore[reportDeprecated]
