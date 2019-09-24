from functools import reduce

#Map
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
print("========================")
print(list(map(str,[1,2,3,4,5,6,7,8,9])))
print("========================")

#Reduce
def add(x, y):
    return x + y

r = reduce(add, [1, 3, 5, 7, 9])
print(r)
print("========================")

def fn(x, y):
    return x * 10 + y

r = reduce(fn, [1, 3, 5, 7, 9])
print(r)
print("========================")

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

r = reduce(fn, map(char2num, '13579'))
print(r)
print("========================")

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print(str2int('13579'))