#字生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        num = yield average
        count = count + 1
        total = total + num
        average = total / count

#委托生成器
def proxy_gen():
    while True:
        yield from average_gen()

#调用方
def main():
    calc_average = proxy_gen()
    next(calc_average)
    print(calc_average.send(10))
    print(calc_average.send(20))
    print(calc_average.send(30))

if __name__ == "__main__":
    main()
