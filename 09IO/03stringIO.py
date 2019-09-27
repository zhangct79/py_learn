from io import StringIO

#StringIO
f = StringIO("Hello!\nHi!\nGreeting!")
print(f.getvalue())
print("1====================")

while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
print("2====================")

from io import BytesIO
#BytesIO
f = BytesIO()
f.write("中文".encode('utf-8'))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
