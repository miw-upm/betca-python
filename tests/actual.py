
def method(arg):
    print('>>> method... return:', arg)
    return arg


class Clazz:
    attribute: int

    def __init__(self, attribute):  # constructor
        self.attribute = attribute

    def class_method(self, arg: int):
        print('>>> Clazz::method... arg:', arg)
        return self.attribute + arg
