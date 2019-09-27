from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import ChainMap
from collections import Counter

#namedtuple
Point = namedtuple("Point", ['x', 'y'])
p = Point(1, 2)
print(type(p))
print("(%s, %s)" % (p.x, p.y))
print("==================")

#deque
q = deque(['a', 'b', 'c'])
q.append("2")
q.appendleft('1')
print(q)
print("==================")

#defaultdict
dd = defaultdict(lambda : 'N/A')
dd['key1'] = "abc"
print(dd["key1"],"|",dd["key2"])
print("==================")

#OrderedDict
d = dict({"a":1, "b":2, "c":3})
print(d)
od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
print(od)
print(od.popitem(last=False))
print(od)
print("==================")

#ChainMap
dict1 = {"u": "zct"}
dict2 = {"u": "gwr"}
chain = ChainMap(dict1, dict2)
print("-u:%s" % chain['u'])
print("==================")
#Counter
c = Counter()
for ch in "programming":
    c[ch] = c[ch] + 1
print(c)