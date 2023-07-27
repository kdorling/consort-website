import functools
import os

from celery import Celery, Task, shared_task
from celery.utils.time import get_exponential_backoff_interval

from django.conf import settings
from django.db import transaction

# this code copied from manage.py
# set the default Django settings module for the 'celery' app.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'consort.settings.dev')

# you can change the name here
app = Celery("consort_tasks")

# read config from Django settings, the CELERY namespace would make celery
# config keys has `CELERY` prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# discover and load tasks.py from from all registered Django apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


class BaseTaskWithRetry(Task):
    autoretry_for = (TypeError,KeyError)
    max_retries = 5
    retry_backoff = 600
    retry_backoff_max = 3600
    retry_jitter = True


class transaction_task_with_retry:
    EXCEPTION_BLOCK_LIST = (
        IndexError,
        KeyError,
        TypeError,
        UnicodeDecodeError,
        ValueError,
    )

    def __init__(self, *args, **kwargs):
        self.task_args = args
        self.task_kwargs = kwargs

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper_func(*args, **kwargs):
            try:
                with transaction.atomic():
                    # add Django db transaction support
                    return func(*args, **kwargs)
            except self.EXCEPTION_BLOCK_LIST:
                # do not retry for those exceptions
                raise
            except Exception as e:
                # here we add Exponential Backoff just like Celery
                countdown = self._get_retry_countdown(task_func)
                raise task_func.retry(exc=e, countdown=countdown)

        task_func = shared_task(*self.task_args, **self.task_kwargs)(wrapper_func)
        return task_func

    def _get_retry_countdown(self, task_func):
        retry_backoff = int(
            self.task_kwargs.get('retry_backoff', 60)
        )
        retry_backoff_max = int(
            self.task_kwargs.get('retry_backoff_max', 600)
        )
        retry_jitter = self.task_kwargs.get(
            'retry_jitter', True
        )

        countdown = get_exponential_backoff_interval(
            factor=retry_backoff,
            retries=task_func.request.retries,
            maximum=retry_backoff_max,
            full_jitter=retry_jitter
        )

        return countdown
