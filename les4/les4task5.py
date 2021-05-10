from functools import reduce

multipliers = [el for el in range(100, 1001, 2)]
mul_all = reduce(lambda x, y: x * y, multipliers)

print(mul_all)
