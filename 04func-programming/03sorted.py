l = [36, 5, -12, 9, -21]

print(sorted(l))
print(sorted(l, key=abs))
print(sorted(l, key=abs, reverse=True))
print("=============")

l = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(l))
print(sorted(l, key = str.lower))
print(sorted(l, key = str.lower, reverse=True))