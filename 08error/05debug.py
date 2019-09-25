import logging
def foo (s):
    n = int(s)
    assert n !=0, "n is zero"
    return 10 / n

def bar():
    foo("0")

bar()