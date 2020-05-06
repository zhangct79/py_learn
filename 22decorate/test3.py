from functools import wraps

def decorator(func):
    @wraps(func) #保留原有函数的名称、注释等信息
    def wrap_func(*args, **kw):
        print("你想要执行的代码")
        return func(*args,**kw)

    return wrap_func

@decorator
def sum(x=1,y=2, name='nonemous'):
    return x + y, name

z, n = sum()
print(z,n)
print("===============")
z, n = sum(x=3,y=2,name='zhangct')
print(z,n)