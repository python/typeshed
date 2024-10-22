from __future__ import annotations

from typing_extensions import assert_type

from wtforms import Form, StringField


class MyForm(Form):
    name = StringField()


form = MyForm()
assert_type(form, MyForm)
assert_type(form.name, StringField)
