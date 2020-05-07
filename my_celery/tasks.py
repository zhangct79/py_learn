from celery import Celery


app = Celery('app2', broker='redis://:root@192.168.164.134:6379/2', backend='redis://:root@192.168.164.134:6379/3')

@app.task
def add(x, y):
    print("running...")
    return x + y


#celery -A my_celery.tasks worker -l info -P eventlet