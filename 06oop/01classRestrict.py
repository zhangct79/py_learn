class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print(self):
        print("%s:%s" % (self.__name, self.__score))


stu = Student("张春涛", 99)
stu.print()
stu.__score = 60
stu.print()
stu._Student__score = 60
stu.print()