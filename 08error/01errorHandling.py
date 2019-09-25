try:
    print("try...")
    r = 10 / 0
    print("result:",r)
except ZeroDivisionError as e:
    print("except:", e)
finally:
    print("finally...")
print("============1END=================")


try:
    print("try...")
    r = 10 / int('a')
    print("result:", r)
except ZeroDivisionError as e:
    print("except:", e)
except ValueError as e:
    print("except:", e)
finally:
    print("finally...")
print("============2END=================")

try:
    print("try...")
    r = 10 / int('2')
    print("result:", r)
except ZeroDivisionError as e:
    print("except:", e)
except ValueError as e:
    print("except:", e)
else:
    print("no error")
finally:
    print("finally...")
print("============3END=================")
