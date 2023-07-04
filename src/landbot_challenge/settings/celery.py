from .base import *  # noqa

env = environ.Env()


# App
broker_url = env.str("BROKER_URL", default="")
task_serializer = "json"
accept_content = ["json"]
timezone = "UTC"
worker_max_tasks_per_child = env.int("WORKER_MAX_TASKS_PER_CHILD", default=50)
worker_max_memory_per_child = env.int("WORKER_MAX_MEMORY_PER_CHILD", default=None)
worker_concurrency = env.int("WORKER_CONCURRENCY", default=None)
task_always_eager = env.bool("CELERY_ALWAYS_EAGER", default=False)

imports = ("landbot_challenge.task_queue.worker.tasks",)

# Queues
task_default_queue = "openfinance-tasks"
worker_enable_remote_control = False
task_create_missing_queues = False
