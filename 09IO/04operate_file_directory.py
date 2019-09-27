import os
import shutil

print(os.name)
print(os.environ.get('PATH'))
print("===============")

print(os.path.abspath('.'))
#创建目录的完整路径
p = os.path.join('D:\PycharmProjects\py_learn\\09IO', 'testdir')
#删除目录
os.rmdir(p)
#创建目录
os.mkdir(p)

#文件路径拆分
print(os.path.split("D:\PycharmProjects\py_learn\\09IO\\files\\test.txt"))
print(os.path.splitext("D:\PycharmProjects\py_learn\\09IO\\files\\test.txt"))
print("===============")

#os.rename("D:\PycharmProjects\py_learn\\09IO\\files\\test.py", "D:\PycharmProjects\py_learn\\09IO\\files\\test.txt")
