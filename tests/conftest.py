import pytest


@pytest.fixture(scope="session")
def celery_app():
    import src.tasks.example  # noqa: F401 — run @shared_task decorators before finalize()
    from celery import Celery

    app = Celery("leisurely_test")
    app.conf.update(
        broker_url="memory://",
        result_backend="cache+memory://",
        task_always_eager=True,
        task_serializer="json",
        result_serializer="json",
        accept_content=["json"],
    )

    app.finalize()
    app.set_default()
    app.set_current()
    yield app
    app.close()


@pytest.fixture(autouse=True)
def _enforce_test_app(celery_app):
    celery_app.set_current()
    celery_app.set_default()
