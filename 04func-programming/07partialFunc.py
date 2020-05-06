'''
## 偏函数
函数在执行时，要带上所有必要的参数进行调用。但是，有时参数可以在函数被调用之前提前获知。
这种情况下，一个函数有一个或多个参数预先就能用上，以便函数能用更少的参数进行调用。
'''
import functools
int2 = functools.partial(int, base=2)


print(int2('101101'))

max2 = functools.partial(max, 10)
print(max2(1, 3, 8))

