from __future__ import absolute_import

import time

from celery import shared_task


@shared_task()
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True


@shared_task()
def periodic_task():
    print('wasim')
    return True


@shared_task(name='task_list_2')
def test_app(a):
    print('2nd task', a)
    return True


@shared_task()
def test_app2(a):
    print(a)
    return True
