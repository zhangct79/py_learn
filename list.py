person = ['zhangct', 'guwenren', 'zhanglina']
print(person,len(person),person[1],person[-1])

person[1] = 'abc'
person.append("lixiaochun")
print(person)

person.insert(0,"jack")
print(person)

person.pop()
print(person)