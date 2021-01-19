my_list = [1, 2, 3, 4, 5]

__iter = iter(my_list)

x = map(lambda item: item + 1, filter(lambda item: item % 2 == 0, __iter))

print(list(x))
