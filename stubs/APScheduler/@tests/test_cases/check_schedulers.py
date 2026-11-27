from __future__ import annotations

import asyncio
from typing_extensions import assert_type

from apscheduler.job import Job
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.tornado import TornadoScheduler
from apscheduler.schedulers.twisted import TwistedScheduler

# Each scheduler takes its own options beside BaseScheduler's.
scheduler = BackgroundScheduler(daemon=False, timezone="UTC")
scheduler.configure(daemon="off", job_defaults={"coalesce": "true"})
BackgroundScheduler(dameon=False)  # type: ignore
AsyncIOScheduler(event_loop=asyncio.new_event_loop())
AsyncIOScheduler(event_loop="myapp:loop")
AsyncIOScheduler(daemon=False)  # type: ignore
TornadoScheduler(io_loop="myapp:loop", timezone="UTC")
TwistedScheduler(reactor="myapp:reactor")
TwistedScheduler(io_loop=None)  # type: ignore


def tick() -> None: ...


job = scheduler.add_job(tick, "interval", seconds=5)
assert_type(job, Job)
# None names the date trigger, as it does for add_job.
assert_type(job.reschedule(None, run_date="2030-01-01"), Job)
