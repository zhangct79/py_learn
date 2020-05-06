from functools import wraps

def decorator(func):
    @wraps(func) #保留原有函数的名称、注释等信息
    def wrap_func(*args, **kw):
        print("你想要执行的代码")
        return func(*args,**kw)

    return wrap_func

@decorator
def sum(*args, **kwargs):
    for k in kwargs:
        print(k+":"+str(kwargs[k]))

    c = 0
    for a in args:
        c = c + a

    return c

n = sum()
print(n)
print("==============")
n = sum(1,2,3,4,5,name="zhangct",age=30)
print(n)