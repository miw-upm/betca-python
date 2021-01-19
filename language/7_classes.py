# __***__ are especial functions and attributes


def dynamic_function():
    print('dynamic_function')


class MyClass:
    """A simple example class"""  # default: __doc__=...
    i: int  # it is a instance attribute
    att = 'static'  # it is a static attribute

    def __init__(self, name):  # constructor: __init__
        print('Init MyClass:', name)
        self.i = len(name)
        self.name = name  # 'other' is a instance attribute
        self.dynamic = dynamic_function

    def public(self):  # public
        return 'hello world (' + str(self.i) + ')'

    def __private(self):  # private
        pass


print('0- type of class: ', type(MyClass))

print('1 ---------------- ')
my_class = MyClass('me')
my_class.dynamic()
my_class.new_attribute = "New!!!"
my_class.new_function = dynamic_function
print(my_class.new_attribute)


# Inheritance
class ChildClass(MyClass):
    def __init__(self):
        super().__init__('child')


print('2 ---------------- ')
ChildClass()


class Two:
    two: str

    def __init__(self):
        print('Init Two')


# Multiple inheritance
class Multiple(MyClass, Two):
    value: str


print('3 ---------------- ')
multiple = Multiple('multiple')
multiple.i = 3
multiple.name = "name"
multiple.two = "2"
multiple.value = "value"


class WithDecorator:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_string(cls, name_str):
        first_name, last_name = map(str, name_str.split(' '))
        return cls(first_name, last_name)

    @staticmethod
    def is_full_name(name_str):
        names = name_str.split(' ')
        return len(names) > 1


#  __doc__  __init__  __name__  __module__  __call__ ...

print('4 ---------------- ')
print('__doc__ ', MyClass.__doc__)
print('__name__ ', MyClass.__name__)
print('__module__ ', MyClass.__module__)


class Callable:
    def __call__(self, value):  # class default function
        print('__call__ >> value: ', value)


my_callable = Callable()
my_callable("!!!")  # class is callable
# my_class() ERROR!!!
