from _typeshed import Incomplete

COLUMN_NAMES: Incomplete
COLUMN_TYPES: Incomplete

class PandasMol2:
    mol2_text: str
    header: str
    code: str
    mol2_path: str
    def __init__(self) -> None: ...
    @property
    def df(self): ...
    @df.setter
    def df(self, value) -> None: ...
    def read_mol2(self, path, columns: Incomplete | None = None): ...
    def read_mol2_from_list(self, mol2_lines, mol2_code, columns: Incomplete | None = None): ...
    @staticmethod
    def rmsd(df1, df2, heavy_only: bool = True): ...
    def distance(self, xyz=(0.0, 0.0, 0.0)): ...
    @staticmethod
    def distance_df(df, xyz=(0.0, 0.0, 0.0)): ...
