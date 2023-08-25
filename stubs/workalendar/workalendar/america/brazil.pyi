from _typeshed import Incomplete

from ..core import WesternCalendar

class Brazil(WesternCalendar):
    FIXED_HOLIDAYS: Incomplete
    include_sao_jose: bool
    sao_jose_label: str
    include_sao_pedro: bool
    sao_pedro_label: str
    include_sao_joao: bool
    sao_joao_label: str
    include_labour_day: bool
    include_servidor_publico: bool
    servidor_publico_label: str
    include_consciencia_negra: bool
    consciencia_negra_day: Incomplete
    consciencia_negra_label: str
    include_easter_sunday: bool
    include_immaculate_conception: bool
    immaculate_conception_label: str
    def get_variable_days(self, year): ...

class BrazilAcre(Brazil):
    FIXED_HOLIDAYS: Incomplete

class BrazilAlagoas(Brazil):
    FIXED_HOLIDAYS: Incomplete
    include_sao_pedro: bool
    include_sao_joao: bool
    include_consciencia_negra: bool

class BrazilAmapa(Brazil):
    FIXED_HOLIDAYS: Incomplete
    include_sao_jose: bool
    sao_jose_label: str
    include_consciencia_negra: bool

class BrazilAmazonas(Brazil):
    FIXED_HOLIDAYS: Incomplete
    include_consciencia_negra: bool
    include_immaculate_conception: bool

class BrazilBahia(Brazil):
    FIXED_HOLIDAYS: Incomplete

class BrazilCeara(Brazil):
    FIXED_HOLIDAYS: Incomplete
    include_sao_jose: bool

class BrazilDistritoFederal(Brazil):
    FIXED_HOLIDAYS: Incomplete

class BrazilEspiritoSanto(Brazil):
    include_servidor_publico: bool

class BrazilGoias(Brazil):
    include_servidor_publico: bool

class BrazilMaranhao(Brazil):
    FIXED_HOLIDAYS: Incomplete
    include_immaculate_conception: bool

class BrazilMinasGerais(Brazil):
    FIXED_HOLIDAYS: Incomplete

class BrazilMatoGrosso(Brazil):
    include_consciencia_negra: bool
    consciencia_negra_day: Incomplete

class BrazilMatoGrossoDoSul(Brazil):
    FIXED_HOLIDAYS: Incomplete

class BrazilPara(Brazil):
    FIXED_HOLIDAYS: Incomplete
    include_immaculate_conception: bool

class BrazilParaiba(Brazil):
    FIXED_HOLIDAYS: Incomplete

class BrazilPernambuco(Brazil):
    FIXED_HOLIDAYS: Incomplete
    include_sao_joao: bool

class BrazilPiaui(Brazil):
    FIXED_HOLIDAYS: Incomplete

class BrazilParana(Brazil):
    FIXED_HOLIDAYS: Incomplete

class BrazilRioDeJaneiro(Brazil):
    FIXED_HOLIDAYS: Incomplete
    include_fat_tuesday: bool
    fat_tuesday_label: str
    include_servidor_publico: bool
    servidor_publico_label: str
    include_consciencia_negra: bool
    consciencia_negra_label: str
    include_immaculate_conception: bool
    def get_dia_do_comercio(self, year): ...
    def get_variable_days(self, year): ...

class BrazilRioGrandeDoNorte(Brazil):
    FIXED_HOLIDAYS: Incomplete
    include_sao_pedro: bool
    sao_pedro_label: str

class BrazilRioGrandeDoSul(Brazil):
    FIXED_HOLIDAYS: Incomplete

class BrazilRondonia(Brazil):
    FIXED_HOLIDAYS: Incomplete

class BrazilRoraima(Brazil):
    FIXED_HOLIDAYS: Incomplete

class BrazilSantaCatarina(Brazil):
    FIXED_HOLIDAYS: Incomplete

class BrazilSaoPauloState(Brazil):
    FIXED_HOLIDAYS: Incomplete

class BrazilSaoPauloCity(BrazilSaoPauloState):
    FIXED_HOLIDAYS: Incomplete
    include_fat_tuesday: bool
    fat_tuesday_label: str
    include_easter_sunday: bool
    include_corpus_christi: bool
    include_good_friday: bool
    good_friday_label: str
    include_consciencia_negra: bool
    consciencia_negra_label: str

class BrazilSergipe(Brazil):
    FIXED_HOLIDAYS: Incomplete

class BrazilTocantins(Brazil):
    FIXED_HOLIDAYS: Incomplete

class BrazilVitoriaCity(BrazilEspiritoSanto):
    FIXED_HOLIDAYS: Incomplete
    include_corpus_christi: bool
    include_good_friday: bool
    good_friday_label: str

class BrazilVilaVelhaCity(BrazilEspiritoSanto):
    FIXED_HOLIDAYS: Incomplete

class BrazilCariacicaCity(BrazilEspiritoSanto):
    FIXED_HOLIDAYS: Incomplete
    include_corpus_christi: bool
    include_good_friday: bool
    good_friday_label: str
    include_sao_joao: bool
    sao_joao_label: str

class BrazilGuarapariCity(BrazilEspiritoSanto):
    FIXED_HOLIDAYS: Incomplete
    include_sao_pedro: bool
    include_consciencia_negra: bool
    consciencia_negra_day: Incomplete
    include_immaculate_conception: bool

class BrazilSerraCity(BrazilEspiritoSanto):
    FIXED_HOLIDAYS: Incomplete
    include_fat_tuesday: bool
    fat_tuesday_label: str
    include_ash_wednesday: bool
    ash_wednesday_label: str
    include_good_friday: bool
    good_friday_label: str
    include_sao_pedro: bool
    include_immaculate_conception: bool
    def get_variable_days(self, year): ...

class BrazilRioBrancoCity(BrazilAcre):
    FIXED_HOLIDAYS: Incomplete

class BrazilMaceioCity(BrazilAlagoas):
    FIXED_HOLIDAYS: Incomplete

class BrazilManausCity(BrazilAmazonas):
    FIXED_HOLIDAYS: Incomplete

class BrazilMacapaCity(BrazilAmapa):
    FIXED_HOLIDAYS: Incomplete

class BrazilSalvadorCity(BrazilBahia):
    FIXED_HOLIDAYS: Incomplete

class BrazilFortalezaCity(BrazilCeara):
    FIXED_HOLIDAYS: Incomplete

class BrazilGoianiaCity(BrazilGoias):
    FIXED_HOLIDAYS: Incomplete

class BrazilBeloHorizonteCity(BrazilMinasGerais):
    FIXED_HOLIDAYS: Incomplete

class BrazilCampoGrandeCity(BrazilMatoGrossoDoSul):
    FIXED_HOLIDAYS: Incomplete

class BrazilCuiabaCity(BrazilMatoGrosso):
    FIXED_HOLIDAYS: Incomplete
    include_easter_sunday: bool
    include_corpus_christi: bool
    include_good_friday: bool
    good_friday_label: str

class BrazilBelemCity(BrazilPara):
    FIXED_HOLIDAYS: Incomplete

class BrazilJoaoPessoaCity(BrazilParaiba):
    FIXED_HOLIDAYS: Incomplete

class BrazilRecifeCity(BrazilPernambuco):
    FIXED_HOLIDAYS: Incomplete

class BrazilTeresinaCity(BrazilPiaui):
    FIXED_HOLIDAYS: Incomplete

class BrazilCuritibaCity(BrazilParana):
    FIXED_HOLIDAYS: Incomplete

class BrazilNatalCity(BrazilRioGrandeDoNorte):
    FIXED_HOLIDAYS: Incomplete

class BrazilPortoVelhoCity(BrazilRondonia):
    FIXED_HOLIDAYS: Incomplete

class BrazilBoaVistaCity(BrazilRoraima):
    FIXED_HOLIDAYS: Incomplete

class BrazilPortoAlegreCity(BrazilRioGrandeDoSul):
    FIXED_HOLIDAYS: Incomplete

class BrazilChapecoCity(BrazilSantaCatarina):
    FIXED_HOLIDAYS: Incomplete

class BrazilFlorianopolisCity(BrazilSantaCatarina):
    FIXED_HOLIDAYS: Incomplete

class BrazilJoinvilleCity(BrazilSantaCatarina):
    FIXED_HOLIDAYS: Incomplete

class BrazilAracajuCity(BrazilSergipe):
    FIXED_HOLIDAYS: Incomplete

class BrazilSorocabaCity(BrazilSaoPauloState):
    FIXED_HOLIDAYS: Incomplete

class BrazilPalmasCity(BrazilTocantins):
    FIXED_HOLIDAYS: Incomplete

class BrazilBankCalendar(Brazil):
    include_fat_tuesday: bool
    fat_tuesday_label: str
    include_good_friday: bool
    include_ash_wednesday: bool
    include_corpus_christi: bool
    include_easter_sunday: bool
    def get_last_day_of_year_for_only_internal_bank_trans(self, year): ...
    def get_variable_days(self, year): ...
    def find_following_working_day(self, day): ...

IBGE_TUPLE: Incomplete
IBGE_REGISTER: Incomplete
