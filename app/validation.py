from app.figures import Figure
from typing import Union


class Validation:
    def __init__(self, *args):
        self.is_correct_type(*args)
        self.is_positive_values(*args)
    
    def is_positive_values(self, *args):
        if any(map(lambda x: x <= 0, args)):
            raise ValueError('Only positive numbers')
    
    def is_correct_type(self, *args):
        if any(map(lambda x: not isinstance(x, (int, float)), args)):
            raise ValueError('Values type must be integer or float')
        
    def is_possible_triangle(
        self, a: Union[int, float], b: Union[int, float], c: Union[int, float]
    ):
        return a + b > c and a + c > b and b + c > a   
