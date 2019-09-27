import threading

balance = 0
lock = threading.Lock()

def change(n):
    global balance
    balance = balance + n
    balance = balance - n

def loop(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change(n)
        finally:
            lock.release()

t1 = threading.Thread(target=loop, args=(5,))
t2 = threading.Thread(target=loop, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()

print(balance)