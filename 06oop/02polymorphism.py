#多态

class Animal(object):
    def run(self):
        print("Animal is running...")

class Dog(Animal):
    def run(self):
        print("Dog is running...")

class Cat(Animal):
    def run(self):
        print("Cat is running...")

class Timer(object):
    def run(self):
        print("Start...")

def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Cat())
run_twice(Dog())
#并不是Animal的实例，python是弱类型的
run_twice(Timer())