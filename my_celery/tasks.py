from celery import Celery


app = Celery('app2', broker='redis://:root@192.168.164.134:6379/0', backend='redis://:root@192.168.164.134:6379/0')

@app.task
def add(x, y):
    print("running...")
    return x + y


#celery -A celery_tasks.tasks worker -l info -P eventlet