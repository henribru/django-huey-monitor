import logging
import time

from huey import crontab
from huey.contrib.djhuey import periodic_task, task


logger = logging.getLogger(__name__)


@task()
def raise_error_task(error_class_name, msg):
    logger.info('Raise %r with msg=%r', error_class_name, msg)
    ErrorClass = __builtins__[error_class_name]
    raise ErrorClass(msg)


@task()
def delay_task(name='<no-name>', sleep=3):
    logger.info('delay called from %r sleep %r sec...', name, sleep)
    time.sleep(sleep)
    logger.info('delay %r sleep ended.', name)


@periodic_task(crontab(minute='1'), context=True)
def one_minute_test_task(task):
    logger.info('one_minute_test_task UUID: %s', task.id)
