#列表生成器#
import os

L = list(range(1,11))
print(L)

L1 = [x * x for x in range(1,11)]
print(L1)

L2 = [m + n for m in "ABC" for n in "XYZ"]
print(L2)

print([d for d in os.listdir(".")])