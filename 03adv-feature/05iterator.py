#迭代器
#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#生成器都是Iterator（迭代器）对象

from collections import Iterator
from collections import Iterable

print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance([], Iterable))
