from celery import current_app

# Create your views here.
from django.views import View


class TaskView(View):
    def get(self):
        pass

    @staticmethod
    def test_task(value='wasim'):
        print('was')
        b = current_app.send_task(
            'task_list_2',
            args=(value,),
            queue='default'
        )

        c = current_app.send_task(
            'task_list_2',
            args=('value',),
            queue='single_queue'
        )
        print(b.status, c.status)
