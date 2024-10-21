from wtforms.fields.choices import (
    RadioField as RadioField,
    SelectField as SelectField,
    SelectMultipleField as SelectMultipleField,
)
from wtforms.fields.core import Field as Field, Flags as Flags, Label as Label
from wtforms.fields.datetime import (
    DateField as DateField,
    DateTimeField as DateTimeField,
    DateTimeLocalField as DateTimeLocalField,
    MonthField as MonthField,
    TimeField as TimeField,
    WeekField as WeekField,
)
from wtforms.fields.form import FormField as FormField
from wtforms.fields.list import FieldList as FieldList
from wtforms.fields.numeric import (
    DecimalField as DecimalField,
    DecimalRangeField as DecimalRangeField,
    FloatField as FloatField,
    IntegerField as IntegerField,
    IntegerRangeField as IntegerRangeField,
)
from wtforms.fields.simple import (
    BooleanField as BooleanField,
    ColorField as ColorField,
    EmailField as EmailField,
    FileField as FileField,
    HiddenField as HiddenField,
    MultipleFileField as MultipleFileField,
    PasswordField as PasswordField,
    SearchField as SearchField,
    StringField as StringField,
    SubmitField as SubmitField,
    TelField as TelField,
    TextAreaField as TextAreaField,
    URLField as URLField,
)
