#yield
astr = "ABC"
alist=[1,2,3]
adict={"name":"zct", "age":18}
agenerator = (x for x in range(4, 8))

def gen(*args):
    for item in args:
        for i in item:
            yield i

new_list = gen(astr, alist, adict, agenerator)
print(list(new_list))
print("==============")

#yield from

def gen2(*args):
    for item in args:
        yield from item

new_list = gen2(astr, alist, adict, agenerator)
print(list(new_list))