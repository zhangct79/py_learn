#!/usr/bin/python3
# 文件名: test.py


from module import module1
from custom import module2
import module3
from module import module1

print(module1.greeting('zhangct'))
module2.hello()
module3.hello()
