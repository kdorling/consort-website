from celery import shared_task
from django.core import management

from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)

@shared_task()
def update_index():
   logger.info("Updating search index")
   management.call_command("update_index")
