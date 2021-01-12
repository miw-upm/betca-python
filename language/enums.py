from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2


print(Color.RED.name)
print(Color.RED.value)
print(Color['RED'].name)
for color in Color:
    print(color.name)


class FruitEnum(str, Enum):
    PEAR = 'pear'
    BANANA = 'banana'


print(FruitEnum.BANANA.name)
