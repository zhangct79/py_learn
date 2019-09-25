import logging
def foo (s):
    n = int(s)
    if n==0:
        raise ValueError("错误值：%s" % s)
    return 10 / n

def bar():
    try:
        foo("0")
    except ValueError as e:
        logging.exception(e)
        raise

bar()