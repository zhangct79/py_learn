def consumer():
    while True:
        mm = yield '200 OK'
        print('[CONSUMER] Consuming %s...' % mm)

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)

c = consumer()
produce(c)