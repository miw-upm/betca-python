# dict: len(my_dict), my_dict['name'] or my_dict.get("name"), .keys(), .values(), .clear(), .copy()
my_dict = {"name": "John", "age": 36, "dni": 12345678}

print(my_dict.keys())

for key in my_dict.keys():
    print(my_dict[key])
    print(my_dict.get(key))

for value in my_dict.values():
    print(value)

print(my_dict['age'])
