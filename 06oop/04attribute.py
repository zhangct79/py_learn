class Student(object):
    name = "Student"

s1 = Student()
s2 = Student()

print(Student.name)
print(s1.name)
print(s2.name)
print('================')
s1.name = "zhangct"
print(s1.name)
print(s2.name)
print('================')
del s1.name
print(s1.name)
print(s2.name)
print(Student.name)
