#继承

class Animal(object):
    def run(self):
        print("Animal is running...")

class Dog(Animal):
    def run(self):
        print("Dog is running...")

class Cat(Animal):
    pass

d = Dog()
c = Cat()

d.run()
c.run()

print(isinstance(c, Animal))
print(isinstance(c, Cat))
print(isinstance(c, Dog))