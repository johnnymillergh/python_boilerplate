from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from loguru import logger
from tzlocal import get_localzone

from python_boilerplate.common.common_function import get_cpu_count
from python_boilerplate.common.profiling import elapsed_time

# https://apscheduler.readthedocs.io/en/3.x/userguide.html#configuring-the-scheduler
# https://crontab.guru/

jobstores = {"default": MemoryJobStore()}
executors = {"default": ThreadPoolExecutor(max_workers=get_cpu_count() * 2)}
job_defaults = {"coalesce": False, "max_instances": 3}


scheduler = BackgroundScheduler(
    jobstores=jobstores,
    executors=executors,
    job_defaults=job_defaults,
    timezone=get_localzone(),
)


def configure() -> None:
    """
    Configure APScheduler.
    """
    logger.warning(f"APSScheduler configured: {scheduler}")
    scheduler.start()


@elapsed_time("WARNING")
def cleanup() -> None:
    """
    Clean up APScheduler.
    """
    logger.warning(
        f"APScheduler is being shutdown: {scheduler}, running: {scheduler.running}"
    )
    # Shutdown the job stores and executors but does not wait for any running tasks to complete.
    scheduler.shutdown(wait=False)
    logger.warning(
        f"APScheduler {scheduler} has been shutdown, running: {scheduler.running}"
    )
