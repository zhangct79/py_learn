s = set([1,2,3,4,3,2])
print(s)

s.add(5)
s.add(4)
print(s)

s.remove(2)
print(s)

jenkins = {1,2,4,5}
mysql = {1,2,3}

# 增加4,5，删除3
print(jenkins - mysql)
print(mysql - jenkins)