# Generator

def fun():
    n = 1
    while(n<=10):
        yield n * n
        n += 1
vals = fun()
print(type(vals))
# print(vals.__next__())
# print(vals.__next__())
# print(vals.__next__())
# print(vals.__next__())
# print(vals.__next__())
for i in vals:
    print(i)