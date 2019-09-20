#生成器#

g = (x * x for x in range(1,11))
print(g)
print(next(g))
print(next(g))
print("===========")

for x in g:
    print(x)
print("===========")

#斐波那契数列函数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return "done"

fib(6)
print("===========")

#斐波那锲数列生成器
def fib_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return "done"

print(fib_generator(6))
for x in fib_generator(6):
    print(x)


print("===========")
g = fib_generator(6)
while True:
    try:
        x = next(g)
        print(x)
    except StopIteration as e:
        print("Generator return value : ", e.value)
        break

