def cheese_shop(kind, *arguments, **keywords) -> int:  # position, *: optional, **: dict
    print('1- ', "-- Do you have any", kind, "?")
    for arg in arguments:
        print('1- ', arg)
    for key in keywords:  # .keys() is optional,
        print('1- ', key, ":", keywords[key])
    return 10


print('0- type of def: ', type(cheese_shop))

g = cheese_shop("-Position-",
                "Optional-1", "Optional-2",
                key1="Michael Palin", key2="John Cleese", key3="Cheese Shop Sketch")
print("1- ", 'cheese-shop return: ', g)


def model(index, **keywords):  # keywords: Dict[str,Any]
    print(index, 'keywords: ', keywords)
    for key in keywords:  # keywords.keys() is optional,
        print(index, key, ":", keywords[key])


my_dict = {"name": "John", "age": 36, "dni": 12345678}
model('2- ', **my_dict)  # convert key-value pairs into arguments
# model(my_dict) ERROR!!!
model('3- ', one=my_dict)


def make_increment(n):
    return lambda param: param + n


f = make_increment(665)
print('4- ', 'lambda: ', f(1))

# variable scope
global_var = 'global'


def fun0():
    non_local_var = 'nonlocal'

    def fun1():
        global global_var  # for updating
        nonlocal non_local_var  # for updating
        local_var = 'local'
        non_local_var = 'from f1'
        global_var = 'from f1'
        print('6- ', 'fun1 >> global_var:', global_var, ', non_local_var:', non_local_var, ', local_var:', local_var)

    fun1()


fun0()
