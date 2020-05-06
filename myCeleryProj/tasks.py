from myCeleryProj.app import app
import time

@app.task
def taskA(x, y):
    time.sleep(2)
    c = x + y
    print("taskA:%s" % (c))
    return c

@app.task
def taskB():
    time.sleep(2)
    print("taskB")
    return "taskB"