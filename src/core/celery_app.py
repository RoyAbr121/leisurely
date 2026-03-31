from celery import Celery

from src.core.config import settings

celery_app = Celery(
    "leisurely",
    broker=settings.celery_broker_url,
    include=["src.tasks.example"],
)

celery_app.conf.update(
    result_backend=settings.celery_result_backend,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    result_expires=3600,
    task_track_started=True,
    task_acks_late=True,
    worker_prefetch_multiplier=1,
)
