from _typeshed import Incomplete

from ..core import WesternCalendar

class Switzerland(WesternCalendar):
    include_good_friday: bool
    include_easter_sunday: bool
    include_easter_monday: bool
    include_ascension: bool
    include_whit_sunday: bool
    include_whit_monday: bool
    include_christmas: bool
    include_boxing_day: bool
    include_epiphany: bool
    include_corpus_christi: bool
    include_assumption: bool
    include_all_saints: bool
    include_immaculate_conception: bool
    include_berchtolds_day: bool
    include_st_josephs_day: bool
    FIXED_HOLIDAYS: Incomplete
    def has_berchtolds_day(self, year): ...
    def get_federal_thanksgiving_monday(self, year): ...
    def get_variable_days(self, year): ...

class Aargau(Switzerland):
    include_berchtolds_day: bool
    include_corpus_christi: bool
    include_all_saints: bool
    include_immaculate_conception: bool

class AppenzellInnerrhoden(Switzerland):
    include_corpus_christi: bool
    include_assumption: bool
    include_all_saints: bool
    include_immaculate_conception: bool

class AppenzellAusserrhoden(Switzerland):
    include_labour_day: bool

class Bern(Switzerland):
    include_berchtolds_day: bool

class BaselLandschaft(Switzerland):
    include_labour_day: bool

class BaselStadt(Switzerland):
    include_labour_day: bool

class Fribourg(Switzerland):
    include_berchtolds_day: bool
    include_labour_day: bool
    include_corpus_christi: bool
    include_assumption: bool
    include_all_saints: bool
    include_immaculate_conception: bool

class Geneva(Switzerland):
    include_boxing_day: bool
    FIXED_HOLIDAYS: Incomplete
    def get_genevan_fast(self, year): ...
    def get_variable_days(self, year): ...

class Glarus(Switzerland):
    include_berchtolds_day: bool
    include_all_saints: bool
    FIXED_HOLIDAYS: Incomplete

class Graubunden(Switzerland):
    include_epiphany: bool
    include_st_josephs_day: bool
    include_corpus_christi: bool
    include_immaculate_conception: bool

class Jura(Switzerland):
    include_berchtolds_day: bool
    include_labour_day: bool
    include_corpus_christi: bool
    include_assumption: bool
    include_all_saints: bool
    include_boxing_day: bool
    FIXED_HOLIDAYS: Incomplete

class Luzern(Switzerland):
    include_berchtolds_day: bool
    include_epiphany: bool
    include_st_josephs_day: bool
    include_corpus_christi: bool
    include_assumption: bool
    include_all_saints: bool
    include_immaculate_conception: bool

class Neuchatel(Switzerland):
    include_boxing_day: bool
    include_labour_day: bool
    FIXED_HOLIDAYS: Incomplete
    def has_berchtolds_day(self, year): ...
    def get_variable_days(self, year): ...

class Nidwalden(Switzerland):
    include_st_josephs_day: bool
    include_corpus_christi: bool
    include_assumption: bool
    include_all_saints: bool
    include_immaculate_conception: bool

class Obwalden(Switzerland):
    include_berchtolds_day: bool
    include_corpus_christi: bool
    include_assumption: bool
    include_all_saints: bool
    include_immaculate_conception: bool
    FIXED_HOLIDAYS: Incomplete

class StGallen(Switzerland):
    include_all_saints: bool

class Schaffhausen(Switzerland):
    include_berchtolds_day: bool
    include_labour_day: bool

class Solothurn(Switzerland):
    include_berchtolds_day: bool
    include_st_josephs_day: bool
    include_labour_day: bool
    include_corpus_christi: bool
    include_assumption: bool
    include_all_saints: bool
    include_immaculate_conception: bool

class Schwyz(Switzerland):
    include_epiphany: bool
    include_st_josephs_day: bool
    include_corpus_christi: bool
    include_assumption: bool
    include_all_saints: bool
    include_immaculate_conception: bool

class Thurgau(Switzerland):
    include_berchtolds_day: bool
    include_labour_day: bool

class Ticino(Switzerland):
    include_good_friday: bool
    include_epiphany: bool
    include_st_josephs_day: bool
    include_labour_day: bool
    include_corpus_christi: bool
    include_assumption: bool
    include_all_saints: bool
    include_immaculate_conception: bool
    FIXED_HOLIDAYS: Incomplete

class Uri(Switzerland):
    include_epiphany: bool
    include_st_josephs_day: bool
    include_corpus_christi: bool
    include_assumption: bool
    include_all_saints: bool
    include_immaculate_conception: bool

class Vaud(Switzerland):
    include_berchtolds_day: bool
    include_boxing_day: bool
    def get_variable_days(self, year): ...

class Valais(Switzerland):
    include_good_friday: bool
    include_easter_monday: bool
    include_whit_monday: bool
    include_st_josephs_day: bool
    include_corpus_christi: bool
    include_assumption: bool
    include_all_saints: bool
    include_immaculate_conception: bool
    include_boxing_day: bool

class Zug(Switzerland):
    include_berchtolds_day: bool
    include_corpus_christi: bool
    include_assumption: bool
    include_all_saints: bool
    include_immaculate_conception: bool

class Zurich(Switzerland):
    include_berchtolds_day: bool
    include_labour_day: bool
