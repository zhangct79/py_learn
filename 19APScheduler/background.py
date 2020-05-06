# coding:utf-8
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',filename='log2.txt',filemode='a')

def aps_task(x):
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)


scheduler = BackgroundScheduler()
scheduler.add_job(func=aps_task, args=['circle task',], trigger='interval', seconds=3, id='aps_task')
scheduler._logger = logging
scheduler.start()