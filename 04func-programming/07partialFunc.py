#偏函数
import functools
int2 = functools.partial(int, base=2)

print(int2('101101'))

max2 = functools.partial(max, 10)
print(max2(1, 3, 8))

