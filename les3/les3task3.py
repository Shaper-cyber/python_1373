def my_func(a, b, c):
    list_stroke = [a, b, c]
    list_stroke = sorted(list_stroke)
    list_stroke.pop(0)
    return sum(list_stroke)


print(my_func(-1, 2, 1))
