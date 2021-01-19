def fun():
    pass


class Clazz:
    def show(self):
        print(self, 'show')


print(type(fun))
print(type(Clazz))

var = 23
var_2 = 23.4
var_3 = fun
var_4: float
var_5: fun = fun
var_5()
var_6: Clazz = Clazz()
var_6.show()


print(type(var))
print(type(var_2))
print(type(var_3))
# error: print(type(var4)) # var4 is undefined
print(type(var_5))
print(type(var_6))

