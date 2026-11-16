from __future__ import annotations

from datetime import tzinfo
from collections.abc import Callable
from typing import Any
from typing_extensions import assert_type

from wtforms import DateTimeLocalField, Form, SelectField, StringField
from wtforms.fields.core import _Text
from wtforms.meta import _SupportsGettextAndNgettext
from wtforms.validators import DateRange

# render_kw is None unless it was passed to the field
field = StringField()
assert_type(field.render_kw, "dict[str, Any] | None")
if field.render_kw is not None:
    field.render_kw["class"] = "form-control"

# DefaultMeta.get_translations() returns None unless `locales` is set (the default is False)
form = Form()
translations = form.meta.get_translations(form)
if translations is not None:
    translations.gettext("Not a valid choice.")
assert_type(form.meta.translations_cache, dict[tuple[str, ...] | None, _SupportsGettextAndNgettext])

# the messages of validators and fields are None unless passed explicitly
assert_type(DateRange().message, _Text | None)
assert_type(SelectField().invalid_choice_message, _Text | None)

assert_type(DateTimeLocalField().tz, tzinfo | Callable[[], tzinfo | None] | None)
