#带参数的装饰器
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s()" % (text,func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log("execute")
def hello(name):
    print("hello %s" % name)

f = hello
print(f.__name__)
f("zct");