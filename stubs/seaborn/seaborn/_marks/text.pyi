from dataclasses import dataclass

from seaborn._marks.base import MappableColor, MappableFloat, MappableString, Mark, document_properties

@document_properties
@dataclass
class Text(Mark):
    text: MappableString = ...
    color: MappableColor = ...
    alpha: MappableFloat = ...
    fontsize: MappableFloat = ...
    halign: MappableString = ...
    valign: MappableString = ...
    offset: MappableFloat = ...
