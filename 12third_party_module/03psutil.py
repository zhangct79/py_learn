import psutil

print(psutil.virtual_memory())
print(psutil.swap_memory())


for x in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))

