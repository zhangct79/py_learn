class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print(self):
        print("%s:%s" % (self.name, self.score))


stu = Student("张春涛", 99)
stu.print()
stu.score = 60
stu.print()

print(stu)