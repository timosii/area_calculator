from app.figures import Triangle, Circle
from typing import Union

def calculate_area(figure: Union[Triangle, Circle]):
    return figure.get_area()
