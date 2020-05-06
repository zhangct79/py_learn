from myCeleryProj.tasks import *

r1 = taskA.apply_async(args=(1,3))
r2 = taskB.delay()

print(r1)
print(r2)

while True:
    time.sleep(1)
    if r1.successful() and r2.successful():
        print(r1.get())
        print(r2.get())
        print("执行成功")
        break
    else:
        print("任务还未执行完成")

