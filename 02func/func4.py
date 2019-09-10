#递归函数#

#1.普通递归
def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n - 1)
print(fact(1))
print(fact(5))
print(fact(100))
#print(fact(1000))#RecursionError: maximum recursion depth exceeded in comparison
print("========================")


#2.尾递归(防止栈溢出)，尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
def fact_tail(n):
    return fact_iter(n, 1)

def fact_iter(n, result):
    if n==1:
        return result
    return fact_iter(n - 1, n * result)

#print(fact_tail(1000))
