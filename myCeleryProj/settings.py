from datetime import timedelta
from celery.schedules import crontab
from kombu import Queue, Exchange

# 时区
CELERY_TIMEZONE = 'Asia/Shanghai'
# 设置BEAT任务调度
CELERYBEAT_SCHEDULE = {
    'myCeleryProj.tasks.taskA': {
        'task': 'myCeleryProj.tasks.taskA',
        'schedule': timedelta(seconds=20),
        'args': (1, 10)
    },
    'myCeleryProj.tasks.taskB': {
        'task': 'myCeleryProj.tasks.taskB',
        'schedule': crontab(minute='*/2'),
        'args': ()
    }
}

# 中间人redis地址
BROKER_URL = "redis://:root@192.168.164.134:6379/2"
# 结果存储redis地址
CELERY_RESULT_BACKEND = "redis://:root@192.168.164.134:6379/3"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24

# worker任务导入
CELERY_IMPORTS = (
    'myCeleryProj.tasks'
)

# 设置队列
CELERY_QUEUES = (
    Queue('default', exchange=Exchange('default'), routing_key='default'),
    Queue('app_taskA', exchange=Exchange('app_taskA'), routing_key='app_taskA'),
    Queue('app_taskB', exchange=Exchange('app_taskB'), routing_key='app_taskB'),
)

# 设置路由
CELERY_ROUTES = {
    'myCeleryProj.tasks.taskA': {'queue': 'app_taskA', 'routing_key': 'app_taskA'},
    'myCeleryProj.tasks.taskB': {'queue': 'app_taskB', 'routing_key': 'app_taskB'}
}


