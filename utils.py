from dataclasses import dataclass
from enum import Enum

class MealType(Enum):
    BREAKFAST = 1
    LUNCH = 2
    DINNER = 3
    SIDES = 4
    APPETIZER = 5
    DESSERT = 6

class MeasuringUnit(Enum):
    QUARTER_TEASPOON = 1
    HALF_TEASPOON = 2
    TEASPOON = 3
    HALF_TABLESPOON = 4
    TABLESPOON = 5
    FOURTH_CUP = 6
    THIRD_CUP = 7
    HALF_CUP = 8
    THREE_FOURTHS_CUP = 9
    CUP = 10
    OZ = 11

@dataclass
class Ingredient:
    name: str
    quantity: float
    unit: MeasuringUnit
    cost: float

@dataclass
class RecipeTime:
    days: int
    hours: int
    minutes: int