import threading

local_class = threading.local()

def process_sutdent():
    student = local_class.student
    print('Hello, %s in (%s)' % (student, threading.current_thread().name))

def run_thread(name):
    local_class.student = name
    process_sutdent()

t1 = threading.Thread(target=run_thread, name="Thread-A", args=('zhangct',))
t2 = threading.Thread(target=run_thread, name="Thread-B", args=('zhangln',))
t1.start()
t2.start()
t1.join()
t2.join()
