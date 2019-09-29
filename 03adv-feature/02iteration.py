#迭代#
#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）

from collections import Iterable

print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))


d = {'a': 1, 'b': 2, 'c': 3}

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

for k,v in d.items():
    print(k,":",v)