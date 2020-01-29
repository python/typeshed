from typing import Any

from django_filters import filters

class BooleanFilter(filters.BooleanFilter):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

# Names in __all__ with no definition:
#   AllValuesFilter
#   AllValuesMultipleFilter
#   BaseCSVFilter
#   BaseInFilter
#   BaseRangeFilter
#   CharFilter
#   ChoiceFilter
#   DateFilter
#   DateFromToRangeFilter
#   DateRangeFilter
#   DateTimeFilter
#   DateTimeFromToRangeFilter
#   DurationFilter
#   Filter
#   IsoDateTimeFilter
#   IsoDateTimeFromToRangeFilter
#   LookupChoiceFilter
#   ModelChoiceFilter
#   ModelMultipleChoiceFilter
#   MultipleChoiceFilter
#   NumberFilter
#   NumericRangeFilter
#   OrderingFilter
#   RangeFilter
#   TimeFilter
#   TimeRangeFilter
#   TypedChoiceFilter
#   TypedMultipleChoiceFilter
#   UUIDFilter
