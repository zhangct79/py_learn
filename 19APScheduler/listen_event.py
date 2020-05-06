# coding:utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',filename='log1.txt',filemode='a')

def aps_task(x):
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)

def date_task(x):
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)
    print(1/0)

def my_listener(event):
    if event.exception:
        print('task is wrong!!!!!!!')
    else:
        print('task is right...')

scheduler = BlockingScheduler()
scheduler.add_job(func=date_task, args=['once task, error',], next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=15), id='date_task')
scheduler.add_job(func=aps_task, args=['circle task',], trigger='interval', seconds=3, id='aps_task')
scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
scheduler._logger = logging

scheduler.start()