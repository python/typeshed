"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Score(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ScoreType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ScoreTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Score._ScoreType.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        Curriculum: Score._ScoreType.ValueType  # 1
        """map generated score (from curriculum maps with special scoring)"""
        Melee: Score._ScoreType.ValueType  # 2
        """summation of in-progress and current units/buildings value + minerals + vespene"""

    class ScoreType(_ScoreType, metaclass=_ScoreTypeEnumTypeWrapper): ...
    Curriculum: Score.ScoreType.ValueType  # 1
    """map generated score (from curriculum maps with special scoring)"""
    Melee: Score.ScoreType.ValueType  # 2
    """summation of in-progress and current units/buildings value + minerals + vespene"""

    SCORE_TYPE_FIELD_NUMBER: builtins.int
    SCORE_FIELD_NUMBER: builtins.int
    SCORE_DETAILS_FIELD_NUMBER: builtins.int
    score_type: global___Score.ScoreType.ValueType
    score: builtins.int
    """Note: check score_type to know whether this is a melee score or curriculum score"""
    @property
    def score_details(self) -> global___ScoreDetails: ...
    def __init__(
        self,
        *,
        score_type: global___Score.ScoreType.ValueType | None = ...,
        score: builtins.int | None = ...,
        score_details: global___ScoreDetails | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["score", b"score", "score_details", b"score_details", "score_type", b"score_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["score", b"score", "score_details", b"score_details", "score_type", b"score_type"]) -> None: ...

global___Score = Score

@typing_extensions.final
class CategoryScoreDetails(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NONE_FIELD_NUMBER: builtins.int
    ARMY_FIELD_NUMBER: builtins.int
    ECONOMY_FIELD_NUMBER: builtins.int
    TECHNOLOGY_FIELD_NUMBER: builtins.int
    UPGRADE_FIELD_NUMBER: builtins.int
    none: builtins.float
    """Used when no other category is configured in game data"""
    army: builtins.float
    economy: builtins.float
    technology: builtins.float
    upgrade: builtins.float
    def __init__(
        self,
        *,
        none: builtins.float | None = ...,
        army: builtins.float | None = ...,
        economy: builtins.float | None = ...,
        technology: builtins.float | None = ...,
        upgrade: builtins.float | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["army", b"army", "economy", b"economy", "none", b"none", "technology", b"technology", "upgrade", b"upgrade"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["army", b"army", "economy", b"economy", "none", b"none", "technology", b"technology", "upgrade", b"upgrade"]) -> None: ...

global___CategoryScoreDetails = CategoryScoreDetails

@typing_extensions.final
class VitalScoreDetails(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIFE_FIELD_NUMBER: builtins.int
    SHIELDS_FIELD_NUMBER: builtins.int
    ENERGY_FIELD_NUMBER: builtins.int
    life: builtins.float
    shields: builtins.float
    energy: builtins.float
    def __init__(
        self,
        *,
        life: builtins.float | None = ...,
        shields: builtins.float | None = ...,
        energy: builtins.float | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["energy", b"energy", "life", b"life", "shields", b"shields"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["energy", b"energy", "life", b"life", "shields", b"shields"]) -> None: ...

global___VitalScoreDetails = VitalScoreDetails

@typing_extensions.final
class ScoreDetails(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IDLE_PRODUCTION_TIME_FIELD_NUMBER: builtins.int
    IDLE_WORKER_TIME_FIELD_NUMBER: builtins.int
    TOTAL_VALUE_UNITS_FIELD_NUMBER: builtins.int
    TOTAL_VALUE_STRUCTURES_FIELD_NUMBER: builtins.int
    KILLED_VALUE_UNITS_FIELD_NUMBER: builtins.int
    KILLED_VALUE_STRUCTURES_FIELD_NUMBER: builtins.int
    COLLECTED_MINERALS_FIELD_NUMBER: builtins.int
    COLLECTED_VESPENE_FIELD_NUMBER: builtins.int
    COLLECTION_RATE_MINERALS_FIELD_NUMBER: builtins.int
    COLLECTION_RATE_VESPENE_FIELD_NUMBER: builtins.int
    SPENT_MINERALS_FIELD_NUMBER: builtins.int
    SPENT_VESPENE_FIELD_NUMBER: builtins.int
    FOOD_USED_FIELD_NUMBER: builtins.int
    KILLED_MINERALS_FIELD_NUMBER: builtins.int
    KILLED_VESPENE_FIELD_NUMBER: builtins.int
    LOST_MINERALS_FIELD_NUMBER: builtins.int
    LOST_VESPENE_FIELD_NUMBER: builtins.int
    FRIENDLY_FIRE_MINERALS_FIELD_NUMBER: builtins.int
    FRIENDLY_FIRE_VESPENE_FIELD_NUMBER: builtins.int
    USED_MINERALS_FIELD_NUMBER: builtins.int
    USED_VESPENE_FIELD_NUMBER: builtins.int
    TOTAL_USED_MINERALS_FIELD_NUMBER: builtins.int
    TOTAL_USED_VESPENE_FIELD_NUMBER: builtins.int
    TOTAL_DAMAGE_DEALT_FIELD_NUMBER: builtins.int
    TOTAL_DAMAGE_TAKEN_FIELD_NUMBER: builtins.int
    TOTAL_HEALED_FIELD_NUMBER: builtins.int
    CURRENT_APM_FIELD_NUMBER: builtins.int
    CURRENT_EFFECTIVE_APM_FIELD_NUMBER: builtins.int
    idle_production_time: builtins.float
    """Sum of time any available structure able to produce a unit is not. The time stacks, as in, three idle barracks will increase idle_production_time three times quicker than just one."""
    idle_worker_time: builtins.float
    """Sum of time any worker is not mining. Note a worker building is not idle and three idle workers will increase this value three times quicker than just one."""
    total_value_units: builtins.float
    """Sum of minerals and vespene spent on completed units."""
    total_value_structures: builtins.float
    """Sum of minerals and vespene spent on completed structures."""
    killed_value_units: builtins.float
    """Sum of minerals and vespene of units, belonging to the opponent, that the player has destroyed."""
    killed_value_structures: builtins.float
    """Sum of minerals and vespene of structures, belonging to the opponent, that the player has destroyed."""
    collected_minerals: builtins.float
    """Sum of minerals collected by the player."""
    collected_vespene: builtins.float
    """Sum of vespene collected by the player."""
    collection_rate_minerals: builtins.float
    """Estimated income of minerals over the next minute based on the players current income. The unit is minerals per minute."""
    collection_rate_vespene: builtins.float
    """Estimated income of vespene over the next minute based on the players current income. The unit is vespene per minute."""
    spent_minerals: builtins.float
    """Sum of spent minerals at the moment it is spent. For example, this number is incremented by 50 the moment an scv is queued in a command center.  It is decremented by 50 if that unit is canceled."""
    spent_vespene: builtins.float
    """Sum of spent vespene at the moment it is spent. For example, this number is incremented by 50 when a reaper is queued but decremented by 50 if it is canceled."""
    @property
    def food_used(self) -> global___CategoryScoreDetails:
        """The following entries contains floating point values for the following catgories:
          none - There is no category defined in game data.
          army - This category includes all military units but not workers.
          economy - This category contains town halls, supply structures, vespene buildings and workers.
          technology - This category is any structure that produces units or upgrades, Barracks and Engineering Bays both fall in this category, for example.
          upgrade - This category is upgrades such as warp gate or weapons upgrades.

        Sum of food, or supply, utilized in the categories above.
        """
    @property
    def killed_minerals(self) -> global___CategoryScoreDetails:
        """Sum of enemies catagories destroyed in minerals."""
    @property
    def killed_vespene(self) -> global___CategoryScoreDetails:
        """Sum of enemies catagories destroyed in vespene."""
    @property
    def lost_minerals(self) -> global___CategoryScoreDetails:
        """ Sum of lost minerals for the player in each category."""
    @property
    def lost_vespene(self) -> global___CategoryScoreDetails:
        """Sum of lost vespene for the player in each category."""
    @property
    def friendly_fire_minerals(self) -> global___CategoryScoreDetails:
        """Sum of the lost minerals via destroying the players own units/buildings."""
    @property
    def friendly_fire_vespene(self) -> global___CategoryScoreDetails:
        """Sum of the lost vespene via destroying the players own units/buildings."""
    @property
    def used_minerals(self) -> global___CategoryScoreDetails:
        """Sum of used minerals for the player in each category for each existing unit or upgrade. Therefore if a unit died worth 50 mierals this number will be decremented by 50."""
    @property
    def used_vespene(self) -> global___CategoryScoreDetails:
        """Sum of used vespene for the player in each category. Therefore if a unit died worth 50 vespene this number will be decremented by 50."""
    @property
    def total_used_minerals(self) -> global___CategoryScoreDetails:
        """Sum of used minerals throughout the entire game for each category. Unliked used_minerals, this value is never decremented."""
    @property
    def total_used_vespene(self) -> global___CategoryScoreDetails:
        """Sum of used vespene throughout the entire game for each category. Unliked used_vespene, this value is never decremented."""
    @property
    def total_damage_dealt(self) -> global___VitalScoreDetails:
        """Sum of damage dealt to the player's opponent for each category."""
    @property
    def total_damage_taken(self) -> global___VitalScoreDetails:
        """Sum of damage taken by the player for each category."""
    @property
    def total_healed(self) -> global___VitalScoreDetails:
        """Sum of health healed by the player. Note that technology can be healed (by queens) or repaired (by scvs)."""
    current_apm: builtins.float
    """Recent raw APM."""
    current_effective_apm: builtins.float
    """Recent effective APM."""
    def __init__(
        self,
        *,
        idle_production_time: builtins.float | None = ...,
        idle_worker_time: builtins.float | None = ...,
        total_value_units: builtins.float | None = ...,
        total_value_structures: builtins.float | None = ...,
        killed_value_units: builtins.float | None = ...,
        killed_value_structures: builtins.float | None = ...,
        collected_minerals: builtins.float | None = ...,
        collected_vespene: builtins.float | None = ...,
        collection_rate_minerals: builtins.float | None = ...,
        collection_rate_vespene: builtins.float | None = ...,
        spent_minerals: builtins.float | None = ...,
        spent_vespene: builtins.float | None = ...,
        food_used: global___CategoryScoreDetails | None = ...,
        killed_minerals: global___CategoryScoreDetails | None = ...,
        killed_vespene: global___CategoryScoreDetails | None = ...,
        lost_minerals: global___CategoryScoreDetails | None = ...,
        lost_vespene: global___CategoryScoreDetails | None = ...,
        friendly_fire_minerals: global___CategoryScoreDetails | None = ...,
        friendly_fire_vespene: global___CategoryScoreDetails | None = ...,
        used_minerals: global___CategoryScoreDetails | None = ...,
        used_vespene: global___CategoryScoreDetails | None = ...,
        total_used_minerals: global___CategoryScoreDetails | None = ...,
        total_used_vespene: global___CategoryScoreDetails | None = ...,
        total_damage_dealt: global___VitalScoreDetails | None = ...,
        total_damage_taken: global___VitalScoreDetails | None = ...,
        total_healed: global___VitalScoreDetails | None = ...,
        current_apm: builtins.float | None = ...,
        current_effective_apm: builtins.float | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["collected_minerals", b"collected_minerals", "collected_vespene", b"collected_vespene", "collection_rate_minerals", b"collection_rate_minerals", "collection_rate_vespene", b"collection_rate_vespene", "current_apm", b"current_apm", "current_effective_apm", b"current_effective_apm", "food_used", b"food_used", "friendly_fire_minerals", b"friendly_fire_minerals", "friendly_fire_vespene", b"friendly_fire_vespene", "idle_production_time", b"idle_production_time", "idle_worker_time", b"idle_worker_time", "killed_minerals", b"killed_minerals", "killed_value_structures", b"killed_value_structures", "killed_value_units", b"killed_value_units", "killed_vespene", b"killed_vespene", "lost_minerals", b"lost_minerals", "lost_vespene", b"lost_vespene", "spent_minerals", b"spent_minerals", "spent_vespene", b"spent_vespene", "total_damage_dealt", b"total_damage_dealt", "total_damage_taken", b"total_damage_taken", "total_healed", b"total_healed", "total_used_minerals", b"total_used_minerals", "total_used_vespene", b"total_used_vespene", "total_value_structures", b"total_value_structures", "total_value_units", b"total_value_units", "used_minerals", b"used_minerals", "used_vespene", b"used_vespene"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["collected_minerals", b"collected_minerals", "collected_vespene", b"collected_vespene", "collection_rate_minerals", b"collection_rate_minerals", "collection_rate_vespene", b"collection_rate_vespene", "current_apm", b"current_apm", "current_effective_apm", b"current_effective_apm", "food_used", b"food_used", "friendly_fire_minerals", b"friendly_fire_minerals", "friendly_fire_vespene", b"friendly_fire_vespene", "idle_production_time", b"idle_production_time", "idle_worker_time", b"idle_worker_time", "killed_minerals", b"killed_minerals", "killed_value_structures", b"killed_value_structures", "killed_value_units", b"killed_value_units", "killed_vespene", b"killed_vespene", "lost_minerals", b"lost_minerals", "lost_vespene", b"lost_vespene", "spent_minerals", b"spent_minerals", "spent_vespene", b"spent_vespene", "total_damage_dealt", b"total_damage_dealt", "total_damage_taken", b"total_damage_taken", "total_healed", b"total_healed", "total_used_minerals", b"total_used_minerals", "total_used_vespene", b"total_used_vespene", "total_value_structures", b"total_value_structures", "total_value_units", b"total_value_units", "used_minerals", b"used_minerals", "used_vespene", b"used_vespene"]) -> None: ...

global___ScoreDetails = ScoreDetails
