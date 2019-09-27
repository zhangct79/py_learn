from urllib import request, parse

with request.urlopen('https://www.baidu.com/') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    print("-------------------")
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print("-------------------")
    print('Data:', data.decode('utf-8'))
