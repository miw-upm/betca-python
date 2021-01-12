# functions
# If / and * are not present, arguments may be passed to a function by position or by keyword.


def cheese_shop(kind, *arguments, **keywords) -> int:  # keywords: Dict[str,Any]
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    for key in keywords:  # .keys() is optional,
        print(key, ":", keywords[key])
    for item in keywords.items():
        print(item[0], ':', item[1])
    return 10


g = cheese_shop("Limburger", "It's very runny, sir.",
                "It's really very, VERY runny, sir.",
                shopkeeper="Michael Palin",
                client="John Cleese",
                sketch="Cheese Shop Sketch")
print('cheese_shop: ', g)


def model(**keywords):  # keywords: Dict[str,Any]
    print('keywords ', keywords)


my_dict = {"name": "John", "age": 36, "dni": 12345678}
model(**my_dict)  # convert key-value pairs into arguments


def make_increment(n):
    return lambda param: param + n


f = make_increment(42)
print('lmbda: ', f(1))

# variable scope
glb = 'global'


def fun0():
    nl = 'nonlocal'

    def fun1():
        global glb  # for updating
        nonlocal nl  # for updating
        loc = 'local'
        print('fun1: ', glb, ':', nl, ':', loc)
        nl = 'from local'
        glb = 'from local'

    fun1()


fun0()
print('glb: ', glb)
