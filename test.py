import time


def hi(name="yasoob"):
    return "hi " + name


print("1:",hi())
# output: 'hi yasoob'

# 我们甚至可以将一个函数赋值给一个变量，比如
greet = hi
# 我们这里没有在使用小括号，因为我们并不是在调用hi函数
# 而是在将它放在greet变量里头。我们尝试运行下这个

print("2:",greet())
# output: 'hi yasoob'

time.sleep(1)

# 如果我们删掉旧的hi函数，看看会发生什么！
try:
    del hi
    print("3:",hi())
    # outputs: NameError
except Exception as e:
    print(e)

print("4:",greet())
# outputs: 'hi yasoob'