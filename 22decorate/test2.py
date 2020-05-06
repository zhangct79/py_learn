def func(*args, **kw):
    print(args,kw)
    print("============")
    for a in  args:
        print(a);

    print("============")
    for key in kw:
        print(key+":"+str(kw[key]))


func(1,2,3,{"name":"zhangct","name":"zhangln","age":30},city="harbin",databases=15)