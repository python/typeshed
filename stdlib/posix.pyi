import sys

if sys.platform != "win32":
    # Actually defined here, but defining in os allows sharing code with windows
    from os import (
        CLD_CONTINUED as CLD_CONTINUED,
        CLD_DUMPED as CLD_DUMPED,
        CLD_EXITED as CLD_EXITED,
        CLD_TRAPPED as CLD_TRAPPED,
        EX_CANTCREAT as EX_CANTCREAT,
        EX_CONFIG as EX_CONFIG,
        EX_DATAERR as EX_DATAERR,
        EX_IOERR as EX_IOERR,
        EX_NOHOST as EX_NOHOST,
        EX_NOINPUT as EX_NOINPUT,
        EX_NOPERM as EX_NOPERM,
        EX_NOTFOUND as EX_NOTFOUND,
        EX_NOUSER as EX_NOUSER,
        EX_OK as EX_OK,
        EX_OSERR as EX_OSERR,
        EX_OSFILE as EX_OSFILE,
        EX_PROTOCOL as EX_PROTOCOL,
        EX_SOFTWARE as EX_SOFTWARE,
        EX_TEMPFAIL as EX_TEMPFAIL,
        EX_UNAVAILABLE as EX_UNAVAILABLE,
        EX_USAGE as EX_USAGE,
        F_LOCK as F_LOCK,
        F_OK as F_OK,
        F_TEST as F_TEST,
        F_TLOCK as F_TLOCK,
        F_ULOCK as F_ULOCK,
        O_APPEND as O_APPEND,
        O_ASYNC as O_ASYNC,
        O_CREAT as O_CREAT,
        O_DIRECT as O_DIRECT,
        O_DIRECTORY as O_DIRECTORY,
        O_DSYNC as O_DSYNC,
        O_EXCL as O_EXCL,
        O_LARGEFILE as O_LARGEFILE,
        O_NDELAY as O_NDELAY,
        O_NOATIME as O_NOATIME,
        O_NOCTTY as O_NOCTTY,
        O_NOFOLLOW as O_NOFOLLOW,
        O_NONBLOCK as O_NONBLOCK,
        O_RDONLY as O_RDONLY,
        O_RDWR as O_RDWR,
        O_RSYNC as O_RSYNC,
        O_SYNC as O_SYNC,
        O_TRUNC as O_TRUNC,
        O_WRONLY as O_WRONLY,
        P_ALL as P_ALL,
        P_PGID as P_PGID,
        stat_result as stat_result,
        P_PID as P_PID,
        PRIO_PGRP as PRIO_PGRP,
        PRIO_PROCESS as PRIO_PROCESS,
        PRIO_USER as PRIO_USER,
        R_OK as R_OK,
        RTLD_GLOBAL as RTLD_GLOBAL,
        RTLD_LAZY as RTLD_LAZY,
        RTLD_LOCAL as RTLD_LOCAL,
        RTLD_NODELETE as RTLD_NODELETE,
        RTLD_NOLOAD as RTLD_NOLOAD,
        RTLD_NOW as RTLD_NOW,
        SCHED_BATCH as SCHED_BATCH,
        SCHED_FIFO as SCHED_FIFO,
        SCHED_IDLE as SCHED_IDLE,
        SCHED_OTHER as SCHED_OTHER,
        SCHED_RESET_ON_FORK as SCHED_RESET_ON_FORK,
        SCHED_RR as SCHED_RR,
        SCHED_SPORADIC as SCHED_SPORADIC,
        SEEK_DATA as SEEK_DATA,
        SEEK_HOLE as SEEK_HOLE,
        TMP_MAX as TMP_MAX,
        W_OK as W_OK,
        WCONTINUED as WCONTINUED,
        WCOREDUMP as WCOREDUMP,
        WEXITED as WEXITED,
        WEXITSTATUS as WEXITSTATUS,
        WIFCONTINUED as WIFCONTINUED,
        WIFEXITED as WIFEXITED,
        WIFSIGNALED as WIFSIGNALED,
        WIFSTOPPED as WIFSTOPPED,
        WNOHANG as WNOHANG,
        WNOWAIT as WNOWAIT,
        WSTOPPED as WSTOPPED,
        WSTOPSIG as WSTOPSIG,
        WTERMSIG as WTERMSIG,
        WUNTRACED as WUNTRACED,
        X_OK as X_OK,
        listdir as listdir,
        times_result as times_result,
        uname_result as uname_result,
    )

    if sys.platform == "linux":
        from os import (
            GRND_NONBLOCK as GRND_NONBLOCK,
            GRND_RANDOM as GRND_RANDOM,
            RTLD_DEEPBIND as RTLD_DEEPBIND,
            XATTR_CREATE as XATTR_CREATE,
            XATTR_REPLACE as XATTR_REPLACE,
            XATTR_SIZE_MAX as XATTR_SIZE_MAX,
        )
    if sys.platform != "darwin":
        from os import (
            POSIX_FADV_DONTNEED as POSIX_FADV_DONTNEED,
            POSIX_FADV_NOREUSE as POSIX_FADV_NOREUSE,
            POSIX_FADV_NORMAL as POSIX_FADV_NORMAL,
            POSIX_FADV_RANDOM as POSIX_FADV_RANDOM,
            POSIX_FADV_SEQUENTIAL as POSIX_FADV_SEQUENTIAL,
            POSIX_FADV_WILLNEED as POSIX_FADV_WILLNEED,
        )

    NGROUPS_MAX: int
    O_ACCMODE: int
    ST_APPEND: int
    ST_MANDLOCK: int
    ST_NOATIME: int
    ST_NODEV: int
    ST_NODIRATIME: int
    ST_NOEXEC: int
    ST_NOSUID: int
    ST_RDONLY: int
    ST_RELATIME: int
    ST_SYNCHRONOUS: int
    ST_WRITE: int

    if sys.version_info >= (3, 8):
        from os import posix_spawn as posix_spawn, posix_spawnp as posix_spawnp
    environ: dict[bytes, bytes]
