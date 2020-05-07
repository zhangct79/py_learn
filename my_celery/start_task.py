from my_celery.tasks import *

result = add.delay(12,12)

print(result.get())
print(result.successful())

