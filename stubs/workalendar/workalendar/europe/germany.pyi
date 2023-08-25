from _typeshed import Incomplete

from ..core import WesternCalendar

class Germany(WesternCalendar):
    include_labour_day: bool
    FIXED_HOLIDAYS: Incomplete
    include_easter_monday: bool
    include_ascension: bool
    include_whit_monday: bool
    include_good_friday: bool
    include_boxing_day: bool
    boxing_day_label: ClassVar[str]
    all_time_include_reformation_day: bool
    include_reformation_day_2018: bool
    def include_reformation_day(self, year): ...
    def get_reformation_day(self, year): ...
    def get_variable_days(self, year): ...

class BadenWurttemberg(Germany):
    include_epiphany: bool
    include_corpus_christi: bool
    include_all_saints: bool

class Bavaria(Germany):
    include_epiphany: bool
    include_corpus_christi: bool
    include_all_saints: bool
    include_assumption: bool

class Berlin(Germany):
    def get_international_womens_day(self, year): ...
    def get_liberation_day(self, year): ...
    def get_variable_days(self, year): ...

class Brandenburg(Germany):
    include_easter_sunday: bool
    all_time_include_reformation_day: bool

class Bremen(Germany):
    include_reformation_day_2018: bool

class Hamburg(Germany):
    include_reformation_day_2018: bool

class Hesse(Germany):
    include_corpus_christi: bool

class MecklenburgVorpommern(Germany):
    all_time_include_reformation_day: bool

class LowerSaxony(Germany):
    include_reformation_day_2018: bool

class NorthRhineWestphalia(Germany):
    include_corpus_christi: bool
    include_all_saints: bool

class RhinelandPalatinate(Germany):
    include_corpus_christi: bool
    include_all_saints: bool

class Saarland(Germany):
    include_corpus_christi: bool
    include_assumption: bool
    include_all_saints: bool

class Saxony(Germany):
    all_time_include_reformation_day: bool
    def get_repentance_day(self, year): ...
    def get_variable_days(self, year): ...

class SaxonyAnhalt(Germany):
    include_epiphany: bool
    all_time_include_reformation_day: bool

class SchleswigHolstein(Germany):
    include_reformation_day_2018: bool

class Thuringia(Germany):
    all_time_include_reformation_day: bool
