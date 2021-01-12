from enum import Enum
from typing import Optional, Literal

from pydantic import BaseModel, constr, conint, StrictBool
from pydantic.color import Color


class Dto(BaseModel):
    id: str
    name: str
    description: str
    value: Optional[int]


class FruitEnum(str, Enum):
    pear = 'pear'
    banana = 'banana'


# Constrained Types:  NegativeFloat, NegativeInt, PositiveFloat, PositiveInt, conbytes, condecimal, confloat,
#     conint, conlist, conset, constr
# Strict Types: StrictStr, StrictInt, StrictFloat, and StrictBool
# Color: 'black', '7fffd4', (255, 255, 255, 0.5), 'rgb(255, 255, 255)', 'hsl(270, 60%, 70%)'
class ValidationDto(BaseModel):
    id: constr(min_length=1, max_length=10)
    name: constr(min_length=4, strip_whitespace=True)
    description:  constr(regex=r'^miw-(betca|spring|python)$')  # miw-betca, miw-spring or miw-python
    value: Optional[conint(multiple_of=5)]
    adult: StrictBool
    color: Color
    fruit: FruitEnum
    kind: Literal["Light", "PushButton", "Blind"]
