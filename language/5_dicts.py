# dict: len(my_dict), my_dict['name'] or my_dict.get("name"), .keys(), .values(), .clear(), .copy()
my_dict = {"name": "John", "age": 36, "dni": 12345678, "role": None}
print('1- ', my_dict.keys())
print('1- ', my_dict.values())

for key in my_dict.keys():
    print('2- ', key, ':', my_dict[key])
    print('2- ', key, ':', my_dict.get(key))

print('3- ', my_dict['age'])

my_dict.setdefault('name', 'only-if-not-exist')
my_dict.setdefault('new', 'new-value')
print('4- ', my_dict.keys(), '::', my_dict.values())
print('5- ', my_dict)
