from typing_extensions import assert_type

import pandas as pd
import tabulate

# Regression for #16708: tabulate() accepts a pandas.DataFrame at
# runtime (the PyPI description says so), and it iterates as column
# names, not rows.
df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
assert_type(tabulate.tabulate(df), str)

# Existing tabular forms keep working.
assert_type(tabulate.tabulate([["a", "b"], ["c", "d"]]), str)
assert_type(tabulate.tabulate({"a": [1, 2], "b": [3, 4]}), str)
