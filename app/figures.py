from math import pi, isclose, sqrt
from typing import Literal, Union
from app.validation import Validation
from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def get_area(self) -> Union[int, float]:
        pass


class Triangle(Figure):
    def __init__(
        self, a: Union[int, float], b: Union[int, float], c: Union[int, float]
    ):
        self.a = a
        self.b = b
        self.c = c
        Validation(a,b,c).is_possible_triangle(a,b,c)

    def is_right_triangle(self) -> bool:
        sorted_sides = sorted([self.a, self.b, self.c])
        return isclose(
            sorted_sides[2] ** 2, sorted_sides[0] ** 2 + sorted_sides[1] ** 2
        )

    def get_area(self):
        p = (self.a + self.b + self.c) / 2
        area = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return area


class Circle(Figure):
    def __init__(self, radius: Union[int, float]):
        self.radius = radius
        self.validation = Validation('circle')

    def get_area(self, r: int):
        return 2 * pi * r
