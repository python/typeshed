import pycountry.db

LOCALES_DIR: str
DATABASE_DIR: str
__version__: str | None

def resource_filename(package_or_requirement: str, resource_name: str) -> str: ...
def get_version(distribution_name: str) -> str | None: ...
def remove_accents(input_str: str) -> str: ...

class ExistingCountries(pycountry.db.Database):
    data_class: type
    root_key: str
    def search_fuzzy(self, query: str) -> list[pycountry.db.Country]: ...

class HistoricCountries(ExistingCountries):
    data_class: type
    root_key: str

class Scripts(pycountry.db.Database):
    data_class: str
    root_key: str

class Currencies(pycountry.db.Database):
    data_class: str
    root_key: str

class Languages(pycountry.db.Database):
    no_index: list[str]
    data_class: str
    root_key: str

class LanguageFamilies(pycountry.db.Database):
    data_class: str
    root_key: str

class SubdivisionHierarchy(pycountry.db.Data):
    country_code: str
    parent_code: str | None
    def __init__(self, **kw: str) -> None: ...
    @property
    def country(self) -> pycountry.db.Country | None: ...
    @property
    def parent(self) -> SubdivisionHierarchy | None: ...

class Subdivisions(pycountry.db.Database):
    data_class: type
    no_index: list[str]
    root_key: str
    def get(  # type: ignore[override]
        self, *, default: SubdivisionHierarchy | None = ..., **kw: str
    ) -> SubdivisionHierarchy | None | list[SubdivisionHierarchy]: ...
    def match(self, query: str) -> list[SubdivisionHierarchy]: ...
    def partial_match(self, query: str) -> list[SubdivisionHierarchy]: ...
    def search_fuzzy(self, query: str) -> list[SubdivisionHierarchy]: ...

countries: ExistingCountries
subdivisions: Subdivisions
historic_countries: HistoricCountries
currencies: Currencies
languages: Languages
language_families: LanguageFamilies
scripts: Scripts
