from celery import shared_task


@shared_task(name="task_clear_session")
def task_clear_session():
    from django.core.management import call_command
    call_command('clearsessions')
