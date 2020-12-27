print(f"File one __name__ is set to: {__name__}")


class MyClass:
    """A simple example class"""  # default: __doc__=...
    i: int  # it is a instance
    att = 'static'  # it is a static

    def __init__(self, name):  # constructor
        print('MyClass init')
        self.i = len(name)
        self.other = name  # 'other' is a instance

    def f(self):  # public
        return 'hello world (' + str(self.i) + ')'

    def __private(self):  # private
        pass


class ChildClass(MyClass):

    def __init__(self):
        super().__init__('child')


class DynamicClass:
    pass


def fun():
    print('dynamic fun...')


class Dto:
    name: str
    mobile: int


# when the interpreter runs a module, the __name__ variable will be set as  __main__,
# But if the code is importing the module from another module, then the __name__  will be set to that module’s name.
if __name__ == "__main__":
    print('running main... ')
    c = MyClass('one')
    c3 = MyClass('three')
    print('one: ', c.i, c.other, c.att)
    print('three: ', c3.i, c3.other, c3.att)
    print(c.f())
    print(c.__doc__)
    print(MyClass.__name__)  # it is 'MyClass'
    print(MyClass.att, c.att)
    child = ChildClass()

    # Dynamic class
    dynamic = DynamicClass()
    dynamic.name = 'Ops'
    dynamic.fun = fun
    dynamic.fun()

