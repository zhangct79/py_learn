#装饰器
import functools

def log(func):
    def wrapper(*args, **kw):
        print("call %s()" % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2019-9-24')

f = now
print(f.__name__)
f()
