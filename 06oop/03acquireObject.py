import types

#type
print(type(123)==int)
print(type('abc')==str)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)
print(type(x for x in range(10)))
print("===================")

#isinstance
print(isinstance([1,2,3], (list, tuple)))
print(isinstance((1,2,3), (list, tuple)))
print("===================")

#dir
print(dir(object))
print("ABC".__len__())
print(len("ABC"))
print("ABC".lower())

print("###############")
class MyDog(object):
    def __len__(self):
        return 10
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

dog = MyDog()
print(len(dog))
print(dog.__len__())
print(dir(dog))
print(hasattr(dog, 'x'))
print(getattr(dog, 'x'))
print(getattr(dog, 'z', 404))
setattr(dog, 'x', 19)
print(getattr(dog, 'x'))

print(hasattr(dog, 'power'))
fn = getattr(dog, 'power')
print(fn())