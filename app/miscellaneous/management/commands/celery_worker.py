import shlex
import subprocess
import sys

from django.core.management.base import BaseCommand
from django.utils import autoreload


def restart_celery():
    celery_worker_cmd = "celery -A consort worker"
    cmd = f'pkill -f "{celery_worker_cmd}"'
    if sys.platform == "win32":
        cmd = "taskkill /f /t /im celery.exe"

    subprocess.call(shlex.split(cmd))
    #subprocess.call(shlex.split(f"{celery_worker_cmd} --loglevel=info --concurrency=2"))
    subprocess.call(shlex.split(f"celery -A consort multi start high_priority low_priority --loglevel=info --concurrency=1 -Q:high_priority high_priority,default -Q:low_priority low_priority"))


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting celery worker with autoreload...")
        autoreload.run_with_reloader(restart_celery)
