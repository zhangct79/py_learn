with open("D:/PycharmProjects/py_learn/09IO/files/test.txt", 'r') as f:
    for line in f.readlines():
        print(line.strip())
        print("------------")

with open("D:/PycharmProjects/py_learn/09IO/files/test.txt", 'rb') as f:
    print(f.read())