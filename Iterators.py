# Iterators

l = [1,2,3,4,5]

it = iter(l)

print(it.__next__())
it.__next__()
print(next(it))
it.__next__()
print(it.__next__())
