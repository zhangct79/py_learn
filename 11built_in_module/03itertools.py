import itertools
import time


#takewhile
naturals = itertools.count(1)
ns = itertools.takewhile(lambda x: x < 10, naturals)
for n in ns:
    print(n)
    time.sleep(1)

#repeat
ns = itertools.repeat("A", 2)
for n in ns:
    print(n)
    time.sleep(1)

#cycle
cs = itertools.cycle("ABC")
for c in cs:
    print(c)
    time.sleep(1)

#count
naturals = itertools.count(1)
for n in naturals:
    print(n)
    time.sleep(1)

