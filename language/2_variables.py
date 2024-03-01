from datetime import date

# types: str, int, float, complex, bool, list, tuple, range, dict, set, frozenset, bytes, bytearray, memoryview
str_var: str  # STATIC var is not defined, it is not possible to use until creating with '='
# print(str_var) ERROR!!!
str_var = 'string'  # DYNAMIC. str_var is created. It is possible use '...' or "...", esc==\

var = 5  # var is created, it is var = int(5)
null_var = None  # None is null and var is created
casting_var = str(var)  # casting: str(), float()...
i = 3 + 2j  # complex: i.real, i.imag ...
var = 'other'  # dynamic type: from int to str

# One line: one sentence. With \ the line continue
large_str = '''line one\
line one & end of line
other line'''  # '\' without end of line
print('1- ', large_str[-10:-5])  # Use negative indexes to start from the end of the string
print('2- ', large_str[0:5])
print('3- ', large_str[5:])
print('4- ', large_str[:])  # it is copy
age = 36
anniversary = date(1991, 10, 12)
txt = f"My name is \"John\", and I am {age}, my anniversary is {anniversary:%A, %B %d, %Y}"  # \ is esc %A: day of week, %B: montnt...
print('5-',txt)
print('6- ', 'text {}'.format(age))
print('7- ', f'text {age}')

my_list = ["apple", "banana", "cherry"]  # list .append .extend .remove .pop .popleft .clear .reverse ...
my_tuple = "apple", "banana", "cherry"  # tuple immutable
my_tuple2 = ("apple", "banana", "cherry")  # tuple immutable
my_range = range(0, 6)  # 0,1,2,3,4,5
my_range2 = range(0, 10, 2)  # 0,2,4,6,8
my_set = {"apple", "banana", "cherry"}  # set, eliminating duplicate
my_set_immutable = frozenset({"apple", "banana", "cherry"})  # set immutable

bytes_var = b'byte'

print('8- type of str_var: ', type(str_var))
print('9- type of age: ', type(age))
print('10- type of anniversary: ', type(anniversary))
print('11- type of bytes_var: ', type(bytes_var))
