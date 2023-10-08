import sys

if sys.platform != "win32":
    ABDAY_1: int
    ABDAY_2: int
    ABDAY_3: int
    ABDAY_4: int
    ABDAY_5: int
    ABDAY_6: int
    ABDAY_7: int

    ABMON_1: int
    ABMON_2: int
    ABMON_3: int
    ABMON_4: int
    ABMON_5: int
    ABMON_6: int
    ABMON_7: int
    ABMON_8: int
    ABMON_9: int
    ABMON_10: int
    ABMON_11: int
    ABMON_12: int

    LC_MESSAGES: int

    DAY_1: int
    DAY_2: int
    DAY_3: int
    DAY_4: int
    DAY_5: int
    DAY_6: int
    DAY_7: int

    ERA: int
    ERA_D_T_FMT: int
    ERA_D_FMT: int
    ERA_T_FMT: int

    MON_1: int
    MON_2: int
    MON_3: int
    MON_4: int
    MON_5: int
    MON_6: int
    MON_7: int
    MON_8: int
    MON_9: int
    MON_10: int
    MON_11: int
    MON_12: int

    CODESET: int
    D_T_FMT: int
    D_FMT: int
    T_FMT: int
    T_FMT_AMPM: int
    AM_STR: int
    PM_STR: int

    RADIXCHAR: int
    THOUSEP: int
    YESEXPR: int
    NOEXPR: int
    CRNCYSTR: int
    ALT_DIGITS: int

    def nl_langinfo(__key: int) -> str: ...
