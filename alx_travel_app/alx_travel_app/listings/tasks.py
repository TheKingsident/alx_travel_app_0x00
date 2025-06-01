# listings/tasks.py
from celery import shared_task

@shared_task
def test_task():
    print("Task executed")
    return "Success"
