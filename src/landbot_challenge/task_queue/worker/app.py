import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "landbot_challenge.settings.base")
app = Celery("worker")
app.config_from_object("landbot_challenge.settings.celery")
app.conf.timezone = "UTC"
app.conf.task_ignore_result = True
