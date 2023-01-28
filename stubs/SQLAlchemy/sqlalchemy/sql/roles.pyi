from abc import abstractmethod
from typing import NoReturn

from ..sql.selectable import Subquery

class SQLRole:
    allows_lambda: bool
    uses_inspection: bool

class UsesInspection:
    uses_inspection: bool

class AllowsLambdaRole:
    allows_lambda: bool

class HasCacheKeyRole(SQLRole): ...
class ExecutableOptionRole(SQLRole): ...
class LiteralValueRole(SQLRole): ...
class ColumnArgumentRole(SQLRole): ...
class ColumnArgumentOrKeyRole(ColumnArgumentRole): ...
class StrAsPlainColumnRole(ColumnArgumentRole): ...
class ColumnListRole(SQLRole): ...
class TruncatedLabelRole(SQLRole): ...
class ColumnsClauseRole(AllowsLambdaRole, UsesInspection, ColumnListRole): ...
class LimitOffsetRole(SQLRole): ...
class ByOfRole(ColumnListRole): ...
class GroupByRole(AllowsLambdaRole, UsesInspection, ByOfRole): ...
class OrderByRole(AllowsLambdaRole, ByOfRole): ...
class StructuralRole(SQLRole): ...
class StatementOptionRole(StructuralRole): ...
class OnClauseRole(AllowsLambdaRole, StructuralRole): ...
class WhereHavingRole(OnClauseRole): ...
class ExpressionElementRole(SQLRole): ...
class ConstExprRole(ExpressionElementRole): ...
class LabeledColumnExprRole(ExpressionElementRole): ...
class BinaryElementRole(ExpressionElementRole): ...
class InElementRole(SQLRole): ...
class JoinTargetRole(AllowsLambdaRole, UsesInspection, StructuralRole): ...
class FromClauseRole(ColumnsClauseRole, JoinTargetRole): ...

class StrictFromClauseRole(FromClauseRole):
    # Meant to be overriden if necessary, but non-abstract classes don't necessarily implement it
    @property
    def description(self) -> NoReturn | str: ...

class AnonymizedFromClauseRole(StrictFromClauseRole): ...
class ReturnsRowsRole(SQLRole): ...
class StatementRole(SQLRole): ...

class SelectStatementRole(StatementRole, ReturnsRowsRole):
    @abstractmethod
    def subquery(self) -> Subquery: ...

class HasCTERole(ReturnsRowsRole): ...
class IsCTERole(SQLRole): ...
class CompoundElementRole(AllowsLambdaRole, SQLRole): ...
class DMLRole(StatementRole): ...
class DMLTableRole(FromClauseRole): ...
class DMLColumnRole(SQLRole): ...
class DMLSelectRole(SQLRole): ...
class DDLRole(StatementRole): ...
class DDLExpressionRole(StructuralRole): ...
class DDLConstraintColumnRole(SQLRole): ...
class DDLReferredColumnRole(DDLConstraintColumnRole): ...
