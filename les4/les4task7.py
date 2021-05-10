from functools import reduce


def fact(n):
    a = [el for el in range(1, n+1)]
    factor = reduce(lambda x, y: x * y, a)
    yield factor


for i in fact(4):
    print(i)
