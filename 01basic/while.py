names = ['zhangct','zhangln','lixc']

for name in names:
    print(name)

sum = 0
n = 10
while n > 0:
    if n < 5:
        break
    sum = sum + n
    n = n - 1

print(sum)