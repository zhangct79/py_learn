from functools import wraps
# 装饰工
def decorator(func):
    # 包裹方法
    def wrap_func():
        print("包起来喽")
        func()

    # 返回包裹
    return wrap_func

def decorator_2(func):
    @wraps(func)
    # 包裹方法
    def wrap_func():
        print("包起来喽")
        func()

    # 返回包裹
    return wrap_func


# 装修工来啦
@decorator
# 待包装的类
def hello():
    print("hello world!")

# 不改变函数名称的装修工来啦
@decorator_2
# 待包装的类
def hello1():
    print("hello world!")

if __name__ == "__main__":
    hello()
    print(hello.__name__)
    print("===================")
    hello1()
    print(hello1.__name__)