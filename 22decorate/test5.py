from functools import wraps

def decorator(func):
    '''
    装修工
    :param func: 要装饰的函数
    :return: 装饰后的函数
    '''
    def wrap_func(*args, **kw):
        '''
        包装函数
        :param args:可变参数，自动组装成tuple
        :param kw:关键字参数，自动组装成dictionary
        :return:要装饰函数的返回值
        '''
        print("你想要执行的代码")
        return func(*args,**kw)

    return wrap_func


def sum(*args, **kwargs):
    '''
    合计函数
    :param args:可变参数，传递要合计的整数
    :param kwargs: 关键字参数，认可扩展信息
    :return:
    '''
    for k in kwargs:
        print(k+":"+str(kwargs[k]))

    c = 0
    for a in args:
        c = c + a

    return c

n = decorator(sum)()
print(n)
print("==============")
n = decorator(sum)(1,2,3,4,5,name="zhangct",age=30)
print(n)