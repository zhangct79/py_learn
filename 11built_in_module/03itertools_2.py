import itertools

#chain
for c in itertools.chain("ABC",'XYZ'):
    print(c)
print("===========")

for key, group in itertools.groupby("AaAbCBcBCBAAaaAADD",lambda x: x.upper()):
    print("%s[%s]" % (key, list(group)))
print("===========")


for key, group in itertools.groupby(sorted("AaAbCBcBCBAAaaAADD",key=str.upper),lambda x: x.upper()):
    print("%s[%s]" % (key, list(group)))