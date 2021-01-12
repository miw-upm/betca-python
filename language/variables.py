import datetime

# types: str, int, float, complex, bool, list, tuple, range, dict, set, frozenset, bytes, bytearray, memoryview
str_var: str  # STATIC var is not defined, it is not possible to use until creating with =
str_var = 'string'  # DYNAMIC. str_var is created. It's possible  "string", esc==\
var = 5  # var is created
null_var = None  # None is null and var is created
casting_var = str(var)  # casting: str(), float()...
i = 3 + 2j  # complex: i.real, i.imag ...
var = 'other'  # dynamic type
# One line: one sentence. With \ the line continue
large_str = '''line one\
line one & end of line
other line'''  # '\' without end of line
print(large_str[-10:-5])  # Use negative indexes to start from the end of the string
print(large_str[0:5])
print(large_str[5:])
age = 36
anniversary = datetime.date(1991, 10, 12)
txt = f"My name is \"John\", and I am {age}, my anniversary is {anniversary:%A, %B %d, %Y}"
print('text {}'.format(age))

my_list = ["apple", "banana", "cherry"]  # list .append .extend .remove .pop .popleft .clear .reverse ...
my_tuple = "apple", "banana", "cherry"  # tuple immutable
my_tuple2 = ("apple", "banana", "cherry")  # tuple immutable
my_range = range(0, 6)  # 0,1,2,3,4,5
my_range2 = range(0, 10, 2)  # 0,2,4,6,8
my_set = {"apple", "banana", "cherry"}  # set, eliminating duplicate
my_set_immutable = frozenset({"apple", "banana", "cherry"})  # set immutable

bytes_var = b'byte'
