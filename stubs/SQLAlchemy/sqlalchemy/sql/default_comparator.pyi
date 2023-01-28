from ..sql.operators import _AnyOperator

operator_lookup: dict[str, tuple[_AnyOperator] | tuple[_AnyOperator, _AnyOperator]]
