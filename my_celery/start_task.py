from tasks import add

result = add.delay(12,12)

print(result.get())
print(result.successful())

