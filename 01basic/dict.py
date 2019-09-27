import mysql.connector

student = {'zhangct':120, "zhangln":98,"lixc":100}
print(student["zhangct"])

student["zhangct"] = 119
print(student)

print(student.get("zhangln"))