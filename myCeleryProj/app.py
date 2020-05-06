from celery import Celery

app = Celery("myCeleryProj")
app.config_from_object("myCeleryProj.settings")

if __name__ == "__main__":
    app.start()


# pip install eventlet
# 启动 worker
# celery -A myCeleryProj.app worker -c 3 -l info -P eventlet

# 启动 worker并指定任务队列
# celery -A myCeleryProj.app worker -l info -Q app_taskA -P eventlet
# celery -A myCeleryProj.app worker -l info -Q app_taskB -P eventlet

# 启动 BEAT
# CELERY -A myCeleryProj.app beat

# 启动 flower
# CELERY -A myCeleryProj.app flower