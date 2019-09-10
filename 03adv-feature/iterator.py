#迭代器
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

from collections import Iterator
from collections import Iterable

print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance([], Iterable))
