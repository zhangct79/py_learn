#函数参数#

#1.默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5))
print(power(5, 3))
print("======================")

#2.可变参数(自动组装成tuple）
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum

print(calc(1,2))
print(calc(1,2,3))
nums = [1,3,5]
print(calc(*nums))
print("======================")

#3.关键字参数（自动组装成dict）
def person(name, age, **kw):
    print("name:",name,"age",age,"other",kw)

person("zhangct", 40)
person("zhangct", 40, city="haerbin", birthday="1979-01-05")
extra = {"city":"haerbin", "birthday":"1979-01-05"}
person("zhangct", 40, **extra)